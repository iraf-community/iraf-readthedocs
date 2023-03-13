.. _starlist:

starlist: Make an artificial star list
======================================

**Package: artdata**

.. raw:: html

  <section id="s_task">
  <h3>Task</h3>
  <p>
  starlist -- make an artificial star list
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  starlist starlist nstars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_starlist">
  <dt><b>starlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='starlist' Line='starlist' -->
  <dd>The name of the output text file for the x and y coordinates
  and magnitudes of the artificial stars.  Output will be appended to this
  file is it exists.
  </dd>
  </dl>
  <dl id="l_nstars">
  <dt><b>nstars = 5000</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nstars' Line='nstars = 5000' -->
  <dd>The number of stars in the output star list.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Examine plots and change the parameters of the spatial luminosity
  distributions interactively.
  </dd>
  </dl>
  <p>
  			SPATIAL DISTRIBUTION
  </p>
  <dl id="l_spatial">
  <dt><b>spatial = <span style="font-family: monospace;">"uniform"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spatial' Line='spatial = "uniform"' -->
  <dd>Type of spatial distribution.  The types are:
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>The stars are uniformly distributed between <i>xmin</i>, <i>xmax</i>, <i>ymin</i>,
  and <i>ymax</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>hubble</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='hubble' Line='hubble' -->
  <dd>The stars are distributed around the center of symmetry <i>xcenter</i> and
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
  <dd>The range of output coordinates in x and y.
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
  <dt><b>core_radius = 30</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='core_radius' Line='core_radius = 30' -->
  <dd>The core radius of the Hubble spatial distribution in pixels.
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
  <dt><b>sseed = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sseed' Line='sseed = 1' -->
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
  <dd>Type of luminosity distribution.  The types are:
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>The stars are uniformly distributed between <i>minmag</i> and <i>maxmag</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>powlaw</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='powlaw' Line='powlaw' -->
  <dd>The stars are distributed according to a power law with coefficient
  <i>power</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>salpeter</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='salpeter' Line='salpeter' -->
  <dd>The stars are distributed with a Salpeter luminosity function between
  <i>minmag</i> and <i>maxmag</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>bands</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='bands' Line='bands' -->
  <dd>The stars are distributed with a Bahcall and Soneira luminosity function
  between <i>minmag</i> and <i>maxmag</i>.  The function is described
  by the parameters <i>alpha</i>, <i>beta</i>, <i>delta</i> and <i>mstar</i>
  whose default values give a best fit to the observed main sequence in several
  nearby globular clusters.
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
  <dd>The range of output magnitudes.  The <span style="font-family: monospace;">"salpeter"</span> luminosity function
  imposes limits of -4 and 16 and the <span style="font-family: monospace;">"bands"</span> luminosity function
  imposes limits of -7 and 17 relative to the zero point given by
  <i>mzero</i>.
  </dd>
  </dl>
  <dl id="l_mzero">
  <dt><b>mzero = -4.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mzero' Line='mzero = -4.' -->
  <dd>The zero point for converting the output relative magnitudes
  to absolute magnitudes for the Salpeter and Bahcall and Soneira
  luminosity functions.  For example the default values give an
  absolute magnitude range of -3 to +4.
  </dd>
  </dl>
  <dl id="l_power">
  <dt><b>power = 0.6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='power' Line='power = 0.6' -->
  <dd>Coefficient for the power law magnitude distribution.
  The default value of 0.6 is the value for a homogeneous
  and isotropic distribution with no cutoff in distance.
  </dd>
  </dl>
  <dl id="l_alpha">
  <dt><b>alpha = 0.74, beta = 0.04, delta = 0.294, mstar = 1.28</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='alpha' Line='alpha = 0.74, beta = 0.04, delta = 0.294, mstar = 1.28' -->
  <dd>The parameters of the Bahcall and Soneira luminosity function.
  </dd>
  </dl>
  <dl id="l_lseed">
  <dt><b>lseed = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lseed' Line='lseed = 1' -->
  <dd>The initial value supplied to the random number generator used to
  generate the output magnitudes.
  If a value of <span style="font-family: monospace;">"INDEF"</span> is given then the clock
  time (integer seconds since 1980) is used as the seed yielding
  different random numbers for each execution.
  </dd>
  </dl>
  <p>
  			USER FUNCTIONS
  </p>
  <dl id="l_sfile">
  <dt><b>sfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sfile' Line='sfile' -->
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
  <dd>The number of points at which the <i>spatial</i> density function is 
  sampled. If the <i>spatial</i> density function is analytic or approximated
  analytically (the <span style="font-family: monospace;">"uniform"</span> and <span style="font-family: monospace;">"hubble"</span> options) the function is sampled
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
  <dt><b>lfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lfile' Line='lfile' -->
  <dd>The name of the input text file containing the sampled luminosity
  function, one sample point per line, with the magnitude and relative probability
  in columns one and two respectively. The sample points need not be
  uniformly spaced or normalized.
  </dd>
  </dl>
  <dl id="l_nlsample">
  <dt><b>nlsample = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlsample' Line='nlsample = 100' -->
  <dd>The number of points at which the luminosity function is sampled. If
  the luminosity function is analytic or approximated analytically (the
  <span style="font-family: monospace;">"salpeter"</span> and <span style="font-family: monospace;">"bands"</span> options) the function is sampled directly.  If
  it is read from a file  (the <span style="font-family: monospace;">"file"</span> option) an initial smoothing step
  is performed before sampling.
  </dd>
  </dl>
  <dl id="l_lorder">
  <dt><b>lorder = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lorder' Line='lorder = 10' -->
  <dd>The order of the spline fits used to evaluate the integrated
  <i>luminosity</i> function.
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
  <b>Starlist</b> generates a list of x and y coordinates and magnitudes
  for a sample of <i>nstars</i> stars based on a user selected spatial
  density function <i>spatial</i>  and luminosity function
  <i>luminosity</i> and writes (appends) the results to the text file
  <i>starlist</i>. If the <i>interactive</i> parameter is <span style="font-family: monospace;">"yes"</span> the user
  can interactively examine plots of the spatial density function,
  the radial density function, and the luminosity function, and alter the
  parameters of the task until a satisfactory artificial field is
  generated.
  </p>
  <p>
  The spatial density function generates x and y values around a center
  of symmetry defined by <i>xcenter</i> and <i>ycenter</i> within the x and
  y limits <i>xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> according to
  the spatial density function specified by <i>spatial</i>.  The three
  supported spatial density functions are listed below where R is the
  radial distance in pixels, P is the relative spatial density, C is a
  constant and f is the best fitting cubic spline function to the spatial
  density function R(user), P(user) supplied by the user in the text file
  <i>sfile</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  uniform:  P = C
  hubble:   P = 1.0 / (1 + R / core_radius) ** 2 + base
  file:     P = f (R(user), P(user))
  </pre></div>
  <p>
  The Hubble and user file spatial density function are sampled at
  <i>nssample</i> equally spaced points, and integrated to give the
  spatial density probability function at each sampled point. The
  integrated probability function is normalized and approximated by a
  cubic spline of order <i>sorder</i>.  The x and y coordinates are
  computed by randomly sampling the integrated probability function until
  <i>nstars</i> stars which satisfy the x and y coordinate limits
  <i>xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> are generated.
  </p>
  <p>
  The luminosity function generates relative magnitude values between
  <i>minmag</i> and <i>maxmag</i> according to the luminosity function
  specified by <i>luminosity</i>.  The four supported luminosity functions
  are defined below where M is the magnitude, P is the relative luminosity
  function, C is a constant and f is the best fitting cubic spline
  function to the luminosity function M(user), P(user) supplied by the
  in the text file <i>lfile</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  uniform:  P = C
  
  powlaw:   P = C * 10. ** (power * M)
  
  salpeter: P = C * 10. ** (-3.158 + 1.551e-1*dM - 5.194e-3*dM**2)
  
            dM = M - mzero
  
                             C * 10. ** (beta * dM)
  bands:   P =  --------------------------------------------------
               (1. + 10. ** ((beta-alpha)*delta*dM))) ** 1. /delta
  
           dM = M - mstar - mzero
  
  file:    P = f (M(user), P(user))
  </pre></div>
  <p>
  The Salpeter and <span style="font-family: monospace;">"bands"</span> functions are defined in terms of absolute
  magnitudes so the parameter <i>mzero</i> is used to convert from
  relative magnitudes.  Equivalently, one could use absolute magnitudes
  for the magnitude limits while setting the zero point to 0.
  </p>
  <p>
  The luminosity function is sampled at <i>nlsample</i> equally spaced
  points, and integrated to give the luminosity probability function at
  each sampled point. The probablity function is normalized and
  approximated by a cubic spline of order <i>lorder</i>. The magnitudes
  are computed by randomly sampling the integrated probability function
  until <i>nstars</i> objects which satisfy the magnitude limits
  <i>minmag</i> and <i>maxmag</i> are generated.  The Salpeter luminosity
  is a best fit function to the data of McCuskey (McCuskey, 1966, Vistas
  Astr. 7, 141). The Bahcall and Soneira function and the default values
  of the parameters are discussed by Bahcall and Soneira (Ap.J.  Supp. 44, 73).
  </p>
  </section>
  <section id="s_cursors">
  <h3>Cursors</h3>
  <p>
  The following interactive keystroke commands are available from within the
  STARLIST task.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Starlist Keystroke Commands
  
  ?       Print options
  f       Fit  one or more of the following
              Spatial density function (SDF)
              Luminosity functions (LF)
  x       Plot the x-y spatial density function
  r       Plot the histogram of the radial density function
  m       Plot the histogram of the luminosity function
  :       Colon escape commands (see below)
  q       Exit program
  </pre></div>
  <p>
  The following parameters can be shown or set from within the STARLIST task.
  </p>
  <div class="highlight-default-notranslate"><pre>
                  Starlist Colon Commands
  
  :show                   Show starlist parameters
  :nstars     [value]     Number of stars
  
  :spatial    [string]    Spatial density function (SDF)
                          (uniform|hubble|file)
  :xmin       [value]     Minimum X value
  :xmax       [value]     Maximum X value
  :ymin       [value]     Minimum Y value
  :ymax       [value]     Maximum Y value
  :xcenter    [value]     X center for SDF
  :ycenter    [value]     Y center for SDF
  :core       [value]     Core radius for Hubble density function
  :base       [value]     Background density for Hubble density function
  
  :luminosity [string]    Luminosity function (LF)
                          (uniform|powlaw|salpeter|bands|file)
  :minmag     [value]     Minimum magnitude
  :maxmag     [value]     Maximum magnitude
  :mzero      [value]     Magnitude zero-point for salpeter and bands LF
  :power      [value]     Exponent for powlaw LF
  :alpha      [value]     Alpha parameter for bands LF
  :beta       [value]     Beta parameter for bands LF
  :delta      [value]     Delta parameter for bands LF
  :mstar      [value]     Mstar parameter for bands LF
  
  :sfile      [string]    File containing the user SDF
  :nssample   [value]     Number of SDF sample points
  :sorder     [value]     Order of spline fit to integrated SDF
  :lfile      [string]    File containing the user LF
  :nlsample   [value]     Number of LF sample points
  :lorder     [value]     Order of spline fit to the integrated LF
  
  :rbinsize   [value]     Resolution of radial profile histogram (pixels)
  :mbinsize   [value]     Resolution of magnitude histogram (mag)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a uniform artificial starfield of 5000 stars for a 512 square image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; starlist starfield.dat 5000
  ar&gt; mkobjects starfield obj=starfield.dat gain=2 rdnoise=10 poisson+
  </pre></div>
  <p>
  This example takes about a minute on a SPARCstation 1.
  </p>
  <p>
  2. Create a globular cluster field of 5000 stars for a 512 square image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; starlist gc.dat 5000 spat=hubble lum=bands
  ar&gt; mkobjects starfield obj=gc.dat gain=2 rdnoise=10 poisson+
  </pre></div>
  <p>
  This example takes about a minute on a SPARCstation 1.
  </p>
  <p>
  3. Examine the distributions for a Hubble spatial distribution
  and Salpeter magnitude distribution using 1000 stars without
  creating a data file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; starlist dev$null 1000 inter+ spat=hubble lum=salpeter
          ... an x-y plot will appear on the screen
          ... type r to examine the radial density function
          ... type m to examine the luminosity function
          ... type = to make a copy of any of the plots
          ... type q to quit
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_STARLIST">
  <dt><b>STARLIST V2.11+</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='STARLIST' Line='STARLIST V2.11+' -->
  <dd>The random number seeds can be set from the clock time by using the value
  <span style="font-family: monospace;">"INDEF"</span> to yield different random numbers for each execution.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The spline approximation to the spatial density and luminosity
  probability functions can  cause wiggles in the output spatial density
  and luminosity functions. Users can examine the results interactively
  and experiment with the spline order and number of sample points if
  they are not satisfied with the results of STARLIST. The default setup
  of 10 sample points per spline piece is generally satisfactory for the
  spatial density and luminosity functions supplied here.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gallist mkobjects
  </p>
  
  </section>
  
  <!-- Contents: 'TASK' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSORS' 'EXAMPLES' 'REVISIONS' 'BUGS' 'SEE ALSO'  -->
  
