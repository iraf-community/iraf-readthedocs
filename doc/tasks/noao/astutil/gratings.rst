.. _gratings:

gratings: Compute and print grating parameters
==============================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gratings
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_echelle">
  <dt><b>echelle = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='echelle' Line='echelle = no' -->
  <dd>Is the grating an echelle grating?  This selects whether the angle of
  incidence is greater or less than blaze angle when the angle of incidence
  or blaze angle are not specified.  For an echelle the angle of incidence
  is generally greater than the blaze angle.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f = 590.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f' Line='f = 590.' -->
  <dd>Focal length in millimeters.  Technically it is defined by the equation x =
  f * tan (theta) where x is distance from the optical axis on the detector
  and theta is the diffraction angle; i.e. it converts angular measures to
  millimeters on the detector.  If the focal length is specified as INDEF it
  is computed from the dispersion, which is required in this case, and the
  other parameters.
  </dd>
  </dl>
  <dl id="l_gmm">
  <dt><b>gmm = 226.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gmm' Line='gmm = 226.' -->
  <dd>Grating grooves per millimeter.  If specified as INDEF it is computed
  from the order, which is required in this case, and the other parameters.
  </dd>
  </dl>
  <dl id="l_blaze">
  <dt><b>blaze = 4.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blaze' Line='blaze = 4.5' -->
  <dd>Blaze angle in degrees.  It is always specified or printed as a positive
  angle relative to the grating normal.  If specified as INDEF it is
  computed from the other parameters.
  </dd>
  </dl>
  <dl id="l_theta">
  <dt><b>theta = -10.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='theta' Line='theta = -10.5' -->
  <dd>Angle of incidence in degrees.  The angle of incidence must be in the plane
  perpendicular to face of the grating.  The angle of incidence may be
  specified relative to the grating normal or the blaze angle though it is
  always printed relative to the grating normal.  To specify it relative to
  the blaze angle add 360 degrees; for example to have an angle of 15 degrees
  less than the blaze angle specify 360 - 15 = 345.  If the angle of
  incidence is specified as INDEF it is computed from the other parameters.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>Order for which the wavelength and dispersion are specified.  If specified
  as INDEF it will be computed from the grooves per mm, which is required in
  this case, and the other parameters.
  </dd>
  </dl>
  <dl id="l_wavelength">
  <dt><b>wavelength = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavelength' Line='wavelength = INDEF' -->
  <dd>Blaze wavelength in Angstroms.  If specified as INDEF it will be computed
  from the other parameters.
  </dd>
  </dl>
  <dl id="l_dispersion">
  <dt><b>dispersion = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispersion' Line='dispersion = INDEF' -->
  <dd>Blaze dispersion in Angstroms per millimeter.  If specified as INDEF it
  will be computed from the focal length, which is required in this case,
  and the other parameters.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the grating parameters specified as INDEF from the other
  grating parameters and prints the final set of self-consistent parameters.
  The parameters are the focal length to the detector, the grooves per
  millimeter of the grating, the blaze angle of the grating, the angle of
  incidence of the incoming light to the grating (which is required to be in
  the plane perpendicular to the face of the grating), the diffraction order,
  and the blaze wavelength and dispersion at the blaze wavelength on the
  detector for that order.  There must be five of these parameters specified
  to compute the remaining two with the exceptions that the combinations
  of the grooves per millimeter and the order or the focal length and
  dispersion must not be simultaneously unspecified.  There are two cases in
  which the computation will not succeed, if not enough parameters are
  specified or when the combination of parameters is not possible.  In these
  cases a warning is printed and the input parameters, including INDEF
  values, are printed.
  </p>
  <p>
  If more than the minimum number of parameters are specified then some of
  the specified parameters will be adjusted to give a self-consistent set.
  In particular, if all parameters are specified the input wavelength and
  dispersion are ignored and new values are calculated.  If only one
  parameter is not specified then the dispersion is adjusted if it is not the
  dispersion the wavelength is adjusted if it is the dispersion.
  </p>
  <p>
  When the order is not specified, the nearest integer order is computed from
  the other non-integer parameters and then the wavelength and dispersion are
  recomputed based on the integer order.
  </p>
  <p>
  The basic grating equation used is
  </p>
  <div class="highlight-default-notranslate"><pre>
  (1)     m * lambda = (sin(theta) + sin(beta)) / g
  </pre></div>
  <p>
  where m is the order, lambda the wavelength, g the grooves per wavelength unit,
  theta the angle of incidence to the grating normal, and beta the angle of
  diffraction to the normal.  The diffraction angle relative to that
  of the blaze maximum, psi, is given by
  </p>
  <div class="highlight-default-notranslate"><pre>
  (2)     beta = psi + 2 * blaze - theta
  </pre></div>
  <p>
  where blaze is the blaze angle.  The diffraction angle psi is related to
  position on the detector, again measured from the blaze peak, by
  </p>
  <div class="highlight-default-notranslate"><pre>
  (3)     x = f * tan(psi)
  </pre></div>
  <p>
  where f is the effective focal length (as defined by this equation).
  At the blaze maximum psi = x = 0 and the wavelength and dispersion
  per millimeter on the detector are given by (1) and the derivative of (1)
  with respect to x:
  </p>
  <div class="highlight-default-notranslate"><pre>
  (4)     wavelength = 1E7*(sin(theta)+sin(2*blaze-theta))/(gmm*order)
  (5)     dispersion = 1E7*cos(2*blaze-theta)/(gmm*order*f)
  </pre></div>
  <p>
  where the variable names are the same as the program parameters and
  the factor of 1E7 is the conversion between millimeters and Angstroms.
  </p>
  <p>
  Equations (4) and (5) are the ones solved by this task.  There are a some
  interesting points to note about the angle of incidence.  There are two
  solutions of these equations one with the angle of incidence less than the
  blaze angle and one greater than the blaze angle.  For an echelle the angle
  of incidence is generally set greater than the blaze angle to avoid light
  lost by reflections back along the angle of incidence.  The <i>echelle</i>
  parameter is used to determine which side of the blaze angle the angle of
  incidence will be computed in the cases in which it is not specified;
  greater than the blaze angle when yes and less than the blaze angle when
  no.
  </p>
  <p>
  In spectrographs it is often the case that the angle between the
  incoming beam and center of the diffracted beam, delta, is fixed where
  </p>
  <div class="highlight-default-notranslate"><pre>
  (6)     delta = 2 * |theta - blaze|
  </pre></div>
  <p>
  This fixes the angle between the blaze angle and the angle of incidence
  needed to center the blaze function on the detector.  If one wants to
  solve (4) and (5) for the blaze angle with this difference fixed the
  angle of incidence may be specified relative to the blaze angle by
  adding 360 degrees to the difference.  An example best describes this.
  The Kitt Peak 4m Echelle Spectrograph has a 12 degree angle
  between the incoming beam to the echelle grating and the beam to the
  crossdisperser.  Then |theta - blaze| = 6 degrees.  For an echelle the
  angle of incidence is greater than the blaze angle (relative to the
  grating normal) so if we set the angle of incidence to 6 + 360
  and the blaze angle to INDEF the resulting computation will
  determine blaze and theta with a fixed 6 degree angle.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The default values are for a grating of 226 grooves per millimeter
  in a 590 mm focal length camera.  For a blaze angle of 4.5 degrees
  and an angle of incidence of -10.5 degrees (the angle is on the
  other side of the grating normal relative to the blaze angle) the
  first order wavelength and dispersion at the blaze peak is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gratings
  Grating parameters:
    Focal length = 590. mm
    Grating = 226. grooves/mm
    Blaze angle = 4.5 degrees
    Incidence angle = -10.5 degrees
    Order = 1
    Blaze wavelength = 6706.696 Angstroms
    Blaze dispersion = 70.69458 Angstroms/mm
  </pre></div>
  <p>
  2.  To find nearest order and the dispersion for a wavelength of 3400
  Angstroms:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gratings order=INDEF wave=3400
  Grating parameters:
    Focal length = 590. mm
    Grating = 226. grooves/mm
    Blaze angle = 4.5 degrees
    Incidence angle = -10.5 degrees
    Order = 2
    Blaze wavelength = 3353.348 Angstroms
    Blaze dispersion = 35.34729 Angstroms/mm
  </pre></div>
  <p>
  3.  To find the grating parameters need to center 8000 Angstroms with
  a dispersion of 90 Angstroms per millimeter:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gratings gmm=INDEF blaze=INDEF theta=345 wave=8000 disp=90
  Grating parameters:
    Focal length = 590. mm
    Grating = 177.8237 grooves/mm
    Blaze angle = 4.223008 degrees
    Incidence angle = -10.77702 degrees
    Order = 1
    Blaze wavelength = 8000. Angstroms
    Blaze dispersion = 90. Angstroms/mm
  </pre></div>
  <p>
  4.  What focal length should be used to get a dispersion of 20 Angstroms/mm
  at 6700 Angstroms:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gratings f=INDEF wave=6700 disp=20
  Grating parameters:
    Focal length = 2085.49 mm
    Grating = 226. grooves/mm
    Blaze angle = 4.5 degrees
    Incidence angle = -10.5 degrees
    Order = 1
    Blaze wavelength = 6706.696 Angstroms
    Blaze dispersion = 20. Angstroms/mm
  </pre></div>
  <p>
  5.  What are the first order wavelength parameters for an echelle of
  31.6 grooves per millimeter with a 63 degree blaze, and a 6 degree
  angle of incidence relative to the blaze angle.  Then what are
  the wavelength parameters in 80th order and what order is 6563 in.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gratings gmm=31.6 blaze=63 theta=69
  Grating parameters:
    Focal length = 590. mm
    Grating = 31.6 grooves/mm
    Blaze angle = 63. degrees
    Incidence angle = 69. degrees
    Order = 1
    Blaze wavelength = 560838.9 Angstroms
    Blaze dispersion = 292.1256 Angstroms/mm
  cl&gt; gratings gmm=31.6 blaze=63 theta=69 order=80
  Grating parameters:
    Focal length = 590. mm
    Grating = 31.6 grooves/mm
    Blaze angle = 63. degrees
    Incidence angle = 69. degrees
    Order = 80
    Blaze wavelength = 7010.487 Angstroms
    Blaze dispersion = 3.651571 Angstroms/mm
  cl&gt; gratings gmm=31.6 blaze=63 theta=69 order=INDEF wave=6563
  Grating parameters:
    Focal length = 590. mm
    Grating = 31.6 grooves/mm
    Blaze angle = 63. degrees
    Incidence angle = 69. degrees
    Order = 85
    Blaze wavelength = 6598.105 Angstroms
    Blaze dispersion = 3.436772 Angstroms/mm
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  artdata.mkechelle
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
