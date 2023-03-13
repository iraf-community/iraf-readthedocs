.. _mskregions:

mskregions: Create or modify masks using regions lists
======================================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mskregions regions masks refimages
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_regions">
  <dt><b>regions</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='regions' Line='regions' -->
  <dd>The list of input regions files. The number of regions files must be one or
  equal to the number of output mask images. Regions files contain a list of
  region specifications one region per line. The region specifications may be
  a simple region description, e.g. <span style="font-family: monospace;">"circle 100. 100. 50."</span>, or a region
  expression, e.g.  <span style="font-family: monospace;">"circle (100., 100., 50.) &amp;&amp; circle (125., 100., 50.)"</span>.
  </dd>
  </dl>
  <dl id="l_masks">
  <dt><b>masks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masks' Line='masks' -->
  <dd>The output masks. The size of the output masks defaults to the size of
  the reference image or the value of the dims parameter in that order of
  precedence.
  </dd>
  </dl>
  <dl id="l_refimages">
  <dt><b>refimages</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refimages' Line='refimages' -->
  <dd>The optional list of reference images. If the reference image list is defined
  there must be one reference image for every output mask.
  </dd>
  </dl>
  <dl id="l_dims">
  <dt><b>dims = <span style="font-family: monospace;">"512,512"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dims' Line='dims = "512,512"' -->
  <dd>The default output mask dimensions. The value of dims is a comma delimited
  list of dimensions.
  </dd>
  </dl>
  <dl id="l_depth">
  <dt><b>depth = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='depth' Line='depth = 0' -->
  <dd>The default output mask depth in bits currently 27.
  </dd>
  </dl>
  <dl id="l_regnumber">
  <dt><b>regnumber = <span style="font-family: monospace;">"constant"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='regnumber' Line='regnumber = "constant"' -->
  <dd>The region definition scheme. The options are:
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Assign all the mask regions the value of <i>regval</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>number</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='number' Line='number' -->
  <dd>Assign each region a sequential value beginning with <i>regval</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_regval">
  <dt><b>regval = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='regval' Line='regval = 1' -->
  <dd>The starting mask region value.
  </dd>
  </dl>
  <dl id="l_exprdb">
  <dt><b>exprdb = <span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exprdb' Line='exprdb = "none"' -->
  <dd>The file name of an optional expression database. An expression database
  may be used to define symbolic constants or a library of custom function
  macros.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Add the region list to an existing mask ?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print task status messages ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Mskregions reads a list of region specifications from the input files
  <i>regions</i> and writes the results to the output masks <i>masks</i> image.
  The number of regions files must be on or equal to the number of output
  masks. The size of the output mask is determined by the reference image
  <i>refimages</i> if any <i>refmasks</i> if any or the values in the
  <i>dims</i> parameter in that order of precedence.
  </p>
  <p>
  The output mask is an integer image. Therefore all mask values must be
  integer. The mask values assigned to the regions in <i>regions</i> are
  determined  by the <i>regnumber</i> and <i>regval</i> parameters. By
  default all new regions are assigned the value of 1. The depth of the output
  mask in bits is defined by the <i>depth</i> parameter. The default value is
  27 bits.
  </p>
  <p>
  The input region specifications may be region descriptions or region
  expressions. Region descriptions are simple definitions of common geometric
  shapes. Evaluation of the regions expressions is carried out one line at a time.
  </p>
  <p>
  <b>Regions Definitions</b>
  </p>
  <p>
  The following region definitions are supported.
  </p>
  <div class="highlight-default-notranslate"><pre>
      point x1 y1
     circle xc yc r
    ellipse xc yc r ratio theta
        box x1 y1 x2 y2)
  rectangle xc yc r ratio theta
     vector x1 y1 x2 y2 width
        pie xc yc theta1 theta2
    polygon x1 y1 ..., xn yn
       cols ranges
      lines ranges
   cannulus xc yc r1 r2
   eannulus xc yc r1 r2 ratio theta
   rannulus xc yc r1 r2 ratio theta
   pannulus width x1 y1 ... xn yn
  </pre></div>
  <p>
  <b>Operands Used in Region Expressions</b>
  </p>
  <p>
  Input operands are represented symbolically in the input expression. Use of
  symbolic operands allows the same expression to be used with different data
  sets, simplifies the expression syntax, and allows a single input image
  to be used several places in the same expression.
  </p>
  <p>
  There is a special builtin type of operand used to represent the
  mask pixel coordinates in a mask expression.  These operands have the
  special reserved names <span style="font-family: monospace;">"I"</span>, <span style="font-family: monospace;">"J"</span>, <span style="font-family: monospace;">"K"</span>, etc., up to the dimensions of the
  output image.  The names must be upper case to avoid confusion to with the
  input operands <span style="font-family: monospace;">"i"</span> and <span style="font-family: monospace;">"m"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  I                x coordinate of pixel (column)
  J                y coordinate of pixel (line)
  K                z coordinate of pixel (band)
  </pre></div>
  <p>
  <b>Operators Used in Region Expressions</b>
  </p>
  <p>
  The expression syntax implemented by mskexpr provides the following
  set of operators:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ( expr )                grouping
  &amp;&amp;                      logical and
  ||                      logical or
  !                       logical not
  </pre></div>
  <p>
  <b>Functions Used in Region Expressions</b>
  </p>
  <p>
  Mskexpr supports a group of boolean region functions which can be used to set
  values inside or outside of certain geometric shapes. The routines may be
  called in two ways. The first way assumes that the output masks are two-
  dimensional. The second way assumes that they are multi-dimensional and
  specifies which dimensions the geometric operator applies to.
  </p>
  <div class="highlight-default-notranslate"><pre>
      point (x1, x2)
     circle (xc, yc, r)
    ellipse (xc, yc, r, ratio, theta)
        box (x1, y1, x2, y2)
  rectangle (xc, yc, r, ratio, theta)
     vector (x1, y1, x2, y2, width)
        pie (xc, yc, theta1, theta2)
    polygon (x1, y1, ..., xn, yn)
       cols (ranges)
      lines (ranges)
   cannulus (xc, yc, r1, r2)
   eannulus (xc, yc, r1, r2, ratio, theta)
   rannulus (xc, yc, r1, r2, ratio, theta)
   pannulus (width, x1, y1, ..., xn, yn)
  
      point (I, J, x1, x2)
     circle (I, J, xc, yc, r)
    ellipse (I, J, xc, yc, r, ratio, theta)
        box (I, J, x1, y1, x2, y2)
  rectangle (I, J, xc, yc, r, ratio, theta)
     vector (I, J, x1, y1, x2, y2, width)
        pie (I, J, xc, yc, theta1, theta2)
    polygon (I, J, x1, y1, .., xn, yn)
       cols (I, ranges)
      lines (J, ranges)
   cannulus (I, J, xc, yc, r1, r2)
   eannulus (I, J, xc, yc, r1, r2, ratio, theta)
   rannulus (I, J, xc, yc, r1, r2, ratio, theta)
   pannulus (I, J, width, x1, y1, ..., xn, yn)
  
      xc,yc - center coordinates in pixels
      r1,r2 - semi-major axis lengths in pixels
      ratio - ratio of semi-minor / semi-major axes
   theta[n] - position angle in degrees
      x1,y1 - starting coordinates in pixels
      x2,y2 - ending coordinates in pixels
  x[n],y[n] - vertices of a polygon
     ranges - string defining a range, e.g. "100-200,300,400-500"
  </pre></div>
  <p>
  <b>The Expression Database</b>
  </p>
  <p>
  The <i>mskexpr</i> expression database provides a macro facility which can be
  used to create custom libraries of functions for specific applications. A
  simple example follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Sample MSKEXPR expression database file.
  
  # Constants.
  SQRTOF2=        1.4142135623730950488
  PI=             3.1415926535897932385
  
  # Simple bad data functions.
  bdata1          (i &lt; -100 || i &gt; 25000)
  bdata2          (i &lt; -100 || i &gt; 32000)
  
  # New regions functions.
  cmpie(xc,yc,r,t1,t2)    circle (xc, yc, r) &amp;&amp; (! pie (xc, yc, t1, t2))
  </pre></div>
  <p>
  The complete syntax of a macro entry is as follows:
  </p>
  <p>
          &lt;symbol&gt;[<span style="font-family: monospace;">'('</span> arg-list <span style="font-family: monospace;">')'</span>][<span style="font-family: monospace;">':'</span>|<span style="font-family: monospace;">'='</span>]     replacement-text
  </p>
  <p>
  The replacement text may appear on the same line as the macro name or may
  start on the next line, and may extend over multiple input lines if necessary.
  If so, continuation lines must be indented.  The first line with no whitespace
  at the beginning of the line terminates the macro. Macro functions may be
  nested.  Macro functions are indistinguishable from intrinsic functions in
  expressions.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a 0-valued 512 x 512 mask and set all the pixels inside a circular
  annulus to 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type regions.dat
  cannulus 256. 256. 20. 40.
  cl&gt; mskregions regions.dat mask.pl ""
  </pre></div>
  <p>
  2. Repeat the previous example but set all the pixels outside the circular
  annulus to 1. Note that in this case the user must use regions expression
  syntax not region definition syntax
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type region.dat
  ! cannulus (256., 256., 20., 40.)
  cl&gt; mskregions regions.dat mask.pl ""
  </pre></div>
  <p>
  3. Create a 0-valued 512 x 512 mask and set all the pixels inside the
  intersection of 2 circles to 1. The &amp; operator produces the same result
  as &amp;&amp;.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type regions.dat
  circle (220., 220., 50.) &amp;&amp; circle (240., 220., 50.)
  cl&gt; mskexpr regions.dat mask.pl ""
  </pre></div>
  <p>
  4. Create a 0 valued 512 x 512 mask and set all the pixels inside a circle
  excluding a wedge shaped region to 1. The expression cmpie is used defined
  and stored in the expression database <span style="font-family: monospace;">"myexpr.db"</span> 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type myexpr.db
  # Sample MSKEXPR expression database file.
  
  # Constants.
  SQRTOF2=        1.4142135623730950488
  PI=             3.1415926535897932385
  
  # Simple bad data functions.
  bdata1          (i &lt; -100 || i &gt; 25000)
  bdata2          (i &lt; -100 || i &gt; 32000)
  
  # New regions functions.
  cmpie(xc,yc,r,t1,t2)    circle (xc, yc, r) &amp;&amp; (! pie (xc, yc, t1, t2))
  
  cl&gt; type regions.dat
  cmpie (256., 256., 50., 0., 30.) ? 1 : 0
  
  cl&gt; mskregions regions.dat mask.pl "" exprdb=myexpr.db
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imexpr, mskexpr
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
