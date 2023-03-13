.. _fcache:

fcache: List, clean or manipulate the file cache
================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fcache cmd
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_cmd">
  <dt><b>cmd</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cmd' Line='cmd' -->
  <dd>Cache command to execute.  A description of each command is given below.
  </dd>
  </dl>
  <dl id="l_pattern">
  <dt><b>pattern = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pattern' Line='pattern = "*"' -->
  <dd>Filename substring pattern to match when initializing the cache with
  the <i>init</i> command.
  </dd>
  </dl>
  <dl id="l_src">
  <dt><b>src = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='src' Line='src = ""' -->
  <dd>Source string used to generate the cache filename.  This is typically
  the full path to a local file being cached or a URL.
  </dd>
  </dl>
  <dl id="l_fname">
  <dt><b>fname = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fname' Line='fname = ""' -->
  <dd>Name of the file in the cache.
  </dd>
  </dl>
  <dl id="l_extn">
  <dt><b>extn = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extn' Line='extn = ""' -->
  <dd>Cache filename extension.
  </dd>
  </dl>
  <dl id="l_age">
  <dt><b>age = -1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='age' Line='age = -1' -->
  <dd>Age of the file (in days) to be purged with the <i>purge</i> command.  A value
  less than zero means that the <i>cache_age</i> environment variable should 
  is used to set the age, a value of zero means to delete all files in the 
  cache  (same as the <i>init</i> command), a value greater than zero means 
  that files older than this age will be deleted.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print status information as the task processes the command.
  </dd>
  </dl>
  <dl id="l_wait">
  <dt><b>wait = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wait' Line='wait = yes' -->
  <dd>Block on operation?  If 'yes' then the task will block until the requested
  file becomes available in the cache.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = <span style="font-family: monospace;">"cache$"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = "cache$"' -->
  <dd>Cache directory to be used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>FCACHE</i> command is used to list or manage the system file cache
  named by the <i>cache</i> parameter.  If the <i>cache</i> directory does not
  exist, it will be created when required.  The <i>cache_age</i> environment
  variable determines the default maximum age of files in the cache, older
  files are automatically removed by the login.cl as part of the startup
  process.
  </p>
  <p>
  The IRAF file cache is used primarily to cache local copies of URLs in the
  system to prevent repeated downloads when accessing URLs from tasks.  This
  allows a URL to be passed to multiple tasks without explicitly requiring
  the user to create a named (temporary) file themselves.
  </p>
  <p>
  The <i>cmd</i> parameter determines the action to take, other parameters are
  used as needed depending on the command according to the following table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Command     Input Pars      Output Pars     Action
  -------     ----------      -----------     ------
  init        pattern                         Initialize the cache
  purge       age                             Purge old files
  destroy                                     Destroy the cache
  list                                        List cache contents
  lookup      src             fname,extn      Lookup a file in the cache
  access      src                             Is file in cache?
  add         src extn        fname           Add file to the cache
  delete      src             fname           Delete file from cache
  wait        src                             Wait for access to file
  </pre></div>
  <p>
  The <i>lookup</i> command works in two ways:  If a <i>src</i> string is
  provided then the <i>fname</i> parameter will contain the matching cached
  file (and <i>extn</i> will contain the optional extension), if the <i>fanme</i>
  parameter is specified then on output <i>src</i> will contain the original
  filename/URL.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Remove all <span style="font-family: monospace;">"url"</span> files from the cache.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fcache init pattern="url"
  </pre></div>
  <p>
  2. List the contents of the file cache.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fcache list
  </pre></div>
  <p>
  3. Destroy a cache directory (i.e. remove it entirely).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fcache destroy cache="/tmp/cache"
  </pre></div>
  <p>
  4. Purge all cache files older than 7 days:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fcache purge age=7
  </pre></div>
  <p>
  5. Determine if a URL is already in the cache:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fcache add src="/tmp/dpix.fits"
  cl&gt; fcache list
       f1128531670  1  /tmp/dpix.fits
        f789045894  1  http://iraf.noao.edu/vao/dpix.fits
  cl&gt; fcache access src="/tmp/dpix.fits"
  yes
  cl&gt; fcache access src="http://iraf.noao.edu/vao/dpix.fits"
  yes
  </pre></div>
  <p>
  6. Delete a cached URL:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fcache delete src="http://iraf.noao.edu/vao/dpix.fits"
  </pre></div>
  <p>
  7. Add a local file to the cache, then look it up:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fcache add src="/tmp/test.fits"
  cl&gt; fcache lookup src="/tmp/test.fits"
  cl&gt; =fcache.fname
  f1295587026
  cl&gt; fcache lookup fname="f1295587026"
  cl&gt; =fcache.src
  /tmp/test.fits
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  head
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
