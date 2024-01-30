.. _xnregistar:

xnregistar: Mosaic the images using sub-pixel replication and masking
=====================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xnregistar inlist rmasks output expmap sections
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The input shiftlist normally produced by the xmshifts, xfshifts, xrshifts, or
  xdshifts tasks. Inlist contains the name of the input sky subtracted image,
  the x offset, the y offset, and the exposure time in columns 1 through 4.
  </dd>
  </dl>
  <dl id="l_rmasks">
  <dt><b>rmasks </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmasks' Line='rmasks ' -->
  <dd>The list of input rejection masks normally produced by the xmskcombine
  task. The rjection mask is assumed to consist of 1's and 0's where 1's
  define the good values. Rrmasks may define a list masks which has the same
  length as inlist, or an image keyword containing the name of the rejection
  mask. The default keyword name  written by xmskcombine  is <span style="font-family: monospace;">"REJMASK"</span>.
  If no rejection mask is defined a virtual cosmic ray mask consisting
  entirely of 1's is defined.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output combined image.
  </dd>
  </dl>
  <dl id="l_expmap">
  <dt><b>expmap </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expmap' Line='expmap ' -->
  <dd>The name of the output exposure map image. 
  </dd>
  </dl>
  <dl id="l_sections">
  <dt><b>sections</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sections' Line='sections' -->
  <dd>The optional output sections or corners file suitable for input to the
  maskdereg task. If defined sections contains the name of the input images
  in <i>sinlist</i> if it is defined or <i>inlist</i>, the x and y coordinates of
  the lower left corner of the input image in the combined output image, and the
  x and y coordinates of the upper right corner of the input image in the output
  image in columns 1 through 5 respectively.
  </dd>
  </dl>
  <dl id="l_sinlist">
  <dt><b>sinlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sinlist' Line='sinlist = ""' -->
  <dd>The list of image names that will be written to the sections file.
  If sinlist is undefined then the input image names in <i>inlist</i> are used.
  </dd>
  </dl>
  <dl id="l_nprev_omask">
  <dt><b>nprev_omask = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nprev_omask' Line='nprev_omask = 0' -->
  <dd>The number of previous object masks to combine to create an objects mask.
  By default no object masks are defined. If nprev_omask is 1 then the
  object mask of the previous image is used to mask the current image,
  if <i>nprev_omask</i> = 2 then the 2 previous object masks are used, etc.
  </dd>
  </dl>
  <dl id="l_blkrep">
  <dt><b>blkrep = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blkrep' Line='blkrep = yes' -->
  <dd>Use block replication to magnify the image if <i>mag</i> &gt; 1 rather than
  bilinear interpolation ?
  </dd>
  </dl>
  <dl id="l_mag">
  <dt><b>mag = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mag' Line='mag = 1' -->
  <dd>The default magnification factor. If mag = 1 the scale of the output image
  is the same as the scale of the input images. If mag &gt; 1 then the input
  images are block replicated by a factor of mag before being combined
  to create the output images.
  </dd>
  </dl>
  <dl id="l_fractional">
  <dt><b>fractional = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fractional' Line='fractional = no' -->
  <dd>If fractional is yes then the input images are shifted by the fractional
  part of the total offset in inlist before being combined. If fractional
  is no then the fractional part of the pixel shift is lost.
  </dd>
  </dl>
  <dl id="l_pixin">
  <dt><b>pixin = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixin' Line='pixin = yes' -->
  <dd>If pixin is yes the input offsets called a and b are assumed to be defined in
  the reference image pixel coordinate system x and y and ab_sense, xscale,
  yscale, and a2x_angle default to yes, -1.0, -1.0, and 0.0 respectively.
  </dd>
  </dl>
  <dl id="l_ab_sense">
  <dt><b>ab_sense = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ab_sense' Line='ab_sense = yes' -->
  <dd>Is the rotation of the a to b axis counter-clockwise ? The x and b
  axes are the axes along which the input offsets are measured. Ab_sense
  defaults to yes if pixin is yes.
  </dd>
  </dl>
  <dl id="l_xscale">
  <dt><b>xscale = 1.0, yscale = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xscale' Line='xscale = 1.0, yscale = 1.0' -->
  <dd>The number of pixel coordinates x and y per input coordinates a and b.
  For example if the input offsets are measured in arcseconds and the pixel
  scale is 0.25 arcseconds per pixel then xscale and yscale should be set to 4.0.
  Xscale and yscale default to -1.0 and -1.0 if pixin is yes.
  </dd>
  </dl>
  <dl id="l_a2x_angle">
  <dt><b>a2x_angle = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='a2x_angle' Line='a2x_angle = 0' -->
  <dd>The angle in degrees of the a offset axis measured counter-clockwise to the
  image x axis. A2x_angle defaults to 0.0 is pixin is yes.
  </dd>
  </dl>
  <dl id="l_ncoavg">
  <dt><b>ncoavg = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncoavg' Line='ncoavg = 1' -->
  <dd>The number of co-averages per input image. The total exposure time for
  an image is ncoavg * exptime * secpexp where exptime is read from inlist.
  </dd>
  </dl>
  <dl id="l_secpexp">
  <dt><b>secpexp = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='secpexp' Line='secpexp = 1.0' -->
  <dd>The number of seconds per unit exposure time.
  </dd>
  </dl>
  <dl id="l_y2n_angle">
  <dt><b>y2n_angle = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y2n_angle' Line='y2n_angle = 0.0' -->
  <dd>The angle in degrees from the image y axis to the north axis measured from north
  through east. Y2n_angle can be used to orient the output image to within 45
  degrees of N up and E left if set correctly.
  </dd>
  </dl>
  <dl id="l_rotation">
  <dt><b>rotation = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rotation' Line='rotation = yes' -->
  <dd>Is the rotation of the input image north axis to the east axis
  counter-clockwise ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XNREGISTAR uses the image names, positional offsets, and exposure time data in
  <i>inlist</i> to create a combined output image <i>output</i> and associated
  exposure map image <i>expmap</i>. Bad data in each input image is
  excluded from the output image and exposure map image using the rejection
  masks <i>rmasks</i>. Rejection masks consist entirely of 1's and 0's with
  1's defining the good pixels. Rejection masks are normally created by
  the XMSKCOMBINE task which combines information in the global bad pixel
  mask,  the cosmic ray masks (normally written by the XZAP or XNZAP tasks),
  the input image holes mask (normally written by the XSLM task), and the
  object masks (normally written by the MKMASK and MASKDEREG tasks), to create
  a single rejection mask for each input image. If the sections file
  <i>sections</i> is defined an output file describing the location of each
  input image in the output image is also written. The sections file is suitable
  for input to the MASKDEREG task.
  </p>
  <p>
  The input image names in column 1 of <i>inlist</i> are the names of the sky
  subtracted images normally written by the XSLM task. If <i>sinlist</i> is <span style="font-family: monospace;">""</span>
  these names are written to the sections file <i>sections</i>. Otherwise the
  names in sinlist are used. The number of images in sinlist must be 0 or
  the same as the number of input images. 
  </p>
  <p>
  The offsets in columns 2 and 3 of <i>inlist</i> are assumed to be defined
  in the ab coordinate system. If <i>pixin</i> = yes then the ab coordinate
  system is assumed to be the same as the xy coordinate system of the
  reference image used to compute the offsets. If pixin = no then the
  <i>ab_sense</i>, <i>xscale</i>, <i>yscale</i>, and <i>a2x_angle</i> are used
  to determine the transformation from the ab to the xy coordinate system.
  If <i>mag</i> is &gt; 1 then the input images are block replicated by a factor
  of mag before being combined into the output image and output exposure map
  image.
  </p>
  <p>
  The integer pixel offsets for each input image are computed as shown below.
  These offsets are passed directly to the IMCOMBINE task which does the actual
  image combining. The quantities a and b are the coordinates as read directly
  from <i>inlist</i>. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  tmag = mag
  if (pixin == yes) {
      ab_sense = yes
      txscale = -1.0
      tyscale = -1.0
      ta2x = 0.0
      sign = 1
  } else if (ab_sense == yes) {
      txscale = xscale
      tyscale = yscale
      ta2x = a2x_angle
      sign = 1
  } else {
      txscale = xscale
      tyscale = yscale
      ta2x = a2x_angle
      sign = -1
  }
  
  x = tmag * (txscale * a * cos (ta2x) +
      tyscale * b * sign * sin (ta2x))
  y = tmag * (tyscale * b * sign * cos (ta2x) -
      txscale * a * sin (ta2x))
  if (x == 0.0)
      ix = 0
  else
      ix = int (x + 0.5 * (x / abs (x)))
  if (y == 0.0)
      iy = 0
  else
      iy = int (y + 0.5 * (y / abs (y)))
  
  </pre></div>
  <p>
  If <i>fractional</i> = yes then the input images are shifted by the fractional
  part of the pixel offsets using the IMSHIFTS task before being combined with
  the IMCOMBINE task. If fractional = no the fractional part of the shift is
  ignored. The fractional shifts are defined as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xfrac = newx - ix
  yfrac = newy - iy
  </pre></div>
  <p>
  The input images are multiplied by a factor equal to <i>ncoavg /
  (mag * mag)</i> before being summed into the combined output image <i>output</i>.
  The summed output image is divided by the exposure map image to compute
  the final output image. Each input image contributes a factor equal to 
  <i>texp * ncoavg * secpexp</i> to the exposure map image, where texp is the
  exposure time read from <i>inlist</i>.
  </p>
  <p>
  The bad data masks <i>bpmask</i>, <i>crmasks</i>, <i>holes</i>, and <i>omasks</i>
  are used to exclude bad pixels, known cosmic ray pixels, and undefined pixels
  from the combined output image and output exposure map image.
  </p>
  <p>
  Finally if <i>y2n_angle</i> and <i>rotation</i> are set correctly the output
  image and the output exposure map image will be oriented to within 45 degrees
  of north pointing up and east pointing left.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the total offsets for the series of 25 demo sky subtracted images
  whose total offsets were computed with the xdshifts task. Combine the images
  with xnregister using the bad pixel mask demo.pl. The output image and
  exposure map image will be written to demo.mosaic and exp_demo.mosaic
  respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type simlist
  demo01.sub.im
  demo02.sub.imh
  demo03.sub.imh
  ...
  ...
  demo24.sub.imh
  demo25.sub.imh
  
  cl&gt; xdshifts @simlist "" offsets cradius=5.0
  
  cl&gt; xmskcombine @simlist badpix.pl "" "" "" ".rjm"
  
  cl&gt; xnregistar offsets REJMASK  demo.mosaic demo.mosaic.exp ""
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  xmshifts,xfshifts,xrshifts,xdshifts,xslm,xzap,xnzap,imshift,blkrep,imcombine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
