.. _quickfit:

quickfit: Fit an ellipse to the solar limb.
===========================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  quickfit image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Name of image to be fit.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 4' -->
  <dd>Squibby brightness threshold to use in determining limb points.
  </dd>
  </dl>
  <dl id="l_xguess">
  <dt><b>xguess = 1024</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xguess' Line='xguess = 1024' -->
  <dd>X coordinate of center of first guess circle.
  </dd>
  </dl>
  <dl id="l_yguess">
  <dt><b>yguess = 1024</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yguess' Line='yguess = 1024' -->
  <dd>Y coordinate of center of first guess circle.
  </dd>
  </dl>
  <dl id="l_halfwidth">
  <dt><b>halfwidth = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='halfwidth' Line='halfwidth = 50' -->
  <dd>Halfwidth of window centered on previous limb point to search through
  for a limb point on the current line.
  </dd>
  </dl>
  <dl id="l_rowspace">
  <dt><b>rowspace = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rowspace' Line='rowspace = 20' -->
  <dd>Number of rows to skip between limbpoints near center in y.
  </dd>
  </dl>
  <dl id="l_rejectcoeff">
  <dt><b>rejectcoeff = .02</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rejectcoeff' Line='rejectcoeff = .02' -->
  <dd>Least squares rejection coefficient.  If radius of a limbpoint is more than
  this far from the limb, where limbradius = 1.0, it is not used in the fit.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Quickfit finds the least squares best fit ellipse to the limb in a full
  disk scan.  Quickfit returns the ellipse parameters (x,y coordinates of
  the ellipse center and the x and y semidiameters), the number of limbpoints
  found, the number of limbpoints rejected, and the fraction of limb
  points rejected by the least squares routine.  This 'fraction rejected'
  allows the user to determine to some extent the goodness of the data and
  allows him or her to rerun Quickfit with different parameters to take
  this goodness into account.  Quickfit also returns the sub-earth latitude
  and longitude when in verbose mode.  The ellipse and ephemeris parameters
  are stored in the image header for future reference.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To find the best fit ellipse for the limb in an image called <span style="font-family: monospace;">"image1"</span> and to
  see verbose output, one would use the following command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; quickfit image1 v+
  </pre></div>
  <p>
  This will also use the default values of rowspace, halfwidth,
  and rejectcoeff.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
