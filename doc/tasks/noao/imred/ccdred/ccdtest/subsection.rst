.. _subsection:

subsection: Create an artificial subsection CCD observation
===========================================================

**Package: ccdtest**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  subsection subimage image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_subimage">
  <dt><b>subimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subimage' Line='subimage' -->
  <dd>Subsection image to be created.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Full image from which to take the subsection readout.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 82, nlines = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 82, nlines = 50' -->
  <dd>Number of image columns and lines in the full subsection image including
  bias regions.
  </dd>
  </dl>
  <dl id="l_ccdsec">
  <dt><b>ccdsec=<span style="font-family: monospace;">"[26:75,26:75]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdsec' Line='ccdsec="[26:75,26:75]"' -->
  <dd>CCD section of the subsection.  This is the image section of the full
  image to be used.
  </dd>
  </dl>
  <dl id="l_datasec">
  <dt><b>datasec = <span style="font-family: monospace;">"[1:50,1:50]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datasec' Line='datasec = "[1:50,1:50]"' -->
  <dd>Data section of the image.
  </dd>
  </dl>
  <dl id="l_trimsec">
  <dt><b>trimsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimsec' Line='trimsec = ""' -->
  <dd>Trim section for later processing.
  </dd>
  </dl>
  <dl id="l_biassec">
  <dt><b>biassec=<span style="font-family: monospace;">"[51:82,1:50]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='biassec' Line='biassec="[51:82,1:50]"' -->
  <dd>Prescan or overscan bias section.
  </dd>
  </dl>
  <dl id="l_overwrite">
  <dt><b>overwrite = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='overwrite' Line='overwrite = no' -->
  <dd>Overwrite an existing image?  If no a new observation is not created.
  There is no warning message.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This script task generates artificial CCD subsection observations
  which include bad pixels, bias and zero levels, dark counts, flat
  field response variations and sky brightness levels.  It creates an
  subsection image which includes a bias section from a previously
  created image (created by the task <b>artobs</b>).  This task is
  designed to be used with the <b>ccdred</b> package and includes
  appropriate image header information.
  </p>
  <p>
  First the task checks whether the requested image exists.  If it does
  exist and the overwrite flag is no then a new observations is not created.
  If the overwrite flag is set then the old image is deleted and a new
  observation is created.
  </p>
  <p>
  The image section give by the parameter <i>ccdsec</i> of the reference
  image is copied to the new image.  It is assumed the reference image
  contains any desired zero level, bias, flat field, and dark count
  effects.  The bias section is then added with a bias value given by
  <b>artobs.biasval</b> with noise given by <b>artobs.sigma</b>.
  </p>
  <p>
  Also the image header parameters from the reference image are
  copied and the data, bias, trim, and ccd section parameters are
  updated.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To create some test CCD images first create full frame observations with
  the task <b>artobs</b>.  Then set the subsection parameters
  for the size of the subsection observation, the data section, trim section,
  bias section, and the CCD section of the subsection observation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; artobs obj 5 object filter=V
  cl&gt; subsection obj1 object
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkimage, artobs, demo
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
