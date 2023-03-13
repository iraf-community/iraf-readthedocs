.. _touch:

touch: Change file access and modification times
================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  touch files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>List of files to be created or touched.
  </dd>
  </dl>
  <dl id="l_create">
  <dt><b>create = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='create' Line='create = yes' -->
  <dd>If enabled, the file will be created as a zero-length text file if it doesn't
  already exist.
  </dd>
  </dl>
  <dl id="l_atime">
  <dt><b>atime = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='atime' Line='atime = yes' -->
  <dd>Change the access time of the file.  Will not change the modification time
  unless <i>mtime</i> is also set.
  </dd>
  </dl>
  <dl id="l_mtime">
  <dt><b>mtime = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mtime' Line='mtime = yes' -->
  <dd>Change the modification time of the file.  Will not change the access time
  unless <i>atime</i> is also set.
  </dd>
  </dl>
  <dl id="l_time">
  <dt><b>time = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='time' Line='time = ""' -->
  <dd>Time and date to set for the file.  The format of this string may be any
  of DD/MM/YY or CCYY-MM-DD (in which case time is assumed to be midnight of
  that day), or CCYY-MM-DDTHH:MM:SS[.SSS...] to specify both date and time.
  If not specified, the current system time is used unless the <i>ref_file</i>
  parameter is set.  If specified, <i>ref_file</i> will be ignored.
  </dd>
  </dl>
  <dl id="l_ref_file">
  <dt><b>ref_file = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ref_file' Line='ref_file = ""' -->
  <dd>Use the corresponding times of the specified file for modifying the
  times of the <i>input_files</i>.  If not specified, the current time is
  used unless the <i>time</i> parameter is set.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print verbose output of the files and times being reset.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>touch</i> task sets the access and modification times of each file
  in the <i>files</i> list.  The file will be created if it does not already
  exist when the <i>create</i> parameter is set.  The time used can be
  specified by <i>time</i> parameter or by the corresponding fields of the
  file specified by <i>ref_file</i>, otherwise the current system time will
  be used.  The task will update both the modification and access times of
  the file unless disabled by the <i>atime</i> or <i>mtime</i> parameter.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Update the times of all SPP source files in the current directory:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; touch *.x
  </pre></div>
  <p>
  2.  Create an empty file on a remode node:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; touch ursa!/data/trigger_file
  </pre></div>
  <p>
  3.  Reset the file modification time to 2:33:45 pm on June 5, 2003:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; touch nite1.fits time="2003-06-05T14:23:45"
  </pre></div>
  <p>
  4.  Reset the file modification time to match dev$hosts:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; touch nite1.fits ref_file=dev$hosts
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
