.. _gallist:

gallist: Make an artificial galaxies list
=========================================

**Package: artdata**

.. raw:: html

  <section id="s_task">
  <h3>Task</h3>
  <p>
  gallist -- make an artificial galaxies list
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gallist gallist ngals
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_gallist">
  <dt><b>gallist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gallist' Line='gallist' -->
  <dd>The name of the output text file for the x and y coordinates,
  magnitudes, profile types, half-flux radii, axial ratios, and position
  angles of the artificial galaxies.  Output will be appended to this
  file if it exists.
  </dd>
  </dl>
  <dl id="l_ngals">
  <dt><b>ngals = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngals' Line='ngals = 100' -->
  <dd>The number of galaxies in the output galaxies list.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Examine plots and change the parameters of the spatial, luminosity, and
  morphology distributions interactively.
  </dd>
  </dl>
  <p>
  			SPATIAL DISTRIBUTION
  </p>
  <dl id="l_spatial">
  <dt><b>spatial = <span style="font-family: monospace;">"uniform"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spatial' Line='spatial = "uniform"' -->
  <dd>Type of spatial distribution for the galaxies.  The types are:
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>The galaxies are uniformly distributed between <i>xmin</i>, <i>xmax</i>,
  <i>ymin</i>, and <i>ymax</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>hubble</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='hubble' Line='hubble' -->
  <dd>The galaxies are distributed around the center of symmetry <i>xcenter</i> and
  <i>ycenter</i> according to a Hubble density law of core radius
  <i>core_radius</i> and background density <i>base</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='file' Line='file' -->
  <dd>The radial density function is contained in the text file <i>sfile</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = 1., xmax = 512., ymin = 1., ymax = 512.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = 1., xmax = 512., ymin = 1., ymax = 512.' -->
  <dd>The range of the output coordinates in pixels.
  </dd>
  </dl>
  <dl id="l_xcenter">
  <dt><b>xcenter = INDEF, ycenter = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcenter' Line='xcenter = INDEF, ycenter = INDEF' -->
  <dd>The coordinate of the center of symmetry for the <span style="font-family: monospace;">"hubble"</span>
  and <span style="font-family: monospace;">"file"</span> radial density functions. The default is the
  midpoint of the coordinate limits.
  </dd>
  </dl>
  <dl id="l_core_radius">
  <dt><b>core_radius = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='core_radius' Line='core_radius = 50' -->
  <dd>The core radius of the Hubble density distribution in pixels.
  </dd>
  </dl>
  <dl id="l_base">
  <dt><b>base = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='base' Line='base = 0.0' -->
  <dd>The background density relative to the central density of the Hubble
  density distribution.
  </dd>
  </dl>
  <dl id="l_sseed">
  <dt><b>sseed = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sseed' Line='sseed = 2' -->
  <dd>The initial value supplied to the random number generator used to
  generate the output x and y coordinates.
  If a value of <span style="font-family: monospace;">"INDEF"</span> is given then the clock
  time (integer seconds since 1980) is used as the seed yielding
  different random numbers for each execution.
  </dd>
  </dl>
  <p>
  			MAGNITUDE DISTRIBUTION
  </p>
  <dl id="l_luminosity">
  <dt><b>luminosity = <span style="font-family: monospace;">"powlaw"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='luminosity' Line='luminosity = "powlaw"' -->
  <dd>Type of luminosity distribution for the galaxies.  The types are:
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>The galaxies are uniformly distributed between <i>minmag</i> and
  <i>maxmag</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>powlaw</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='powlaw' Line='powlaw' -->
  <dd>The galaxies are distributed according to a power law with coefficient
  <i>power</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>schecter</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='schecter' Line='schecter' -->
  <dd>The galaxies are distributed according to a Schecter luminosity
  function with characteristic magnitude <i>mstar</i> and power law exponent
  <i>alpha</i> between <i>minmag</i> and <i>maxmag</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='file' Line='file' -->
  <dd>The luminosity function is contained in the text file <i>lfile</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_minmag">
  <dt><b>minmag = -7., maxmag = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minmag' Line='minmag = -7., maxmag = 0.' -->
  <dd>The range of output relative magnitudes.
  </dd>
  </dl>
  <dl id="l_mzero">
  <dt><b>mzero = 15.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mzero' Line='mzero = 15.' -->
  <dd>Magnitude zero point for Schecter luminosity function.
  </dd>
  </dl>
  <dl id="l_power">
  <dt><b>power = 0.6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='power' Line='power = 0.6' -->
  <dd>Coefficient for the power law magnitude distribution The default value
  of 0.6 is the Euclidean value.
  </dd>
  </dl>
  <dl id="l_alpha">
  <dt><b>alpha = -1.24</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='alpha' Line='alpha = -1.24' -->
  <dd>The power law exponent of the Schecter luminosity function.
  The default value is that determined by Schecter from nearby galaxies.
  </dd>
  </dl>
  <dl id="l_mstar">
  <dt><b>mstar = -21.41</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mstar' Line='mstar = -21.41' -->
  <dd>The characteristic magnitude of the Schecter luminosity function.
  </dd>
  </dl>
  <dl id="l_lseed">
  <dt><b>lseed = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lseed' Line='lseed = 2' -->
  <dd>The initial value supplied to the random number generator used to
  generate the output magnitudes.
  If a value of <span style="font-family: monospace;">"INDEF"</span> is given then the clock
  time (integer seconds since 1980) is used as the seed yielding
  different random numbers for each execution.
  </dd>
  </dl>
  <p>
  			MORPHOLOGY DISTRIBUTION
  </p>
  <dl id="l_egalmix">
  <dt><b>egalmix = 0.4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='egalmix' Line='egalmix = 0.4' -->
  <dd>The fraction of the galaxies that are <span style="font-family: monospace;">"ellipticals"</span> represented
  by a de Vaucouleurs surface brightness law as opposed to <span style="font-family: monospace;">"spirals"</span>
  represented by an exponential disk surface brightness law.
  </dd>
  </dl>
  <dl id="l_ar">
  <dt><b>ar = 0.3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ar' Line='ar = 0.3' -->
  <dd>Minimum elliptical galaxy axial ratio (major/minor ratio).
  </dd>
  </dl>
  <dl id="l_eradius">
  <dt><b>eradius = 20.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='eradius' Line='eradius = 20.0' -->
  <dd>The maximum elliptical galaxy half-flux semi-major scale radius.  This is
  the radius of an elliptical galaxy with magnitude <i>minmag</i>
  before a random factor is added.  Spiral galaxies and fainter galaxies
  are scaled from this value.
  </dd>
  </dl>
  <dl id="l_sradius">
  <dt><b>sradius = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sradius' Line='sradius = 1.0' -->
  <dd>Ratio between half-flux scale radii of spiral and elliptical models at the
  same magnitude.  For example an elliptical galaxy with magnitude
  <i>minmag</i> will have radius <i>eradius</i> while a spiral galaxy
  of the same magnitude with have radius <i>sradius</i> * <i>eradius</i>.
  </dd>
  </dl>
  <dl id="l_absorption">
  <dt><b>absorption = 1.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='absorption' Line='absorption = 1.2' -->
  <dd>Absorption correction for edge on spirals in magnitudes.
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z = 0.05</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z' Line='z = 0.05' -->
  <dd>Minimum redshift for power law distributed galaxies.  This is the
  redshift assigned galaxies of magnitude <i>minmag</i>.  The redshifts
  are assumed proportional to the square root of the apparent luminosity;
  i.e the luminosity distance proportional to redshift.  The redshift is used
  for computing the mean apparent sizes of the galaxies
  according to (1+z)**2 / z.
  </dd>
  </dl>
  <p>
  			USER FUNCTIONS
  </p>
  <dl id="l_sfile">
  <dt><b>sfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sfile' Line='sfile = ""' -->
  <dd>The name of the input text file containing the sampled spatial radial
  density
  function, one sample point per line, with the radius and relative probability
  in columns one and two respectively. The sample points need not be
  uniformly spaced or normalized.
  </dd>
  </dl>
  <dl id="l_nssample">
  <dt><b>nssample = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nssample' Line='nssample = 100' -->
  <dd>The number of points at which the spatial density function is 
  sampled. If the spatial density function is analytic or approximated
  analytically (the <span style="font-family: monospace;">"hubble"</span> option) the function is sampled
  directly. If the function is read from a file  (the <span style="font-family: monospace;">"file"</span> option) an
  initial smoothing step is performed before sampling.
  </dd>
  </dl>
  <dl id="l_sorder">
  <dt><b>sorder = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sorder' Line='sorder = 10' -->
  <dd>The order of the spline fits used to evaluate the integrated spatial
  density function.
  </dd>
  </dl>
  <dl id="l_lfile">
  <dt><b>lfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lfile' Line='lfile = ""' -->
  <dd>The name of the input text file containing the sampled luminosity
  function, one sample point per line, with the magnitude and relative
  probability in columns one and two respectively. The sample points need
  not be uniformly spaced or normalized.
  </dd>
  </dl>
  <dl id="l_nlsample">
  <dt><b>nlsample = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlsample' Line='nlsample = 100' -->
  <dd>The number of points at which the luminosity function is 
  sampled. If the luminosity function is analytic or approximated
  analytically (the <span style="font-family: monospace;">"uniform"</span>, <span style="font-family: monospace;">"powlaw"</span> and <span style="font-family: monospace;">"schecter"</span> options) the
  function is sampled directly.  If it is read from a file
  (the <span style="font-family: monospace;">"file"</span> option) an initial smoothing step is performed before sampling.
  </dd>
  </dl>
  <dl id="l_lorder">
  <dt><b>lorder = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lorder' Line='lorder = 10' -->
  <dd>The order of the spline fits used to evaluate the integrated
  luminosity function.
  </dd>
  </dl>
  <p>
  			INTERACTIVE PARAMETERS
  </p>
  <dl id="l_rbinsize">
  <dt><b>rbinsize = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rbinsize' Line='rbinsize = 10.' -->
  <dd>The bin size in pixels of the plotted histogram of the radial density
  distribution.
  </dd>
  </dl>
  <dl id="l_mbinsize">
  <dt><b>mbinsize = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mbinsize' Line='mbinsize = 0.5' -->
  <dd>The bin size in magnitudes of the plotted histogram of the luminosity function.
  </dd>
  </dl>
  <dl id="l_dbinsize">
  <dt><b>dbinsize = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dbinsize' Line='dbinsize = 0.5' -->
  <dd>The bin size in pixels of the plotted histogram of the half-power semi-major
  axis distribution.
  </dd>
  </dl>
  <dl id="l_ebinsize">
  <dt><b>ebinsize = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ebinsize' Line='ebinsize = 0.1' -->
  <dd>The bin size of the plotted histogram of the axial ratio distribution.
  </dd>
  </dl>
  <dl id="l_pbinsize">
  <dt><b>pbinsize = 20.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pbinsize' Line='pbinsize = 20.' -->
  <dd>The bin size in degrees of the plotted histogram of the position angle
  distribution.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = stdgraph</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = stdgraph' -->
  <dd>The default graphics device.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>The graphics cursor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Gallist</b> generates a list of x and y coordinates, magnitudes,
  morphological types, half-power radii, axial ratios, and position
  angles for a sample of <i>ngals</i> galaxies based on a user selected
  spatial density function <i>spatial</i>  and luminosity function
  <i>luminosity</i> and writes (appends) the results to the text file
  <i>gallist</i>. If the <i>interactive</i> parameter is <span style="font-family: monospace;">"yes"</span> the user can
  interactively examine plots of the spatial density function, the
  radial density function,  the luminosity function, radii, axial ratios,
  and position angle distributions and alter the parameters of the task
  until a satisfactory artificial field is generated.
  </p>
  <p>
  The spatial density function generates x and y values around a center
  of symmetry defined by <i>xcenter</i> and <i>ycenter</i> within the x and
  y limits <i>xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> according to
  the spatial density function specified by <i>spatial</i>.  The three
  supported spatial density functions are listed below where R is the
  radial distance in pixels, P is the relative spatial density, C is a
  constant, and f is the best fitting cubic spline function to the spatial
  density function R(user), P(user) supplied by the user in the text file
  <i>sfile</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  uniform:  P = C
  hubble:   P = 1.0 / (1 + R / core_radius) ** 2 + base
  file:     P = f (R(user), P(user))
  </pre></div>
  <p>
  The Hubble and user spatial density functions are sampled at
  <i>nssample</i> equally spaced points, and integrated to give the
  spatial density probability function at each sampled point. The
  integrated probability function is normalized and approximated by a
  cubic spline of order <i>sorder</i>.  The x and y coordinates are
  computed by randomly sampling the integrated probability function until
  <i>ngals</i> galaxies which satisfy the x and y coordinate limits
  <i>xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> are generated.
  </p>
  <p>
  The luminosity function generates relative magnitude values between
  <i>minmag</i> and <i>maxmag</i> (before absorption effects are added)
  according to the luminosity function specified by <i>luminosity</i>.
  The four supported luminosity functions are listed below where M is the
  magnitude, P is the relative luminosity function, C is a constant and f
  is the best fitting cubic spline function to the luminosity function
  M(user), P(user) supplied by the user in the text file <i>lfile</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  uniform:   P = C
  powlaw:    P = C * 10. ** (power * M)
  schecter:  P = C * 10. ** (alpha * dM) * exp (-10. ** dM)
  file:      P = f (M(user), P(user))
  
  where      dM = 0.4 * (mstar - M + mzero)
  </pre></div>
  <p>
  The uniform distribution is not very physical but may be useful for
  testing.  The power law distribution is that expected for a homogeneous
  and isotropic distribution of galaxies.  The default value of 0.6 is
  that which can be calculated simply from Euclidean geometry.  Observations
  of faint galaxies generally show a smaller value.  The Schecter
  function provides a good approximation to a galaxy cluster when
  used in conjunction with the Hubble spatial distribution (though there
  is no mass segregation applied).  The <span style="font-family: monospace;">"best fit"</span> values for the
  parameters <i>mstar</i> and <i>alpha</i> are taken from the paper by
  Schecter (Ap.J 203, 297, 1976).  The <i>mzero</i> parameter is used
  to convert to absolute magnitudes.  Note that it is equivalent to
  set <i>mzero</i> to zero and adjust the characteristic magnitude
  to the same relative magnitude scale or to use absolute magnitudes
  directly.
  </p>
  <p>
  The Schecter and user file distributions are sampled at <i>nlsample</i>
  equally spaced points, and integrated to give the luminosity
  probability function at each sampled point. The probability function is
  normalized and approximated by a cubic spline of order <i>lorder</i>.
  The magnitudes are computed by randomly sampling the integrated
  probability function until <i>ngals</i> objects which satisfy the
  magnitude limits <i>minmag</i> and <i>maxmag</i> are generated.
  </p>
  <p>
  The artificial galaxies have one of two morphological types,
  <span style="font-family: monospace;">"ellipticals"</span> with a de Vaucouleurs surface brightness law and
  <span style="font-family: monospace;">"spirals"</span> with an exponential surface brightness law. The fraction
  of elliptical galaxies is set by the parameter <i>egalmix</i>.  The
  position angles of the major axis are distributed uniformly between 0.0
  and 360.0 degrees.  The axial ratio (major to minor) of the elliptical
  models is allowed to range uniformly between 1 and <i>ar</i>
  (that is E0 - E7).
  </p>
  <p>
  The spiral models have inclinations, i, ranging uniformly between 0 and
  90 degrees.  The axial ratio is then given by
  </p>
  <p>
  	a/b = sqrt (sin(i)**2 * .99 + .01)
  </p>
  <p>
  which is taken from Holmberg in Galaxies and the Universe (which
  references the work of Hubble).  Note the axial ratio is limited to
  0.1 by this formula.  An internal absorption correction is then
  made based on the inclination using the relation
  </p>
  <p>
  	dM = A * (min (10, cosecant (i)) - 1) / 9
  </p>
  <p>
  where is the absorption of an edge on galaxy relative to face on and
  the cosecant is limited to 10.  Note that this correction changes
  allows galaxies with magnitudes less than <i>maxmag</i> and alters
  the luminosity function somewhat.  Or in other words, the luminosity
  function is based on absorption corrected magnitudes.
  </p>
  <p>
  The sizes of the galaxy images are scaled from the maximum half-flux
  radius of an elliptical galaxy given by the parameter <i>eradius</i>.
  This is the radius given to an elliptical galaxy of magnitude
  <i>minmag</i> (prior to adding a random factor described below).  The
  ratio between the half-flux radii of the exponential disk and de
  Vaucouleurs models at a given total magnitude is set by the parameter
  <i>sradius</i> (note this is a fraction of <i>eradius</i> and not an
  actual radius).  This allows adjusting the relative surface brightness
  of elliptical and spiral models.
  </p>
  <p>
  The distribution of sizes is based on the apparent
  magnitude of the galaxies.  For the power law magnitude distribution
  the cosmological redshift factor for angular diameters is used.  The
  redshift/magnitude relation is assumed to be such that the redshift is
  proportional to the luminosity distance (the square root of the
  apparent luminosity).  Thus,
  </p>
  <div class="highlight-default-notranslate"><pre>
                Z = z * 10. ** (0.2 * (M - minmag))
                Zfactor = ((1+Z)**2 / Z) / ((1+z)**2 / z)
  ellipticals:  r = eradisus * Zfactor
  spirals:      r = sradius * eradius * Zfactor
  </pre></div>
  <p>
  where z is the reference redshift at the minimum magnitude, and Z is the
  redshift at magnitude M.  For very small z the size varies as the
  luminosity distance but at larger z the images appear more extended with
  lower surface brightness.  For very deep simulations a pure luminosity
  distance relation gives faint galaxies which are too small and compact
  compared to actual observations.
  </p>
  <p>
  For the other magnitude distributions, the Schecter cluster function
  in particular where all galaxies are at the same distance, the scale radius
  obeys the following relation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ellipticals:  r = eradius * 10. ** ((minmag - M) / 6)
  spirals:      r = sradius * eradius * 10. ** ((minmag - M) / 6)
  </pre></div>
  <p>
  This relation gives the size decreasing slightly less rapidly than that
  giving a constant surface brightness.  This relation is taken from
  Holmberg (Galaxies and the Universe).
  </p>
  <p>
  A uniform random factor of 50% is added to the sizes computed for
  the power law magnitude distribution and 20% for the other distributions.
  </p>
  <p>
  The interactive spatial plot shows the positions of the galaxies, the
  galaxy type (circles are de Vaucouleurs profiles and other types are
  diamonds), and rough size.
  </p>
  </section>
  <section id="s_cursors">
  <h3>Cursors</h3>
  <p>
  The following interactive keystroke commands are available from within the
  GALLIST task.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Gallist Keystroke Commands
  
  ?       Print options
  f       Fit one or more of following
              Spatial density function (SDF)
              Luminosity  function (LF)
              Distribution of morphological type
              Diameter distribution
              Roundness distribution
              Position angle distribution
  x       Plot the x-y spatial density function
  r       Plot the histogram of the radial density function
  m       Plot the histogram of the luminosity function
  d       Plot the histogram of the diameter values
  e       Plot the histogram of the roundness values
  p       Plot the histogram of the position angle values
  :       Colon escape commands (see below)
  q       Exit program
  </pre></div>
  <p>
  The following parameters can be shown or set from within the GALLIST task.
  </p>
  <div class="highlight-default-notranslate"><pre>
                  Gallist Colon Commands
  
  :show                   Show gallist parameters
  :ngal       [value]     Number of galaxies
  
  :spatial    [string]    Spatial density function (SDF) (uniform|hubble|file)
  :xmin       [value]     Minimum X value
  :xmax       [value]     Maximum X value
  :ymin       [value]     Minimum Y value
  :ymax       [value]     Maximum Y value
  :xcenter    [value]     X center for SDF
  :ycenter    [value]     Y center for SDF
  :core       [value]     Core radius for Hubble density function
  :base       [value]     Background density for Hubble density function
  
  :luminosity [string]    Luminosity function (LF)
                          (uniform|powlaw|schecter|file)
  :minmag     [value]     Minimum magnitude
  :maxmag     [value]     Maximum magnitude
  :mzero      [value]     Magnitude zero-point of schecter LF
  :power      [value]     Power law coefficient for powlaw LF
  :alpha      [value]     Schecter parameter
  :mstar      [value]     Characteristic mag for Schecter LF
  
  :egalmix    [value]     Elliptical/Spiral galaxy ratio
  :ar         [value]     Minimum elliptical galaxy axial ratio
  :eradius    [value]     Maximum elliptical half flux radius
  :sradius    [value]     Spiral/elliptical radius at same magnitude
  :z          [value]     Minimum redshift
  :absorption [value]     Absorption correction for spirals
  
  :lfile      [string]    Name of the LF file
  :sfile      [string]    Name of the SDF file
  :nlsample   [value]     Number of LF sample points
  :lorder     [value]     Order of spline approximation to the integrated LF
  :nssample   [value]     Number of SDF sample points
  :sorder     [value]     Order of spline approximation to the integrated SDF
  
  :rbinsize   [value]     Resolution of radial SDF histogram in pixels
  :mbinsize   [value]     Resolution of magnitude histogram in magnitudes
  :dbinsize   [value]     Resolution of diameter histogram in pixels
  :ebinsize   [value]     Resolution of roundness histogram in pixels
  :pbinsize   [value]     Resolution of position angle histogram in degrees
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a galaxy cluster with a power law distribution of field galaxies
  and stars as background/foreground.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; gallist galaxies.dat 100 spatial=hubble lum=schecter egal=.8
  ar&gt; gallist galaxies.dat 500
  ar&gt; starlist galaxies.dat 100
  ar&gt; mkobjects galaxies obj=galaxies.dat gain=3 rdnoise=10 poisson+
  </pre></div>
  <p>
  Note that the objects are appended to the same file.  Actually making
  the image with <b>mkobjects</b> takes about 5 minutes (2.5 min cpu) on a
  SPARCstation 1.
  </p>
  <p>
  2. Examine the distributions for a uniform spatial distribution
  and power law magnitude distribution using 1000 galaxies without
  creating a data file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; gallist dev$null 1000 inter+
          ... an x-y plot will appear on the screen
          ... type r to examine the radial density function
          ... type m to examine the luminosity function
          ... type d to examine the half-flux radii distribution
          ... type e to examine the axial ratio distribution
          ... type = to make a copy of any of the plots
          ... type q to quit
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_GALLIST">
  <dt><b>GALLIST V2.11+</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='GALLIST' Line='GALLIST V2.11+' -->
  <dd>The random number seeds can be set from the clock time by using the value
  <span style="font-family: monospace;">"INDEF"</span> to yield different random numbers for each execution.
  </dd>
  </dl>
  <dl id="l_GALLIST">
  <dt><b>GALLIST V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='GALLIST' Line='GALLIST V2.11' -->
  <dd>The default value for the minimum elliptical galaxy axial ratio was
  change to 0.3 to cover the range E0-E7 uniformly.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  This is a first version and is not intended to produce a full model
  of galaxy fields.  Some of the relations used are empirical and
  simple minded with the aim being to produce reasonably realistic images.
  </p>
  <p>
  The spline approximation to the spatial density and luminosity
  probability functions can cause wiggles in the output spatial density
  and luminosity functions. Users can examine the results interactively
  and experiment with the spline order and number of sample points if
  they are not satisfied with the results of GALLIST. The default setup
  of 10 sample points per spline piece is generally satisfactory for the
  spatial density and luminosity functions supplied here.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  starlist mkobjects
  </p>
  
  </section>
  
  <!-- Contents: 'TASK' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSORS' 'EXAMPLES' 'REVISIONS' 'BUGS' 'SEE ALSO'  -->
  
