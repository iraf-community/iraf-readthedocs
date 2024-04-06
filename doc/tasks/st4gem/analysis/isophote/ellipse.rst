.. _ellipse:

ellipse: Fit elliptical isophotes.
==================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ellipse  in_image out_table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'ellipse' task fits elliptical isophotes to galaxy images --- this 
  task performs the basic isophotal analysis used by other tasks in this 
  package.
  </p>
  <p>
  The task reads one 2-dimensional image section and produces as main output
  one table which contains 40 or more columns with parameters for each fitted 
  isophote, one table row for each isophote. Optional products include a
  family of tables that contain each individual elliptical sample extracted
  from the image at each isophote, in the form intensity versus position 
  angle, as well as individual plots of these samples.
  During the fitting process, some of the isophote parameters can be displayed 
  in tabular form on the user's terminal screen (i.e., they are sent to 
  STDOUT); these parameters allow the user to monitor the fitting process. 
  The task can also be run in interactive mode, where the user has greater 
  control over its operation.
  </p>
  <p>
  The main output table content is described in more detail near the end of this 
  section. For galaxy brightness profile analysis (1-D), see task  
  'fitting.nfit1d'.
  For a more detailed description of some internal features of this task,
  use `help ellipse opt=sys'.
  </p>
  <p>
  The image is measured using an iterative method described by Jedrzejewski
  (Mon.Not.R.Astr.Soc., 226, 747, 1987). Each isophote is fitted at a 
  pre-defined, fixed semi-major axis length. The task starts from a first
  guess elliptical isophote defined by approximate values for the X and Y 
  center coordinates, ellipticity and position angle. Using these values, 
  the image is sampled along an elliptical path (see 'samplepar' pset)
  producing a 1-dimensional intensity distribution as a function of position 
  angle E. The harmonic content of this distribution is analyzed by least-squares 
  fitting to the function:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  y  =  y0 + A1 * sin(E) + B1 * cos(E) + A2 * sin(2 * E) + B2 *
  cos (2 * E)
  
  </pre></div>
  <p>
  Each one of the harmonic amplitudes A1, B1, A2, B2 is related to a
  specific ellipse geometric parameter, in the sense that it conveys
  information regarding how much the current parameter value deviates 
  from the <span style="font-family: monospace;">"true"</span> one. To compute this deviation, the local image radial
  gradient has to be taken into account too. The algorithm picks up the
  largest amplitude among the four, estimates the local gradient and
  computes the corresponding increment in the associated ellipse parameter.
  That parameter is updated,  and the image is resampled.  This process is 
  repeated until any one of the following criteria are met: 
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>The largest harmonic amplitude is less than a given fraction
  of the rms residual of the intensity data around the harmonic fit.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>A user-specified maximum number of iterations is reached.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd>More than a given fraction of the elliptical sample points have no
  valid data in then, either because they lie outside the image boundaries 
  or because they where flagged out from the fit (see below).
  </dd>
  </dl>
  <p>
  In any case, a minimum number of iterations is always performed. 
  See 'controlpar' pset for details.
  If iterations stop because of reasons 2 or 3 above, then 
  those ellipse parameters that generated the lowest absolute 
  values for harmonic amplitudes will be used. 
  At this point, the image data sample coming from the best fit 
  ellipse is fitted by the following function:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  y  =  y0  +  An * sin(n * E)  +  Bn * cos(n * E)
  
  </pre></div>
  <p>
  with n = 3 and n = 4.  The amplitudes (A3, B3, A4, B4),
  divided by the semi-major axis length and local intensity 
  gradient, measure the isophote's deviations from perfect 
  ellipticity (the amplitudes divided by semi-major axis and gradient, are
  the actual quantities written at the output table). 
  </p>
  <p>
  The task then measures the integrated intensity and
  the number of non-flagged pixels inside the elliptical isophote
  and also inside the corresponding circle with same center and radius
  equal to the semi-major axis length. These parameters, some other associated 
  parameters, and some auxiliary information, are written to the 
  output table(s). See 'magpar' pset.
  </p>
  <p>
  Optionally, the user can explicitly define a list of upper harmonics to 
  be fitted to the best-fit intensity sample. The output table will contain
  additional columns with these harmonic amplitudes and their errors.  
  </p>
  <p>
  It must be emphasized that the algorithm was designed explicitly with
  a galaxy brightness distribution in mind. In particular, a well defined
  negative radial intensity gradient across the region being fitted is 
  paramount for the achievement of stable solutions. Use of the
  algorithm in other types of images (e.g., planetary nebulae) may lead
  to inability to converge to any acceptable solution.
  </p>
  <p>
  After fitting the ellipse that corresponds to a given value of the
  semi-major axis (by the process described above), the axis length is
  incremented/decremented following a pre-defined rule. At each step, 
  the starting ellipse parameters are taken from the previously fitted 
  ellipse that has the closest semi-major axis length to the current one.
  On low surface brightness regions (i.e., those having large radii), the 
  small values of the image radial gradient can induce large corrections and 
  meaningless values for the ellipse parameters. The task has capabilities to 
  stop increasing semi-major axis based on several criteria, including
  signal-to-noise ratio. See the 'geompar' pset for details.
  </p>
  <p>
  Errors in intensity, magnitude and local gradient are obtained directly
  from the rms scatter of intensity data along the fitted ellipse. 
  Ellipse geometry parameter errors are obtained from the internal errors in 
  the harmonic fit, after removal of the first and second fitted harmonics.
  Harmonic amplitude errors are obtained from the fit error after removal of 
  all harmonics up to, and including, the one being considered. See error
  analysis in Busko, I., 
  1996, Proceedings of the Fifth Astronomical Data Analysis
  Software and Systems Conference, Tucson, PASP Conference Series v.101,
  ed. G.H. Jacoby and J. Barnes, p.139-142.
  </p>
  <p>
  Interactive mode can be used with either an image server (Ximtool/SAOimage)
  or standard IRAF graphics (stdgraph). In interactive mode, the task begins
  by automatically displaying the input image and waiting for cursor commands.
  The 'device' task parameter selects the color of the graphics overlay on the
  gray-scale display, or the standard graphics output. Frame 1 of the image
  server is used. Due to limitations in the current graphics-image
  interface in IRAF, screen updates during cursor processing take a time 
  proportional to the display buffer size. Small sizes (up to 512 x 512) are recommended. 
  </p>
  <p>
  Using cursor commands, the user can, at any time, list or modify most of the 
  algorithm control parameters, as well as the current ellipse geometry. 
  Functions as zoom, roam, reset, and limited gray-scale control, are also
  available. Pixel masking/unmasking can be done as well. The cursor comes 
  back after each isophote fit, until the user chooses to continue in 
  non-interactive mode, or until the minimum fitting semi-major axis is 
  reached. Type 'help elcursor' for a description of all available cursor 
  commands. 
  </p>
  <p>
  Bad pixel flagging can be accomplished in a number of ways:
  </p>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>If a HST-style Data Quality File (DQF) is associated with the input image, 
  it can be read by the task and used to flag pixels out from the fit. If only 
  the DQF name extension is provided, task assumes DQF has the same root name 
  as the main input image.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>The task can also read a Bad Pixel Mask image, which is stored in the IRAF 
  <span style="font-family: monospace;">"pixel list"</span> format. It has the same root name as the main input image, but 
  with extension '.pl'. The task reads the bad pixel mask automatically at task 
  startup, if available, and its contents can be modified, or it can be created 
  from scratch, by interactive cursor commands. This automatic recognition
  of the bad pixel mask only works when the input image name extension is
  three characters long, such as in <span style="font-family: monospace;">"imh"</span>, <span style="font-family: monospace;">"hhh"</span> or <span style="font-family: monospace;">"fit"</span>.
  The flagging of bad pixels
  in the mask file follows the same convention as the HST Data Quality Files:
  zeroed pixels in the bad pixel mask mean that the corresponding pixel
  in the science image is good; non-zero pixels in the mask mean that the
  corresponding science pixel should be rejected at fitting time. 
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>The task provides also a k-sigma clipping algorithm for cleaning deviant
  sample points at each isophote, thus improving convergency stability against 
  stars, defects, etc. 
  </dd>
  </dl>
  <p>
  The task can be run in either memory-intensive or disk-intensive modes.
  Disk-intensive is not recommended unless as a last resort to overcome
  <span style="font-family: monospace;">"Out of memory"</span> problems, because it has a large penalty in execution
  speed. In memory-intensive mode the task reads the full input file image 
  section as a real array in memory. If the object to be measured is small
  compared with the frame dimensions, the best approach to save memory is 
  to directly input an appropriate subsection of the larger, original image. 
  All input/output coordinate information can still be handled by the task
  in the original image's coordinate reference system. See the 'geompar' 
  pset for details.
  </p>
  <p>
  Output directed to STDOUT is a table with one row for each isophote. 
  Each row contains the following data: semi-major axis length, mean 
  isophotal intensity and its rms, ellipticity and its error, position 
  angle and its error, radial gradient relative error, number of valid 
  data points used in the fit, number of flagged data points (either 
  removed from the image or clipped out), number of iterations, and 
  stop condition code.  The stop code can have the following values:
  </p>
  <div class="highlight-default-notranslate"><pre>
   0 - normal.
   1 - less than pre-specified fraction of the extracted data
       points are valid.
   2 - exceeded maximum number of iterations.
   3 - singular matrix in harmonic fit, results may not be valid.
       Also signals insufficient number of data points to fit.
   4 - small or wrong gradient, or ellipse diverged; subsequent
       ellipses at larger semi-major axis may have the same constant
       geometric parameters.
  -1 - isophote was saved before completion of fit (by a cursor
       command in interactive mode).
  
  </pre></div>
  <p>
  The main output table also contains one row for each value of the semi-major 
  axis length. The labeling of each column is as follows: 
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  Column             -  Contents
  
  
  SMA                -  semi-major axis length (pixel)
  INTENS             -  mean isophotal intensity
  INT_ERR            -  error in isophotal intensity (RMS / sqrt(NDATA))
  PIX_VAR            -  estimate of pixel variance (RMS * sqrt(SAREA))
  RMS                -  root-mean-square scatter around isophotal intensity
  ELLIP              -  ellipticity
  ELLIP_ERR          -  ellipticity error
  PA                 -  position angle (degrees counterclokwise from +y)
  PA_ERR             -  position angle error
  X0, Y0             -  ellipse center (pixel)
  X0_ERR, Y0_ERR     -  error of ellipse center
  GRAD               -  local radial intensity gradient
  GRAD_ERR           -  gradient error
  GRAD_R_ERR         -  gradient relative error
  RSMA               -  (semi-major axis length) ** 1/4
  MAG                -  mean isophotal magnitude
  MAG_LERR, MAG_UERR -  lower and upper magnitude errors
  TFLUX_E            -  total flux enclosed by ellipse
  TFLUX_C            -  total flux enclosed by circle
  TMAG_E             -  total flux enclosed by ellipse, in magnitudes
  TMAG_C             -  total flux enclosed by circle, in magnitudes
  NPIX_E             -  total number of valid pixels inside ellipse
  NPIX_C             -  total number of valid pixels inside circle
  A3, B3             -  3rd harmonic deviations from ellipse
  A4, B4             -  4th harmonic deviations from ellipse
  A3_ERR, B3_ERR     -  3rd harmonic deviation errors
  A4_ERR, B4_ERR     -  4th harmonic deviation errors
  NDATA              -  number of valid data points on isophote
  NFLAG              -  number of flagged data points on isophote
  NITER              -  number of iterations
  STOP               -  stop condition code
  A_BIG              -  maximum (in abs. value ) among 1st and 2nd
                        harmonic amplitudes
  SAREA              -  average sector area on isophote (pixel)
  AIn, BIn           -  optional n-th harmonic amplitudes
  AIn_ERR, BIn_ERR   -  optional n-th harmonic amplitude errors
  
  The input image name is written to the main output table header.
  
  The task has also the capability to read in a table previously generated
  by itself when applied to a given image, and use the ellipse geometry
  information in each table row to measure another (related) image. In
  this mode the fitting algorithm is disabled and the task just extracts
  photometry information from the image. This mode is activated by setting
  task parameter 'inellip' to the name of the table that contains the
  results of a former execution of the task. This feature is useful when
  measuring paired images e.g. as in a multicolor set to derive color
  indices and gradients.
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>Image section to be measured. If a .pl mask file exists in the same
  directory, a explicit extension should be provided in the input file name.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>Main output table name.
  </dd>
  </dl>
  <dl>
  <dt><b>(dqf = <span style="font-family: monospace;">""</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(dqf = "") [file name]' -->
  <dd>Data Quality File name or extension. If set to <span style="font-family: monospace;">"none"</span>, eventually existing 
  DQF is ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(inellip = <span style="font-family: monospace;">""</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inellip = "") [file name]' -->
  <dd>Input table in <span style="font-family: monospace;">"ellipse"</span> format, to be used in no-fit, photometry-only
  mode.
  </dd>
  </dl>
  <dl>
  <dt><b>(geompar) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(geompar) [pset]' -->
  <dd>Pset with geometry-defining parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(controlpar) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(controlpar) [pset]' -->
  <dd>Pset with algorithm control parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(samplepar) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(samplepar) [pset]' -->
  <dd>Pset with sampling control parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(magpar) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(magpar) [pset]' -->
  <dd>Pset with magnitude scale parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(interactive = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(interactive = no) [boolean]' -->
  <dd>Run task in interactive mode ? 
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"red"</span>) [string, allowed values: |stdgraph|white|red|green|blue|yellow]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "red") [string, allowed values: |stdgraph|white|red|green|blue|yellow]' -->
  <dd>Interactive device. For gray-scale image servers ('Ximtool', 'SAOimage'), 
  use color of graphics overlay. Server process must be already activated
  at workstation. For standard IRAF line-graphics, use 'stdgraph'.
  </dd>
  </dl>
  <dl>
  <dt><b>(icommands = <span style="font-family: monospace;">""</span>) [*imcur]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(icommands = "") [*imcur]' -->
  <dd>Optional file with image cursor commands. If left empty, task will read
  standard <span style="font-family: monospace;">"imcur"</span> input when in interactive mode.
  </dd>
  </dl>
  <dl>
  <dt><b>(gcommands = <span style="font-family: monospace;">""</span>) [*gcur]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(gcommands = "") [*gcur]' -->
  <dd>Optional file with graphics cursor commands. If left empty, task will read
  standard <span style="font-family: monospace;">"gcur"</span> input when in interactive mode.
  </dd>
  </dl>
  <dl>
  <dt><b>(masksz = 5) [int, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(masksz = 5) [int, min=1]' -->
  <dd>Size of pixel masking area when <span style="font-family: monospace;">'m'</span> cursor command not in region mode.
  </dd>
  </dl>
  <dl>
  <dt><b>(region = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(region = no) [boolean]' -->
  <dd>Pixel masking by <span style="font-family: monospace;">'m'</span> cursor key is in region mode ?
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>List summary at STDOUT ?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by I.Busko
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  elcursor, geompar, controlpar, samplepar, magpar, nfit1d.
  </p>
  <p>
  For a more detailed description of some internal features of this task,
  use `help ellipse option=sysdoc'.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
