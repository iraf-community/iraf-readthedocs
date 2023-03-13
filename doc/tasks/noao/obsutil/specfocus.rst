.. _specfocus:

specfocus: Determine spectral focus and alignment variations
============================================================

**Package: obsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  specfocus images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of 1D or 2D focus images.  Typically the input is a list of raw
  2D CCD images of arc slit spectra.  The 1D image input is provided to
  allow use of extraction techniques beyond those provided by this task.
  </dd>
  </dl>
  <dl id="l_focus">
  <dt><b>focus = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='focus' Line='focus = ""' -->
  <dd>List of focus identification values to be associated with each input image
  or an image header keyword containing the values.  The list may be an
  explicit list of values, a range specification, an @ file containing the
  values, or an image header keyword.  If none of these is given the
  identification values are simple index values in the order of the input
  images.  A range specification has the forms A, AxC, A-BxC where A is a
  starting value, B is an ending value, and C is an increment.
  </dd>
  </dl>
  <dl id="l_corwidth">
  <dt><b>corwidth = 20.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='corwidth' Line='corwidth = 20.' -->
  <dd>Correlation width in pixels.
  </dd>
  </dl>
  <dl id="l_level">
  <dt><b>level = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='level' Line='level = 0.5' -->
  <dd>Percent or fraction of the correlation peak at which to measure focus
  widths.  The default is 50% or full width at half maximum.
  </dd>
  </dl>
  <dl id="l_shifts">
  <dt><b>shifts = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts' Line='shifts = yes' -->
  <dd>Compute dispersion shifts across the dispersion when there are multiple
  samples?  If yes and there are multiple samples across the dispersion
  (<i>ndisp</i> &gt; 1), pixel shifts relative to the central sample are
  determine by crosscorrelation.
  </dd>
  </dl>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 2' -->
  <dd>Dispersion axis for 2D images.  The image header keyword DISPAXIS has
  precedence over this value.
  </dd>
  </dl>
  <dl id="l_nspectra">
  <dt><b>nspectra = 1, ndisp = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nspectra' Line='nspectra = 1, ndisp = 1' -->
  <dd>The number of spectral samples across the dispersion
  and the number of subpieces along the dispersion to divide the spectra
  into.  If <i>nspectra</i> is greater than one then information about
  variations across the dispersion will be determined and if <i>ndisp</i> is
  greater than 1 information about variations along the dispersion will be
  determined.  <i>Nspectra</i> applies only to 2D images.  For 1D spectra in
  multispec format each line is used as a separate sample.
  </dd>
  </dl>
  <dl id="l_slit1">
  <dt><b>slit1 = INDEF, slit2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='slit1' Line='slit1 = INDEF, slit2 = INDEF' -->
  <dd>The lower and upper edges of the slit (or data region) in pixel
  coordinates (lines or columns) across the dispersion axis.  A value
  of INDEF specifies the image edges.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>File in which to record the results.  If no file is specified no log
  output is produced.
  </dd>
  </dl>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  All keys select an image and a sample (one of the <i>ndisp</i> samples along
  the dispersion and one of the <i>nspectra</i> samples across the dispersion)
  which is then generally highlighted.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Help summary
  b  Best focus at each sample summary graphs
  d  Delete image, sample, or point
  p  Profiles at one sample for all images and all samples for one image
  q  Quit
  r  Redraw
  s  Spectra at one sample for all images and all samples for one image
  u  Undelete spectrum, sample, or point
  w  Profile widths verses focus and distribution of widths
  z  Zoom on a single sample showing correlation profile and spectrum
  &lt;space&gt;  Status line output for selected image and sample
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task estimates the dispersion width of spectral lines in sequences of
  arc spectra taken at different focus settings (or with some other parameter
  varied).  The widths can be measured at different spatial and dispersion
  positions, called <span style="font-family: monospace;">"samples"</span>, on the detector.  The width estimates are
  recorded and displayed graphically to investigate dependencies and
  determine appropriate settings for the spectrograph setup.  The task may
  also measure dispersion shifts when multiple spectral samples are
  specified.  This task does not measure the focus point-spread-function
  width across the dispersion.
  </p>
  <p>
  The input images are specified with an image template list.  The list may
  consist of explicit image names, wildcard templates, and @ files.  A
  <span style="font-family: monospace;">"focus"</span> value is associated with each image.  This may be any numeric
  quantity (integer or floating point).  The focus values may be specified in
  several ways.  If no value is given then index numbers are assigned to
  the images in the order in which they appear in the image list.  A range
  list may be specified as described in the help topic <b>ranges</b>.  This
  consists of individual values, ranges of values, a starting value and a
  step, and a range with a step.  The elements of the list are separated by
  commas, ranges are separated by hyphens, and a step is indicated by the
  character <span style="font-family: monospace;">'x'</span>.  Long range lists, such as a list of individual focus
  values, may be placed in a file and specified with the @&lt;filename&gt;
  convention.  Finally, a parameter in the image header may be used for the
  focus values by simply specifying the parameter name.
  </p>
  <p>
  Two dimensional long slit images are summed into one or more one
  dimensional spectra across the dispersion.  The dispersion axis is defined
  either by the image header parameter DISPAXIS or the <i>dispaxis</i> task
  parameter with the image header parameter having precedence.  The range of
  lines or columns across the dispersion to be used is specified by the
  parameters <i>slit1</i> and <i>slit2</i>.  If specified as INDEF then the
  image limits are used.  This range is then divided into the number of
  spectra given by the parameter <i>nspectra</i>.  Use of more than one
  spectrum across the dispersion allows investigation of variations along the
  slit.  In addition, if the parameter <i>shifts</i> is set the spectrum
  nearest the center is used as a reference against which shifts in the
  dispersion positions of the features in the other spectra are determined by
  crosscorrelation.
  </p>
  <p>
  The conversion of two dimensional spectra to one dimensional spectra may
  also be performed separately using the tasks in the <b>apextract</b>
  package.  This would be done typically for multifiber or echelle format
  spectra.  If the two dimensional spectra have been extracted to one
  dimensional spectra in this way the task ignores the dispersion axis and
  number of spectra parameters.  The data limits (<i>slit1</i> and
  <i>slit2</i>) are still used to select a range of lines in  <span style="font-family: monospace;">"multispec"</span>
  format images.  The <i>shifts</i> parameter also applies when there are
  multiple spectra per image.  However, it does not make sense in the case of
  echelle spectra and so it should be set to no in that case.
  </p>
  <p>
  In addition to dividing the spatial axis into a number of spectra the
  dispersion axis may also be divided into a set of subspectra.  The number
  of divisions is specified by the <i>ndisp</i> parameter which applies to
  both long slit and 1D extracted spectra.  When the dispersion axis is
  divided into more than one sample, the dependence of the dispersion widths
  and shifts along the dispersion may be investigated.
  </p>
  <p>
  Each spectral sample has a low order continuum subtracted using a
  noninteractive iterative rejection algorithm to exclude the spectral
  lines.  This technique is described further under the topic
  <i>continuum</i>.  The continuum subtracted spectrum is then tapered with a
  cosine bell function and autocorrelated.  The length of the taper and the
  range of shifts for the correlation is set by the <i>corwidth</i>
  parameter.  This parameter should be only slightly bigger than the expected
  feature widths to prevent correlations between different spectral lines.
  The correlation profile is offset to zero at the edges of the profile and
  normalized to unity at the profile center.  The profiles may be viewed as
  described below.
  </p>
  <p>
  If there is more than one spatial sample the central spectrum is also
  crosscorrelated against the other spectra at the same dispersion
  sample.  The crosscorrelation is computed in exactly the same way as
  the autocorrelation.  The crosscorrelation profiles are only used for
  determining shifts between the two samples and are not used in the
  width determinations.
  </p>
  <p>
  A cubic spline interpolator is fit to the profiles and this interpolation
  function is used to determined the profile width and center.  The width is
  measured at a point given by the <i>level</i> parameter relative to the
  profile peak.  It may be specified as a fraction of the peak if it is less
  than one or a percentage of the peak if it is greater than one.  The
  default value of 0.5 selects the full width at half maximum.  The
  autocorrelation width is divided by the square root of two to yield an
  estimate of the width of the spectral features in the spectrum in units of
  pixels.
  </p>
  <p>
  Having computed the width and shift for each input image at each sample,
  the <span style="font-family: monospace;">"best focus"</span> values (focus, width, and shift) are estimated for each
  sample.  As discussed later, it is possible to exclude some samples
  from this calculation by deleting them graphically.
  First the images with the smallest measured width at each distinct
  focus are selected since it is possible to input more than one image at the
  same focus.  The selected images are sorted by focus value and the image
  with the smallest width is found.  If that image has the lowest or highest
  focus (which will always be the case if there are only one or two images)
  then the best focus, width, and shift are those measured for that image.
  If there are three or more focus values and the minimum width focus image
  is not an endpoint then parabolic interpolation is used to find the minimum
  width.  The focus at this minimum width is the <span style="font-family: monospace;">"best focus"</span>.
  The dispersion shift is the parabolic interpolation of the shifts at
  the best focus.  The <span style="font-family: monospace;">"average best focus"</span> values are then the average of
  the <span style="font-family: monospace;">"best focus"</span> values over all samples.
  </p>
  <p>
  After computing the correlation profiles, the profile widths and shifts,
  and the best focus values, an interactive graphics mode is entered.  This
  is described in detail below.  The graphics mode is exited with the <span style="font-family: monospace;">'q'</span>
  key.  At this point the results are written to the standard output (usually
  the terminal) and to a logfile if one is specified.  The output begins with
  a banner identifying the task, version of IRAF, the user, and the date and
  time.  The next line gives the best average focus and width.  This banner
  also appears in all plots.  Then each image is listed with the focus value
  and average width (over all samples).  Finally the image with the smallest
  average width is identified and tables showing the width and shifts (if
  computed) at each sample position are printed.  If there is only one sample
  then the tables are not output.
  </p>
  <p>
  INTERACTIVE GRAPHICS MODE
  </p>
  <p>
  There are five types of plot formats which are selected with the <span style="font-family: monospace;">'b'</span>, <span style="font-family: monospace;">'p'</span>,
  <span style="font-family: monospace;">'s'</span>, <span style="font-family: monospace;">'w'</span>, and <span style="font-family: monospace;">'z'</span> keys.  The available formats and their content are
  modified depending on the number of images and the number of samples.  If
  there is only one image or one sample per image some of the plot formats
  are not available.  If there are a large number of images or a large number
  of samples the content of the plot formats may be abbreviated for
  legibility.
  </p>
  <p>
  In all plots there is a concept of the current image and the current
  sample.  In general there is an indication, usually a box, of which image
  and sample is the current one.  The current image and sample are
  changed by pointing at a particular point, box, circle, or symbol for that
  image and sample and typing a key.
  </p>
  <p>
  The <span style="font-family: monospace;">'b'</span> key produces summary graphs of the best focus values (as described
  above) at each sample position.  There must be more than one image and more
  than one sample (either along or across the dispersion or both).  This is
  the initial plot shown when this condition is satisfied.  The central graph,
  which is always drawn, represents the best focus (smallest) width at each
  sample by circles of size proportional to the width.  The position of the
  circle indicates the central line and column of the sample.  If there are
  multiple samples across the dispersion and the <i>shifts</i> parameter is
  set then little vectors are also drawn from the center of the circle in the
  direction of the shift and with length proportional to the shift.  If there
  are 5 or fewer samples in each dimension the values of the best focus and
  the width and shift (if computed and nonzero) at that focus, are printed on
  the graph next to the circles.  If there are more samples this information
  may be obtained by pointing at the sample and typing the space key.
  </p>
  <p>
  In addition to the spatial graph there may be graphs along the line or column
  axes.  These graphs again show the widths as circles but one axis is either
  the line or column and the other axis is either the best focus value or the
  shift.  The focus graph marks the best average focus (over all samples) by
  a dashed line and a solid line connects the mean focus at each column or
  line.  The focus graphs will only appear if there is more than one sample
  along a particular image axis.  The shift graphs will only appear if the
  shifts are computed (<i>shifts</i> parameter is yes) and there is more than
  one sample along a particular dimension.  Lines are drawn at zero shift and
  connecting the mean shift at each point along the spatial axis.  Note that
  there is always a point at zero shift which is the reference sample.
  </p>
  <p>
  The best focus graphs are the exception in showing a current image and
  sample.  When changing to one of the other plots based on a current image
  and sample the circle from the central spatial graph nearest the cursor is
  used (note that the other focus and shift graphs are ignored).  The sample
  is defined by it's spatial position and the image is the one with
  focus closest to the best focus value of that sample.
  </p>
  <p>
  The <span style="font-family: monospace;">'w'</span> key produces a graph showing the sample widths as a function of
  focus value.  There must be more than one image and more than one sample
  for this type of graph.  The top graph is a symbol plot of width verses
  focus.  The symbols are crosses except for the current image which is shown
  with pluses.  The current sample is highlighted with a box.  Also shown is
  a long dashed line connecting the widths for the current sample at each
  focus value and short dashed lines showing the best average focus and
  width.
  </p>
  <p>
  The lower portion of the <span style="font-family: monospace;">'w'</span> key are graphs showing the
  widths as circles with size proportional to the width and position
  corresponding to the spatial position of the sample in the image.  If there
  are more than 5 samples in either dimension the graph is for the current
  image.  Otherwise there is a box for each image with the focus value
  (provided there are not too many images) indicated.  The circles are
  arranged as they would be spatially in columns and rows.  The samples
  closest to the best focus are indicated by pluses.  This allows seeing
  where the best focus values cluster.  The current image and sample are
  indicated by highlighting boxes.
  </p>
  <p>
  The <span style="font-family: monospace;">'p'</span> key produces graphs of the autocorrelation profiles.  This also
  requires more than one image and more than one sample.  The top graph shows
  the profiles of all images at a particular sample and the bottom graph shows
  the profiles of all samples at a particular image.  The bottom sample boxes
  are arranged in columns and rows in the same way the samples are
  distributed in the image.  The current image and current sample are
  highlighted by a box.
  </p>
  <p>
  The profiles are drawn with a solid line using the interpolator function
  and the actual pixel lags are indicated with pluses.  The profiles are
  drawn shifted by the amount computed from the crosscorrelation.
  Note that the shift is added to the autocorrelation profile
  and the crosscorrelation profile is not what is plotted.  The zero shift
  position is indicated by a vertical line.  If there are less than 25 boxes
  the boxes are labeled by the width, shift (if nonzero), and focus.
  </p>
  <p>
  The <span style="font-family: monospace;">'s'</span> key plot is similar to the <span style="font-family: monospace;">'p'</span> key plot but shows the spectra
  rather than the profiles.  The top graphs are the spectra of each image at
  a particular sample and the bottom graphs are the spectra of each sample
  for a particular image.  The current image and sample are highlighted by a
  box.
  </p>
  <p>
  The <span style="font-family: monospace;">'z'</span> key graphs the autocorrelation profile and the spectrum
  of a single sample.  This graph provides scales which are not
  provided with the <span style="font-family: monospace;">'p'</span> and <span style="font-family: monospace;">'s'</span> graphs.  If there is only one image
  and one sample then this is the only plot available.
  </p>
  <p>
  It is possible to exclude some of the samples from the calculation
  of the best focus and best average focus values.  This is done by
  deleting them using the <span style="font-family: monospace;">'d'</span> key.  When using the <span style="font-family: monospace;">'d'</span> key you must
  specify the sample to be deleted in one of the graphs.  You are
  then asked if only that sample (point) is to be deleted, if all
  samples from that image are to be deleted, or if the same sample
  from all images is to be deleted.  The deleted data is no longer
  shown explicitly but the space occupied by the data is still present
  so that the data may be included again by typing the <span style="font-family: monospace;">'u'</span> undelete
  key.  When the task is exited with the <span style="font-family: monospace;">'q'</span> key the printed and
  logged results will have the deleted data excluded.
  </p>
  <p>
  The remaining cursor keys do the following.  The <span style="font-family: monospace;">'?'</span> key gives a
  summary of the cursor keys.  The <span style="font-family: monospace;">'r'</span> key redraws the current plot.
  The space key prints information about the current sample.  This
  is mostly used when there are too many images or samples to annotate
  the graphs with the focus, width, and shift.  Finally the <span style="font-family: monospace;">'q'</span>
  key quits the task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  A series of 2D focus images is obtained with focus values
  starting at 400 in steps of -50.  The slit is between columns 50
  and 130.  There are 3 samples across the dispersion and 3 along
  the dispersion.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lpar specfocus
         images = "@imlist"       List of images
         (focus = "400x-50")     Focus values
      (corwidth = 20)             Correlation width
         (level = 0.5)            Percent or fraction of peak
        (shifts = yes)            Compute shifts across the disp?\n
      (dispaxis = 2)              Dispersion axis (long slit only)
      (nspectra = 3)              Number of spec samples (ls only)
         (ndisp = 3)              Number of dispersion samples
         (slit1 = 50)             Lower slit edge
         (slit2 = 130)            Upper slit edge\n
       (logfile = "logfile")      Logfile
          (mode = "ql")
  cl&gt; specfocus @imlist
  &lt;Interactive graphics which is exited with the <span style="font-family: monospace;">'q'</span> key&gt;
  SPECFOCUS: NOAO/IRAF V2.10EXPORT valdes Thu 19:41:41 17-Sep-92
    Best avg focus at 206.6584 with avg width of 2.91 at 50% of peak
  
    -- Average Over All Samples
  
                                   Image  Focus  Width
                              jdv011.imh   100.   3.78
                              jdv010.imh   150.   3.28
                              jdv009.imh   200.   2.95
                              jdv008.imh   250.   3.17
                              jdv007.imh   300.   3.41
                              jdv006.imh   350.   3.74
                              jdv005.imh   400.   4.16
  
    -- Image jdv009.imh at Focus 200. --
  
          Width at 50% of Peak:
  
                       Columns
                         50-76      77-103    104-130
             Lines  +---------------------------------
             2-267  |    2.93       2.58       2.74
           268-533  |    3.17       2.76       2.89
           534-799  |    3.77       2.23       3.50
  
          Position Shifts Relative To Central Sample:
  
                       Columns
                         50-76      77-103    104-130
             Lines  +---------------------------------
             2-267  |    0.68       0.00       0.18
           268-533  |    0.64       0.00       0.13
           534-799  |    0.92       0.00       0.16
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imexamine, implot, ranges, splot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'CURSOR COMMANDS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
