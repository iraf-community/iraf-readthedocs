.. _flatfit:

flatfit: Sum and normalize flat field spectra
=============================================

**Package: iids**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  flatfit root records
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_root">
  <dt><b>root</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='root' Line='root' -->
  <dd>The root file name for the input names of the flat field
  spectra to be accumulated and fit for normalization.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The range of spectra indicating the elements of the string.
  The names of the spectra will be formed by appending the range
  elements to the input root name.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>This is the root file name for the names of the spectra which will
  be created during normalization. The aperture number for the observation
  will be appended to the root in form <span style="font-family: monospace;">"root.nnnn"</span> where nnnn is the aperture
  number with leading 0's.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"chebyshev"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "chebyshev"' -->
  <dd>The accumulated spectra are fit by this function type - either
  chebyshev or legendre polynomials, or spline3 or spline1 interpolators.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 4' -->
  <dd>The order of the fit using the above function. This should generally be
  a low order fit to avoid introduction of high spatial frequency wiggles.
  </dd>
  </dl>
  <dl id="l_niter">
  <dt><b>niter = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niter' Line='niter = 1' -->
  <dd>The number of iterations to reject discrepant pixels upon initial
  startup of the solution.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = 2.0' -->
  <dd>The number of sigmas for which data values less than this cutoff are
  rejected.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = 2.0' -->
  <dd>The number of sigmas for which data values greater than this cutoff are
  rejected.
  </dd>
  </dl>
  <dl id="l_ngrow">
  <dt><b>ngrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrow' Line='ngrow = 0' -->
  <dd>The number of pixels on either side of a rejected pixel to also be rejected.
  </dd>
  </dl>
  <dl id="l_div_min">
  <dt><b>div_min = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='div_min' Line='div_min = 1.0' -->
  <dd>During the normalization process, a division by zero will produce
  this value as a result.
  </dd>
  </dl>
  <dl id="l_interact">
  <dt><b>interact = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interact' Line='interact = yes' -->
  <dd>If set to yes, graphical interaction with the normalization process
  is provided for at least the first aperture for which sums are available.
  If set to no, no interaction is provided.
  </dd>
  </dl>
  <dl id="l_all_interact">
  <dt><b>all_interact = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='all_interact' Line='all_interact = no' -->
  <dd>If set to yes, then interaction will be provided for all apertures
  for which sums have been accumulated. If set to no then the parameter interact
  will determine if the first aperture data is to be interactive.
  </dd>
  </dl>
  <dl id="l_coincor">
  <dt><b>coincor = )_.coincor</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coincor' Line='coincor = )_.coincor' -->
  <dd>If set to yes, coincidence correction is applied to the data during
  the summation process, and the following three parameters are required.
  See <b>coincor</b> for more about this correction.
  <dl>
  <dt><b>ccmode = )_.ccmode</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ccmode' Line='ccmode = )_.ccmode' -->
  <dd>The mode by which the coincidence correction is to be performed.
  This may be <span style="font-family: monospace;">"iids"</span> or <span style="font-family: monospace;">"photo"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>deadtime = )_.deadtime</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='deadtime' Line='deadtime = )_.deadtime' -->
  <dd>The detector deadtime in seconds.
  </dd>
  </dl>
  <dl>
  <dt><b>power = )_.power</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='power' Line='power = )_.power' -->
  <dd>Power law IIDS non-linear correction exponent.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  When null the standard cursor is used otherwise
  the specified file is used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The specified spectra are added by aperture number to produce
  summations which are then fit by a specified fitting function.
  The fitting function is then divided into the sum to produce a
  normalized (to 1.0) sum in which the low frequency spatial
  response has been removed.
  </p>
  <p>
  The resultant normalized images may then be divided into all other
  data to remove the pixel-to-pixel variations without introducing
  any color terms. The spectra may be used directly if they happen
  to be object spectra in which the low frequency response is to be
  removed.
  </p>
  <p>
  During the accumulation process the spectra may be corrected for
  coincidence losses if the detector is subject to the phenomenon.
  </p>
  <p>
  After accumulating all input spectra, the pixels in each sum are
  fit according to
  the specified function. If the interactive switches are set, then
  graphical interaction is made available. If only the interact parameter
  is set to yes, then only the data from the first aperture will
  be available for interaction. Data from subsequent apertures will
  be fit using the same parameters and number of iterations as the
  first. If the all_interact parameter is also
  set, then data from each aperture will be presented for interaction.
  </p>
  <p>
  At each step in the fit, pixels which are discrepant by more than
  <span style="font-family: monospace;">"upper"</span> sigmas above the fit, or <span style="font-family: monospace;">"lower"</span> sigmas below the fit, are
  rejected. The rejection process may be applied many times (iterations)
  to continue rejecting pixels. If the upper and lower sigmas are
  not equal, the resulting fit will be biased slightly above the mean
  (for lower &lt; upper) or below the mean (upper &lt; lower). This is useful
  when the spectrum being fit is that of a star having either absorption
  or emission lines.
   
  A display is presented of the sum and the fit through the data.
  A status line is printed containing the fit type, the order of
  the fit, the rms residual from the fit, and the number of data
  points in the fit after one iteration of rejection.
  </p>
  <p>
  The following cursor keystrokes are then active:
  </p>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='?' -->
  <dd>Clear the screen and display the active keystrokes
  </dd>
  </dl>
  <dl>
  <dt><b>/</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='/' -->
  <dd>Indicate active keystrokes on the status line
  </dd>
  </dl>
  <dl id="l_e">
  <dt><b>e</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='e' Line='e' -->
  <dd>Change plot mode to an error plot. This display is defined
  as the deviation from the fit divided by the data values [ (data - fit)/ data]
  at each pixel
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='f' Line='f' -->
  <dd>Change plot mode back to the fit through the data display
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Change the order of the fit.
  </dd>
  </dl>
  <dl id="l_l">
  <dt><b>l</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='l' Line='l' -->
  <dd>Change the lower rejection criterion (in units of sigma).
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='u' Line='u' -->
  <dd>Change the upper rejection criterion.
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='s' Line='s' -->
  <dd>Change both rejection criteria to the same value.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='r' Line='r' -->
  <dd>Reinstate rejected pixels.
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='i' Line='i' -->
  <dd>Iterate one more time.
  </dd>
  </dl>
  <dl id="l_n">
  <dt><b>n</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='n' Line='n' -->
  <dd>Iterate several more times - the user is prompted for the count.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='q' Line='q' -->
  <dd>Quit and accept the solution
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;CR&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='&lt;CR&gt;' -->
  <dd>RETURN is the same as <span style="font-family: monospace;">'q'</span> but a confirmation request to exit must be
  answered as yes.
  </dd>
  </dl>
  <p>
  All keystrokes but ?,/,e,f, and q force another iteration which will
  reject additional pixels. To fully inhibit pixel rejection, the sigmas
  should be set to a large value (e.g. 100).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example will accumulate 8 spectra and fit the first
  aperture data interactively but not the second, and apply coincidence
  corrections to the sums. The upper and lower rejection criteria
  have been altered to bias the seventh order fit to a higher level.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flatfit nite1 1-4,201-204 coin+ low=1.4 up=3 order=7
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  For some reason, the error plot is supposed to have a zero level line
  drawn, but none appears.
  </p>
  <p>
  As in most of the IRAF software, the order of a fit refers to the number
  of terms in the fit, so that a fit of order 1 implies a constant and order
  2 implies a linear fit.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  coincor, flatdiv
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