System Documentation
--------------------

.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  This document presents in deeper detail some issues not thoroughly
  discussed in the `ellipse' task and related psets' help pages:
  </p>
  <div class="highlight-default-notranslate"><pre>
   1 - the basic isophote fitting formulae.
   2 - radial gradient computation.
   3 - errors.
   4 - image sampling.
   5 - integrated magnitude precision.
   6 - convergency diagnostic.
   7 - object locator.
   8 - image/graphics display.
   9 - ellipticity X eccentricity.
  10 - ASCII output.
  </pre></div>
  </section>
  <section id="s_1__basic_formulae">
  <h3>1. basic formulae</h3>
  <p>
  The basic isophote fitting algorithm, as described in reference [1], 
  computes corrections for the current ellipse's geometrical parameters
  by essentially <span style="font-family: monospace;">"projecting"</span> the fitted harmonic amplitudes onto the
  image plane:
  </p>
  <div class="highlight-default-notranslate"><pre>
                                                - B1
  major axis center position correction = -----------------     (pixel)
                                                  I'
  
                                            - A1 (1 - ellip)
  minor axis center position correction = ------------------    (pixel)
                                                  I'
  
                            - 2 B2 (1 - ellip)
  ellipticity correction = -------------------
                                  I' a
  
                                   2 A2 (1 - ellip)
  position angle correction = ------------------------------    (radians)
                               I' a [(1 - ellip)**2 - 1]
  
  </pre></div>
  <p>
  where I' is the local radial intensity gradient, <span style="font-family: monospace;">`a'</span> is the current
  semi-major axis, and A1, B1, A2, B2 are the current least-squares-fitted 
  harmonic amplitudes. In each of the above formulae, I' is the fundamental 
  <span style="font-family: monospace;">"geometrical"</span> factor used to <span style="font-family: monospace;">"project"</span> amplitudes, which are 
  intensity-like quantities, onto the ellipse  geometrical plane.
  The <span style="font-family: monospace;">`a'</span> term in the denominator is used to transform from pixel
  units to a non-dimensional scale (ellipticity and angle), and the 
  remaining factors are geometrical corrections.
  </p>
  </section>
  <section id="s_2__radial_gradient_computation">
  <h3>2. radial gradient computation</h3>
  <p>
  The radial intensity gradient is the most critical quantity computed
  by the fitting algorithm. As can be seen from the above formulae, small
  I' values lead to large values for the correction terms. Thus, I' errors
  may lead to large fluctuations in these terms, when I' itself is small. 
  This happens usually at the fainter, outer isophotes of galaxy images. 
  It was found by numerical experiments [2] that the precision to which a 
  given elliptical isophote can be fitted is related to the relative error 
  in the local radial gradient.
  </p>
  <p>
  Because of the gradient's critical role, the task has a number of 
  features to allow its estimation even under difficult conditions. 
  The default gradient computation, the one used at first by the task when 
  it starts to fit a new isophote, is based on the extraction of two intensity 
  samples: #1 at the current ellipse position, and #2 at a similar ellipse 
  with a 10% larger semi-major axis. #1 sample, which will be used also for 
  harmonic fitting, is extracted using the current integration mode (bi-linear, 
  mean, etc.). To speed up processing, #2 sample is extracted using faster 
  nearest-neighbor sampling. This faster sampling is disabled when either 
  the current semi-major axis length is smaller than 20 pixels, or the 
  gradient error at the last isophote fitted so far is larger than 20%.
  </p>
  <p>
  If the gradient so estimated is not meaningful, the algorithm extracts
  another #2 sample, this time using in full the current integration method 
  and a 20% larger radius. In this context, meaningful gradient means 
  <span style="font-family: monospace;">"shallower"</span>, but still close to within a factor 3 from the previous 
  isophote's gradient estimate. 
  </p>
  <p>
  If still no meaningful gradient can be measured, the task uses the value
  measured at the last fitted isophote, but decreased (in absolute value) 
  by a factor 0.8. This factor is roughly what is expected from semi-major axis
  geometrical sampling steps of 10 - 20 % and a deVaucouleurs law or an 
  exponential disk in its inner region (r &lt;~ 5 req). When using the last 
  isophote's gradient as estimator for the current one, the current gradient 
  error cannot be computed and is set to INDEF.
  </p>
  <p>
  As a last resort, if no previous gradient estimate is available, the
  task just guesses the current value by setting it to be (minus) 10 %
  of the mean intensity at sample #1. This case usually happens only at 
  the first isophote fitted by the task.
  </p>
  <p>
  The use of approximate gradient estimators may seem in contradiction with
  the fact that isophote fitting errors depend on gradient error, as well as
  with the fact that the algorithm itself is so sensitive to the gradient
  value. 
  The rationale behind the use of approximate estimators, however, is based
  on the fact that the gradient value is used only to compute increments,
  not the ellipse parameters themselves. Approximate estimators are useful
  along the first steps in the iteration sequence, in particular when local 
  image contamination (stars, defects, etc.) might make it difficult to find 
  the correct path towards the solution. At convergency, however, if the
  gradient is still not well determined, the subsequent error computations,
  and the task's behavior from that point on, will take the fact into account 
  properly. For instance, the 3rd and 4th harmonic amplitude errors depend
  on the gradient relative error, and if this is not computable at the
  current isophote, the task uses a reasonable estimate (80% of the value at
  the last successful isophote) in order to
  generate sensible estimates for those harmonic errors.
  </p>
  </section>
  <section id="s_3__errors">
  <h3>3. errors</h3>
  <p>
  Most parameters computed directly at each isophote have their errors 
  defined by standard error propagation formulae. Errors in the ellipse
  geometry parameters, on the other hand, cannot be estimated in the same
  way, since these parameters are not computed directly but result from a 
  number of updates from a starting guess value. An error analysis based on 
  numerical experiments [2] showed that the best error estimators for these
  geometrical parameters can be found by simply <span style="font-family: monospace;">"projecting"</span> the harmonic
  amplitude errors that come from the least-squares covariance matrix by
  the same formulae above (1) used to <span style="font-family: monospace;">"project"</span> the associated parameter 
  updates. In other words, errors for ellipse center, ellipticity and
  position angle are computed by the same formulae as in (1), but replacing
  the least-squares amplitudes by their errors. This is empirical and 
  difficult to justify in terms of any theoretical error analysis, but 
  showed in practice to produce reliable error estimators.
  </p>
  </section>
  <section id="s_4__image_sampling">
  <h3>4. image sampling</h3>
  <p>
  When sampling is done using elliptical sectors (mean or median modes),
  Jedrzejewski's method uses an elaborate, high-precision scheme to take 
  into account partial pixels that lie along elliptical sector boundaries.
  In the `ellipse' task this scheme was not implemented. Instead, pixels 
  at sector boundaries are either fully included or discarded, depending on
  the precise position of their centers in relation to the elliptical
  geometric locus corresponding to the current isophote. This design decision 
  is based on two arguments: (i) it would be difficult to include
  partial pixels in median computation, and (ii) speed. It remains to be
  seen the loss in isophote fitting precision due to this simpler 
  implementation, as compared with the original method.
  </p>
  <p>
  Even when the chosen integration mode is not bi-linear, the sampling
  algorithm resorts to it in case the number of sampled pixels inside any
  given sector is less than 5. If was found that bi-linear mode gives
  smoother samples in those cases.
  </p>
  <p>
  Tests performed with artificial images showed that cosmic rays and 
  defective pixels can be very effectively removed from the fit by a 
  combination of median sampling and sigma-clipping. Sigma-clip alone 
  is effective only for small contamination levels.
  </p>
  </section>
  <section id="s_5__integrated_magnitude_precision">
  <h3>5. integrated magnitude precision</h3>
  <p>
  The integrated fluxes, magnitudes and areas computed by `ellipse' where 
  checked against results produced by the `noao.digiphot.apphot' tasks 
  `phot' and `polyphot', using artificial galaxy images. Quantities computed 
  by `ellipse' match the <span style="font-family: monospace;">"reference"</span> ones within &lt; 0.1 % in all tested cases.
  </p>
  </section>
  <section id="s_6__convergency_diagnostic">
  <h3>6. convergency diagnostic</h3>
  <p>
  The basic convergency criterion for stopping iterations at a given
  isophote compares the largest harmonic amplitude among A1, B1, A2, B2, 
  with a fixed, user-definable fraction of the fit's root-mean-square 
  residual. To check the convergency behavior after running `ellipse',
  the plot of the largest amplitude after convergency (stored in output 
  table's A_BIG column) as a function of the isophote rms value (stored in 
  column RMS) can be used for a quick look at the convergency amplitudes.
  Because RMS is not the residual after the harmonic fit, but just the raw 
  root-mean-square scatter of intensity values along the elliptical path,
  the average slope of that plot should be significantly smaller than the 
  convergency parameter `conver' value, and outliers may give information 
  on how far from convergency the fit was at each isophote.
  </p>
  </section>
  <section id="s_7__object_locator">
  <h3>7. object locator</h3>
  <p>
  When designing the new version of `ellipse', high priority was given to
  make it as independent as possible from user input. However, the algorithm
  simply does not run if not supplied with reasonably accurate object
  coordinates. In other words, it can not find the desired object to be
  measured in the input frame. Because of that, the task implementation
  pays special attention to the values supplied by the user as object 
  coordinates. Before starting the fit itself, it runs an
  <span style="font-family: monospace;">"object locator"</span> routine around the specified or assumed object coordinates,
  to check if minimal conditions for starting a reasonable fit are met.
  This routine, in the current implementation, performs a scan over a
  10 X 10 pixel window centered on the input object coordinates. At each
  scan position, it extracts two concentric circular samples with radii
  4 and 8 pixels, using bi-linear sub-pixelized interpolation. It computes
  a signal-to-noise-like criterion using the intensity averages and standard 
  deviations at each annulus
  </p>
  <div class="highlight-default-notranslate"><pre>
              aver1 - aver2
  CRIT = -------------------------
         sqrt (std1 ^2 + std2 ^ 2)
  </pre></div>
  <p>
  and locates the pixel inside the scanned window where this criterion is
  a maximum. If the criterion so computed exceeds a given threshold, it
  assumes that a suitable object was detected at that position. 
  </p>
  <p>
  The default threshold value is set to 1. This value, and the annuli and
  window sizes currently used, were found by trial and error using a
  number of both artificial and real galaxy images. It was found that very
  flat galaxies (ellipticity ~ 0.7) cannot be detected by such a simple
  algorithm. In such cases the user must resort to task parameter
  'olthresh' in the 'controlpar' pset. By lowering its value the object
  locator becomes less strict, in the sense that it will accept lower
  signal-to-noise data. 
  </p>
  <p>
  The object locator algorithm, including its numerical parameters, must
  be regarded as still in an experimental phase. Input and suggestions
  from users are welcome.
  </p>
  </section>
  <section id="s_9__image_graphics_display">
  <h3>9. image/graphics display</h3>
  <p>
  The display feature is implemented in a similar way as in task
  `imexamine': the `ellipse' task issues a command to the CL, and this
  command is simply a call to the either `display' or `contour' tasks,
  depending on which visualization device is being used.  
  </p>
  <p>
  The `display' or `contour' command line is enriched with arguments 
  which ensure proper alignment of image and graphics, as well as allow 
  the control of zooming and gray-scale functions by the user.
  </p>
  <p>
  The actual commands issued by `ellipse' look like:
  </p>
  <div class="highlight-default-notranslate"><pre>
  display "section_name" 1 "optional_user_parameters" erase+ border+ \
           fill+ xcenter=0.5 ycenter=0.5 xsize=1. ysize=1. xmag=1. ymag=1. \
           mode=h &gt;&amp; dev$null
  
  or
  
  contour "section_name" "optional_user_parameters" append- mode=h &gt;&amp; dev$null
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"section_name"</span> is the actual file name of the image being measured,
  eventually appended with a section specification that allows the <span style="font-family: monospace;">"fill+"</span>
  display mode (or the graphics routine) to simulate a zoom effect. The 
  <span style="font-family: monospace;">"optional_user_parameters"</span> string is the user-defined string built by the 
  `dispars:' cursor command.
  </p>
  <p>
  Notice that there is room for some misbehavior if the user writes 
  something unacceptable in the :dispars string. `ellipse' does not check 
  this string, simply passes it to the underlying system.
  </p>
  <p>
  Notice also that the spelling of parameter names, as well as their meaning,
  are hard-coded inside ellipse's source code. If by any reason the 
  `display' or `contour' tasks are modified in future system versions, the
  `ellipse' source code will have to be modified accordingly.
  </p>
  </section>
  <section id="s_9__ellipticity_x_eccentricity">
  <h3>9. ellipticity x eccentricity</h3>
  <p>
  Why task `ellipse' works with <span style="font-family: monospace;">"ellipticity"</span> instead of the canonical
  ellipse eccentricity ? The main reason is that ellipticity, defined
  as 
  </p>
  <div class="highlight-default-notranslate"><pre>
              minor axis
  e  =  1  -  ----------
              major axis
  </pre></div>
  <p>
  relates better with the visual <span style="font-family: monospace;">"flattening"</span> of an ellipse. It is easy,
  by looking to a flattened circle, to guess its ellipticity as, say,
  0.1. The same ellipse has, however, an eccentricity of 0.44, which is
  not obvious from its visual aspect. The quantities relate as
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  eccentricity  =  sqrt [ 1 -  (1 - ellipticity)^2 ]
  
  </pre></div>
  </section>
  <section id="s_10__why_the_new_version_does_not_support_ascii_output">
  <h3>10. why the new version does not support ascii output</h3>
  <p>
  The older version of `ellipse' supported output in either binary table
  format or ASCII format. The new version enforces all its numeric output
  to be in binary table format only. The basic reason behind this change is
  that in binary table format the results' full numeric precision is
  preserved. If the need ever arises to generate ASCII output, use task
  `tables.ttools.tdump' to extract the information from ellipse's output
  binary tables and dump it to ASCII files.
  </p>
  </section>
  <section id="s_11__references">
  <h3>11. references</h3>
  <dl>
  <dt><b>[1]</b></dt>
  <!-- Sec='11. REFERENCES' Level=0 Label='' Line='[1]' -->
  <dd>JEDRZEJEWSKI, R., 1987, Mon. Not. R. Astr. Soc., 226, 747.
  </dd>
  </dl>
  <dl>
  <dt><b>[2]</b></dt>
  <!-- Sec='11. REFERENCES' Level=0 Label='' Line='[2]' -->
  <dd>BUSKO, I., 1996, Proceedings of the Fifth Astronomical Data Analysis
  Software and Systems Conference, Tucson, PASP Conference Series v.101,
  ed. G.H. Jacoby and J. Barnes, p.139-142.
  </dd>
  </dl>
  
  </section>
  
  <!-- Contents: 'INTRODUCTION' '1. BASIC FORMULAE' '2. RADIAL GRADIENT COMPUTATION' '3. ERRORS' '4. IMAGE SAMPLING' '5. INTEGRATED MAGNITUDE PRECISION' '6. CONVERGENCY DIAGNOSTIC' '7. OBJECT LOCATOR' '9. IMAGE/GRAPHICS DISPLAY' '9. ELLIPTICITY X ECCENTRICITY' '10. WHY THE NEW VERSION DOES NOT SUPPORT ASCII OUTPUT' '11. REFERENCES'  -->
  
