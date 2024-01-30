.. _sum32:

sum32: Compute the 32-bit FITS 1's complement checksum
======================================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sum32 input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>A list of files, often but not exclusively FITS images.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Report verbose information for each file?
  </dd>
  </dl>
  <dl id="l_nimages">
  <dt><b>nimages</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimages' Line='nimages' -->
  <dd>[Output] The number of images in the input list.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SUM32 computes the 32-bit 1's complement checksum for a list of files.
  This is the algorithm used for the standard FITS checksum [1].  Any 32-bit 
  checksum will generate a 10 digit hash value.  The special feature of the 1's
  complement checksum is that this hash is straightforward to invert (and
  thus is not suited to protect against explicit mischief).
  </p>
  <p>
  Since the checksum can be computed, it is possible to force a file's checksum
  to a specific value.  Without this feature it would be impossible to convey
  a checksum within the original file.  Files (typically FITS) that have been
  so treated will be reported as <span style="font-family: monospace;">"sum_zeroed"</span> in the task output.  The file
  size in bytes is also reported.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Report the 1's complement checksum for a list of files:
  
          fitsutil&gt; sum32 *.fits
          sum_zeroed       584640 test1.fits.fz
          1363490151       532800 test2.fits
          2002849261       172800 test3.fits
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  [1] http://fits.gsfc.nasa.gov/registry/checksum.html
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REFERENCES'  -->
  
