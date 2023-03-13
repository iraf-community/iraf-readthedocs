.. _apmask:

apmask: Create and IRAF pixel list mask of the apertures
========================================================

**Package: apextract**

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
  <dd>List of input images with aperture definitions.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output mask names.  As a convention the extension <span style="font-family: monospace;">".pl"</span> (pixel
  list) should be used.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>Apertures to recenter, resize, trace, and create a mask.  This only applies
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
  <dl id="l_trace">
  <dt><b>trace = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trace' Line='trace = yes' -->
  <dd>Trace apertures?
  </dd>
  </dl>
  <dl id="l_fittrace">
  <dt><b>fittrace = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fittrace' Line='fittrace = yes' -->
  <dd>Fit the traced points interactively?  The <i>interactive</i> parameter
  must also be yes.
  </dd>
  </dl>
  <dl id="l_mask">
  <dt><b>mask = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mask' Line='mask = yes' -->
  <dd>Create mask images?
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion axis) to
  be used in finding, recentering, resizing, editing, and starting to
  trace spectra.  A value of INDEF selects the middle of the image.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of dispersion lines to be summed or medianed.  The lines are taken
  around the specified dispersion line.  A positive value takes the
  sum and a negative value selects a median.
  </dd>
  </dl>
  <dl id="l_buffer">
  <dt><b>buffer = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='buffer' Line='buffer = 0.' -->
  <dd>Buffer to add to aperture limits.  One use for this is to increase
  the width of the apertures when a mask is used to fit data between
  the apertures.
  </dd>
  </dl>
  </section>
  <section id="s_additional_parameters">
  <h3>Additional parameters</h3>
  <p>
  I/O parameters and the default dispersion axis are taken from the
  package parameters, the default aperture parameters from
  <b>apdefault</b>, automatic aperture finding parameters from
  <b>apfind</b>, recentering parameters from <b>aprecenter</b>, resizing
  parameters from <b>apresize</b>, parameters used for centering and
  editing the apertures from <b>apedit</b>, and tracing parameters from
  <b>aptrace</b>.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Pixel list masks are created from the aperture definitions in the input
  images.  Pixel list masks are a compact way to define arbitrary
  regions of an image.  The masks may be used directly as an image with values
  of 1 (in an aperture) and 0 (outside an aperture).  Alternatively,
  some tasks may use a mask to define regions to be operated upon.
  When this task was written there were no such tasks though eventually
  some tasks will be converted to use this general format.  The intent
  of making an aperture mask is to someday allow using it with the task
  <b>imsurfit</b> to fit a background or scattered light surface.
  (See <b>apscatter</b> for an alternative method).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To replace all data outside the apertures by zero:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apmask image image.pl nfind=10
  cl&gt; imarith image * image.pl image1
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APMASK">
  <dt><b>APMASK V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APMASK' Line='APMASK V2.11' -->
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
  apdefault, aprecenter, apresize, apedit, aptrace, apall
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
