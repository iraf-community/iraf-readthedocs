.. _urlget:

urlget: Get a (http) URL to a named file
========================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  urlget url fname
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_url">
  <dt><b>url</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='url' Line='url' -->
  <dd>The URL to download.
  </dd>
  </dl>
  <dl id="l_fname">
  <dt><b>fname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fname' Line='fname' -->
  <dd>The name of the file to create containing the URL contents.  If not
  specified, the trailing part of the URL is used as the filename.
  </dd>
  </dl>
  <dl id="l_use_cache">
  <dt><b>use_cache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='use_cache' Line='use_cache = yes' -->
  <dd>Use the system file cache?  If 'yes' and the file already exists in the
  cache, the cached file will be copied to the output filename.
  If 'no' then the URL will be downloaded again.
  </dd>
  </dl>
  <dl id="l_extn">
  <dt><b>extn = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extn' Line='extn = ""' -->
  <dd>Optional filename extension to put on the cached filename.  This can be
  used to force files to be saved as a particular type in the cache.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print verbose output?
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = <span style="font-family: monospace;">"cache$"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = "cache$"' -->
  <dd>Logical cache directory name.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>URLGET</i> task is used to download a URL (HTTP protocol only) to a 
  local file named by the <i>fname</i> parameter.  If no <i>fname</i> is given, 
  a filename is constructed from the last part of the URL (i.e.
  characters trailing any of the <span style="font-family: monospace;">'?'</span>, <span style="font-family: monospace;">'/'</span>, or <span style="font-family: monospace;">'&amp;'</span> delimiters).  Because 
  the URL may not point to a static file, use of the <i>fname</i> parameter
  is recommended.
  </p>
  <p>
  If the <i>use_cache</i> parameter is set, the URL will only be downloaded if
  it does not already exist in the file cache pointed to by the <i>cache</i>
  parameter, otherwise the cached file will be copied to the output filename.
  The <i>extn</i> parameter may be to used to force a specific file extension
  to be appended to the filename in the cache, this allows a URL to be passed
  to a task and treated as if it were a file of a specific type.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Download a FITS image from a URL (these are equivalent):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; urlget http://iraf.noao.edu/foo.fits
  cl&gt; urlget http://iraf.noao.edu/foo.fits foo.fits
  </pre></div>
  <p>
  2. Force a URL to be downloaded again:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; urlget http://iraf.noao.edu/foo.fits use_cache=no
  </pre></div>
  <p>
  3. Download a URL with special characters:
  </p>
  <div class="highlight-default-notranslate"><pre>
      cl&gt; urlget http://iraf.noao.edu/scripts/tget?f=foo.fits
  or
      cl&gt; s1 = "http://iraf.noao.edu/scripts/tget?f=foo.fits"
      cl&gt; urlget(s1)
  or
      cl&gt; s1 = "http://iraf.noao.edu/scripts/tget?f=foo.fits&amp;d=/iraf/web"
      cl&gt; urlget(s1,"foo.fits",verbose+)
  </pre></div>
  <p>
  Escaping special characters isn't required from the commandline since the
  URL is assumed to be whitespace or comma delimited.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
