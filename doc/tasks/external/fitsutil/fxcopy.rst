.. _fxcopy:

fxcopy: Copy FITS files or FITS extension to an output FITS file
================================================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxcopy input output groups
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
  <dd>Output filename. 
  </dd>
  </dl>
  <dl id="l_groups">
  <dt><b>groups = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groups' Line='groups = "" [string]' -->
  <dd>Specify the list of extensions from the input file to be copied to the output
  file; this list follows the syntax of the ranges utilities; i.e. things
  like 1,2,3; 1-9 or 9,7,13,1-4 are acceptable. Also <span style="font-family: monospace;">'0'</span> to represent the
  Primary FITS unit is accepted.
  </dd>
  </dl>
  <dl id="l_new_file">
  <dt><b>new_file = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_file' Line='new_file = yes' -->
  <dd>Speficify whether to create a new output file or if new_file is 'no' to
  overwrite an existent one.
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
  Fcopy is an extension to the 'imcopy' command allowing many input FITS
  files or selected extensions to be appended to an output FITS file.
  </p>
  <p>
  FITS extensions are numbered from zero -as the primary unit, with one as
  the first extension two as the second extension and so on.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To put together all of the FITS files starting with <span style="font-family: monospace;">'f'</span> into one new output
  file.
  </p>
  <p>
  	im&gt; fxcopy f*.fits bigf.fits new_file=yes
  </p>
  <p>
  2. To copy extensions 1,3,5 from input file g10.fits into a new file. If you 
  want to append to an existent file, set 'new_file = no'.
  </p>
  <p>
  	im&gt; fxcopy g10.fits g3.fit groups=<span style="font-family: monospace;">"1,3,5"</span> new_file=yes
  </p>
  <p>
  3. Selected extensions from various input files.
  </p>
  <p>
  	im&gt; fxcopy fa.fits[2],fb.fits[5],fb.fits[7] fall.fits
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Fxcopy does not accept sections in the filename nor extension numbers. 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy, fxheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
