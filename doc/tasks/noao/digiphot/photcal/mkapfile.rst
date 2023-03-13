.. _mkapfile:

mkapfile: Prepare  aperture corrections file from apphot/daophot output
=======================================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkapfile photfiles naperts apercors
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_photfiles">
  <dt><b>photfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photfiles' Line='photfiles' -->
  <dd>A list of APPHOT photometry files containing the images names or image ids, x-y
  coordinates, filter ids, exposure times, airmasses, aperture radii,
  magnitudes, and magnitude errors
  of all the objects to be used to compute the aperture corrections.
  </dd>
  </dl>
  <dl id="l_naperts">
  <dt><b>naperts</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naperts' Line='naperts' -->
  <dd>The number of aperture radii for which aperture radii, magnitudes, and
  magnitude errors are to be extracted from <i>photfiles</i>.
  </dd>
  </dl>
  <dl id="l_apercors">
  <dt><b>apercors</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apercors' Line='apercors' -->
  <dd>The name of the output text file containing the aperture
  corrections computed between <i>smallap</i> and <i>largeap</i>
  for each image in <i>photfiles</i>.
  </dd>
  </dl>
  <dl id="l_smallap">
  <dt><b>smallap = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='smallap' Line='smallap = 1' -->
  <dd>The index of the smallest extracted aperture for which the aperture 
  correction is to be computed.
  </dd>
  </dl>
  <dl id="l_largeap">
  <dt><b>largeap = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='largeap' Line='largeap = 0' -->
  <dd>The index of the largest extracted aperture for which the aperture 
  correction is to be computed. If <i>largeap</i> is 0, then
  the largest aperture is <i>naperts</i>.
  </dd>
  </dl>
  <dl id="l_magfile">
  <dt><b>magfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magfile' Line='magfile = ""' -->
  <dd>The name of an optional output text file containing the magnitudes
  of all the stars in <i>photfiles</i>, corrected to the aperture <i>largeap</i>
  by using the measured magnitude and computed aperture correction at
  which the estimated error is a minimum.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>The name of an optional output text file containing details of the curve
  of growth model fit for each image in <i>photfiles</i>. If <i>logfile</i> is
  <span style="font-family: monospace;">""</span>, no file is written.  If <i>append</i> = <span style="font-family: monospace;">"no"</span> a new logfile is written, if
  <span style="font-family: monospace;">"yes"</span> output is appended to an existing logfile.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>The name of an optional output plot file containing plots of the
  curve of growth model fit, the fit residuals versus aperture radius,
  magnitude inside the first aperture, x coordinate, and y coordinate,
  and the aperture correction versus aperture radius for each image
  in <i>photfiles</i>. If <i>plotfile</i> is <span style="font-family: monospace;">""</span>, no file is written.
  If <i>append</i> = <span style="font-family: monospace;">"no"</span> a new plotfile is written, if
  <span style="font-family: monospace;">"yes"</span> output is appended to an existing plotfile.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Open <i>logfile</i> and/or <i>plotfile</i> in append mode ?
  </dd>
  </dl>
  <dl id="l_obsparams">
  <dt><b>obsparams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsparams' Line='obsparams = ""' -->
  <dd>The name of an optional input text file containing the correct filter ids,
  exposure times, and airmasses for each image whose values are either
  undefined or incorrectly stored in <i>photfiles</i>. The observing parameters
  for each image are listed in <i>obsparams</i>,
  1 image per line with the image name in column 1 and the filter id,
  exposure time, and airmass in
  <i>obscolumns</i>. The image names must match those in <i>photfiles</i>.
  </dd>
  </dl>
  <dl id="l_obscolumns">
  <dt><b>obscolumns = <span style="font-family: monospace;">"2 3 4 5"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obscolumns' Line='obscolumns = "2 3 4 5"' -->
  <dd>The list of numbers separated by commas or whitespace specifying which
  columns in the text file <i>obsparams</i> contain the correct filter ids,
  exposure times, airmasses, and times of observation respectively. The
  number 0 can be used as
  a place holder in the obscolumns string. For example to correct only
  the <i>photfiles</i> airmass values, <i>obscolumns</i> should be set to
  <span style="font-family: monospace;">"0 0 column 0"</span>, where column is the airmass column number.
  </dd>
  </dl>
  <dl id="l_maglim">
  <dt><b>maglim = 0.10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maglim' Line='maglim = 0.10' -->
  <dd>The maximum magnitude error permitted in the input magnitude measurements.
  Data at and following the first aperture radius whose associated magnitude
  measurement has an error greater than <i>magerr</i> is rejected on input.
  </dd>
  </dl>
  <dl id="l_nparams">
  <dt><b>nparams = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nparams' Line='nparams = 3' -->
  <dd>The number parameters in the five parameter curve of growth model to be fit.
  The remaining parameters 5 - nparams parameters are held constant.
  For <i>nparams</i> = 3, the parameters <i>swings</i>,
  <i>pwings</i>, and <i>pgauss</i> are fit, and <i>rgescale</i> and 
  and <i>xwings</i> maintain their default values.
  <i>Nparams</i> must be greater than or equal to one.
  </dd>
  </dl>
  <dl id="l_swings">
  <dt><b>swings = 1.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='swings' Line='swings = 1.2' -->
  <dd>The slope of the power law component of the analytic curve of growth model
  describing the seeing independent part of the stellar profile. For a
  physically reasonable profile <i>swings</i> must be greater than 1.
  </dd>
  </dl>
  <dl id="l_pwings">
  <dt><b>pwings = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pwings' Line='pwings = 0.1' -->
  <dd>The fraction of the total power in the seeing independent
  part of the stellar profile, if <i>xwings</i> is 0.0.
  </dd>
  </dl>
  <dl id="l_pgauss">
  <dt><b>pgauss = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pgauss' Line='pgauss = 0.5' -->
  <dd>The fraction of the total power in the seeing dependent part of the
  profile contained in the gaussian rather than the exponential component
  of the analytic curve of growth function.
  </dd>
  </dl>
  <dl id="l_rgescale">
  <dt><b>rgescale = 0.9</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rgescale' Line='rgescale = 0.9' -->
  <dd>The ratio of the exponential to the gaussian radial scale
  lengths in the seeing dependent part of the profile.
  In practice the curve of growth model fits for most data do not depend
  significantly on this parameter and it can be left at its default value.
  </dd>
  </dl>
  <dl id="l_xwings">
  <dt><b>xwings = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xwings' Line='xwings = 0.0' -->
  <dd>A parameter describing the effect of airmass on the total power 
  in the seeing independent part of the stellar profile, where this quantity
  is defined as defined as <i>pwings</i> + <i>xwings</i> * <i>airmass</i>.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Fit the curve of growth interactively ?
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Verify interactive user input ? This option is used only if <i>obsparams</i>
  is set to the standard input STDIN.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The interactive graphics cursor.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The default graphics device.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKAPFILE takes a list of APPHOT photometry files <i>photfiles</i>, 
  containing the image names, x and y coordinates, filter ids, exposure times,
  airmasses, aperture radii, measured magnitudes, and magnitude errors for
  one or more stars in one or more images, computes the aperture correction
  between the apertures <i>smallap</i> and <i>largeap</i> for each image using
  a weighted average of the computed model curve of growth and the observed
  curve of growth, and writes the computed aperture corrections
  to <i>apercors</i>.
  </p>
  <p>
  MKAPFILE computes the aperture corrections by performing the following steps:
  1) extracts the image names,  x and y coordinates, filter ids, exposure
  times, airmasses, times of observation, and <i>naperts</i> aperture radii,
  measured magnitudes,
  and magnitude errors for all the objects in <i>photfiles</i>, 2) rejects data
  for all aperture radii greater than any aperture radius for which the magnitude
  or magnitude error is INDEF, the magnitude error is &gt; <i>maglim</i>,
  or the number of apertures left containing good data is &lt; 2, 
  3) adds in quadrature a magnitude error of 0.001 magnitudes to the extracted
  magnitude errors, 4) edits any incorrect or undefined values of
  the filter id, exposure time, airmass, and time of observation
  in <i>photfiles</i> using the values
  in <i>obsparams</i> if defined, or default values of INDEF, 1.0, 1.25, and INDEF
  respectively, 5) computes the theoretical and observed curve of growth
  curve for each image, 6) computes the adopted curve of growth for each
  image by combining the theoretical and observed curves with weights that
  favor the observed curve at smaller aperture radii and the theoretical curve
  at larger aperture radii, 7) integrates the adopted growth curve between
  the <i>smallap</i> and <i>largeap</i> apertures to
  compute the final aperture correction, 8) writes the results for each image
  to <i>apercors</i>, 9) optionally computes magnitudes for all the stars
  in <i>photfiles</i> corrected to <i>largeap</i> using the observed magnitude
  and computed correction for which the signal to noise is highest,
  10) optionally writes a <i>logfile</i> containing the details of the
  fit for all the individual images, 11) optionally writes a file of
  plots of the fit, the residuals, and the curve of growth for all the
  images.
  </p>
  <p>
  MKAPFILE extracts the fields/columns IMAGE, XCENTER, YCENTER, IFILTER,
  ITIME, XAIRMASS, OTIME, RAPERT, MAG and MERR from <i>photfiles</i>.
  The number of aperture radii,
  magnitudes, and magnitude errors extracted are specified by <i>naperts</i>.
  For example if <i>naperts</i>
  is 15, then the first 15 values of RAPERT, MAG, and MERR are extracted
  from <i>photfiles</i>.
  </p>
  <p>
  Values of the filter ids, exposure times, airmasses, and times of
  observation which are undefined
  or incorrect in <i>photfiles</i>, can be entered or corrected by reading values
  from the file <i>obsparams</i>, a simple multi-column text file with a
  format specified by <i>obscolumns</i>.
  If no values are read from <i>photfiles</i> or <i>obsparams</i>, default values
  for the filter id, exposure time, airmass, and time of observation
  of <span style="font-family: monospace;">"INDEF"</span>, 1.0, 1.25, and INDEF respectively will be assigned.
  It must be emphasized that the airmass is actually used in the curve of
  growth analysis only if <i>nparams</i> is equal to
  5, and that the quantities filter id, exposure time, and time of observation
  are not used in
  the analysis at all. However if the user should wish to use the corrected
  magnitudes optionally computed and written to <i>magfile</i> in any subsequent
  analysis it is important to include the correct values of
  these quantities in <i>magfile</i>. 
  </p>
  <p>
  If <i>interactive</i> is <span style="font-family: monospace;">"yes"</span>, the user can interact with the curve of
  growth fitting process by examining plots of the model fit, the residuals
  versus aperture radius, magnitude in the first aperture, x and y coordinates,
  and the aperture correction
  as a function of radius, by changing the number of parameters to be fit and
  their initial values, deleting and undeleting points with the graphics
  cursor, refitting the model curve of growth and reexamining the results
  until satisfied. Users should realize when deleting or undeleting points
  with the graphics cursor that all
  the apertures above the marked point will be deleted or undeleted.
  </p>
  <p>
  The output aperture corrections file <i>apercors</i> is a simple text
  file containing the image name in column 1, the aperture correction
  computed from <i>smallap</i> to <i>largeap</i> in column 2, and the
  estimated error in the aperture correction in column 3.
  The sign of the aperture correction is such that the
  correction must be added to the observed magnitude to compute the corrected
  magnitude. <i>Apercors</i> is written in a form suitable for input to
  the MKNOBSILE, MKOBSFILE, or OBSFILE tasks.
  </p>
  <p>
  If <i>magfile</i> is not <span style="font-family: monospace;">""</span>, a file containing the image name, x and y
  position, filter id, exposure time, airmass, time observation,
  magnitude corrected to
  <i>largeap</i> using the observed magnitude and computed correction at the
  aperture radius with the highest signal-to-noise ratio, the associated
  magnitude error, and the radius to which the correction was made,
  for all the stars in all the images in <i>photfiles</i>.
  <i>Magfile</i> is written in a form suitable for input to the OBSFILE task.
  </p>
  <p>
  If <i>logfile</i> is not <span style="font-family: monospace;">""</span>, all the details and diagnostics of the
  curve of growth fit are logged either to a new file, if <i>append</i> = <span style="font-family: monospace;">"no"</span>
  or to a previously existing file, <i>append</i> = <span style="font-family: monospace;">"yes"</span>. The output
  consists of: 1) a banner listing
  the date, time, and <i>apercors</i> for which the entry is relevant, 2)
  a listing of the number of parameters <i>nparams</i> in the five parameter
  curve of growth model to be fit, the initial values of all the parameters, and
  the small and large aperture numbers, 3) the fitted values of the
  curve of growth model parameters and their errors where parameters which
  were not fit have zero-valued errors, 4) the computed seeing radius
  for each image,
  5) the theoretical, observed, and adopted curves of growth and
  their associated errors, 6) the aperture correction to  largeap,
  the estimated total aperture correction to an
  aperture radius twice the largest aperture radius, and the estimated error
  in the aperture correction, 7) the aperture
  correction from <i>smallap</i> to <i>largeap</i>, 8) for each star
  in the image the observed magnitudes, magnitude corrected to the largest
  aperture, and magnitude corrected to twice the largest aperture, and
  finally, 9) a summary of the mean adopted curve of growth, the mean residual,
  and the mean residual squared for all the data for all the images
  as a function of aperture radius.
  </p>
  <p>
  If <i>plotfile</i> is not <span style="font-family: monospace;">""</span>, plots of the final curve of growth model fit,
  residuals as a function of aperture radius, magnitude, x, y, and the
  aperture correction to the largest aperture <i>largeap</i>
  for each image in <i>photfiles</i> are saved in the plot metacode file
  <i>plotfile</i>..
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following commands are available in interactive graphics cursor mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Keystroke Commands
  
  ?       Print help
  w       Print computed aperture correction
  c       Print coordinates of star nearest cursor
  f       Compute a new fit
  d       Delete point(s) nearest the cursor
  u       Undelete point(s) nearest the cursor
  m       Plot the observed and model cog versus radius
  r       Plot the cog fit residuals versus radius
  b       Plot the cog fit residuals versus magnitude
  x       Plot the cog residuals versus the x coordinate
  y       Plot the cog residuals versus the y coordinate
  a       Plot the aperture correction versus radius
  g       Redraw the current plot
  n       Move to the next image
  p       Move to the previous image
  q       Quit task
  
          Colon commands
  
  :show   parameters   Show the initial cog model parameter values
  :show   model        Show the fitted cog model parameters
  :show   seeing       Show the computed seeing radii for all images
  :image  [value]      Show/set the image to be analyzed
  
          Colon Parameter Editing Commands
  
  :smallap   [value]  Show/set the index of the smallest aperture
  :largeap   [value]  Show/set the index of the largest aperture
  :nparams   [value]  Show/set the number of cog model parameters to fit
  :swings    [value]  Show/set initial power law slope of stellar wings
  :pwings    [value]  Show/set fraction of total power in stellar wings
  :pgauss    [value]  Show/set fraction of total core power in gaussian
  :rgescale  [value]  Show/set ratio of exp to gauss radial scales
  :xwings    [value]  Show/set the extinction coefficient
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The algorithm used to compute the aperture correction is the DAOGROW
  algorithm developed by Peter Stetson (1990, see the references section).
  </p>
  <p>
  In this algorithm the stellar profile is approximated by the following
  3 component model where P, G, E denote the power law, gaussian, and
  exponential analytic components of the model respectively. The subscript i
  denotes quantities that are a function of each image. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  I[r,X[i];RO[i],swings,pwings,pgauss,regscale,xwings] =
      (pwings + X[i] * xwings) * P[r;swings] + (1 - pwings - X[i] *
      xwings) * (pgauss * G[r;RO[i]] + (1 - pgauss) *
      E[r;rgescale,RO[i]])
  
  P[r;swings] = mnorm * (1 + r ** 2) ** swings
        mnorm = (swings - 1) / PI
  
  G[r;RO[i]] = gnorm * exp (-0.5 * r ** 2 / RO[i] ** 2)
       gnorm = 1 / (2 * PI * RO[i] ** 2)
  
  E[r;RO[i]] = hnorm  * exp (-r / (rgescale * RO[i]))
       hnorm = 1 /  (2 * PI * (rgescale * RO[i]) ** 2)
  </pre></div>
  <p>
  This equation is actually applied to the magnitude differences between
  apertures where the observed magnitude differences are computed as follows
  for image i, star j, and aperture k.
  </p>
  <div class="highlight-default-notranslate"><pre>
  mdiff[i,j,k] = m[i,j,k] - m[i,j,k-1]           k=2,..,naperts
  </pre></div>
  <p>
  The observed differences are fit by least-squares techniques to 
  to the theoretical model differences represented by the following equation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  diff[i,j,k] = -2.5 * log10 (integral (2 * PI * r * I) from 0 to r[k] /
            integral (2 * PI * r * I) from 0 to r[k-1])
  </pre></div>
  <p>
  The integrals of the three model components P, G, and E are the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  integral (2 * PI * r * P) = 1 - (1 + r ** 2) ** -swings
  
  integral (2 * PI * r * G) = 1 - exp (-r ** 2 / (2 * RO[i] ** 2))
  
  integral (2 * PI * r * H) = 1 + (1 + r / (rgescale * RO[i]) *
                        exp (-r / (rgescale * RO[i]))
  </pre></div>
  <p>
  In a given run of MKAPFILE the seeing radius
  RO[i] is fit separately for each image, but the parameters swings, pwings,
  pgauss, rgescale, and xwings are fit to the entire data set. Therefore
  the RO[i] values define a family curves, each differing from the other
  by the seeing radius RO[i] alone. It turns out that for most data the
  fits do not depend significantly on the <i>rgescale</i> and <i>xwings</i>
  parameters.  Therefore by default <i>nparams</i> is set to 3 and
  <i>rgescale</i> and <i>xwings</i> are set to default values of 0.9 and 0.0
  respectively.
  </p>
  <p>
  After the theoretical and observed growth curves are computed for
  each image, they are combined to produce an adopted growth curve. The
  weighting scheme used in the combining process is such that at small radii
  where the observed magnitude differences have the smallest errors,
  the observed values,
  are favored, and at large radii  the theoretical curve is favored. At
  all points in the computation of the theoretical curve, the observed curve,
  and the adopted curve, tests are made for deviant data points and these
  are down-weighted. The adopted curve is integrated between <i>smallap
  and fIlargeap</i> to produce the aperture correction for each image.
  </p>
  <p>
  Because the error in the observed magnitudes grows rapidly toward
  larger radii, while the error in the aperture correction grows
  rapidly toward smaller radii, the combined error for the star will
  have some minimum value, usually at an intermediate aperture. If
  <i>magfile</i> is not <span style="font-family: monospace;">""</span>, the magnitudes corrected to <i>largeap</i>
  using the observed magnitude and correction where the  error
  is lowest are written to <i>magfile</i>, along with the image id, x and y
  coordinates, filter ids, exposure times, airmasses, and errors in the
  magnitude. This file can be read into the OBSFILE program so as to
  create a photometry catalog suitable for input into PHOTCAL.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  A full description of the DAOGROW algorithm used by MKAPFILE can be
  found in the article <span style="font-family: monospace;">"On the Growth-Curve Method for Calibrating
  Stellar Photometry with CCDs"</span> by Peter Stetson in PASP 102, 932
  (1990).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Prepare an aperture corrections file from a set of observations
  from 5 different data frames taken in a single night.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkapfile *.mag.* 15 apercor
  
      ... plot of the cog for the first image will appear
  
      ... type r to examine fit residuals versus radius
  
      ... type a to examine the aperture correction curve
          versus radius
  
      ... type n to look at results for next image
  
      ... type d to remove a discrepant point
  
      ... type f to refit the cog
  
      ... type r to examine the residuals for this image
  
      ... type p to recheck the residuals for the first image
  
      ... step through the remaining image deleting points and
          refitting as necessary
  
      ... type q to quit
  
      ... the compute aperture corrections will appear in apercor
  </pre></div>
  <p>
  2. Repeat the previous example in non-interactive mode saving all the
  details and plots of the fit in the log and plot file respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkapfile *.mag.* 15 apercor inter- logfile=apercor.log\
      plotfile=apercor.plot
  
  ph&gt; page apercor.log
  
      ... page through the log file
  
  ph&gt; gkiextract apercor.plot "1-25" | stdplot
  
      ... send all the plots of the fit to the default plotter
  </pre></div>
  <p>
  3. Compute the magnitudes corrected to largeap, of all the standard
  stars observed in a night using the observed magnitude and computed magnitude
  correction at the aperture radius with the lowest error.
  Assume that the filter ids (U,B,V), exposure times, and airmasses were
  all present and correct in the photometry files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkapfile stdfiles 15 apercor inter- magfile="stdfiles.ap"\
      logfile=apercor.log plotfile=apercor.plot
  
  ph&gt; obsfile stdfiles.ap "1,2,3,4,5,6,7,8,9" "U,B,V" imsets stdobs
  
      ... create a standard star observations file suitable for
          input to the photcal package
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
  apfile, mknobsfile,mkobsfile,obsfile
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
