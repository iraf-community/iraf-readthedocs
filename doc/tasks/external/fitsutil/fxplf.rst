.. _fxplf:

fxplf: Converts a pixel list file into a BINTABLE extension
===========================================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxplf input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>Can be a list of 'pl' filenames or just one pl file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string] ' -->
  <dd>Output FITS filename. 
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
  Fxplf will create a new BINTABLE extension on a new or existent FITS
  file. The 'pl' data is located in the 'heap' area of the extension 
  and the BINTABLE data consists of one entry with 2 integers. The first 
  integer is the number of 16bits  integers  in the heap and the second
  is the offset from the last BINTABLE data block.
  </p>
  <p>
  If the output FITS file does not exist, a dummy primary FITS header is 
  created before appending the BINTABLE extension.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To put together all of the Pixel list files starting with <span style="font-family: monospace;">'f'</span>
  into one new output FITS file.
  </p>
  <p>
  	im&gt; fxplf f*.pl bigplf.fits 
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
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
