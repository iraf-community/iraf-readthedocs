.. _funpack:

funpack: Uncompress a FITS file
===============================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  funpack images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>A list of tile compressed FITS images (with '.fz' extensions).
  </dd>
  </dl>
  <dl id="l_keep">
  <dt><b>keep = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keep' Line='keep = no' -->
  <dd>Preserve the input images?  By default the input files will be replaced
  by the corresponding tile compressed FITS files.
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>List the types and contents (FITS HDUs) of the input files?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print each operation as it takes place?  Data volume and timing will
  also be reported.
  </dd>
  </dl>
  <dl id="l_gzip">
  <dt><b>gzip = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gzip' Line='gzip = no' -->
  <dd>Recompress output files with host gzip command?
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
  Funpack will uncompress a list of tile compressed FITS files.
  The input file names must have <span style="font-family: monospace;">".fz"</span> appended.  The output files
  will be standard FITS image files, either single images or MEFs.
  Optionally, the output files may be recompressed using the host
  gzip command.
  </p>
  <p>
  This task is a wrapper script for the CFITSIO funpack command.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Uncompress a tile compressed file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; funpack file3.fits.fz
  </pre></div>
  <p>
  The output file is <span style="font-family: monospace;">"file3.fits"</span>.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ricepack, http://heasarc.gsfc.nasa.gov/fitsio/fpack
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
