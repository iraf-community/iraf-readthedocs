.. _writevt:

writevt: Write an IRAF image to tape in vacuum telescope format.
================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  writevt input_image output_fd
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_image">
  <dt><b>input_image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_image' Line='input_image' -->
  <dd>Name of input image.
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
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Flag to signal program that it should produce verbose output.  This includes
  header information and progress reports.
  </dd>
  </dl>
  <dl id="l_new_tape">
  <dt><b>new_tape = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_tape' Line='new_tape = no' -->
  <dd>New tape flag.  Usage is described above.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Writevt writes a full disk vacuum telescope gram in IRAF image format to tape.
  The IRAF image is 2048x2048 short integers.  The tape format is the same as
  that used to write original data tapes on the mountain.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To write the image <span style="font-family: monospace;">"image1"</span> to mta at 1600 bpi at file number 3 and
  see verbose output the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; writevt image1 mta1600[3] v+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  readvt
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
