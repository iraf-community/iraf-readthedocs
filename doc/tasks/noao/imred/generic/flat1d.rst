.. _flat1d:

flat1d: Make flat field by fitting a 1D func. to the lines or columns
=====================================================================

**Package: generic**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  flat1d input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Calibration images to be used to make the flat fields.  The images may
  contain image sections.  Only the region covered by the section will be
  modified in the output image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Flat field images to be created or modified.  The number of output images
  must match the number of input images.  If an output image does not exist
  it is first created and initialized to unit response.
  </dd>
  </dl>
  <dl id="l_axis">
  <dt><b>axis = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='axis' Line='axis = 1' -->
  <dd>Axis along which the one dimensional fitting is done.  Axis 1 corresponds
  to fitting the image lines and axis 2 corresponds to fitting the columns.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Set the fitting parameters interactively?
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Lines or columns to be used in the fits.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Number of sample points to combined to create a fitting point.
  A positive value specifies an average and a negative value specifies
  a median.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = spline3' -->
  <dd>Function to be fit to the image lines or columns.  The functions are
  <span style="font-family: monospace;">"legendre"</span> (legendre polynomial), <span style="font-family: monospace;">"chebyshev"</span> (chebyshev polynomial),
  <span style="font-family: monospace;">"spline1"</span> (linear spline), and <span style="font-family: monospace;">"spline3"</span> (cubic spline).  The functions
  may be abbreviated.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>The order of the polynomials or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 2.5, high_reject = 2.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 2.5, high_reject = 2.5' -->
  <dd>Low and high rejection limits in units of the residual sigma.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 1' -->
  <dd>Number of rejection iterations.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 1.' -->
  <dd>When a pixel is rejected, pixels within this distance of the rejected pixel
  are also rejected.
  </dd>
  </dl>
  <dl id="l_minflat">
  <dt><b>minflat = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minflat' Line='minflat = 0.' -->
  <dd>When the fitted value is less than the value of this parameter the flat
  field value is set to unity.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics device for interactive graphics output.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Flat fields are created containing only the small scale variations in the
  calibration images.  The large scale variations in the images are modeled
  by fitting a function to each image line or column with deviant pixel rejection.
  The flat field values are obtained by taking the ratio of the image values
  to the function fit.  However, if the fitted value is less than the
  parameter <i>minflat</i> the flat field value is set to unity.
  </p>
  <p>
  The function fitting parameters may be set interactively when the interactive
  flag is set using the interactive curve fitting package <b>icfit</b>.
  The cursor mode commands for this package are described in a separate
  help entry under <span style="font-family: monospace;">"icfit"</span>.  For two dimensional images the user is
  prompted for the sample line or column or a blank-separated range to be
  averaged and graphed.
  Note that the lines or columns are relative the input image section; for
  example line 1 is the first line of the image section and not the first
  line of the image.  Any number of lines or columns may be examined.
  When satisfied with the fit parameters the user
  responds with a carriage return to the line or column prompt.
  The function is then fit to all the lines or columns and the flat field
  ratios are determined.
  </p>
  <p>
  If the output image does not exist initially it is created with the same
  size as the input image <i>without</i> an image section and initialized
  to unit response.  Subsequently the flat field data modifies the pixel
  values in the output image.  Input image sections may be used to restrict
  the region in which the flat field response is determined leaving the
  rest of the output image unmodified.  This ability is particularly useful
  when dealing with multi-aperture data.
  </p>
  <p>
  This task is very similar to <b>fit1d</b> with the addition of the
  parameter <i>minflat</i> and the deletion of the parameter <i>type</i>
  which is always <span style="font-family: monospace;">"ratio"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Create a flat field from the calibration image <span style="font-family: monospace;">"quartz"</span> with the
  spectrum running along the lines.  Exclude the first and last columns,
  use a spline fit of 25 pieces (a width of 32 pixels over 800 columns),
  and set grow to 4 pixels.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flat1d quartz flat order=25 sample="2:799" grow=4 \
  &gt;&gt;&gt; interactive=no
  </pre></div>
  <p>
  or
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flat1d quartz[2:799,*] flat order=25 grow=4 inter-
  </pre></div>
  <p>
  The fitting parameters may be set interactively in which case the fitting
  parameters need not be specified.  The command would be
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flat1d quartz flat
  quartz: Fit column = 1 10
  quartz: Fit column =
  </pre></div>
  <p>
  The user selects sample columns to be fit interactively with the interactive
  curve fitting package.  When satisfied with the fit parameters
  respond with a carriage return to the prompt.  The function is then fit to
  all the columns and the flat field ratios are determined.
  </p>
  <p>
  2.  As an example for multi-slit spectra the locations of the slits are
  determined and a file containing the image sections is created.
  Since there must be the same number of output images another file
  containing the output images is also created.  For
  example the files might contain
  </p>
  <div class="highlight-default-notranslate"><pre>
    File quartzs                  File flats
  _______________                 __________
  quartz[23:40,*]                    flat
  quartz[55:61,*]                    flat
  quartz[73:84,*]                    flat
  </pre></div>
  <p>
  A flat field for the slits is then obtained with the command
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flat1d @quartzs flats axis=2
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_FLAT1D">
  <dt><b>FLAT1D V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='FLAT1D' Line='FLAT1D V2.10.3' -->
  <dd>The image header keyword <span style="font-family: monospace;">"CCDMEAN = 1."</span> is now added or updated.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The creation of multi-slit files and the need for an equal number of
  repeated output files is annoying.  It will be worked on in the future.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fit1d, icfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'BUGS' 'SEE ALSO'  -->
  
