.. _mkcwwcs:

mkcwwcs: Make or update a simple celestial/wavelength 3D wcs
============================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkcwwcs wcsname
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_wcsname">
  <dt><b>wcsname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsname' Line='wcsname' -->
  <dd>Image to be created or modified.  If a new (non-existent) image is specified
  then a data-less image (NDIM=0) is created.
  </dd>
  </dl>
  <dl id="l_wcsref">
  <dt><b>wcsref = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsref' Line='wcsref = ""' -->
  <dd>Image whose WCS is first inherited and then updated.
  </dd>
  </dl>
  <dl id="l_equinox">
  <dt><b>equinox = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='equinox' Line='equinox = INDEF' -->
  <dd>Equinox of the coordinates specified in decimal years.  If INDEF then the
  current value is not modified.
  </dd>
  </dl>
  <dl id="l_ra">
  <dt><b>ra = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ra' Line='ra = INDEF' -->
  <dd>Right ascension in hours.  This may be typed in standard sexagesimal
  notation though it will be converted to decimal hours in EPARAM and
  to decimal degrees in the WCS as required by the standard.  If INDEF
  then the current value is not modified.
  </dd>
  </dl>
  <dl id="l_dec">
  <dt><b>dec = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dec' Line='dec = INDEF' -->
  <dd>Declination in degrees.  This may be typed in standard sexagesimal
  notation though it will be converted to decimal degrees in EPARAM.
  If INDEF then the current value is not modified.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = INDEF, pa = 0., lefthanded = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = INDEF, pa = 0., lefthanded = yes' -->
  <dd>Celestial pixel scale in arc seconds per pixel, the position angle in
  degrees, and the handedness of the axes.  These are all represented by
  the WCS rotation matrix.  If the scale is INDEF the current
  rotation matrix is unchanged and the position angle is ignored.  If the
  scale is not INDEF then orthogonal axes are defined with the same scale on
  both axes.  The handedness of the axes are specified by the
  <i>lefthanded</i> parameter.  The position angle is measured from north
  increasing with the image lines (up in a standard display) and rotated
  towards east.  Note that if the axes are lefthanded the angle is
  counterclockwise and if not it is clockwise.
  </dd>
  </dl>
  <dl id="l_projection">
  <dt><b>projection = <span style="font-family: monospace;">"tan"</span> (tan|sin|linear)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='projection' Line='projection = "tan" (tan|sin|linear)' -->
  <dd>WCS projection function for the celestial axes which may be
  <span style="font-family: monospace;">"tan"</span>, <span style="font-family: monospace;">"sin"</span>, or <span style="font-family: monospace;">"linear"</span>.
  </dd>
  </dl>
  <dl id="l_wave">
  <dt><b>wave = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wave' Line='wave = INDEF' -->
  <dd>Reference wavelength in arbitrary units.  If INDEF then the current
  value is not modified.
  </dd>
  </dl>
  <dl id="l_wscale">
  <dt><b>wscale = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wscale' Line='wscale = INDEF' -->
  <dd>Wavelength scale in arbitrary units per pixel.  If INDEF then the current
  value is not modified.
  </dd>
  </dl>
  <dl id="l_rapix">
  <dt><b>rapix = INDEF, decpix = INDEF, wpix = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rapix' Line='rapix = INDEF, decpix = INDEF, wpix = INDEF' -->
  <dd>The reference pixel for the right ascension (first image axis), for
  the declination (second image axes), and for the wavelength
  (third axis).  The reference pixel may be fractional
  and lie outside the size of the image as allowed by the standard.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKCWWCS creates or modifies a celestial (RA/DEC) plus wavelength
  three-dimensional WCS in an image header.  If a
  new image is specified the WCS is created in a data-less image header.  A
  data-less WCS may be used in various tasks as a template.  If a reference
  WCS is specified it is copied in whole and then desired elements of the WCS
  are modified.  If a new WCS is created without a reference the initial values
  are for the pixel coordinates.
  </p>
  <p>
  The elements of the WCS which may be set are the coordinate equinox,
  the right ascension and declination, the pixel scale, the axes orientation,
  the reference wavelength, the wavelength scale (i.e. dispersion),
  and the reference pixel in the image which corresponds to the specified
  right ascension and declination.  If values are specified the WCS elements
  are left unchanged.
  </p>
  <p>
  The WCS is simple and not completely general because it defines the first
  coordinate axis to be right ascension, the second to be declination, and
  the third to be wavelength.  The axes are orthogonal and the celestial axes
  have a uniform pixel scale (apart from the effects of the projection
  function).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a data-less header by specifying a new wcs name.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkcwwcs new ra=1:20:23.1 dec=-12:11:13 wave=5500. \
  &gt;&gt;&gt; scale=0.25 wscale=1.23
  </pre></div>
  <p>
  The reference pixel will be (0,0,0).  To apply it later to an actual
  image (say with WCSCOPY) would require assigning the reference pixel.
  Note the use of sexagesimal notation.
  </p>
  <p>
  2. Modify the WCS of an existing image by changing the reference value
  and pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkcwwcs old ra=1:20:23.1 dec=-12:11:13 wave=5500. \
  &gt;&gt;&gt; rapix=1234 decpix=345 wpix=1024
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  wcsedit,wcscopy,mkcwcs
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
