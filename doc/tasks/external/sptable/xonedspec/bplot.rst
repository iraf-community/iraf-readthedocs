.. _bplot:

bplot: Batch plots of spectra
=============================

**Package: xonedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bplot images [records]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images to be plotted.  These may be one dimensional, multiaperture,
  long slit, or nonspectral images.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records (imred.irs and imred.iids only)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records (imred.irs and imred.iids only)' -->
  <dd>List of records records to be appended to the input image root names when
  using record number extension format.  The syntax of this list is comma
  separated record numbers or ranges of record numbers.  A range consists of
  two numbers separated by a hyphen.  A null list may be used if no record
  number extensions are desired.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures/lines/columns to be plotted in each image.  If
  <i>apertures</i> is null all of the apertures/lines/columns will be plotted.
  </dd>
  </dl>
  <dl id="l_band">
  <dt><b>band = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='band' Line='band = 1' -->
  <dd>The band or plane of a three dimensional image to be plotted in each image.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Output graphics device.  This may be one of <span style="font-family: monospace;">"stdgraph"</span>, <span style="font-family: monospace;">"stdplot"</span>,
  <span style="font-family: monospace;">"stdvdm"</span>, or the actual device name.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">"onedspec$gcurval.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = "onedspec$gcurval.dat"' -->
  <dd>File(s) containing cursor commands for the SPLOT task.
  The files will be cycled sequentially.  If there is more than one file
  usually the number of files will agree with the number of apertures
  for each image since otherwise different cursor/aperture pairings will
  occur.  The default is a file containing only the (q)uit command.
  </dd>
  </dl>
  <p>
  The following parameters are used in response to particular keystrokes.
  In <b>splot</b> they are query parameters but in <b>bplot</b> they are hidden
  parameters.
  </p>
  <dl id="l_next_image">
  <dt><b>next_image = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='next_image' Line='next_image = ""' -->
  <dd>In response to <span style="font-family: monospace;">'g'</span> (get next image) this parameter specifies the image.
  </dd>
  </dl>
  <dl id="l_new_image">
  <dt><b>new_image = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_image' Line='new_image = ""' -->
  <dd>In response to <span style="font-family: monospace;">'i'</span> (write current spectrum) this parameter specifies the
  name of a new image to create or existing image to overwrite.
  </dd>
  </dl>
  <dl id="l_overwrite">
  <dt><b>overwrite = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='overwrite' Line='overwrite = yes' -->
  <dd>Overwrite an existing output image?  If set to yes it is possible to write
  back into the input spectrum or to some other existing image.  Otherwise
  the user is queried again for a new image name.
  </dd>
  </dl>
  <dl id="l_spec2">
  <dt><b>spec2 = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spec2' Line='spec2 = ""' -->
  <dd>When adding, subtracting, multiplying, or dividing by a second spectrum
  (<span style="font-family: monospace;">'+'</span>, <span style="font-family: monospace;">'-'</span>, <span style="font-family: monospace;">'*'</span>, <span style="font-family: monospace;">'/'</span> keys in the <span style="font-family: monospace;">'f'</span> mode) this parameter is used to get
  the name of the second spectrum.
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.' -->
  <dd>When adding or multiplying by a constant (<span style="font-family: monospace;">'p'</span> or <span style="font-family: monospace;">'m'</span> keys in the <span style="font-family: monospace;">'f'</span> mode)
  the parameter is used to get the constant.
  </dd>
  </dl>
  <dl id="l_wavelength">
  <dt><b>wavelength = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavelength' Line='wavelength = 0.' -->
  <dd>This parameter is used to get a dispersion coordinate value during deblending or
  when changing the dispersion coordinates with <span style="font-family: monospace;">'u'</span>.
  </dd>
  </dl>
  <dl id="l_linelist">
  <dt><b>linelist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linelist' Line='linelist = ""' -->
  <dd>During deblending this parameter is used to get a list of line positions
  and widths.
  </dd>
  </dl>
  <dl id="l_wstart">
  <dt><b>wstart = 0., wend = 0., dw = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wstart' Line='wstart = 0., wend = 0., dw = 0.' -->
  <dd>In response to <span style="font-family: monospace;">'p'</span> (convert to a linear wavelength scale) these parameter
  specify the starting wavelength, ending wavelength, and wavelength per pixel.
  </dd>
  </dl>
  <dl id="l_boxsize">
  <dt><b>boxsize = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boxsize' Line='boxsize = 2' -->
  <dd>In response to <span style="font-family: monospace;">'s'</span> (smooth) this parameter specifies the box size in pixels
  to be used for the boxcar smooth
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The spectra in the input image list are successively processed by the task
  <b>splot</b> with input supplied by the cursor parameter and the output sent
  to the specified graphics device.  The range of apertures and bands
  specified by <i>apertures</i> and <i>bands</i> will be processed for each
  image.  In the <b>iids/irs</b> packages the record extension syntax is used
  with input root names and a record number list.  The hidden parameters from
  <b>splot</b> apply to this task.
  </p>
  <p>
  The cursor file(s) consists of line(s) of the form:
  </p>
  <p>
  	[x y 1] key [command]
  </p>
  <p>
  where x and y are the position of the cursor (may be zero or absent if the
  cursor position is irrelevant) and key is one of the keystrokes understood
  by <b>splot</b>.  If the key is <span style="font-family: monospace;">":"</span> then the <i>colon</i> command string follows.
  The default cursor file consists of the single line:
  </p>
  <p>
  	0 0 1 q
  </p>
  <p>
  If more than one cursor file is specified they are sequentially assigned to
  each aperture and the list is repeated as needed.  This allows the aperture
  to be manipulated in differing ways.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To plot all of apertures of the multiaperture spectra indicated by the file
  <span style="font-family: monospace;">"nite1.lst"</span> on the default plotter and run in the background:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bplot @nite1.lst graphics=stdplot &amp;
  </pre></div>
  <p>
  2. To preview the plots:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bplot @nite1.lst graphics=stdgraph
  </pre></div>
  <p>
  3.  To produce a histogram type plot about Balmer alpha for aperture 5 of
  each spectrum with the IRAF banner suppressed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type curfile
  6555 0 1 a
  6570 0 1 a
  q
  cl&gt; splot.options="auto hist nosysid"
  cl&gt; splot.xmin=6555
  cl&gt; splot.xmax=6570
  cl&gt; bplot @nite1.lst apertures=5 cursor=curfile
  </pre></div>
  <p>
  4. To produce plots with four spectra per page:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bplot @nite1.lst ... &gt;G nite1.mc
  cl&gt; gkimosiac nite1.mc dev=stdplot
  </pre></div>
  <p>
  The first command redirects the output of the graphics to the metacode
  file nite1.mc.  The task <b>gkimosiac</b> is used to make multiple plots
  per page.  Other tasks in the <b>plot</b> package may be used to
  manipulate and redisplay the contents of the metacode file.
  </p>
  <p>
  5. To plot a list of apertures with a different cursor file for each aperture:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bplot @nite1.lst apertures=3,9,14 cursor=@nite1.cur
  </pre></div>
  <p>
  In this case the file <span style="font-family: monospace;">"nite1.cur"</span> is assumed to be a list of
  individual cursor file names, for instance:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cur.03
  cur.09
  cur.14
  </pre></div>
  <p>
  that are in one to one correspondence with the range of apertures.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_BPLOT">
  <dt><b>BPLOT V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='BPLOT' Line='BPLOT V2.10.3' -->
  <dd>The query parameters from SPLOT were added as hidden parameters in BPLOT
  to allow use of those keys in a batch way.
  </dd>
  </dl>
  <dl id="l_BPLOT">
  <dt><b>BPLOT V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='BPLOT' Line='BPLOT V2.10' -->
  <dd>The <i>apertures</i> and <i>band</i> parameters been added to select
  apertures from multiple spectra and long slit images, and bands from 3D
  images.  Since the task is a script calling <b>splot</b>, the many revisions
  to that task also apply.  The version in the <b>irs/iids</b> packages
  selects spectra using the record number extension syntax.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The cursor file command keystrokes cannot include any of the cursor
  mode (CAPITALIZED) keys.  This results from the implementation of
  the cursor mode commands as external to both BPLOT and SPLOT.
  </p>
  <p>
  When first entered, SPLOT will always display an initial plot.  BPLOT
  calls SPLOT once for each aperture in each image and thus produces
  N(apertures)*N(images) initial plots.  The plots are not optional because
  of the possible confusion a blank screen might cause an inexperienced
  user.  If the initial plots are unwanted they must be edited out of the
  graphics stream.  This can be done as follows, by directing the
  graphics output of BPLOT to a metacode file and then using GKIEXTRACT
  to remove only the desired plots from the metacode file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bplot @nite1.lst cursor=curfile &gt;G nite1.mc
  cl&gt; gkiextract nite1.mc 2x2 | gkimosaic dev=stdplot
  </pre></div>
  <p>
  This assumes that curfile is designed to produce only one plot in
  addition to the non-optional initial plot.  In this case there will be
  two plots per aperture per image and we extract every other plot starting
  with the second (as encoded in the range string:  <span style="font-family: monospace;">"2x2"</span>).
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  splot, specplot, slist, gkiextract, gkimosaic, implot, graph, ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'BUGS' 'SEE ALSO'  -->
  
