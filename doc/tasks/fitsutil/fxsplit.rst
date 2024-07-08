.. _fxsplit:

fxsplit: Split a multiple extension FITS file into single FITS files
====================================================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxsplit input_list
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>Can be a list of FITS filenames. Output names will have the input root
  name plus a count.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print each operation as it takes place?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Fxsplit will split a FITS file with multiple extensions into individual
  FITS files. The output file names are similar to the input file but they
  will have a count number appended to the root name.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Split a MEF file that have 2 extensions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; fxsplit file3.fits
  </pre></div>
  <p>
     The output file are: file30.fits, file31.fits file32.fits	 
  </p>
  <p>
  2. To split 2 or more MEF files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; fxsplit g10.fits,msc.fits
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fxcopy,imcopy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
