.. _ldumpf:

ldumpf: List the permanent files on a Cyber DUMPF tape
======================================================

**Package: mtlocal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ldumpf dumpf_file file_list
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_dumpf_file">
  <dt><b>dumpf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dumpf_file' Line='dumpf_file' -->
  <dd>The DUMPF data source, i.e., the name of a magtape device or a DUMPF
  format disk file.   If reading from tape, the files to be listed are
  specified by the <i>file_list</i> parameter.
  </dd>
  </dl>
  <dl id="l_file_list">
  <dt><b>file_list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_list' Line='file_list' -->
  <dd>A string listing the DUMPF files to be listed from <i>dumpf_file</i>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Cyber permanent files stored on DUMPF tapes are listed.  The permanent file
  name, cycle number, owner id, dates of last attach, last alteration and
  the creation date are printed.  Task <b>ldumpf</b> lists the contents of a 
  DUMPF tape;
  to convert IPPS rasters stored on DUMPF tapes to IRAF images, use task
  <b>rdumpf</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  List all permanent files on a DUMPF tape:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ldumpf mta 1-999
  </pre></div>
  <p>
  List information for the 4th permanent file on the tape:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ldumpf mta 4
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The Cyber format readers, including task <i>ldumpf</i>, have not been 
  implemented on SUN/IRAF and AOS/IRAF.
  </p>
  <p>
  The current version of IRAF magtape I/O does not read beyond the first
  volume of a multivolume tape.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rdumpf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
