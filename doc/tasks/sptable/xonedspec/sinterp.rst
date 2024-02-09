.. _sinterp:

sinterp: Interpolate a table of x,y pairs to create a spectrum
==============================================================

**Package: xonedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sinterp tbl_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_tbl_file">
  <dt><b>tbl_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tbl_file' Line='tbl_file' -->
  <dd>The name of a file which contains the x,y pairs to be used as
  the basis for interpolation. The pairs must be in order of
  increasing x.
  </dd>
  </dl>
  <p>
  The following parameters may or may not be necessary, depending
  on the options selected.
  </p>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>If a few single elements are desired, rather than a full
  array of elements, the user may enter a sequence of x values
  from the terminal or a file to be used to interpolate into
  the x,y table (parameter curve_gen=no).
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>If parameter make_image=yes, then an image file name is needed
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 5' -->
  <dd>If the interpolator is a polynomial fit or spline (interp_mode=
  chebyshev, legnedre, spline3, spline1), the order of the fit
  is required.
  </dd>
  </dl>
  <dl id="l_x1">
  <dt><b>x1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x1' Line='x1' -->
  <dd>If parameter curve_gen=yes, this is the starting x value to
  begin the curve generation.
  </dd>
  </dl>
  <p>
  Of the following three parameters, two must be specified, and the
  third will be derived.
  </p>
  <dl id="l_x2">
  <dt><b>x2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x2' Line='x2 = 0.0' -->
  <dd>As above, but x2 determines the endpoint of the curve.
  </dd>
  </dl>
  <dl id="l_dx">
  <dt><b>dx = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dx' Line='dx = 0.0' -->
  <dd>As above, but dx determines the pixel-to-pixel increment
  to be used during the curves generation.
  </dd>
  </dl>
  <dl id="l_npts">
  <dt><b>npts = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='npts' Line='npts = 0' -->
  <dd>As above, but this determines the number of pixels to be generated.
  </dd>
  </dl>
  <dl id="l_curve_gen">
  <dt><b>curve_gen = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='curve_gen' Line='curve_gen = no' -->
  <dd>If this parameter is set to yes, then parameters x1, and two of
  the three x2, dx, npts are required. The output is in the form
  of new x,y pairs and may be redirected to a text file.
  But if parameter make_image is also yes, the output is
  in the form of an IRAF image file having the name given by
  the parameter image. If curve_gen=no, the user must supply
  a set of x values and interpolation is performed on those values.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = no' -->
  <dd>If set to yes, then curve_gen=yes is implied and an image file name
  is requied. A one dimensional IRAF image is created.
  </dd>
  </dl>
  <dl id="l_tbl_size">
  <dt><b>tbl_size = 1024</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tbl_size' Line='tbl_size = 1024' -->
  <dd>This parameter defines the maximum size to be set aside for
  memory storage of the input x,y pairs.
  </dd>
  </dl>
  <dl id="l_interp_mode">
  <dt><b>interp_mode = <span style="font-family: monospace;">"chebyshev"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp_mode' Line='interp_mode = "chebyshev"' -->
  <dd>This parameter controls the method of interpolation. The linear
  and curve options are true interpolators, while chebyshev,
  legendre, spline3, and splin1 are fits to the data.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The specified file is read assuming it is a text file containing
  pairs of x,y values in the form: xxx yyy. The table is used
  to define the function y(x). The pairs must be entered in the file
  in increasing order of x.
  </p>
  <p>
  The user specifies either specific x values for which the function
  is to be evaluated, or specifies that a sequence of values beginning
  with x1 are to be generated. In the former case, the explicit x values
  may come either from the keyboard or from a file. In the latter case
  the user must also specify the sequence by defining the increment, dx,
  the endpoint, x2, and the number of points to generate in the sequence.
  Then y(x) is evaluated at x1, x1+dx, x1+2*dx, ...  , x1+(n-2)*dx, x2.
  Only 2 of the 3 parameters (x2, dx, npts) are needed to fully
  specify the sequence.
  </p>
  <p>
  The output of the function evaluation is either new x,y pairs written
  to STDOUT, or an IRAF image.
  </p>
  <p>
  The function used to evaluated the tabular data may be any of the following
  forms:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>Linear interpolation between points.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>Smooth interpolation between points.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd>A polynomial fit of either Legendre or Chebyshev types.
  </dd>
  </dl>
  <dl>
  <dt><b>(4)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(4)' -->
  <dd>A cubic or linear spline.
  </dd>
  </dl>
  <p>
  If the table of x,y pairs is very large, the parameter tbl_size
  should be set to the number of pairs. For example, if a spectrum
  is available as a text file of x,y pairs (such as might be
  obtained from IUE), and the number of pairs is 4096, then tbl_size
  should be set to 4096. This provides for sufficient memory to
  contain the table.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following shows how a text file may be used to generate a spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sinterp textfile make+ x1=4000 x2=5000 npts=1024 \
  &gt;&gt;&gt; image=testimage interp_mode=curve
  </pre></div>
  <p>
  The following sequence shows how to generate a spectrum of an IRS
  standard star using the calibration file data as the source.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lcalib flam feige34 caldir=onedstds$irscal/ &gt;textfile
  cl&gt; sinterp textfile make+ x1=3550 dx=1.242 npts=1024 \
  &gt;&gt;&gt; interp_mode=linear image=feige34
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SINTERP">
  <dt><b>SINTERP V2.10.3+</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SINTERP' Line='SINTERP V2.10.3+' -->
  <dd>The image header dispersion coordinate system has been updated to the
  current system.
  </dd>
  </dl>
  <dl id="l_SINTERP">
  <dt><b>SINTERP V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SINTERP' Line='SINTERP V2.10' -->
  <dd>This task is unchanged.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  lcalib
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
