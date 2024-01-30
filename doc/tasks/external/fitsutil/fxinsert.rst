.. _fxinsert:

fxinsert: Insert FITS files or extensions into another MEF file
===============================================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxinsert input output groups
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>Can be a list of FITS filenames with or without extension number.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string] ' -->
  <dd>Output filename. The extension number after which the input units are going to
  be inserted is required.
  </dd>
  </dl>
  <dl id="l_groups">
  <dt><b>groups = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groups' Line='groups = "" [string]' -->
  <dd>Specify the list of extensions to insert from the those files without 
  explicit extension number. This list is applied to all input files.
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
  Finsert  will insert one or more FITS units after a specified extension
  number from the output file. A unit can be a whole FITS file or one extension.
  </p>
  <p>
  FITS extensions are numbered from zero -as the primary unit, with one as
  the first extension two as the second extension and so on.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Insert group 3 from input.fits after group 1 from output.fits file.
  
          im&gt; fxinsert input.fits[3] output.fits[1]
  
  2. To insert extensions 1,3,5 from input file g10.fits after group 5 from
     g30.fits file.
  
          im&gt; fxinsert g10.fits g30.fits[5] groups="1,3,5"
  
  3. Insert files and extensions.
  
          im&gt; fxinsert fa.fits,fb.fits[5],fc.fits foutput.fits[3]
  
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Finsert does not accept EXTNAME or EXTVER values yet.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy, fxheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
