.. _mrotlogr:

mrotlogr: Log some header parameters from a FITS rotation map tape.
===================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mrotlogr input_dev out_file startfnum endfnum append
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_dev">
  <dt><b>input_dev</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_dev' Line='input_dev' -->
  <dd>Tape drive, e.g. <span style="font-family: monospace;">"mta1600"</span> or just <span style="font-family: monospace;">"mta"</span>
  </dd>
  </dl>
  <dl id="l_out_file">
  <dt><b>out_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='out_file' Line='out_file' -->
  <dd>Name of output file to store information. Information is appended to this
  file to allow one to update a previously created file.
  </dd>
  </dl>
  <dl id="l_startfnum">
  <dt><b>startfnum</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='startfnum' Line='startfnum' -->
  <dd>Tape file to start logging.
  </dd>
  </dl>
  <dl id="l_endfnum">
  <dt><b>endfnum</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='endfnum' Line='endfnum' -->
  <dd>Tape file to stop logging.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append' -->
  <dd>Flag to signal that we are appending to an existing file.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Mrotlogr reads FITS headers from successive tape files and compiles
  certain information into a single line of output for each file.
  Currently, the information output for each file includes:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Tape file number, IRAF image name, date, time, and the
  Carrington longitude for each image.
  </pre></div>
  <p>
  If all of these header parameters are not present, only the ones found
  will be printed out and garbage will come out for the empty parameters.
  The date is stored in a header parameter called OBS_DATE, the time is
  stored as 'seconds since midnight' in OBS_TIME and the Carrington
  longitude is stored in L_ZERO.
  To use this script, both the DATAIO package and the VTEL package must
  be loaded.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To log all of the FITS images on a tape mounted on 'mta' and store the
  information in a file called 'CX052' the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; mrotlogr mta CX052 1 999 no
  </pre></div>
  <p>
  2. To log just the 40th through 60th files on mtb and see the output on
  your terminal, the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; mrotlogr mtb STDOUT 40 60 no
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rfits
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
