.. _imfill:

imfill: Set fill value in image according to a mask.
====================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imfill image mask expr value
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task takes as input an image and mask of the same size. It
  evaluates an expression using the mask pixels and sets the
  corresponding image pixel to the fill value whenever the expression is
  true. The variable name in the expression which represents the mask may
  be any alphanumeric string, but the expression may contain only one
  name. For example, the expressions
  </p>
  <div class="highlight-default-notranslate"><pre>
  x .ge. 100 .and. x .lt. 200
  
  and
  
  mask .ge. 100 .and. mask .lt. 200
  
  are both legal and have the same meaning. However, the expression
  
  x .ge. 100 .and. y .lt. 200
  </pre></div>
  <p>
  is illegal and will cause an error. The following logical operators
  are supported. Logical operators are supported in both their Fortran
  and SPP form.
  </p>
  <div class="highlight-default-notranslate"><pre>
  </dd>
  </dl>
  </pre></div>
  All the operators and standard functions of ANSI Fortran are also
  supported. For a list of these operators and functions, see the help
  file for the 'imcalc' task. Usually the expression to be evaluated will be some
  combination of logical operators. However, an arithmetic expression is
  also acceptable and will be interpreted so that zero is false and any
  non-zero value is true.
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='image' Line='image [file name]' -->
  <dd><p>
  The image name. The image is modified in place. If the image name does
  not contain a group specifier, all groups in the image will be
  modified. If the image contains a group specifier, only the specified
  group will be modified.
  </dd>
  </dl>
  </p>
  <dl id="l_mask">
  <dt><b>mask [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='mask' Line='mask [file name]' -->
  <dd><p>
  The mask file name. This task supports both full images used as masks
  and two compressed formats: iraf pixel list (.pl) format and STSDAS
  table format. For a description of how masks are stored in an STSDAS
  table, see the help file for the 'copymask' task.
  </dd>
  </dl>
  </p>
  <dl id="l_expr">
  <dt><b>expr [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='expr' Line='expr [string]' -->
  <dd><p>
  The expression to evaluate. If the expression is too long to pass as a
  parameter, place the expression in a file and set the value of this
  parameter to the file name preceded by an <span style="font-family: monospace;">"@"</span> character.
  </dd>
  </dl>
  </p>
  <dl id="l_value">
  <dt><b>value [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='value' Line='value [real]' -->
  <dd><p>
  The fill value. The fill value will be set in the image whenever the
  expression is true.
  </dd>
  </dl>
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  1. Set the image to zero when the mask is non-zero. All groups in the
  image will be changed.
  <div class="highlight-default-notranslate"><pre>
  im&gt; imfill w0001.d0h w0001.q0h "x .ne. 0" 0.
  </pre></div>
  2. Set the image to zero when the mask is non-zero. Only change the 
  first group.
  <div class="highlight-default-notranslate"><pre>
  im&gt; imfill w0001.d0h[1] w0001.q0h[1] "x .ne. 0" 0.
  </pre></div>
  3. Set the image to zero on the basis of an expression stored in a 
  file.
  <div class="highlight-default-notranslate"><pre>
  im&gt; imfill w0001.d0h w0001.q0h @imfill.dat 0.
  </pre></div>
  The file 'imfill.dat' contains the following line:
  <div class="highlight-default-notranslate"><pre>
  (x .ge. 100 .and. x .lt. 200) .or. x .eq. 300
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  copymask, imcalc
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'SEE ALSO'  -->
  
