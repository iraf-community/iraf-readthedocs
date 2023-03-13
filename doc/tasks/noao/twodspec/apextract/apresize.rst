.. _apresize:

apresize: Resize apertures
==========================

**Package: apextract**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apresize input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images in which apertures are to be resized.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>Apertures to recenter, resize, trace, and extract.  This only applies
  to apertures read from the input or reference database.  Any new
  apertures defined with the automatic finding algorithm or interactively
  are always selected.  The syntax is a list comma separated ranges
  where a range can be a single aperture number, a hyphen separated
  range of aperture numbers, or a range with a step specified by <span style="font-family: monospace;">"x&lt;step&gt;"</span>;
  for example, <span style="font-family: monospace;">"1,3-5,9-12x2"</span>.
  </dd>
  </dl>
  <dl id="l_references">
  <dt><b>references = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='references' Line='references = ""' -->
  <dd>List of reference images to be used to define apertures for the input
  images.  When a reference image is given it supersedes apertures
  previously defined for the input image. The list may be null, <span style="font-family: monospace;">""</span>, or
  any number of images less than or equal to the list of input images.
  There are three special words which may be used in place of an image
  name.  The word <span style="font-family: monospace;">"last"</span> refers to the last set of apertures written to
  the database.  The word <span style="font-family: monospace;">"OLD"</span> requires that an entry exist
  and the word <span style="font-family: monospace;">"NEW"</span> requires that the entry not exist for each input image.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Run this task interactively?  If the task is not run interactively then
  all user queries are suppressed and interactive aperture editing is
  disabled.
  </dd>
  </dl>
  <dl id="l_find">
  <dt><b>find = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='find' Line='find = yes' -->
  <dd>Find the spectra and define apertures automatically?  In order for
  spectra to be found automatically there must be no apertures for the
  input image or reference image defined in the database.
  </dd>
  </dl>
  <dl id="l_recenter">
  <dt><b>recenter = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = no' -->
  <dd>Recenter the apertures?
  </dd>
  </dl>
  <dl id="l_resize">
  <dt><b>resize = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resize' Line='resize = yes' -->
  <dd>Resize the apertures?
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = yes' -->
  <dd>Edit the apertures?  The <i>interactive</i> parameter must also be yes.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion axis) to
  be used in resizing the spectra.  A value of INDEF selects the middle of the
  image.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of dispersion lines to be summed or medianed.  The lines are taken
  around the specified dispersion line.  A positive value takes a
  sum and a negative value selects a median.
  </dd>
  </dl>
  <dl id="l_llimit">
  <dt><b>llimit = INDEF, ulimit = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='llimit' Line='llimit = INDEF, ulimit = INDEF' -->
  <dd>Lower and upper aperture size limits.  If the parameter <i>ylevel</i> is
  INDEF then these limits are assigned to all apertures.  Otherwise
  these parameters are used as limits to the resizing operation.
  A value of INDEF places the aperture limits at the image edge (for the
  dispersion line used).
  </dd>
  </dl>
  <dl id="l_ylevel">
  <dt><b>ylevel = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ylevel' Line='ylevel = 0.1' -->
  <dd>Data level at which to set aperture limits.  If it is INDEF then the
  aperture limits are set at the values given by the parameters
  <i>llimit</i> and <i>ulimit</i>.  If it is not INDEF then it is a
  fraction of the peak or an actual data level depending on the parameter
  <i>peak</i>.  It may be relative to a local background or to zero
  depending on the parameter <i>bkg</i>.
  </dd>
  </dl>
  <dl id="l_peak">
  <dt><b>peak = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='peak' Line='peak = yes' -->
  <dd>Is the data level specified by <i>ylevel</i> a fraction of the peak?
  </dd>
  </dl>
  <dl id="l_bkg">
  <dt><b>bkg = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bkg' Line='bkg = yes' -->
  <dd>Subtract a simple background when interpreting the <b>ylevel</b> parameter.
  The background is a slope connecting the first minima
  away from the aperture center.
  </dd>
  </dl>
  <dl id="l_r_grow">
  <dt><b>r_grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='r_grow' Line='r_grow = 0.' -->
  <dd>Change the lower and upper aperture limits by this fractional amount.
  The factor is multiplied by each limit and the result added to limit.
  </dd>
  </dl>
  <dl id="l_avglimits">
  <dt><b>avglimits = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='avglimits' Line='avglimits = no' -->
  <dd>Apply the average lower and upper aperture limits to all apertures.
  </dd>
  </dl>
  </section>
  <section id="s_additional_parameters">
  <h3>Additional parameters</h3>
  <p>
  I/O parameters and the default dispersion axis are taken from the
  package parameters, the default aperture parameters are taken from the
  task <b>apdefault</b>, automatic aperture finding parameters are taken
  from <b>apfind</b>, and parameters used for centering and editing the
  apertures are taken from <b>apedit</b>.
  </p>
  <p>
  When this operation is performed from the task <b>apall</b> all parameters
  except the package parameters are included in that task.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each image in the input image list, the aperture limits are
  redefined to be either specified values or by finding the points at
  which the spectrum profile, linearly interpolated, first crosses a
  specified value moving away from the aperture center at the specified
  dispersion line.  In the latter case the limits may then be increased
  or decreased by a specified percentage, a maximum lower and upper limit,
  may be imposed, and the independent limits may be averaged and the
  single values applied to all the apertures.
  </p>
  <p>
  The simplest resizing choice is to reset all the aperture limits to
  the values specified by <i>llimit</i> and <i>ulimit</i>.  This option
  is selected if the parameter <i>ylevel</i> is INDEF.
  </p>
  <p>
  There are several options for specifying a data level at which an
  aperture is sized.  The most common method (the default) is to specify
  a fraction of the peak value since this is data independent and physically
  reasonable.  This is done by setting the fraction with the parameter
  <i>ylevel</i> and the parameter <i>peak</i> to yes.  If the peak parameter
  is no then the level is a data value.
  </p>
  <p>
  The levels may be relative to zero, as might be used with fibers or
  high dispersion / high signal-to-noise data, or relative to a local
  linear background, as would be appropriate for slit data having a
  significant background.  A background is found and used if the
  parameter <i>bkg</i> is set.  The background determination is very
  simple.  Starting at the peak two background points are found, one in
  each direction, which are inflection points; i.e. the first pixels
  which are less than their two neighbors.  A linear slope is fit and
  subtracted for the purposes of measuring the peak and setting the
  aperture limits.  Note that if the slope is significant the actual
  limits may not correspond to the intercepts of a line at constant data
  value.
  </p>
  <p>
  Once aperture limits, a distance relative to the center, are determined
  they are increased or decreased by a percentage, expressed as a fraction,
  given by the parameter <i>r_grow</i>.  To illustrate the operation,
  if xlow is the initial lower limit then the final lower limit will be:
  </p>
  <p>
  	xlow final = xlow * (1 + r_grow)
  </p>
  <p>
  A value of zero leaves the aperture limits unchanged.
  </p>
  <p>
  After the aperture limits are found, based on the above steps, a fixed lower
  limit, given by the parameter <i>llimit</i>, is applied to the lower
  aperture points and, similarly, a fixed upper limit is applied to the
  upper aperture points.  This feature protects against absurdly wide apertures.
  </p>
  <p>
  Finally, if the parameter <i>avglimits</i> is set the individual aperture
  limits are averaged to form an average aperture.  This average aperture
  is then assigned to all apertures.  This option allows keeping common
  aperture sizes but allowing variation due to seeing changes.
  </p>
  <p>
  The resizing algorithm is available in the interactive aperture editor.
  Here one may select individual apertures or all apertures using the
  <span style="font-family: monospace;">'a'</span> switch.  The resizing algorithm described above is selected using
  the <span style="font-family: monospace;">'z'</span> key.  An simple alternative is the <span style="font-family: monospace;">'y'</span> key which resizes
  apertures to the y level marked by the cursor.
  </p>
  <p>
  If the task is interactive the user is queried whether to perform
  various steps on each image.  The queries may be answered with one of
  the four values <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span> and <span style="font-family: monospace;">"NO"</span>, where an upper case
  response suppresses all further queries to this question.
  </p>
  <p>
  The aperture resizing algorithm may be selected from nearly every task
  in the package with the <i>resize</i> parameter.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To resize all apertures to the range -4 to 4:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apresize image llimit=-4 ulimit=4 ylevel=INDEF
  </pre></div>
  <p>
  2.  To resize all aperture to a point which is 5% of the peak relative
  to a local background:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apresize image ylevel=.05 peak+ bkg+
  </pre></div>
  <p>
  3.  To resize all apertures to the point where the data exceeds 100
  data units:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apresize image ylevel=100 peak- bkg-
  </pre></div>
  <p>
  4.  To resize all apertures to default values of the task except
  averaging all the results at the end:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apresize image avg+
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APRESIZE">
  <dt><b>APRESIZE V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APRESIZE' Line='APRESIZE V2.11' -->
  <dd>The <span style="font-family: monospace;">"apertures"</span> parameter can be used to select apertures for resizing,
  recentering, tracing, and extraction.  This parameter name was previously
  used for selecting apertures in the recentering algorithm.  The new
  parameter name for this is now <span style="font-family: monospace;">"aprecenter"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  center1d, ranges, apfind, aprecenter, apedit, apall
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
