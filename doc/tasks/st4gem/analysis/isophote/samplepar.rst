.. _samplepar:

samplepar: Set image sampling control parameters (pset).
========================================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  samplepar
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This pset is used to set the image sampling parameters associated with
  the 'ellipse' task. Sampling is performed at each iteration of the isophote
  fitting algorithm, both to extract a trial intensity sample along an 
  elliptical path, and to estimate the local radial intensity gradient. 
  In this text, the term <span style="font-family: monospace;">"intensity sample"</span> refers to a two-column table, 
  one column containing values of position angle and the other containing the 
  intensity extracted at each angle. This data is complemented by the ellipse 
  geometry (semi-major axis length, center coordinates, ellipticity, position 
  angle).
  </p>
  <p>
  Three methods are available for sampling an image along the elliptical
  path: bi-linear interpolation, and either mean or median over elliptical
  annulus sectors. These modes are selected using task parameter
  'integrmode'. Bi-linear interpolation extracts a 1-pixel width sample from 
  the image. When using this technique, and when the distance between successive 
  ellipses exceeds 2 pixels, many pixels will never be sampled. Integration over 
  elliptical annuli can be used to overcome this problem and extract all 
  information from the image array. The width of a given annulus is set from 
  halfway between the present and previous ellipse to halfway between the 
  present and next ellipse. Annuli are divided into sectors, and the angular 
  step between successive sectors is such as to make their areas approximately 
  constant over a given annulus. The angular span of a given sector is, however, 
  restricted to a maximum of 12 degrees and a minimum of 3 degrees. Individual 
  image pixels are considered to be inside a sector if the pixel geometric center 
  is inside that sector, otherwise they are not counted. The resulting sample 
  point for that particular sector will be the arithmetic mean or the median of 
  all the (non-flagged) pixels inside the sector. If all pixels in the sector
  are flagged, the sample point will be flagged as INDEF.
  </p>
  <p>
  If any sector vertex is outside the image boundary, its corresponding sample 
  point is flagged as INDEF.  The value of 'integrmode' is ignored when the 
  distance between the present ellipse and the next one is less than 2 pixels, 
  or when the semi-major axis is less than 20 pixels; in these cases bi-linear 
  interpolation is always used.  In the particular case of semi-major axis less 
  than 20 pixels, the interpolation includes a sub-pixel integration procedure,
  that better handles the steep intensity gradient found near a galaxy nucleus. 
  The mean and median methods execute 3-5 times slower than bi-linear 
  interpolation. 
  </p>
  <p>
  The basic convergency criterion discussed in the 'controlpar' pset help page
  relies on comparison with the fit rms. Since the averaging modes (mean and
  median) effectively smooth the extracted samples, the increased number of 
  pixels counted inside each sector as the algorithm proceeds outwards will 
  induce a decrease of the rms residual against which harmonic amplitudes are 
  compared, which translates into a variable convergency criterion along the 
  isophote sequence. To overcome this problem, the actual comparison takes into 
  account the sector area (kept approximately constant along the elliptical
  path). This average sector area is included in the task's main output table. 
  Notice that the equivalent sector area for bi-linear interpolation is 2.0 
  pixels.
  </p>
  <p>
  To increase stability in the convergency process, discrepant points in each
  sample can be found and flagged by a standard  k-sigma clipping routine before 
  submitting them to the harmonic fitting routine. The clipping routine is driven
  by parameters 'usclip' and 'lsclip', the <span style="font-family: monospace;">"k"</span> amplitude factor (upper and lower), and 'nclip', the number of passes (iterations) over the sample. If set to zero, 
  no clipping is performed.
  </p>
  <p>
  Parameter 'fflag' defines the maximum fraction of flagged data points which
  is acceptable in any given sample. If exceeded, the fitting algorithm
  stops increasing the semi-major axis. This happens usually when most of
  the sample is extracted from outside image boundaries.
  </p>
  <p>
  The best-fit sample at each fitted isophote can be optionally plotted
  immediately after fitting, at the graphics device specified by task parameter
  'sdevice'. This feature is turned off if the task is run in interactive
  mode and the graphics devices for both interaction and sample plotting
  are the same. The supported graphics devices are either the standard screen
  and plot devices, as well as the standard spool file 'stdvdm'. This last
  one is useful for automatic keeping a graphics hard-copy of each fitting 
  session.
  </p>
  <p>
  Samples corresponding to individual fitted isophotes can be optionally
  stored as a set of tables, to be used e.g. in subsequent plotting and analysis 
  steps. Parameter 'tsample' defines the root name of the table file family.
  Each table contains two columns, one with the sample angles in degrees, and
  the other with the intensity points. Ellipse data is also included in
  the table header.
  </p>
  <p>
  The angles output to tables can be expressed in two coordinate systems:
  the <span style="font-family: monospace;">"natural"</span> ellipse system, in which angle origin corresponds to the
  upper semi-major axis endpoint, and <span style="font-family: monospace;">"absolute"</span>, in which angle origin
  is the +y direction in the image frame. Selection among these systems
  is done by task parameter 'absangle'. In either case, angles increase
  counterclockwise.
  </p>
  <p>
  Optionally, the user can explicitly define which harmonics are to be
  fitted to the best-fit intensity sample. Task parameter 'harmonics' is
  used to specify the optional harmonic numbers. Harmonic numbers must be
  integer and separated by spaces. They must be entered in ascending
  order, as in 'harmonics = <span style="font-family: monospace;">"5 6 7 8"</span>'. The main output table will contain
  additional columns with the harmonic amplitudes and errors.  Note that,
  in this case, the amplitudes are NOT converted to geometric deviations
  from a perfect ellipse.  Instead, they are written in raw intensity
  units.  Third and fourth harmonics, as explained above, will still be
  written at their standard columns. These amplitudes can be converted into 
  deviations from an ellipse by using task 'ttools.tcalc'. Just divide the 
  respective columns by columns labeled 'SMA' and 'GRAD'. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(integrmode = <span style="font-family: monospace;">"bi-linear"</span>) [string, allowed values: bi-linear|mean|median]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(integrmode = "bi-linear") [string, allowed values: bi-linear|mean|median]' -->
  <dd>Method used to sample the image.
  </dd>
  </dl>
  <dl>
  <dt><b>(usclip = 3.0) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(usclip = 3.0) [real, min=0.0]' -->
  <dd>k-sigma clipping criterion applied to deviant points above the average.
  </dd>
  </dl>
  <dl>
  <dt><b>(lsclip = 3.0) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lsclip = 3.0) [real, min=0.0]' -->
  <dd>k-sigma clipping criterion applied to deviant points below the average.
  </dd>
  </dl>
  <dl>
  <dt><b>(nclip = 0) [int, min=0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nclip = 0) [int, min=0]' -->
  <dd>Number of iterations in the k-sigma clipping algorithm.
  </dd>
  </dl>
  <dl>
  <dt><b>(fflag = 0.5) [real, min=0.0, max=1.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fflag = 0.5) [real, min=0.0, max=1.0]' -->
  <dd>Acceptable fraction of flagged data points in intensity sample.
  </dd>
  </dl>
  <dl>
  <dt><b>(sdevice = <span style="font-family: monospace;">"none"</span>) [string, allowed values: |none|stdgraph|stdplot|stdvdm]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(sdevice = "none") [string, allowed values: |none|stdgraph|stdplot|stdvdm]' -->
  <dd>Graphics device for plotting intensity samples.
  </dd>
  </dl>
  <dl>
  <dt><b>(tsample = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tsample = "none") [string]' -->
  <dd>Root name for tables with intensity samples.
  </dd>
  </dl>
  <dl>
  <dt><b>(absangle = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(absangle = yes) [boolean]' -->
  <dd>Sample angles refer to image coordinate system ?
  </dd>
  </dl>
  <dl>
  <dt><b>(harmonics = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(harmonics = "none") [string]' -->
  <dd>List of optional upper harmonics to fit to each intensity sample.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ellipse
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
