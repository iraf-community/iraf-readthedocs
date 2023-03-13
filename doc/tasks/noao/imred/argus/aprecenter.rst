.. _aprecenter:

aprecenter: Recenter apertures
==============================

**Package: argus**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  aprecenter input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images in which apertures are to be recentered.
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
  <dt><b>recenter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = yes' -->
  <dd>Recenter the apertures?
  </dd>
  </dl>
  <dl id="l_resize">
  <dt><b>resize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resize' Line='resize = no' -->
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
  be used in recentering the spectra.  A value of INDEF selects the middle of the
  image.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of dispersion lines to be summed or medianed.  The lines are taken
  around the specified dispersion line.  A positive value takes a sum
  and a negative values selects a median.
  </dd>
  </dl>
  <dl id="l_aprecenter">
  <dt><b>aprecenter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aprecenter' Line='aprecenter = ""' -->
  <dd>List of apertures to be used in shift calculation.
  </dd>
  </dl>
  <dl id="l_npeaks">
  <dt><b>npeaks = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='npeaks' Line='npeaks = INDEF' -->
  <dd>Select the specified number of apertures with the highest peak values
  to be recentered.  If the number is INDEF all apertures will be selected.
  If the value is less than 1 then the value is interpreted as a fraction
  of total number of apertures.
  </dd>
  </dl>
  <dl id="l_shift">
  <dt><b>shift = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shift' Line='shift = yes' -->
  <dd>Use the median shift from recentering the selected apertures to apply to
  all apertures.  The recentering is then a constant shift for all apertures.
  The median is the average of the two central values for an even number
  of apertures.
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
  For each image in the input image list, the aperture center positions
  are redefined by centering at the specified dispersion line using the
  <b>center1d</b> algorithm with centering parameters from <b>apedit</b>.
  Normally this is done when inheriting apertures from an aperture
  reference image.  The recentering does not change the <span style="font-family: monospace;">"trace"</span> of the
  aperture but simple adds a shift across the dispersion axis.
  </p>
  <p>
  There are a several recentering options.  Each selected aperture may be
  recentered independently.  However, if some or all of the spectra are
  relatively weak this may actually be worse than using the reference
  apertures defined by strong spectra or flat fields in the case of
  fibers or aperture masks.  One may select a subset of apertures to be
  used in calculating shift.  This is done with a the <i>aprecenter</i>
  list of aperture numbers (see
  <b>ranges</b> for the syntax) and/or by selecting a specific number or
  fraction of the apertures with the strongest peak values.  The list
  selection is done first and the strongest remaining apertures are used
  to satisfy the <b>npeaks</b> value.  Though some or all of the apertures
  may be recentered independently the most common case of recentering
  reference apertures is to account for detector shifts.  In this case
  one expects that any shift should be common to all apertures.  The
  <i>shift</i> parameter allows using the new centers for all selected
  apertures to compute a median shift to be added to ALL apertures.  Using
  a median shift for all apertures is the default.
  </p>
  <p>
  The <i>find</i> parameter allows automatically finding apertures if none
  are defined for the image or by a reference image.  Since the purpose
  of this task is to recenter reference apertures it is usually the case
  that reference images are used and apertures are not defined by this
  task.  One case in which the apertures from the image itself might be
  recentered is if one wants to use a different dispersion line.  The
  <i>resize</i> parameter may be used to adjust the widths in a variety
  of ways based on the spectra profiles specific to each image.  The
  aperture positions and any other parameters may also be edited with the
  aperture editing function if selected by the <i>apedit</i> parameter and
  the task is run interactively.  The recentering algorithm may be run
  from the aperture editor using the <span style="font-family: monospace;">'g'</span> keystroke.
  </p>
  <p>
  If the task is interactive the user is queried whether to perform
  various steps on each image.  The queries may be answered with one of
  the four values <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span> and <span style="font-family: monospace;">"NO"</span>, where an upper case
  response suppresses all further queries to this question.
  </p>
  <p>
  The aperture recentering algorithm may be selected from nearly every task
  in the package.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aprecenter newimage reference=flat
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APRECENTER">
  <dt><b>APRECENTER V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APRECENTER' Line='APRECENTER V2.11' -->
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
  center1d, ranges, apfind, apresize, apedit, apall
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
