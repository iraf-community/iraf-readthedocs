.. _acetvmark:

acetvmark: display images with object filtered overlays
=======================================================

**Package: ace**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  acetvmark image frame
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Image with catalog(s) or object mask(s) to be overlayed.  The image
  may be a single image or multi-extension format (MEF) file.
  </dd>
  </dl>
  <dl id="l_frame">
  <dt><b>frame = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame' Line='frame = 1' -->
  <dd>Display frame to be used.
  </dd>
  </dl>
  <dl id="l_catalog">
  <dt><b>catalog = <span style="font-family: monospace;">"!catalog"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalog' Line='catalog = "!catalog"' -->
  <dd>Input catalog defining sources to be overlayed.  A keyword pointer or
  substitution patterns may be used in addtion to any other IRAF list format.
  The catalog need not have been produced by ACE and may be any format
  supported by the <b>tables</b> package.  However, if an object mask is to be
  overlayed the catalog must contain a field, specified by the
  <i>acefilter.catomid</i> parameter, with the object mask identification
  numbers.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields = <span style="font-family: monospace;">"ra,dec"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields = "ra,dec"' -->
  <dd>Fields defining the source coordinates and an optional third field for
  a label.  The label is used only for the <i>tvmark</i> overlays.
  The coordinates may be world coordinates (with right ascension in
  hours if using an RA axis type) or in physical or logical pixel
  coordinates.  The order of the coordinate elements must be pixel
  column and line or celestial longitude and latitude. 
  Note that for simple text files the fields names
  are <span style="font-family: monospace;">"c1"</span>, <span style="font-family: monospace;">"c2"</span>, etc.
  </dd>
  </dl>
  <dl id="l_catfilter">
  <dt><b>catfilter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catfilter' Line='catfilter = ""' -->
  <dd>Catalog filter expression.  If no expression is given then all input
  catalog records are selected.  An expression must evaluate to a boolean
  value.  Operands are case sensitive catalog field names.  Field names
  are those defined by the <b>tables</b> package.  In particular, simple
  text fields may be used as input catalogs and the field names are
  <span style="font-family: monospace;">"c1"</span>, <span style="font-family: monospace;">"c2"</span>, etc.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"world"</span> (logical|physical|world)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "world" (logical|physical|world)' -->
  <dd>Input coordinate type.  The input coordinates must be transformed to
  image pixel coordinates for the overlay.  If the coordinates are in
  image pixel coordinates the value <span style="font-family: monospace;">"logical"</span> is used.  The <span style="font-family: monospace;">"physical"</span>
  type is used for pixel coordinates where either the image has been
  transformed from the catalog image or the catalog was created in
  physical coordinates.  The <span style="font-family: monospace;">"world"</span> coordinate type is based on the
  world coordinate system (WCS) defined in the image.  This is typically
  right ascension and declination but other types maybe used as well.
  Note that right ascension coordinates must be in hours.
  </dd>
  </dl>
  <dl id="l_extnames">
  <dt><b>extnames = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extnames' Line='extnames = ""' -->
  <dd>List of extension name patterns for MEF files.  Note the patterns must
  match the entire name.
  </dd>
  </dl>
  <dl id="l_mark">
  <dt><b>mark = <span style="font-family: monospace;">"circle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mark' Line='mark = "circle"' -->
  <dd>The overlay mark type.  The type <span style="font-family: monospace;">"objmask"</span> invokes <b>acedisplay</b>
  and all other types invokes <b>tvmark</b>.  The options are:
  <dl>
  <dt><b>objmask</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='objmask' Line='objmask' -->
  <dd>Object mask isophote overlays.
  </dd>
  </dl>
  <dl>
  <dt><b>point</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='point' Line='point' -->
  <dd>A point.  To ensure legibility <i>point</i> is actually a square dot whose
  size is specified by <i>pointsize</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>plus</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='plus' Line='plus' -->
  <dd>A plus sign.  The shape of the plus sign is determined by the raster font
  and its size is specified by <i>txsize</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>cross</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cross' Line='cross' -->
  <dd>An x.  The shape of the x is determined by the raster font and its size is
  is specified by <i>txsize</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>circle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='circle' Line='circle' -->
  <dd>A set of concentric circles whose radii are specified by the <i>radii</i>
  parameter.  The radii are in image pixel units.  If the magnifications
  used by display are not equal in x and y circles will become ellipses
  when drawn.
  </dd>
  </dl>
  <dl>
  <dt><b>rectangle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rectangle' Line='rectangle' -->
  <dd>A set of concentric rectangles whose lengths and width/length ratio are
  specified by the <i>lengths</i> parameter.  The lengths are specified in
  image pixel units.  If the magnifications used by the display are not
  equal in x and y then squares will become rectangles when drawn.
  </dd>
  </dl>
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>No mark used to mark only labels.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_radii">
  <dt><b>radii = <span style="font-family: monospace;">"0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radii' Line='radii = "0"' -->
  <dd>If the default mark type is <span style="font-family: monospace;">"circle"</span> than concentric circles of radii
  <span style="font-family: monospace;">"r1,r2,...rN"</span> are drawn around each selected point.
  </dd>
  </dl>
  <dl id="l_lengths">
  <dt><b>lengths = <span style="font-family: monospace;">"0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lengths' Line='lengths = "0"' -->
  <dd>if the default mark type is <span style="font-family: monospace;">"rectangle"</span> then concentric rectangles of
  length and width / length ratio <span style="font-family: monospace;">"l1,l2,...lN ratio"</span> are drawn around
  each selected point.  If ratio is not supplied, it defaults to 1.0
  and squares are drawn.
  </dd>
  </dl>
  <dl id="l_font">
  <dt><b>font = <span style="font-family: monospace;">"raster"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='font' Line='font = "raster"' -->
  <dd>The name of the font.  At present only a simple raster font is supported.
  </dd>
  </dl>
  <dl id="l_color">
  <dt><b>color = 255</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='color' Line='color = 255' -->
  <dd>The numerical value or  color of the marks drawn.  Any number between 0 and
  255 may be specified.  The meaning of the color is device dependent.  In the
  current version of the IRAF display servers (XIMTOOL and DS9) numbers
  between 202 and 217 may be used to display graphics colors.  The current
  color assignments are summarized later in this help page.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='label' Line='label = no' -->
  <dd>Label the marked coordinates with the string in the third field.
  <i>label</i> overrides <i>number</i>.
  </dd>
  </dl>
  <dl id="l_number">
  <dt><b>number = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='number' Line='number = no' -->
  <dd>Label the marked objects with their sequence number in the coordinate
  list.
  </dd>
  </dl>
  <dl id="l_nxoffset">
  <dt><b>nxoffset = 0, nyoffset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxoffset' Line='nxoffset = 0, nyoffset = 0' -->
  <dd>The x and y offset in display pixels of the numbers to be drawn.
  Numbers are drawn by default with the lower left corner of the first
  digit at the coordinate list position.
  </dd>
  </dl>
  <dl id="l_pointsize">
  <dt><b>pointsize = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pointsize' Line='pointsize = 3' -->
  <dd>The size of the default mark type <span style="font-family: monospace;">"point"</span>. Point size will be rounded up
  to the nearest odd number.
  </dd>
  </dl>
  <dl id="l_txsize">
  <dt><b>txsize = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='txsize' Line='txsize = 1' -->
  <dd>The size of text, numbers and the plus and cross marks to be written.
  The size is in font units which are 6 display pixels wide and 7 display 
  pixels high.
  </dd>
  </dl>
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  This task overlays object mask isophotes or marks for objects in a
  catalog.  It makes use of <b>acedisplay</b> and <b>tvmark</b> for
  displaying overlays as well as <b>acefilter</b> for selecting objects.
  While the catalogs and object masks are often created by <b>ace</b> package
  tasks it is possible to use any file that the <b>tables</b> package
  supports which includes simple text files.
  The specified catalog is first filtered using the <i>catfilter</i>
  expression.  The expression may be a null string to select all records
  in the catalog.  If the <i>mark</i> parameter selects <span style="font-family: monospace;">"objmask"</span> the
  object mask associated with the catalog or image is filtered for
  overlaying.
  If the <i>mark</i> parameter is <span style="font-family: monospace;">"objmask"</span> then the image and (possibly
  filtered) object mask are display using <b>acedisplay</b>.   Most of
  that task's current hidden parameters are used.
  For any other mark type the image is first display with <b>acedisplay</b>
  without an object mask overlay.  Then <b>tvmark</b> is invoked to draw the
  desired marks.  In this case the (possibly filtered) catalog coordinates
  selected by the <i>fields</i> parameter are extracted (using <b>tdump</b>) and
  converted to pixel coordinates in the image as defined by the <i>wcs</i>.
  For more on the display options see the help for <b>acedisplay</b>
  and for the marking options see the help for <b>tvmark</b>.
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  acedisplay, acefilter, tvmark, tables
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
