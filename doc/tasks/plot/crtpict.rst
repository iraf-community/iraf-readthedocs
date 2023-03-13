.. _crtpict:

crtpict: Generate greyscale plots of IRAF images
================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  crtpict input 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input images to be processed.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"dicomed"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "dicomed"' -->
  <dd>The output device.
  </dd>
  </dl>
  <dl id="l_auto_fill">
  <dt><b>auto_fill = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='auto_fill' Line='auto_fill = yes' -->
  <dd>If set to yes, the image will be scaled to fit the device viewport.
  The aspect ratio is always preserved when <i>auto_fill</i> = yes.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = 1.0, ymag = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = 1.0, ymag = 1.0' -->
  <dd>When <i>auto_fill</i> = no, the x and y magnification ratios are specified
  by these parameters.
  </dd>
  </dl>
  <dl id="l_replicate">
  <dt><b>replicate = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='replicate' Line='replicate = yes' -->
  <dd>The image pixels are block replicated to fit the device viewport when
  <i>replicate</i> = yes.  Otherwise, the pixels are linearly interpolated
  to match the device pixels.
  </dd>
  </dl>
  <dl id="l_x_block_avg">
  <dt><b>x_block_avg = 1, y_block_avg = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x_block_avg' Line='x_block_avg = 1, y_block_avg = 1' -->
  <dd>These parameters are used when <i>replicate</i> = no to decrease the
  effective output device resolution, and speed up the interpolation.  The
  pixels are interpolated to the block averaged output device, then
  block replicated to fill the device viewport.
  </dd>
  </dl>
  <dl id="l_ztrans">
  <dt><b>ztrans = <span style="font-family: monospace;">"auto"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ztrans' Line='ztrans = "auto"' -->
  <dd>This parameter specifies how the image intensities are mapped into the 
  greyscale values of the output device.  Intensity z1 maps to black, z2 to white.
  The 4 choices for <i>ztrans</i> are:
  <div class="highlight-default-notranslate"><pre>
  "auto"          - z1 and z2 centered on median of image
  "min_max"       - set z1 and z2 to specified intensities
  "none"          - truncate intensities to fit output range
  "user"          - user supplies look up table of values
  </pre></div>
  </dd>
  </dl>
  <dl id="l_lutfile">
  <dt><b>lutfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lutfile' Line='lutfile = ""' -->
  <dd>Name of text file containing the look up table when <i>ztrans</i> = user. 
  The table should contain two columns per line; column 1 contains the 
  intensity, column 2 the desired greyscale output.  
  </dd>
  </dl>
  <dl id="l_contrast">
  <dt><b>contrast = 0.25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='contrast' Line='contrast = 0.25' -->
  <dd>Used when automatically determining z1 and z2.  The slope of the transfer
  function is divided by <i>contrast</i>, so negative values of <i>contrast</i>
  result in a negative transfer function.
  </dd>
  </dl>
  <dl id="l_nsample_lines">
  <dt><b>nsample_lines = 25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsample_lines' Line='nsample_lines = 25' -->
  <dd>Used when automatically determining z1 and z2, this parameter sets the number 
  of image lines to be sampled when determining the median.
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = 0.0, z2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z1' Line='z1 = 0.0, z2 = 0.0' -->
  <dd>These parameters are used when <i>ztrans</i> = <span style="font-family: monospace;">"min_max"</span>, to specify which
  pixel values map to black and white.  
  </dd>
  </dl>
  <dl id="l_perimeter">
  <dt><b>perimeter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='perimeter' Line='perimeter = yes' -->
  <dd>Draw annotated axes around the plot perimeter?
  </dd>
  </dl>
  <dl id="l_image_fraction">
  <dt><b>image_fraction = 0.70</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image_fraction' Line='image_fraction = 0.70' -->
  <dd>The fraction of the vertical device viewport reserved for the image.
  </dd>
  </dl>
  <dl id="l_graphics_fraction">
  <dt><b>graphics_fraction = 0.20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics_fraction' Line='graphics_fraction = 0.20' -->
  <dd>The fraction of the vertical device viewport reserved for histogram
  plots and id information. 
  </dd>
  </dl>
  <dl id="l_greyscale_fraction">
  <dt><b>greyscale_fraction = 0.05</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='greyscale_fraction' Line='greyscale_fraction = 0.05' -->
  <dd>The fraction of the vertical device viewport reserved for the greyscale
  step wedge.  
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Output metacode is appended to this file.
  By naming an output file, the metacode can be <span style="font-family: monospace;">"trapped"</span>, and the normal
  spooling process intercepted.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Procedure <b>crtpict</b> makes a photographic hardcopy plot of IRAF images.
  </p>
  <p>
  The image can be automatically scaled to fill the output plotting window, with 
  the aspect ratio preserved, by setting <b>auto_fill</b> = yes.  When 
  <b>auto_fill</b> = no, magnification factors for the axes are entered as 
  <b>xmag</b> and <b>ymag</b>, where negative values (as well as fractional 
  values &lt; 1.0), indicate that the image is to be reduced.  By default, the
  imaged is enlarged by block replication.  By setting <b>replicate</b> = no,
  the image will be linearly interpolated to fit the device area.  (In this
  case, to speed things up, the <b>block_avg</b> parameters can be set to
  reduce the effective output resolution.)  In either case, if an image needs
  to be reduced in size, it will be decimated.   
  </p>
  <p>
  Four methods of determining the greyscale transformation are available.
  When <i>ztrans</i> = <span style="font-family: monospace;">"none"</span>, no transformation between intensity and 
  greyscale level occurs, the intensities are simply copied, which will most
  likely result in truncation.  With this method, the lowest bits of each pixel, 
  the lowest level variations, are always shown, regardless of the dynamic 
  range of the image.
  </p>
  <p>
  When <i>ztrans</i> = <span style="font-family: monospace;">"auto"</span>,
  the greyscale levels are automatically centered on the median of the image 
  pixels.  The window of intensities spanned by the greyscale is controlled 
  by parameter <i>contrast</i>, which is divided into the calculated slope of 
  the transfer function. The larger the absolute value of <i>contrast</i>, the 
  higher the contrast in the output image.  A subset of the image pixels are 
  used to determine the median; the number of lines sampled is 
  <i>nsample_lines</i>.
  </p>
  <p>
  When <b>ztrans</b> = <span style="font-family: monospace;">"min_max"</span>, intensity <b>z1</b> maps to the minimum
  greyscale level (black), <b>z2</b> maps to the maximum greyscale level
  (white) and the transfer function is linear in between these two endpoints.
  If <i>z1</i> = <i>z2</i>, the image min and max map to black and white, modified
  by <b>contrast</b>.  (NOTE:  When running <i>crtpict</i> on an image created with 
  <i>snap</i>, <b>ztrans</b> should be set to <span style="font-family: monospace;">"min_max"</span>, with <b>z1</b> = 0 and
  <b>z2</b> = 1023, the maximum output value possible from the IIS.)
  </p>
  <p>
  When <b>ztrans</b> = <span style="font-family: monospace;">"user"</span>, a look up table of intensity values and their
  corresponding greyscale levels is read from the file specified by the
  <b>lutfile</b> parameter.  From this information, 
  <i>crtpict</i> constructs a piecewise linear look up table containing
  4096 discrete values.  
  The text format table contains two columns per line; 
  column 1 contains the intensity, column 2 the desired greyscale output.  
  The greyscale values specified by the user must match those available on
  the output device.  Task <b>showcap</b> can be used to determine the range
  of acceptable greyscale levels.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To subsample every 4th pixel of a large image, fill the output area and use
  previously determined values of z1 and z2 for the greyscale transformation
  the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crtpict sunpic[*:4,*:4] ztrans=min z1=0 z2=800
  </pre></div>
  <p>
  2.  To process every image with the root name ccdpic, using default values of
  all parameters, the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crtpict ccdpic*
  </pre></div>
  <p>
  3.  To process images created with <b>snap</b>, ztrans and z2 must be changed
  from their default values:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crtpict iis.snap ztrans=min z2=1023
  </pre></div>
  <p>
  4.  Image `mypic' is processed using the look up table in file `mylut',
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crtpict mypic ztrans=user lutfile=mylut
  </pre></div>
  <p>
  Where file `mylut' contains this information:
  </p>
  <div class="highlight-default-notranslate"><pre>
  10      40
  1500    100
  2500    100
  3500    200
  7500    255
  </pre></div>
  </section>
  <section id="s_timing">
  <h3>Timing</h3>
  <p>
  For a 512 x 512 real image, <b>crtpict</b> takes about 40 cpu seconds with
  <b>auto_fill</b> and <b>replicate</b> = yes.  When <b>auto_fill</b> = yes
  but <b>replicate</b> = no, <b>crtpict</b> requires almost 400 cpu seconds.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  display, showcap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMING' 'SEE ALSO'  -->
  
