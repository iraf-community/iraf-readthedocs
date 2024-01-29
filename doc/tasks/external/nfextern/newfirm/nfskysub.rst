.. _nfskysub:

nfskysub: Subtract sky
======================

**Package: newfirm**

.. raw:: html

  <section id="s_usage___">
  <h3>Usage   </h3>
  <p>
  nfskysub input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to process.  The files may be multi-extension
  FITS files (MEF) or single images.  The order in which the input images
  and MEF extensions are processed is controlled by the program.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"+_ss"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "+_ss"' -->
  <dd>List of output images, a pattern based on the input filenames, or an
  expression.  An expression begins with <span style="font-family: monospace;">'('</span> and evaluates to a filename.
  If it is not an expression then <span style="font-family: monospace;">'+'</span> characters in the string identify a
  pattern where those characters are substituted with the input filename
  excluding any path and extension.  If the value is neither an expression
  or pattern then it is a list which must match the input list.
  Note that a list can be an image template which also includes a replacement
  syntax (see example 2 of
  <a href="imrename"><b>imrename</b></A>
  ).  The output format will be the
  same as the input format such that input MEF files will produce output
  MEF files.  If the input has non-image extensions they will be ignored
  and excluded from the output.  The special value <span style="font-family: monospace;">"+LIST+"</span> will produce
  log output without processing the input.
  </dd>
  </dl>
  <dl id="l_skies">
  <dt><b>skies = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skies' Line='skies = ""' -->
  <dd>List of sky images or an expression evaluating to an image.  If a null
  list is specified the input list is searched for files that satisfy
  the
  <a href="#l_stype"><i>stype</i></A>
  selection expression or, if no <i>stype</i> value is
  specified, the entire input list is used
  as potential sky images.  The list may include MEF files which expand
  to all image extensions.  The use of the sky images is defined by the
  <a href="#l_skymode"><i>skymode</i></A>
  parameter.  The 
  <a href="#l_skymatch"><i>skymatch</i></A>
  parameter may also apply
  when matching a single sky to an input.  In all cases only images with
  the same 
  <a href="#l_imageid"><i>imageid</i></A>
  and 
  <a href="#l_filter"><i>filter</i></A>
  values as the input will be used.
  In all cases the input image will never be used as a sky for itself.
  </dd>
  </dl>
  <dl id="l_skymatch">
  <dt><b>skymatch = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skymatch' Line='skymatch = ""' -->
  <dd>Sky matching logical expression.  If specified the expression is evaluated
  for each potential sky image against the input image.  If the result is
  true the sky image is used and if it is false it is not used.  The
  expression operands use A_ to refer to a sky image and B_ to refer to
  the target input image.  For example, B_CRVAL1 refers to the CRVAL1 keyword in
  the input image.  This parameter is may be used with the <span style="font-family: monospace;">"arcsep"</span>
  function (see
  <a href="procexpr"><b>procexpr</b></A>
  ) to select skies that are nearby but
  offset by a minimum amount.
  </dd>
  </dl>
  <dl id="l_skymode">
  <dt><b>skymode = <span style="font-family: monospace;">"nearest"</span> (nearest|before|after|median &lt;N&gt; &lt;AVG&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skymode' Line='skymode = "nearest" (nearest|before|after|median &lt;N&gt; &lt;AVG&gt;)' -->
  <dd>The type of sky background estimation when sky subtraction is enabled.
  This applies when the 
  <a href="#l_skies"><i>skies</i></A>
  parameter does not explicitly assigning
  a sky image.  As described in the 
  <i>skies</i>
  parameter, a list of
  sky images which match the input in filter and image ID is defined for
  a particular input image.  The list will also exclude the input image,
  if it is in the list, and will apply the 
  <a href="#l_skymatch"><i>skymatch</i></A>
  expression to
  further define the list.  The final list is sorted by the 
  <a href="#l_sortval"><i>sortval</i>.</A>
  The parameter choices are <span style="font-family: monospace;">"nearest"</span> to select the
  nearest image in sort value, <span style="font-family: monospace;">"before"</span> for the nearest before, <span style="font-family: monospace;">"after"</span>
  for the nearest after, and <span style="font-family: monospace;">"median"</span> to form a median from the images.
  The <span style="font-family: monospace;">"median"</span> option takes two optional arguments specifying the number of images
  nearest the input image, in sort value, to be used in the median and
  the number of central values to average.
  The defaults are 5 and 1.  It will also make use of any object mask (
  <a href="#l_obm"><i>obm</i></A>
  )
  associated with a sky to exclude sources from the median.
  For more details on the sky methods see the SKY SUBTRACTION section.
  </dd>
  </dl>
  <dl id="l_stype">
  <dt><b>stype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='stype' Line='stype = ""' -->
  <dd>Logical expression used to identify sky exposures in the input list for
  processing and use as calibration.  This does not apply to images in the
  <a href="#l_skies"><i>skies</i></A>
  list.
  If sky images
  are specified by the 
  <a href="#l_skies"><i>skies</i></A>
  list then this parameter is ignored.  The default expression matches all images.
  </dd>
  </dl>
  <dl id="l_obm">
  <dt><b>obm = <span style="font-family: monospace;">"(objmask)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obm' Line='obm = "(objmask)"' -->
  <dd>List of object masks or an expression evaluating to an object mask.  If a
  list is specified it must either be empty to not use a mask, be a single
  mask to be applied to all input, or a list which matches the input list.
  If no mask is specified all pixels are assumed to be good.  The masks
  are used for the
  <a href="l_skysub"><i>skysub</i></A>
  median option and/or in expressions with
  the operand $O.  For <i>skysub</i> this parameter must be an expression and
  not a list.  The mask could really be any type of mask but it is intended
  to be used for object masking in sky subtraction.  See
  <a href="acesegment"><b>acesegment</b></A>
  for creating object masks.  The mask is matched to the input image using
  physical coordinates (those defined by the LTV/LTM keywords) and so the
  mask need not be the same size.  Pixels which do not overlap the mask
  are treated as good having pixel values of 0.
  A bad pixel mask specified by the keyword BPM may also be referenced in
  expressions by the operand $M.
  </dd>
  </dl>
  <dl id="l_exprdb">
  <dt><b>exprdb = <span style="font-family: monospace;">"newfirm$nfskysub.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exprdb' Line='exprdb = "newfirm$nfskysub.dat"' -->
  <dd>Expression database defining the sky subtraction operation.
  The default database simple defines an unscaled subtraction ($I - $S).
  This text file allows overriding and customizing the operation to
  include masks or scaling derived from keywords.  See <b>nfproc</b>
  for more information on expressions and the expression database.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT"' -->
  <dd>List of logfiles for recording processing information.  The special value
  <span style="font-family: monospace;">"STDOUT"</span> may be used to write to the terminal and multiple files may be
  specified to tee the output to more than one file.  The output is appended
  to any existing output.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>NFSKYSUB</b> sky subtracts NEWFIRM data.  The task is a simple
  wrapper script call <b>NFPROC</b> with only sky subtraction options.
  The input is a list of NEWFIRM exposures and the output is set of
  sky subtracted exposures in the same format as the input.  The output
  filenames are set by a list matching the input list or a pattern based
  on the input filenames.  A logfile can also be output to the terminal
  and/or a file.
  </p>
  <p>
  Input masks may also be used as specified by the BPM keyword and by
  the <i>obm</i> parameter.  The latter is typically an object mask
  produced by a task in the ACE package.
  </p>
  <p>
  The input NEWFIRM data is typically a multiextension format (MEF)
  file.  Extensions are matched by the value of IMAGEID keyword.
  Processing is grouped by filter using the FILTER keyword.  The time
  order of the data is defined by the MJD-OBS keyword and the exposure
  time is given by the EXPTIME keyword.
  </p>
  </section>
  <section id="s_sky_subtraction">
  <h3>Sky subtraction</h3>
  <p>
  The candidate sky images are specified by the 
  <a href="#l_skies"><i>skies</i></A>
  parameter
  or, if null, selected from the input list.  The 
  <a href="#l_skies"><i>skies</i></A>
  parameter may be a
  list of images or an expression resolving to an image for each input image.
  An expression typically selects an image header keyword associating a
  sky image with the input image.  In this case sky subtraction is just a
  simple single image subtraction ignoring the 
  <a href="#l_skymode"><i>skymode</i></A>
  and other sky
  parameters and with no checks on the filter or image ID as described in
  the remainder of this section.
  </p>
  <p>
  When the 
  <a href="#l_skies"><i>skies</i></A>
  parameter is null the 
  <a href="#l_stype"><i>stype</i></A>
  expression is used
  to identify sky images from the input list.  This parameter is not used
  otherwise.  If the 
  <a href="#l_stype"><i>stype</i></A>
  expression is null then all images
  are candidate sky images.  This is typically done when sky subtracting from
  dithered sparse-field observations.
  </p>
  <p>
  One or more sky images is then selected for each input image.  Note
  that the sky selection process may include the input image but it is
  excluded as sky for itself.  The sky images must have the same value
  of the 
  <a href="#l_imageid"><i>imageid</i></A>
  and 
  <a href="#l_filter"><i>filter</i></A>
  expressions as the input image.
  In addition, sky images must satistfy the 
  <a href="#l_skymatch"><i>skymatch</i></A>
  expression which
  allows comparing keywords from the input and candidate sky image using the
  references <span style="font-family: monospace;">"A_&lt;keyword&gt;"</span> and <span style="font-family: monospace;">"B_&lt;keyword&gt;"</span>.  One example is to require a
  sky image to be near, but not too near, the position of the input image.
  The following uses a file containing an expression based on the separation
  of the two images in arc seconds.
  </p>
  <div class="highlight-default-notranslate"><pre>
  skymatch = "@(arcsep.dat)"
  
  where the file arcsep.dat contains
  
  (arcsep(A_RA,A_DEC,B_RA,B_DEC)&gt;600 &amp;&amp;
   arcsep(A_RA,A_DEC_B_RA,B_DEC)&lt;3600))
  
  or
  
  (arcsep(A_CRVAL1/15,A_CRVAL2,B_CRVAL1/15,B_CRVAL2)&gt;600 &amp;&amp;
   arcsep(A_CRVAL1/15,A_CRVAL2,B_CRVAL1/15,B_CRVAL2)&lt;3600))
  </pre></div>
  <p>
  Note that the CRVAL1 values are right ascension in degrees while the arcsep
  function requires hours.  Note that if the data have offset parameters
  those would be easier to use.
  </p>
  <p>
  Another example might be that the sky and input images have different
  nod flags as in the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  skymatch = "(A_NOD!=B_NOD)"
  </pre></div>
  <p>
  Once a set of candidate sky images is selected for a particular input
  image the 
  <a href="#l_skymode"><i>skymode</i></A>
  parameter selects from this list and specifies how
  they are used.  The candidate list is sorted by the MJD-OBS keyword
  values.
  The options <span style="font-family: monospace;">"before"</span>, <span style="font-family: monospace;">"after"</span>, or <span style="font-family: monospace;">"nearest"</span> select a single sky image
  to subtract which has is the nearest before, after, or on either side
  of the input image, respectively.  If there is no image before or
  after as requested then the nearest is used.
  </p>
  <p>
  The option <span style="font-family: monospace;">"median [&lt;N&gt; [&lt;AVG&gt;]]"</span> (where the default value of N is 5
  and of AVG is 1) selects the nearest N/2 (rounded down to an integer)
  sky images before the input image and the (N-1) subsequent images.
  When there are not enough images before or after then images are added
  at the other end.  Of course if there are fewer than N images then all
  are used.  Again, note that if the input image is in the candidate list
  it is excluded with the result that median is computed from N-1 images.
  </p>
  <p>
  The median calculation will make use of any object mask (
  <a href="#l_obm"><i>obm</i></A>
  )
  associated with a sky to exclude sources from the median.  When pixels
  are excluded then the median is taken over a smaller number of pixels.
  After the pixels are sorted the specified average of the central values
  is taken.  Note that if the number of values averaged is rounded
  up to an even number when the number of remaining pixels is even or
  rounded up to an odd number when number of pixels is odd to insure
  a symmetric statistic.  When the average is 1, a classic median,
  this means that for an even number of pixels the average of the central
  two values is the median value.
  </p>
  <p>
  One observing mode is when the science fields are sparse and
  dithered exposures are taken with the intent that sky will be
  obtained from a median of temporally close exposures.  This would
  use the running median method.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <a href="nfproc">nfproc</A>
  <a href="runmed">runmed</A>
  <a href="procexpr">procexpr</A>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE   ' 'PARAMETERS' 'DESCRIPTION' 'SKY SUBTRACTION' 'SEE ALSO'  -->
  
