.. _tcopy:

tcopy: Tape to tape copy routine.
=================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tcopy input_fd output_fd
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_fd">
  <dt><b>input_fd</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_fd' Line='input_fd' -->
  <dd>Tape file or device name for input, e.g. <span style="font-family: monospace;">"mta1600[1]"</span> or <span style="font-family: monospace;">"mtb800"</span>
  </dd>
  </dl>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>List of tape file numbers or ranges delimited by commas, e.g. <span style="font-family: monospace;">"1-3,5-8"</span>.
  `Files' is requested only if no file number is given in `input_fd'.
  Files will be read in ascending order, reguardless of the order of the list.
  Reading will terminate if EOT is reached, thus a list such as <span style="font-family: monospace;">"1-999"</span>
  may be used to read all the files on the tape.
  </dd>
  </dl>
  <dl id="l_output_fd">
  <dt><b>output_fd</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output_fd' Line='output_fd' -->
  <dd>File or device name, e.g. <span style="font-family: monospace;">"mta1600[1]"</span> or <span style="font-family: monospace;">"mtb800"</span>  If a file number is not
  given the user will be asked whether or not this is a new tape.  If it is
  a new tape the file number <span style="font-family: monospace;">"1"</span> will be used.  If it is not a new tape, i.e. 
  it already has data on it, then file number <span style="font-family: monospace;">"EOT"</span> will be used.
  </dd>
  </dl>
  <dl id="l_new_tape">
  <dt><b>new_tape = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_tape' Line='new_tape = no' -->
  <dd>New tape flag.  Usage is described above.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Flag to signal program that it should print information about progress while
  running.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Tcopy copies files from one tape to another reporting read errors on the
  input tape as it goes.  Tcopy, when it encounters a read error, does its
  best to get as much data as possible by validating the input buffer after
  the error, guessing its length, and writing it out to the output tape.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To copy all the files on mta to a new tape on mtb:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; tcopy mta 1-999 mtb yes
  </pre></div>
  <p>
  2. To copy file 5 from mta and append it to the tape on mtb:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; tcopy mta1600[5] mtb no
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  t2d
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
