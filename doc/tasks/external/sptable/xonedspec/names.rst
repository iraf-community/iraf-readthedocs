.. _names:

names: Generate a list of image names from a string
===================================================

**Package: xonedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  names input records
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The root file name for the input records to be calibrated.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The range of spectra to be included in the calibration operation.
  Each range item will be appended to the root name to form an
  image file name.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = ""' -->
  <dd>If not a null string, this character string will be appended to
  all the generated image names. This allows for a specification of
  image sections.
  </dd>
  </dl>
  <dl id="l_check">
  <dt><b>check = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='check' Line='check = no' -->
  <dd>If set to yes, a check is made that each name implied by the range
  specification has at least an image header. The pixel file is not
  checked. If set to no, then all possible image names are generated
  even if no image exists.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A sequence of image names is generated from the input root file name
  and the range description by appending the possible range values to
  the root in the form <span style="font-family: monospace;">"root.nnnn"</span>. At least four digits will follow the
  root.
  </p>
  <p>
  If an append string is specified, this is added to the image name as well.
  </p>
  <p>
  The generated image names are written to STDOUT, but may be redirected
  to a file for further use.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following will generate names of the form nite1.0001, nite1.0002 ...
  nite1.0010 and place the list in the file nite1.lst.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; names nite1 1-10 &gt;nite1.lst
  </pre></div>
  <p>
  The next example uses the append option to specify that only the
  first 512 pixels of each image (spectrum) are to used in the image name.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; names nite1 1-10 append="[1:512]" &gt;nite1.lst
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_NAMES">
  <dt><b>NAMES V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='NAMES' Line='NAMES V2.10' -->
  <dd>This task is unchanged.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The append option is only useful for adding image sections since it is
  added after the ONEDSPEC name is generated.  Appending other strings
  produces names such as root.0012str which are not recognized by
  the package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'BUGS'  -->
  
