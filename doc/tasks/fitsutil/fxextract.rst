.. _fxextract:

fxextract: Extract a FITS extension
===================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxextract input output groups
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>Can be a list of FITS filename or just one name if you are extracting 
  extensions from it. Filename extensions are require.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string] ' -->
  <dd>Output filename or directory. The root name of this filename is used if more
  than one extension is extracted followed by the group number.
  </dd>
  </dl>
  <dl id="l_groups">
  <dt><b>groups = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groups' Line='groups = "" [string]' -->
  <dd>Specify the list of extensions from the input file to be extracted to the 
  output file or directory; this list follows the syntax of the ranges 
  utilities; i.e. things like 1,2,3; 1-9 or 9,7,13,1-4 are acceptable. 
  Also <span style="font-family: monospace;">'0'</span> to represent the Primary FITS unit is accepted.
  </dd>
  </dl>
  <dl id="l_use_extnm">
  <dt><b>use_extnm = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='use_extnm' Line='use_extnm = no' -->
  <dd>Speficify whether to use the value of the header keyword EXTNAME as the
  name of the output filename. If the keyword does not exist in the input header,
  the output root name is used instead.
  </dd>
  </dl>
  <dl id="l_phu">
  <dt><b>phu = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='phu' Line='phu = yes' -->
  <dd>Creates a dummy Primary Header unit for each of the extracted extensions. If
  the value is 'no', the input extension is copied verbatim to the output file.
  <dl>
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='verbose' Line='verbose = yes' -->
  <dd>Print each operation as it takes place?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  Fextract is an extension to the 'imcopy' command allowing one or more
  extensions from the same MEF file to be extracted into different output
  files.
  FITS extensions are numbered from zero -as the primary unit, with one as
  the first extension two as the second extension and so on.
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  1. To extract extension 2,4,5 from a file and not produce a PHU for
  each of them. The output files will be extf2.fits, extf4.fits and 
  extf5.fits.
  <div class="highlight-default-notranslate"><pre>
  im&gt; fxextract mef.fits extf.fits groups=2,4,5 phu=no
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  imcopy, fxsplit
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
