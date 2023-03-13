.. _cgiparse:

cgiparse: Parse STRING_QUERY environment variable into task parameters
======================================================================

**Package: obsutil**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  CGIPARSE parses the STRING_QUERY environment varabile and sets parameters.
  The string format is a list of task.param=value pairs which includes the
  standard QUERY string special characters <span style="font-family: monospace;">'&amp;'</span>, <span style="font-family: monospace;">'+'</span>, and <span style="font-family: monospace;">'%'</span>.  This is
  intended to parse a query from a CGI script.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  cgiparse
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  There are no parameters.  The input is the value of the QUERY_STRING
  environment variable.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  CGIPARSE parses the STRING_QUERY environment varabile and sets parameters.
  The string format is a list of task.param=value pairs which includes the
  standard QUERY string special characters <span style="font-family: monospace;">'&amp;'</span>, <span style="font-family: monospace;">'+'</span>, and <span style="font-family: monospace;">'%'</span>.  This is
  intended to parse a query from a CGI script.
  </p>
  <p>
  The only input is the STRING_QUERY variable.  If it is undefined the
  task simply does nothing.  The string will normally use the standard
  parameters for this type of string.  The data fields are task.param=value
  strings.  As each is parsed the values will be set for the task.  This
  assumes the tasks are defined.  Theere is no error checking for
  undefined tasks or parameters.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  A CGI script calls a CL script with the STRING_QUERY string set.
  The string has <span style="font-family: monospace;">"imheader.longheader=yes"</span>.  CGIPARSE is called and
  when it completes the parameter value is set.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lpar imhead
  cl&gt; lpar imheader
         images =                 image names
        (imlist = "*.imh,*.fits,*.pl,*.qp,*.hhh") default image ...
    (longheader = no)             print header in multi-line format
    (userfields = yes)            print the user fields ...
          (mode = "ql")
  cl&gt; cgiparse
  cl&gt; lpar imheader
         images =                 image names
        (imlist = "*.imh,*.fits,*.pl,*.qp,*.hhh") default image ...
    (longheader = yes)            print header in multi-line format
    (userfields = yes)            print the user fields ...
          (mode = "ql")
  </pre></div>
  <p>
  Note that when running this in a <span style="font-family: monospace;">"#!cl"</span> script where the <span style="font-family: monospace;">"login.cl"</span> is
  not used that you must be careful to have all tasks referenced by the
  query string defined.
  </p>
  <p>
  2.  Below is a <span style="font-family: monospace;">"#!cl"</span> type script that uses CGIPARSE.  It is used for
  a spectral exposure time calculator based on OBSUTIL.SPTIME though many
  aspects are fairly generic for this type of application.
  </p>
  <div class="highlight-default-notranslate"><pre>
  #!/iraf/iraf/bin.freebsd/cl.e -f
  
  file    urldir
  
  # The following must be set for different hosts.
  # The home directory and the urldir are the same but in different syntax.
  # The home directory must have a world writable tmp subdirectory.
  
  set arch = ".freebsd"
  set (home = osfn ("/www/htdocs/noao/staff/brooke/gsmt/"))
  urldir = "/noao/staff/brooke/gsmt/"
  
  # The uparm is a unique temporary directory.
  s1 = mktemp ("uparm") // "/"
  set (uparm = "home$/tmp/" // s1)
  mkdir uparm$
  cd uparm
  printf ("!/bin/chmod a+rw %s\n", osfn("uparm$")) | cl
  
  # The URL directory is the same as uparm.
  urldir = urldir // "tmp/" // s1
  
  # A private graphcap is required to give an path for sgidispatch.
  set graphcap = home$graphcap
  
  # Load packages.
  dataio
  proto
  noao
  onedspec
  spectime
  gsmt
  
  # Parse the CGI string and set parameters.
  cgiparse
  
  # Create the output.
  
  # Start HTML.
  printf ("Content-Type: text/html\n\n")
  printf ("&lt;html&gt;&lt;head&gt;&lt;title&gt;Test&lt;/title&gt;&lt;/head&gt;\n")
  printf ("&lt;body&gt;\n")
  if (cl.line == "...")
      printf ("&lt;center&gt;&lt;h2&gt;SPECTIME&lt;/h2&gt;&lt;/center&gt;\n", cl.line)
  else
      printf ("&lt;center&gt;&lt;h2&gt;%s&lt;/h2&gt;&lt;/center&gt;\n", cl.line)
  printf ("&lt;pre&gt;\n")
  
  # Execute task(s).
  #show QUERY_STRING
  
  setup interactive=no mode=h
  printf ("&lt;/pre&gt;\n")
  printf ("&lt;A Href='http://www.noao.edu/noao/staff/brooke/gsmt/gsmt.php?stage=1'&gt;Back to form&lt;/A&gt;")
  printf ("&lt;pre&gt;\n")
  
  sptime output="counts,snr" graphics="g-gif" interactive=no mode=h
  
  printf ("&lt;/pre&gt;\n")
  printf ("&lt;A Href='http://www.noao.edu/noao/staff/brooke/gsmt/gsmt.php?stage=1'&gt;Back to form&lt;/A&gt;\n")
  
  printf ("&lt;pre&gt;\n")
  
  # Add any gifs created.  We have to wait for them to be created.
  
  gflush
  
  i = 0; j = 1
  while (i != j) {
      sleep 2
      j = i
      files *.gif | count STDIN | scan (i)
  }
  
  if (i &gt; 0) {
      printf ("&lt;br&gt;&lt;p&gt;&lt;em&gt;Note: DN and S/N are per-pixel&lt;/em&gt;&lt;br&gt;\n")
  
      files *.gif &gt; gifs
      list = "gifs"
      while (fscan (list, s1) != EOF) {
          if (access (s1))
                  printf ("&lt;img src=\"%s%s\"&gt;\n", urldir, s1)
      }
      list = ""
      ## delete ("uparm$gifs", verify-)
  }
  
  printf ("&lt;/pre&gt;\n")
  
  # Finish HTML.
  
  printf ("&lt;A Href='http://www.noao.edu/noao/staff/brooke/gsmt/gsmt.php?stage=1'&gt;Back to form&lt;/A&gt;")
  
  printf ("&lt;/body&gt;&lt;/html&gt;\n")
  
  # Clean up.
  ## delete ("*[^g][^i][^f]", verify-)
  
  logout
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
