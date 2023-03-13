.. _mknoise:

mknoise: Make/add noise and cosmic rays to 1D/2D images
=======================================================

**Package: artdata**

.. raw:: html

  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Images to create or modify.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Output images when modifying input images.  If no output images are
  given then existing images in the input list are modified directly.
  If an output image list is given then it must match in number the
  input list.
  </dd>
  </dl>
  <p>
  WHEN CREATING NEW IMAGES
  </p>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = ""' -->
  <dd>Image title to be given to the images.  Maximum of 79 characters.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 512, nlines = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 512, nlines = 512' -->
  <dd>Number of columns and lines.
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = <span style="font-family: monospace;">"artdata$stdheader.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = "artdata$stdheader.dat"' -->
  <dd>Image or header keyword data file.  If an image is given then the image header
  is copied.  If a file is given then the FITS format cards are copied.
  This only applies to new images.   The data file consists of lines
  in FITS format with leading whitespace ignored.  A FITS card must begin
  with an uppercase/numeric keyword.  Lines not beginning with a FITS
  keyword such as comments or lower case are ignored.  The user keyword
  output of <b>imheader</b> is an acceptable data file.  See <b>mkheader</b>
  for further information.
  </dd>
  </dl>
  <p>
  NOISE PARAMETERS
  </p>
  <dl id="l_background">
  <dt><b>background = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = 0.' -->
  <dd>Background to add to images before computing Poisson noise.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = 1.' -->
  <dd>Gain in electrons per data number.  The gain is used for scaling the
  read noise parameter and in computing poisson noise.
  </dd>
  </dl>
  <dl id="l_rdnoise">
  <dt><b>rdnoise = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rdnoise' Line='rdnoise = 0.' -->
  <dd>Gaussian read noise in electrons.
  </dd>
  </dl>
  <dl id="l_poisson">
  <dt><b>poisson = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='poisson' Line='poisson = no' -->
  <dd>Add poisson noise?  Note that any specified background is added to new
  or existing images before computing the Poisson noise.
  </dd>
  </dl>
  <dl id="l_seed">
  <dt><b>seed = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seed' Line='seed = 1' -->
  <dd>Random number seed.  If a value of <span style="font-family: monospace;">"INDEF"</span> is given then the clock
  time (integer seconds since 1980) is used as the seed yielding
  different random numbers for each execution.
  </dd>
  </dl>
  <p>
  COSMIC RAYS
  </p>
  <dl id="l_cosrays">
  <dt><b>cosrays = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cosrays' Line='cosrays = ""' -->
  <dd>List of cosmic ray files.  Cosmic ray files contain lines of cosmic ray
  coordinates and energy (see DESCRIPTION section).  If no
  file or a new (nonexistent) file is specified then a number of random
  cosmic rays given by the parameter <i>ncosrays</i> is generated.  If a
  new file name is specified then the events generated are recorded in the
  file.  If the list of cosmic ray files is shorter than the list of
  input images then the last cosmic ray file is reused.
  </dd>
  </dl>
  <dl id="l_ncosrays">
  <dt><b>ncosrays = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncosrays' Line='ncosrays = 0' -->
  <dd>If no cosmic ray file or a new file is specified then the task will
  generate this number of random cosmic rays.  The positions are
  uniformly random within the limits of the image and the energy is
  uniformly random between zero and a maximum.
  </dd>
  </dl>
  <dl id="l_energy">
  <dt><b>energy = 30000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='energy' Line='energy = 30000.' -->
  <dd>When generating random events the cosmic rays will have a uniform energy
  distribution (in electrons) between zero and this maximum.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 0.5' -->
  <dd>The half-intensity radius of gaussian profile cosmic rays in pixels
  along the major axis.
  </dd>
  </dl>
  <dl id="l_ar">
  <dt><b>ar = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ar' Line='ar = 1.' -->
  <dd>Minor to major axial ratio for cosmic rays.
  </dd>
  </dl>
  <dl id="l_pa">
  <dt><b>pa = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pa' Line='pa = 0.' -->
  <dd>Position angle in degrees measured counterclockwise from the X axis for
  cosmic rays.
  </dd>
  </dl>
  <dl id="l_comments">
  <dt><b>comments = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comments' Line='comments = yes' -->
  <dd>Include comments recording task parameters in the image header?
  </dd>
  </dl>
  <p>
  PACKAGE PARAMETERS
  </p>
  <p>
  These parameters define certain computational shortcuts which greatly
  affect the computational speed.  They should be adjusted with care.
  </p>
  <dl id="l_nxc">
  <dt><b>nxc = 5, nyc = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxc' Line='nxc = 5, nyc = 5' -->
  <dd>Number of cosmic ray centers per pixel in X and Y.  Rather than evaluate
  cosmic rays precisely at each subpixel coordinate, a set of templates
  with a grid of subpixel centers is computed and then the nearest template to
  the desired position is chosen.  The larger the number the more memory
  and startup time required.
  </dd>
  </dl>
  <dl id="l_nxsub">
  <dt><b>nxsub = 10, nysub = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxsub' Line='nxsub = 10, nysub = 10' -->
  <dd>Number of pixel subsamples in X and Y used in computing the cosmic
  ray profiles.  This is the subsampling in the central
  pixel and the number of subsamples decreases linearly from the center.
  This affects the time required to compute the cosmic ray templates.
  </dd>
  </dl>
  <dl id="l_dynrange">
  <dt><b>dynrange = 100000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dynrange' Line='dynrange = 100000.' -->
  <dd>The intensity profile of the gaussian cosmic rays extends to infinity so
  a dynamic range, the ratio of the peak intensity to the cutoff
  intensity, is imposed.  Because the cosmic rays are small this parameter
  is not critical.
  </dd>
  </dl>
  <dl id="l_ranbuf">
  <dt><b>ranbuf = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ranbuf' Line='ranbuf = 0' -->
  <dd>Random number buffer size.  When generating readout and poisson noise,
  evaluation of new random values has an affect on the execution time.
  If truly (or computationally truly) random numbers are not needed
  then this number of random values is stored and a simple
  uniform random number is used to select from the stored values.
  To force evaluation of new random values for every pixel set the
  value of this parameter to zero.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates or modifies images with readout noise, poisson noise,
  and cosmic ray events.  New images are created with the specified
  dimensions and real datatype.  Existing images may be modified in place
  or new images may be created.
  </p>
  <p>
  If a new image is created it is has the mean level given by the parameter
  <i>background</i>.  With no noise and no cosmic rays this task can be used to
  create images of constant background value.  For existing images the
  background is added before computing any noise.  To add noise to an
  existing image without modifying the mean counts set the background
  to zero.
  </p>
  <p>
  For new images a set of header keywords may be added by specifying an
  image or data file with the <i>header</i> parameter (see also <b>mkheader</b>).
  If a data file is specified lines beginning with FITS keywords are
  entered in the image header.  Leading whitespace is ignored and any
  lines beginning with words having lowercase and nonvalid FITS keyword
  characters are ignored.  In addition to this optional header,
  keywords, parameters for the gain and read noise are defined.
  Finally, comments may be added to the image header recording the task
  parameters and any information from the cosmic ray file which are not
  cosmic ray definitions.
  </p>
  <p>
  Poisson photon noise is generated by setting the <i>poisson</i> parameter.
  For new images the input data value is the background while for
  existing images the input data value is added to the background value.
  The data value is then multiplied by the gain, a poisson deviate is
  generated, and divided by the gain.  Expressed as a formula:
  </p>
  <div class="highlight-default-notranslate"><pre>
       New images: out = P(background * gain) / gain
  Existing images: out = P((in+background)*gain) / gain
  </pre></div>
  <p>
  where P(x) is a poisson deviate with mean x, in and out are the input
  and final pixel values, and background and gain are the parameter
  values of the same name.
  </p>
  <p>
  Readout or gaussian noise is generated by specifying a gaussian sigma with
  the parameter <i>rdnoise</i>.  The sigma is divided by the specified gain
  to convert to image data units.  Gaussian random numbers of mean zero are
  then generated for each pixel and added to the image, or background
  value for new images, after the photon noise is computed.
  </p>
  <p>
  Generating gaussian and poisson random numbers computationally is
  the main determinant of the execution time in this task.
  Two things are done to speed up the task.
  First, the gaussian approximation is used for data values greater
  than 20 (after applying the background and gain).  The square root
  of the data value is used as the gaussian sigma about the data
  value.  For values less than 20 a true poisson deviate is generated.
  The second speed up is to allow storing a number of normalized gaussian
  values given by the package parameter <i>ranbuf</i> as they are generated.  If
  more values than this are desired then a uniform random number is used
  to select one of these stored values.  This applies to both the read noise
  and poisson noise gaussian approximation though not the true poisson
  evaluation.  For most purposes this approximation is good and one would
  need to look very hard to detect the nonrandomness in the noise.
  However, if one wants to take the extra computational time then
  by setting the <i>ranbuf</i> parameter to zero each gaussian
  random number will be generated independently.
  </p>
  <p>
  The cosmic ray model is an elliptical gaussian of specified
  half-intensity radius, axial ratio, and position angle.  Normally the
  radius will be small (smaller than the point spread function) and the
  axial ratio will be 1.  The cosmic rays are subsampled and can have the
  number of centers given by the <i>nxc/nyc</i> package parameters.  The method
  of generating the cosmic rays is that described for the task
  <b>mkobjects</b>.  Specifically it is the same as adding gaussian
  profile stars.
  </p>
  <p>
  The total flux (not the peak) of the cosmic ray is given by the energy
  in electrons so that the value is divided by the gain to produce the
  total flux in the image.  Note that this task can be used to add cosmic
  ray spikes to one dimensional images such as spectra but the strengths
  will appear low because of the part of the event which falls outside
  the single line.
  </p>
  <p>
  The positions and energies of the cosmic rays can be specified in a
  file or the task can generate random events.  Specific cosmic rays are
  specified by a file containing lines of x and y positions and energy.
  Positions outside the limits of the image are ignored.  If no cosmic
  ray file is given or if a new, nonexistent file is named then the
  number of cosmic rays given by the <i>ncosrays</i> parameter is
  generated with uniform spatial distribution within the image and
  uniform energy distribution between zero and that given by the
  <i>energy</i> parameter.  By giving a new file name the randomly
  generated cosmic rays will be recorded for reuse or to allow
  identifying the events while testing tasks and algorithms.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a new image with a background of 1000, a read noise
  of 10 electrons, a gain of 2, and 50 random cosmic rays.  Don't keep a
  record of the cosmic rays.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mknoise testim back=1000 rd=10 gain=2 poisson+ ncos=50
  </pre></div>
  <p>
  2. Add cosmic rays to an image and create a new output image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; head cosfile
  20.3 50.1 1000
  325.6 99.6 250
  cl&gt; mknoise dev$pix out=newpix cos=cosfile
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MKNOISE">
  <dt><b>MKNOISE V2.11+</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKNOISE' Line='MKNOISE V2.11+' -->
  <dd>The random number seed can be set from the clock time by using the value
  <span style="font-family: monospace;">"INDEF"</span> to yield different random numbers for each execution.
  </dd>
  </dl>
  <dl id="l_MKNOISE">
  <dt><b>MKNOISE V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKNOISE' Line='MKNOISE V2.11' -->
  <dd>The default value of <span style="font-family: monospace;">"ranbuf"</span> was changed to zero.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkobjects, mkheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
