.. _apbackground:

apbackground: Background subtraction algorithms
===============================================

**Package: apextract**

.. raw:: html

  <p>
  Data from slit spectra allow the determination and subtraction
  of the background sky using information from regions near the object
  of interest.  Background subtraction may also apply to cases of
  scattered light though other techniques for scattered light removal
  may be more appropriate.  The APEXTRACT package provides for determining
  the background level at each wavelength (line or column along the dispersion
  axis) from a set of regions and extrapolating and subtracting the
  background at each pixel extracted from the object profile.  The
  type of background used during extraction is specified by the parameter
  <i>background</i>.  If the value <span style="font-family: monospace;">"none"</span> is used then no background is
  subtracted and any background parameters defined for an aperture are
  ignored.  If the value is <span style="font-family: monospace;">"average"</span>, <span style="font-family: monospace;">"median"</span>, <span style="font-family: monospace;">"minimum"</span> or <span style="font-family: monospace;">"fit"</span> then a
  background is determined, including a variance estimate when using variance
  weighted extraction (see <i>apvariance</i>), and the subtracted background
  spectrum may be output if the <i>extras</i> parameter is set.
  </p>
  <p>
  The basic aperture definition structure used in the APEXTRACT package
  includes associated background regions and fitting parameters.  The
  background regions are specified by a list of colon delimited ranges
  defined relative to the center of the aperture.  There are generally
  two ranges, one on each side of the object, though one sided or more
  complex sets may be used to avoid contaminated or missing parts
  of the slit.  The default ranges are defined by the parameter
  <i>b_sample</i>.  Often the ranges are better set graphically using a
  cursor by invoking the <span style="font-family: monospace;">'b'</span> option of the aperture editor.
  </p>
  <p>
  If the background type is <span style="font-family: monospace;">"average"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"minimum"</span> then pixels
  occupying these regions are averaged, medianed, or the minimum found to
  produce a single background level for all object pixels at each wavelength.  
  Note that the <span style="font-family: monospace;">"average"</span> choice does not exclude any pixels which may
  yield a background contaminated by cosmic rays.  The <span style="font-family: monospace;">"median"</span> or <span style="font-family: monospace;">"minimum"</span>
  is recommended instead.
  </p>
  <p>
  If the background type is <span style="font-family: monospace;">"fit"</span> then a function is fit to the pixels in the
  background regions using the ICFIT options (see <b>icfit</b>).  The
  parameter <i>b_naverage</i> may be used to compute averages or medians of
  groups or all of the points within each sample region.  The fit is defined
  by a function type <i>b_function</i>; one of legendre polynomial, chebyshev
  polynomial, linear spline, or cubic spline, and function order
  <i>b_order</i> (number of polynomial terms or spline pieces).  An
  interactive rejection of grossly deviant points from the fit may also be
  used.  The fitted function can define a constant, sloped, or higher order
  background for the object pixels.
  </p>
  <p>
  Note that the background setting function, the <span style="font-family: monospace;">'b'</span> key in <b>apedit</b>,
  may be used to set the background regions for all the background options
  but it will always show the result of a fit regardless of the background
  type.
  </p>
  <p>
  After determining a background by averaging, medianing, minimizing, or
  fitting, a box car smoothing step may be applied.  The box car size is
  given by the parameter <i>skybox</i>.  When the number of available
  background pixels is small, due to a small slit for instance, the noise
  introduced to the extracted object spectrum may be unsatisfactorily large.
  By smoothing the background one can reduce the noise when the background
  consists of a smooth continuum.  The trade-off, however, is that near sharp
  features the smoothing will smear the features out and give a poorer
  subtraction of these features.  One could extract both the object and
  background separately and apply a background smoothing separately using
  other image processing tools.  However, this is not possible for variance
  weighted extraction because of the intimate connection between the
  background levels, the profile determination, and the variance estimates
  based on both.  Thus, this smoothing feature is included.
  </p>
  <p>
  The background determined by the methods outlined above is actually
  subtracted as a separate step during extraction.  The background
  is also used during profile fitting when cleaning or using variance
  weighted extraction.  See <b>apvariance</b> and <b>approfile</b> for
  further discussion.
  </p>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  approfile apvariance apdefault icfit apall apsum
  </p>
  
  </section>
  
  <!-- Contents: 'SEE ALSO'  -->
  
