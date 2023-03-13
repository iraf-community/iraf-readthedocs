.. _hselect:

hselect: Select a subset of images satisfying a boolean expression
==================================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hselect images fields expr
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Images forming the set from which selected images are to be drawn.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields' -->
  <dd>Comma separated list of keywords or keyword patterns to be extracted
  from each selected image.  The list elements are matched against the
  set of keywords in the header except for those beginning with <span style="font-family: monospace;">"$"</span> which
  are special values or explicit checks for keywords that might be missing.
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr' -->
  <dd>The boolean expression to be used as the selection criteria.  The expression
  is evaluated independently for each image.
  </dd>
  </dl>
  <dl id="l_missing">
  <dt><b>missing = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='missing' Line='missing = "INDEF"' -->
  <dd>Output value for missing keywords.  Note that this will only occur when the
  fields are specified with leading <span style="font-family: monospace;">"$"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The function of <i>hselect</i> is to extract keyword values from a subset
  of images satisfying a boolean selection expression.  The resultant table
  of keyword values is output in list form, suitable for further analysis
  or for use to generate a list of images to be processed by another task.
  </p>
  <p>
  The form of the boolean expression <i>expr</i> is fully documented in the
  manual page for the <i>hedit</i> task.  In the case of <i>hselect</i> task,
  however, the expression need not be parenthesized to be evaluated as an
  expression.
  </p>
  <p>
  The keywords whose values are to be output are specified by the <i>fields</i>
  parameter.  This is a comma delimited list of keywords and patterns.  The
  keywords and patterns are matched against the set of keywords in the image.
  Of particular importance is that explicit keywords, that is without any
  wildcard, are matched against the header and so if the keyword is not in the
  header then the keyword value is not output.  If one wants to explicitly
  output a place holder for a missing keyword use a leading $; e.g. $mykey.
  If the keyword is absent then the value given by the <i>missing</i>
  parameter will be output.  This is useful when scanning the output.
  </p>
  <p>
  In addition to escaping the keyword matching, the leading $ character is
  also used to select special values such as <span style="font-family: monospace;">"$I"</span> for the name of the current
  image.  See <b>hedit</b> for more on the special values and pattern syntax.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the mean exposure time for all the images in a database.  Note that
  the argument <span style="font-family: monospace;">"yes"</span> is a trivial case of a general boolean expression and
  hence need not be quoted.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect n1.* exp yes | average
  </pre></div>
  <p>
  2. Print the name, length of axes 1 and 2, and title of all two dimensional
  images in a database.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect n1.* $I,naxis[12],title 'naxis == 2'
  n1.0001 512     512     quartz
  n1.0002 512     512     "dome flat"
  n1.0005 384     800     "ngc 3127 at 45 degrees"
  cl&gt;
  </pre></div>
  <p>
  3. Produce an image name list for use to drive another task.  The selection
  criterion is all images for which the value of the parameter <span style="font-family: monospace;">"q-flag"</span>
  has the value 1.  Note carefully the use of quotes.  If the @ operator
  is unfamiliar read the manual page for <i>hedit</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect n1.* $I '@"q-flag" == 1' &gt; imlist
  </pre></div>
  <p>
  If the parameter <span style="font-family: monospace;">"q-flag"</span> were instead named <span style="font-family: monospace;">"qflag"</span>, the following
  simpler expression would suffice.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect n1.* $I 'qflag == 1' &gt; imlist
  </pre></div>
  <p>
  4.  Scan a set of keyword and allow for missing keywords.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect pix $I,$exptime,$airmass yes missing=INDEF |
  &gt;&gt;&gt; scan (s1, x, y)
  </pre></div>
  <p>
  Note that when checking for missing values the missing value must be
  of the appropriate type or else you need to use string variables or
  nscan to check.  The default missing value is <span style="font-family: monospace;">"INDEF"</span> which can be
  scanned into both string and numerical variables.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Since individual image headers are currently stored as separate files,
  selection from a large database is quite slow.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  hedit, imgets, imheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
