.. _linpol:

linpol: Calculate polarization frames and Stoke's parameters
============================================================

**Package: nproto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  linpol input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>A list of input images.  There must be either three or four input
  images taken with the polarizer at even multiples of a 45 degree
  position angle.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output data cube which will contain as separate bands the
  fractional linear polarization and angle frames, and optionally the
  Stokes parameter frames.
  </dd>
  </dl>
  <dl id="l_degrees">
  <dt><b>degrees = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='degrees' Line='degrees = yes' -->
  <dd>Report the polarization angle in degrees?  If <b>degrees</b> = no, the
  polarization angle will be reported in radians.
  </dd>
  </dl>
  <dl id="l_stokes">
  <dt><b>stokes = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='stokes' Line='stokes = yes' -->
  <dd>Output the Stokes parameter images?  If <b>stokes</b> = yes, the three
  linear Stokes parameters, I, Q, and U, will be included in the
  <b>output</b> data cube as separate bands.  If <b>stokes</b> = no, only
  the fractional linear polarization and angle frames will appear in the
  output.
  </dd>
  </dl>
  <dl id="l_normalize">
  <dt><b>normalize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normalize' Line='normalize = no' -->
  <dd>Normalize the Q and U frames?  This is appropriate when using a tool
  such as VELVECT to plot the polarization vectors.  If <b>normalize</b> =
  yes, the Q and U Stokes parameter frames will be normalized by dividing
  by the I parameter frame.  This parameter has no effect on either the
  fractional polarization or angle frames.
  </dd>
  </dl>
  <dl id="l_keyword">
  <dt><b>keyword = <span style="font-family: monospace;">"polangle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keyword' Line='keyword = "polangle"' -->
  <dd>This must be set to the name of a header keyword that contains the
  polarizer angle for each of the <b>input</b> images.  LINPOL will only
  accept polarizer angles at even 45 degree separations.  Either four such
  frames, at 0-45-90-135 degrees, or three frames with any one of the
  0-45-90-135 degree frames omitted, may be specified.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  LINPOL calculates the pixel-by-pixel fractional linear polarization and
  polarization angle for a set of either three or four images taken with
  polarizer set at even multiples of a 45 degree position angle.  At least
  three different frames with the header <b>keyword</b> set to one of
  0, 45, 90, or 135 degrees must be specified in the <b>input</b> list.
  </p>
  <p>
  If <b>degrees</b> = yes, the output polarization angle band of the image
  will be in units of degrees, if <b>degrees</b> = no, the angle will be
  reported as radians.  If <b>stokes</b> = yes, the output image
  will consist of five separate bands, one each for the pixel-by-pixel
  fractional linear polarization and the corresponding polarization angle,
  and one for each of the I, Q, and U pixel-by-pixel Stokes parameters.
  If <b>stokes</b> = no, only the fractional polarization and the polarization
  angle will be saved in the output.
  </p>
  <p>
  The <b>normalize</b> parameter is useful for plotting purposes.
  If <b>normalize</b> = yes, the Q and U Stokes parameter frames will be
  normalized by dividing by the I parameter frame.  This may be appropriate
  when using a tool such as VELVECT to plot the polarization vectors.
  This parameter has no effect on either the fractional polarization or
  angle frames.
  </p>
  <p>
  Each input image must contain the corresponding polarizer angle
  in the header keyword specified by the parameter <b>keyword</b>
  Linpol will only accept polarizer angles at even 45 degree separations.
  Either four such frames, at 0-45-90-135 degrees, or three frames with
  any one of the 0-45-90-135 degree frames omitted, may be specified.
  </p>
  <p>
  The output image header will include information describing the particular
  input images that went into its generation and the particular nature of
  each band of the output.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  An observer obtained four exposures of a particular field through a
  polarizer set at a position angle of 0-45-90-135 degrees.  The first
  step in producing a good map of the polarized light from (extended
  or point-like) sources in the field is always to register these frames
  very precisely.  A slight mismatch in the positioning of each pixel
  relative to the shoulders of nearby sources or extended emission will
  result in large errors in the determination of the polarization quantities.
  </p>
  <p>
  Another preprocessing step that may be desirable is to match the PSFs
  (Point Spread Functions) of the various frames.  Ideally, these are
  stable in the raw data (i.e., the seeing at the telescope was constant),
  but if not they must be matched to avoid the same errors as above.  Note
  that it may also be a good idea to <span style="font-family: monospace;">"smooth"</span> the raw images before
  applying linpol to increase the signal-to-noise of the output.
  </p>
  <p>
  After guaranteeing the integrity of the input images, the image header
  <b>keyword</b> must be created to contain the position angle.  The hedit
  task can be used to do this:
  </p>
  <div class="highlight-default-notranslate"><pre>
  hedit im.00 polangle 0 add+
  hedit im.45 polangle 45 add+
  hedit im.90 polangle 90 add+
  hedit im.135 polangle 135 add+
  </pre></div>
  <p>
  At this point, the input images are ready to be processed by linpol.
  </p>
  <p>
  To generate an output image containing the fractional linear
  polarization and polarization angle in separate bands, along with the
  pixel-by-pixel Stokes parameter frames:
  </p>
  <div class="highlight-default-notranslate"><pre>
  np&gt; linpol im.*.imh polar
  </pre></div>
  <p>
  To omit the Stokes parameter frames:
  </p>
  <div class="highlight-default-notranslate"><pre>
  np&gt; linpol im.*.imh polar stokes-
  </pre></div>
  <p>
  To represent the pixel-by-pixel polarization angle in radians, rather
  than degrees:
  </p>
  <div class="highlight-default-notranslate"><pre>
  np&gt; linpol im.*.imh polar degrees-
  </pre></div>
  <p>
  To normalize the Q and U Stokes frames and plot the result with velvect:
  </p>
  <div class="highlight-default-notranslate"><pre>
  np&gt; linpol im.*.imh polar normalize+
  np&gt; imhead polar lo+
  polar[100,100,5][short]: Linear polarization image
      No bad pixels, no histogram, min=unknown, max=unknown
      Line storage mode, physdim [100,100,5], length of user area 2147 s.u.
      Created Wed 10:15:05 29-Apr-92, Last modified Wed 10:15:05 29-Apr-92
      Pixel file 'ursa!/ursa/scr3/iraf/seaman/polar.pix' [ok]
      ...
  
      POL0    = 'im.00.imh'
      POL45   = 'im.45.imh'
      POL90   = 'im.90.imh'
      POL135  = 'im.135.imh'
      POLAR   = 'Band 1 is the percent polarization'
      ANGLE   = 'Band 2 is the polarization angle'
      I-STOKES= 'Band 3 is the Stokes I parameter'
      Q-STOKES= 'Band 4 is the normalized Stokes Q parameter'
      U-STOKES= 'Band 5 is the normalized Stokes U parameter'
  np&gt; velvect polar[*,*,4] polar[*,*,5]
  </pre></div>
  <p>
  Note that the current version of the velvect task is not particularly
  appropriate for this use.  It has no support for reducing the pixel
  resolution of the output plot:  each pixel will generate a plotted vector
  so that to produce an uncrowded (and low <span style="font-family: monospace;">"noise"</span>) plot, the input images
  or output bands must be manually block averaged or otherwise smoothed.
  In addition, the plotted vectors are directed (little arrows) not
  undirected line segments, and the length of the vectors are not easily
  adjusted.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  velvect, imalign, hedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
