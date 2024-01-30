.. _artobs:

artobs: Create an artificial CCD observation
============================================

**Package: ccdtest**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  artobs image exptime ccdtype
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Observation to be created.
  </dd>
  </dl>
  <dl id="l_exptime">
  <dt><b>exptime</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exptime' Line='exptime' -->
  <dd>Exposure time of observation.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype' -->
  <dd>CCD image type of observation.  This type is one of the standard types
  for the CCDRED package.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 132, nlines = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 132, nlines = 100' -->
  <dd>The number of columns and lines in the full image created including
  bias section.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = ""' -->
  <dd>Filter string for the observation.
  </dd>
  </dl>
  <dl id="l_datasec">
  <dt><b>datasec = <span style="font-family: monospace;">"[1:100,1:100]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datasec' Line='datasec = "[1:100,1:100]"' -->
  <dd>Data section of the observation.
  </dd>
  </dl>
  <dl id="l_trimsec">
  <dt><b>trimsec = <span style="font-family: monospace;">"[3:98,3:98]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimsec' Line='trimsec = "[3:98,3:98]"' -->
  <dd>Trim section for later processing.
  </dd>
  </dl>
  <dl id="l_biassec">
  <dt><b>biassec = <span style="font-family: monospace;">"[103:130,*]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='biassec' Line='biassec = "[103:130,*]"' -->
  <dd>Prescan or overscan bias section.
  </dd>
  </dl>
  <dl id="l_imdata">
  <dt><b>imdata = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imdata' Line='imdata = ""' -->
  <dd>Image to be used as source of observation if specified.  The image must
  be at least as large as the data section.
  </dd>
  </dl>
  <dl id="l_skyrate">
  <dt><b>skyrate = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyrate' Line='skyrate = 0.' -->
  <dd>Sky counting rate.  The total sky value will be scaled by the exposure time.
  </dd>
  </dl>
  <dl id="l_badpix">
  <dt><b>badpix = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badpix' Line='badpix = ""' -->
  <dd>Bad pixel region file in the standard CCDRED bad pixel file format.
  </dd>
  </dl>
  <dl id="l_biasval">
  <dt><b>biasval = 500.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='biasval' Line='biasval = 500.' -->
  <dd>Mean bias value of the entire image.
  </dd>
  </dl>
  <dl id="l_badval">
  <dt><b>badval = 500.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badval' Line='badval = 500.' -->
  <dd>Bad pixel value placed at the specified bad pixel regions.
  </dd>
  </dl>
  <dl id="l_zeroval">
  <dt><b>zeroval = 100.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zeroval' Line='zeroval = 100.' -->
  <dd>Zero level of the data section.
  </dd>
  </dl>
  <dl id="l_darkrate">
  <dt><b>darkrate = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='darkrate' Line='darkrate = 1.' -->
  <dd>Dark count rate.  The total dark count will be scaled by the exposure time
  </dd>
  </dl>
  <dl id="l_zeroslope">
  <dt><b>zeroslope = 0.01</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zeroslope' Line='zeroslope = 0.01' -->
  <dd>Slope of the zero level per pixel.
  </dd>
  </dl>
  <dl id="l_darkslope">
  <dt><b>darkslope = 0.002</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='darkslope' Line='darkslope = 0.002' -->
  <dd>Slope of the dark count rate per pixel.  This is also scaled by the exposure
  time.
  </dd>
  </dl>
  <dl id="l_flatslope">
  <dt><b>flatslope = 3.0000000000000E-4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatslope' Line='flatslope = 3.0000000000000E-4' -->
  <dd>The mean flat field response is 1 with a slope given by this value.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = 5.' -->
  <dd>Gaussian noise sigma per pixel.
  </dd>
  </dl>
  <dl id="l_seed">
  <dt><b>seed = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seed' Line='seed = 0' -->
  <dd>Random number seed.  If zero new values are used for every observation.
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
  This script task generates artificial CCD observations which include
  bad pixels, bias and zero levels, dark counts, flat field response
  variations and sky brightness levels.  Optionally, image data from
  a reference image may be included.  This task is designed to be used
  with the <b>ccdred</b> package and includes appropriate image header
  information.
  </p>
  <p>
  First the task checks whether the requested image exists.  If it does
  exist and the overwrite flag is no then a new observations is not created.
  If the overwrite flag is set then the old image is deleted and a new
  observation is created.
  </p>
  <p>
  An empty image of the specified size and of pixel data type short is
  first created.  If a noise sigma is specified it is added to the entire
  image.  If a reference image is specified then image section given by
  the <i>datasec</i> parameter is copied into the data section of the
  observation.  Next a sky level, specified by the <i>skyrate</i>
  parameter times the exposure time, is added to the data section.
  The flat field response with a mean of one and a slope given by the
  <i>flatslope</i> parameter is multiplied into the data section.  If
  a dark count rate and/or a zero level is specified then these effects
  are added to the data section.  Then the specified bias level
  is added to the entire image; i.e. including the bias section.
  Finally, the pixels specified in the bad pixel region file, if one
  is specified, are set to the bad pixel value.
  </p>
  <p>
  The CCD reduction parameters for the data section, the trim section,
  the bias section, exposure time, the CCD image type, and the filter
  are added to the image header (if they are specified) using <b>ccdhedit</b>
  to apply any keyword translation.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To create some test CCD images first set the task parameters such as
  number of columns and lines, data, bias, and trim sections, and data
  values.  The images are then created as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; artobs.filter = "V"         # Set the filter
  cl&gt; artobs zero 0. zero         # Zero level image
  cl&gt; artobs dark 1000. dark skyrate=0.   # Dark count image
  cl&gt; artobs flat 1. flat skyrate=1000.   # Flat field image
  cl&gt; artobs obj 10. object               # Object image
  </pre></div>
  <p>
  Note that the CCD image type is not used explicitly so that for a
  dark count image you must set the sky count rate to zero.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkimage, subsection, demo
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
