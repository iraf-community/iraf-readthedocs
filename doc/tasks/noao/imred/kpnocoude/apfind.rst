.. _apfind:

apfind: Automatically find spectra and define apertures
=======================================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apfind input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images in which spectra are to be identified and
  apertures defined automatically.
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
  input image or reference image defined in the database and the
  parameter <i>nfind</i> must be greater than zero.
  </dd>
  </dl>
  <dl id="l_recenter">
  <dt><b>recenter = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = no' -->
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
  be used in finding the spectra.  A value of INDEF selects the middle of the
  image.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of dispersion lines to be summed or medianed.  The lines are taken
  around the specified dispersion line.  A positive value sums lines and
  a negative value medians lines.
  </dd>
  </dl>
  <dl id="l_nfind">
  <dt><b>nfind = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nfind' Line='nfind = 1' -->
  <dd>Maximum number of apertures to be defined.  This is a query parameter
  so the user is queried for a value except when given explicitly on
  the command line.
  </dd>
  </dl>
  <dl id="l_minsep">
  <dt><b>minsep = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minsep' Line='minsep = 5.' -->
  <dd>Minimum separation between spectra.  Weaker spectra or noise within this
  distance of a stronger spectrum are rejected.
  </dd>
  </dl>
  <dl id="l_maxsep">
  <dt><b>maxsep = 1000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxsep' Line='maxsep = 1000.' -->
  <dd>Maximum separation between adjacent spectra.  This parameter
  is used to identify missing spectra in uniformly spaced spectra produced
  by fiber spectrographs.  If two adjacent spectra exceed this separation
  then it is assumed that a spectrum is missing and the aperture identification
  assignments will be adjusted accordingly.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = <span style="font-family: monospace;">"increasing"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = "increasing"' -->
  <dd>When assigning aperture identifications order the spectra <span style="font-family: monospace;">"increasing"</span>
  or <span style="font-family: monospace;">"decreasing"</span> with increasing pixel position (left-to-right or
  right-to-left in a cross-section plot of the image).
  </dd>
  </dl>
  </section>
  <section id="s_additional_parameters">
  <h3>Additional parameters</h3>
  <p>
  I/O parameters and the default dispersion axis are taken from the
  package parameters, the default aperture parameters are taken from the
  task <b>apdefault</b>, and parameters used for centering and editing the
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
  For each image in the input image list spectra are identified and
  default apertures defined.  The automatic aperture finding is performed
  only if 1) there are no apertures defined for the reference image, 2)
  there are no apertures defined for the input image, 3) the parameter
  <i>find</i> is yes, and 4) the parameter <i>nfind</i> is greater than
  zero.
  </p>
  <p>
  The automatic finding algorithm uses the following steps.  First, all local
  maxima are found.  The maxima are sorted by peak value and the weaker
  of the peaks separated by less than the value given by the parameter
  <i>minsep</i> are rejected.  Finally, at most the <i>nfind</i> strongests
  peaks are kept.  <b>Nfind</b> is a query parameter, so if it is not
  specified explicitly on the command line, the desired number of spectra
  to be found is requested.  After the peaks have been found the
  <b>center1d</b> algorithm is used to refine the centers of the
  profiles.  Apertures having the default parameters set with the task
  <b>apdefault</b> are defined at each center.  This algorithm is also
  available with the <span style="font-family: monospace;">'f'</span> key in the task <b>apedit</b> with the change that
  existing apertures are kept and count toward the maximum number
  specified by <b>nfind</b>.
  </p>
  <p>
  The automatic assignment of aperture numbers, beam numbers, and titles
  has several options.  The simplest is when no aperture identification
  table, parameter <i>apidtable</i>, is specified and the maximum separation
  parameter, <i>maxsep</i>, is very large.  In this case the aperture and
  beam numbers are sequential starting from one and numbered either from
  left-to-right or right-to-left depending on the <i>order</i> parameter.
  There are no aperture titles in this case.  If two adjacent spectra are
  separated by more than the specified maximum then the aperture numbers
  jump by the integer part of the ratio of the separation to the
  specified maximum separation.  This is used when the image is expected
  to have evenly spaced spectra, such as in multifiber spectrographs, in
  which some may be missing due to broken fibers.  Finally, the
  aperture identification table (either a text file or an image
  having a set of SLFIBnnn keyowrds) may contain lines with aperture number,
  beam number, and (optional) title.  The sequential numbers are then
  indices into this table.  Note that the skipping of missing spectra and
  the ordering applies to entries in this table as well.
  </p>
  <p>
  The ways in which the automatic method can fail for evenly spaced
  spectra with missing members are when the first spectrum is missing on
  the side from which the ordering begins and when the expected rather
  the actual number of spectra is used.  In the first case one can use
  the interactive <span style="font-family: monospace;">'o'</span> key of the aperture editing facility to specify the
  identity of any aperture and then all other apertures will be
  appropriately reidentified.  If more spectra are sought than actually
  exist then noise spikes may be mistakenly found.  This problem can be
  eliminated by specifying the actual number of spectra or minimized by
  using the threshold centering parameter.
  </p>
  <p>
  The <i>recenter</i> parameter allows recentering apertures if defined by
  a reference image.  Since the purpose of this task is to find new
  apertures it is usually the case that there are no reference images and
  recentering is not done.  The default apertures are of fixed width.
  The <i>resize</i> parameter may be used to adjust the widths in a
  variety of ways.  The aperture positions and any other parameters may
  also be edited with the aperture editing function if selected by the
  <i>apedit</i> parameter and the task is run interactively.
  </p>
  <p>
  If the task is interactive the user is queried whether to perform
  various steps on each image.  The queries may be answered with one of
  the four values <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span> and <span style="font-family: monospace;">"NO"</span>, where an upper case
  response suppresses all further queries to this question.
  </p>
  <p>
  The aperture finding algorithm may be selected from nearly every task
  in the package.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apfind image nfind=10
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APFIND">
  <dt><b>APFIND V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APFIND' Line='APFIND V2.11' -->
  <dd>The <span style="font-family: monospace;">"apertures"</span> parameter can be used to select apertures for resizing,
  recentering, tracing, and extraction.  This parameter name was previously
  used for selecting apertures in the recentering algorithm.  The new
  parameter name for this is now <span style="font-family: monospace;">"aprecenter"</span>.
  The aperture ID table information may now be contained in the
  image header under the keywords SLFIBnnn.
  </dd>
  </dl>
  <p>
  SEE ALSO
  center1d, apdefault, aprecenter, apresize, apedit, apall
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS'  -->
  
