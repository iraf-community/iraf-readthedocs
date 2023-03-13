.. _bpmedit:

bpmedit: examine and edit bad pixel masks associated with images
================================================================

**Package: tv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bpmedit images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images whose bad pixel masks are to be edit.  The images must
  contain the keyword BPM whose value is an existing bad pixel mask to
  be edit.  If the keyword is missing or the mask does not exit a warning
  is issued and the task proceeds to the next image.
  </dd>
  </dl>
  <dl id="l_bpmkey">
  <dt><b>bpmkey = <span style="font-family: monospace;">"BPM"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmkey' Line='bpmkey = "BPM"' -->
  <dd>The mask to be edited is defined by the value of this keyword.
  </dd>
  </dl>
  <dl id="l_frame">
  <dt><b>frame = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame' Line='frame = 1' -->
  <dd>The display frame where the image with the mask overlay is shown.
  </dd>
  </dl>
  <dl id="l_refframe">
  <dt><b>refframe = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refframe' Line='refframe = 2' -->
  <dd>The display frame with the image without the mask is shown.
  </dd>
  </dl>
  <dl id="l_command">
  <dt><b>command = <span style="font-family: monospace;">"display ..."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='command' Line='command = "display ..."' -->
  <dd>Command for displaying and updating the mask overlay.  This is the
  command used with <b>imedit</b>.  This should be changed with care.
  In the string the following changes are made:
  <div class="highlight-default-notranslate"><pre>
  $image -- substitute the image
   $mask -- substitute the mask being edited
  $frame -- substitute the value of the frame parameter
  $erase -- substituted by imedit
  </pre></div>
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = yes' -->
  <dd>Use the task interactively with the display?  This sets the behavior
  of <b>imedit</b> as described for the parameter of the same name.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Image cursor input.  This is normally either a null string for interactive
  display editing or the value of a file with cursor commands to edit
  non-interactively.  See the help for <b>imedit</b> for more information.
  </dd>
  </dl>
  </section>
  <section id="s_additional_parameters">
  <h3>Additional parameters</h3>
  <p>
  This task calls <b>display</b> to load the image display and <b>imedit</b>
  to do the editing.  The current default parameters are used from those
  tasks except the image names, frames, and the display command are set by
  this task.  Also the search radius is set to zero (i.e. no centering).
  Also the <i>display</i> and <i>cursor</i> parameters override the
  values of the parameters of the same name in <b>imedit</b>.  Of particular
  note is the default value for imedit.value which defines the mask value to
  be set initially.  This value may be changed interactively in <b>imedit</b>.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Bpmedit</b> is a variant of <b>imedit</b>.  It displays the input images
  with the masks overlaid.  The mask is defined
  by the value of the keyword keywords specified by the <i>bpmkey</i>
  parameter.  The editing commands apply to the mask overlay and not the
  image pixels.  In this application the edited values should be integer mask
  values.  In the usual case where zero indicates good pixels and non-zero
  indicates bad pixels one can set and unset values by changing current
  replacement value with <span style="font-family: monospace;">":value"</span>.  Two useful parameters, <span style="font-family: monospace;">":minvalue"</span>
  and <span style="font-family: monospace;">":maxvalue"</span>, are useful in this context to allow editing only
  specific ranges of mask values.  Note that many of the imedit options are
  not useful for mask editing.  The <span style="font-family: monospace;">'?'</span> keystroke prints a list of the
  useful cursor and colon commands.  This list is also shown below.
  </p>
  <p>
  Because it is common to want to see the image pixels to which the
  mask values apply this task loads two image display frames.  In one the
  mask is overlaid and changes to the mask are updated with the
  redisplay options of imedit (note the options to turn on and off
  automatic redisplay).  In the second the image without the mask is
  displayed.  The editing commands may be given in either frame but the
  mask updates will appear only in the mask overlay frame.
  </p>
  <p>
  This task also provides the parameters <i>display</i> and <i>cursor</i>
  to use <b>imedit</b> in a non-interactive manner as described for that
  task.  Because only the setting and clearing of rectangles, circles,
  or vectors makes sense with this task this may not be of great use.
  Also there are many other tasks that can be used to edit masks
  non-interactively.
  </p>
  <p>
  Please read the help for <b>imedit</b> for details of the editing
  process.
  </p>
  <div class="highlight-default-notranslate"><pre>
              BPMEDIT CURSOR KEYSTROKE COMMANDS
  
  The following are the useful commands for BPMEDIT.  Note all
  the commands for IMEDIT are available but only those shown
  here should be used for editing pixel masks.
  
      ?       Print help
      :       Colon commands (see below)
      i       Initialize (start over without saving changes)
      q       Quit and save changes
      r       Redraw image display
      +       Increase radius by one
      -       Decrease radius by one
      I       Interrupt task immediately
      Q       Quit without saving changes
  
  The following editing options are available.  Rectangular
  and vector regions are specified with two positions and
  aperture regions are specified by one position.  The current
  aperture type (circular or square) is used in the latter
  case.  All the following substitute the new value set for
  the "value" parameter (see :value).  Some replace all pixels
  within the mask that have the same pixel value as the value
  at the cursor position.
  
      d       Set rectangle to "value"
      e       Set aperture to "value"
      u       Undo last change (see also <span style="font-family: monospace;">'i'</span>, <span style="font-family: monospace;">'j'</span>, and <span style="font-family: monospace;">'k'</span>)
      v       Set vector to "value"
      =       Replace pixels = to "cursor value" to "value"
      &lt;       Replace pixels &lt; or = to "cursor value" to "value"
      &gt;       Replace pixels &gt; than or = to "cursor value" to "value"
  
              BPMEDIT COLON COMMANDS
  
  The colon either print the current value of a parameter when
  there is no value or set the parameter to the specified
  value.
  
  aperture [type]      Aperture type (circular|square)
  autodisplay [yes|no] Automatic image display?
  command [string]     Display command
  display [yes|no]     Display image?
  eparam               Edit parameters
  radius [value]       Aperture radius
  value [value]        Constant substitution value
  minvalue [value]     Minimum value for modification (INDEF=minimum)
  maxvalue [value]     Maximum value for modification (INDEF=maximum)
  write [name]         Write changes to name
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Interactively edit a mask.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bpmedit wpix
  </pre></div>
  <p>
   
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imedit, display, badpiximage, text2mask, mskexpr, mskregions, imexpr
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
