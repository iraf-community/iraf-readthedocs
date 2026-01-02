.. _vtexamine:

vtexamine: Examine a vacuum telescope tape, print headers and profile.
======================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mtexamine tape_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_tape_file">
  <dt><b>tape_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tape_file' Line='tape_file' -->
  <dd>Tape file, e.g. <span style="font-family: monospace;">"mta1600[2]"</span> or <span style="font-family: monospace;">"mta1600"</span>.
  </dd>
  </dl>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>List of tape file numbers or
  ranges delimited by commas, e.g. <span style="font-family: monospace;">"1-3,5-8"</span>.
  File_list is requested only if no file number is given in tape_file.
  Files will be read in ascending order, regardless of the order of the list.
  Reading
  will terminate if EOT is reached, thus a list such as <span style="font-family: monospace;">"1-999"</span>
  may be used to read all the files on the tape.
  </dd>
  </dl>
  <dl id="l_headers">
  <dt><b>headers=yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='headers' Line='headers=yes' -->
  <dd>Decode and print header information from each file examined.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  By default, vtexamine decodes and prints header and record
  structure information for each file examined.  The header
  information can be turned off by setting headers=no.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To see the header information and determine the record structure of all the
  files on a vacuum telescope tape and send the result to the file vtdump:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; vtexamine mtb1600 1-999 &gt; vtdump
  </pre></div>
  <p>
  2. To just get the record structure for the third file on a vacuum telescope
  tape the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; vtexamine mtb1600[3] headers=no
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The IRAF magtape i/o routines do not permit data beyond a double EOF
  to be accessed. Therefore vtexamine cannot be used to examine tapes with
  embedded double EOFs.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  
