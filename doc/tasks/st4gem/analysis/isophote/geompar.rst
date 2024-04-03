.. _geompar:

geompar: Set geometry-related parameters (pset).
================================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  geompar
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This pset is used to set the geometrical parameters associated with
  the 'ellipse' task. 
  </p>
  <p>
  There are two basic types of geometrical parameters:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>Parameters that specify the first trial ellipse to be used by the task:
  'sma0', 'x0', 'y0', 'ellip0' and 'pa0'. 
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>Parameters that describe how to generate appropriate values for the semi-major 
  axis length: 'minsma', 'maxsma', 'step', 'linear' and 'maxrit'.
  </dd>
  </dl>
  <p>
  After fitting the first isophote, departing from values taken from type 1 
  parameters, the task proceeds by updating the semi-major axis length 
  following rules defined by type 2 parameters, and using at each step for
  the first guess ellipse parameters the solution from the previous fit.
  </p>
  <p>
  The semi-major axis update can be linear or geometric, depending on the 
  'linear' task parameter. If the geometric growing mode is chosen, the 
  semi-major axis length is increased by a factor of (1.  + 'step'), and 
  the process is repeated until either the semi-major axis value reaches 
  the value 'maxsma', or the last fitted ellipse has more than a given 
  fraction of its sampled points flagged out (see 'samplepar' pset). The 
  process then resumes from the first fitted ellipse (at 'sma0') inwards, in 
  steps of (1./(1.  + 'step')), until the semi- major axis length reaches 
  the value 'minsma'. In case of linear growing, the increment or decrement 
  value is given directly by 'step' in pixels. If 'maxsma' is set to INDEF,
  the semi-major axis will grow until a low signal-to-noise criterion is met.
  See 'controlpar' pset for details.
  </p>
  <p>
  Type 1 parameters have default values that usually guarantee that the first
  isophote will be fitted properly. The starting semi-major axis 
  length, 'sma0', cannot be very small or zero because in the very central 
  regions of a galaxy image the geometry information is usually too much 
  distorted due to pixelation and/or seeing. It cannot be too large either, 
  because at external galaxy regions the low signal-to-noise might preclude a 
  proper fit. An intermediate region will ensure the proper balance between 
  high S/N, low geometrical distortion, and reasonably large number of pixels.
  </p>
  <p>
  Position angles are defined in the range -90 &lt; PA &lt;= 90.
  Avoid using as starting position angle 'pa0 = 0.', since the algorithm may 
  not work properly in this case. When the object is such that position angles 
  are near either extreme of the range, noise can make the solution jump back 
  and forth, between successive isophotes, by amounts close to 180 degrees.
  The output table may be cleaned of those jumps by processing it with
  task 'ttools.tcalc' using
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  equals = if PA&lt;0. then PA+180. else PA
  
  </pre></div>
  <p>
  or a similar expression.
  </p>
  <p>
  Parameter 'maxrit' sets the maximum semi-major axis length for iterative
  mode. When fitting at larger semi-major axis lengths, the ellipse geometry
  parameters (center, ellipticity, position angle) are kept fixed at their
  last fitted values. This may be useful for sampling regions of very low
  surface brightness, where the algorithm may become unstable and unable to
  recover reliable geometry information from isophotes. If set to INDEF,
  iterative mode continues out to where lack of either signal-to-noise or
  number of valid data points forces the task to stop growing the semi-major 
  axis (see 'controlpar' pset).
  </p>
  <p>
  The algorithm has no ways of finding where, in the input image section, 
  the galaxy to be measured sits in. That is, 'x0' and 'y0' must be properly 
  set from start. Since they are set by default to INDEF, the task has a number 
  of options to set them properly. First, an object locator routine is run,
  scanning a 10X10 window centered either on the input 'x0', 'y0' coordinates
  or, if any one of them, or both, are set to INDEF, on the input image section 
  center. A number of actions are possible depending on the successful (or not)
  acquisition of an object. Below it is shown what takes place 
  depending on the
  values of parameters 'interactive', 'recenter' and 'xylearn':
  </p>
  <dl id="l_Successful">
  <dt><b>Successful acquisition:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Successful' Line='Successful acquisition:' -->
  <dd><dl>
  <dt><b>Starting 'x0<span style="font-family: monospace;">','</span>y0' set to INDEF or outside image section boundaries:</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Starting' Line='Starting 'x0','y0' set to INDEF or outside image section boundaries:' -->
  <dd>Task begins at once to fit at position found by object locator.
  </dd>
  </dl>
  <dl>
  <dt><b>Valid starting 'x0<span style="font-family: monospace;">','</span>y0':</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Valid' Line='Valid starting 'x0','y0':' -->
  <dd>Task looks to 'recenter' parameter. If 'yes', fit at position found by
  object locator. If 'no', fit at original 'x0<span style="font-family: monospace;">','</span>y0' position.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_Not">
  <dt><b>Not successful acquisition:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Not' Line='Not successful acquisition:' -->
  <dd><dl>
  <dt><b>Starting 'x0<span style="font-family: monospace;">','</span>y0' set to INDEF or outside image section boundaries:</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Starting' Line='Starting 'x0','y0' set to INDEF or outside image section boundaries:' -->
  <dd><dl>
  <dt><b>Interactive mode:</b></dt>
  <!-- Sec='DESCRIPTION' Level=2 Label='Interactive' Line='Interactive mode:' -->
  <dd>Task issues a warning message and turns cursor on at once. User is supposed
  to identify galaxy center in the displayed image (using <span style="font-family: monospace;">'x'</span> cursor keystroke).
  </dd>
  </dl>
  <dl>
  <dt><b>Non-interactive mode:</b></dt>
  <!-- Sec='DESCRIPTION' Level=2 Label='Non' Line='Non-interactive mode:' -->
  <dd>If 'xylearn' is set to 'yes', task prompts user at STDIN for 'x0<span style="font-family: monospace;">','</span>y0',
  even if it is being run with mode=h. If 'xylearn' is set to 'no', aborts.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>Valid starting 'x0<span style="font-family: monospace;">','</span>y0':</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Valid' Line='Valid starting 'x0','y0':' -->
  <dd>Atempts to fit at 'x0<span style="font-family: monospace;">','</span>y0' position anyway.
  </dd>
  </dl>
  </dd>
  </dl>
  <p>
  Parameter 'xylearn' is used to automatically update the pset when valid
  center coordinates become available. If 'xylearn' is set to 'yes' and
  'x0<span style="font-family: monospace;">','</span>y0' are set to INDEF, the task will write to the 'geompar' pset the 
  valid values that will come either from the object locator or the 
  cursor/STDIN input. If 'xylearn' is set to 'no', nothing happens. This
  feature is useful when trying several runs of 'ellipse' on the same 
  object. The first time the task is run, the object center must be 
  defined by the user, but in subsequent runs this step is skipped. 
  </p>
  <p>
  In some cases the object locator algorithm mail fail, even though there
  is enough signal-to-noise to start a fit (e.g. in objects with very
  high ellipticity). In those cases the sensitivity of the algorithm
  can be decreased. See the 'controlpar' pset.
  </p>
  <p>
  Full support for World Coordinate System (WCS) is not available in this
  version of 'ellipse'. However there is a simpler scheme for handling 
  relative coordinates, that works only in pixel units. Task parameter 
  'physical' controls the choice between <span style="font-family: monospace;">"physical"</span> or <span style="font-family: monospace;">"section"</span> coordinate 
  systems. If set to 'no', pixel coordinates relative to the input image section 
  will be used throughout. If set to 'yes', pixel coordinates will be relative 
  to the full 2-D frame corresponding to the input image name eventually stripped 
  of subsection specification. This feature can be useful, for instance, when 
  handling a large image with many objects scattered around the field. 
  Each object can be measured by an independent 'ellipse' call in a batch 
  script, using for each object just the subsection that contains the object, 
  thus saving memory and speeding up the fit. The resulting tables with center
  coordinates will nevertheless share the same coordinate system of the main
  image. This section handling scheme also supports stepping (the same in
  both directions X and Y) and multi-dimensional image files.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(x0 = INDEF) [real, min=1.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(x0 = INDEF) [real, min=1.0]' -->
  <dd>Initial ellipse center X coordinate (pixel).
  </dd>
  </dl>
  <dl>
  <dt><b>(y0 = INDEF) [real, min=1.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(y0 = INDEF) [real, min=1.0]' -->
  <dd>Initial ellipse center Y coordinate (pixel).
  </dd>
  </dl>
  <dl>
  <dt><b>(ellip0 = 0.2) [real, min=0.05, max=1.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ellip0 = 0.2) [real, min=0.05, max=1.0]' -->
  <dd>Initial ellipticity, defined as e = 1 - b/a, thus a circle has zero
  ellipticity. The algorithm diverges at zero ellipticity.
  </dd>
  </dl>
  <dl>
  <dt><b>(pa0 = 20.0) [real, min=-90.0, max=90.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pa0 = 20.0) [real, min=-90.0, max=90.0]' -->
  <dd>Initial position angle, in degrees, measured counterclockwise from the
  +y direction.
  </dd>
  </dl>
  <dl>
  <dt><b>(sma0 = 10.0) [real, min=5.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(sma0 = 10.0) [real, min=5.0]' -->
  <dd>Initial semi-major axis length (pixel).
  </dd>
  </dl>
  <dl>
  <dt><b>(minsma = 0.0) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(minsma = 0.0) [real, min=0.0]' -->
  <dd>Minimum semi-major axis length to be measured (pixel). If set to zero,
  the central pixel intensity will be measured.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxsma = INDEF) [real, min=1.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxsma = INDEF) [real, min=1.0]' -->
  <dd>Maximum semi-major axis length to be measured (pixel).
  </dd>
  </dl>
  <dl>
  <dt><b>(step = 0.1) [real, min=1.0e-3]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(step = 0.1) [real, min=1.0e-3]' -->
  <dd>Step in semi-major axis length between successive ellipses. 
  In case of geometric steps, the semi-major axis length for the next 
  ellipse is calculated as either (1.0 + 'step') or (1.0/(1.0 + 'step')) 
  times the current length, depending on the sense of growing.
  In case of linear steps, the semi-major axis length for the 
  next ellipse is calculated as either SMA + 'step' or SMA - 'step', where 
  SMA is the current length, depending on the sense of growing
  (this is described in more detail in the description section 
  above).  
  </dd>
  </dl>
  <dl>
  <dt><b>(linear = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(linear = no) [boolean]' -->
  <dd>Increase/decrease semi-major axis by linear step, as opposed to geometric ?
  </dd>
  </dl>
  <dl>
  <dt><b>(maxrit = INDEF) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxrit = INDEF) [real, min=0.0]' -->
  <dd>Maximum semi-major axis length for iterative mode. Beyond this length,
  non-iterative mode is entered regardless of other conditions.
  </dd>
  </dl>
  <dl>
  <dt><b>(recenter = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(recenter = yes) [boolean]' -->
  <dd>Allows finding routine to re-center x0-y0 after successful object detection ?
  </dd>
  </dl>
  <dl>
  <dt><b>(xylearn = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xylearn = yes) [boolean]' -->
  <dd>Updates pset with new x0-y0, either from finding routine, from first fit
  or from keyboard input ?
  </dd>
  </dl>
  <dl>
  <dt><b>(physical = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(physical = yes) [boolean]' -->
  <dd>Use physical coordinate system, as opposed to input section coordinate system ?
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
  ellipse, controlpar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
