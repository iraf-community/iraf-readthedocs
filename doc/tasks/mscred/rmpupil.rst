.. _rmpupil:

rmpupil: Remove pupil image
===========================

**Package: mscred**

.. raw:: html

  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images or multiextension files.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of corrected output images or multiextension files.  If no list is
  specified then the input list is used, otherwise the output list must match the
  input list.  If an input and output file are the same the output is
  created in a temporary file and the input is replaced after the output is
  completed.
  </dd>
  </dl>
  <dl id="l_pupil">
  <dt><b>pupil</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pupil' Line='pupil' -->
  <dd>List of pupil images or multiextension files.  The list must either match
  the input list or be a single file to be used for all the input files.
  The pupil pattern is assumed to have a zero background.
  </dd>
  </dl>
  <dl id="l_masks">
  <dt><b>masks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masks' Line='masks' -->
  <dd>List of masks identifying pixels to ignore in the input data.  Pixels to
  ignore have non-zero mask values.  An empty list applies no bad
  pixel mask, a single mask applies to all input data, and a list is matched
  with the input list. A mask is specified by a filename or by
  reference to a filename given by the value of a header keyword in the input
  image.  A header keyword reference is made with the syntax <span style="font-family: monospace;">"!&lt;keyword&gt;"</span>
  where &lt;keyword&gt; is the desired keyword with case ignored.  For
  multiextension files the masks may be either a multiextension file with
  matching extension names or a directory of pixel list files with the
  extension names as the filenames.
  </dd>
  </dl>
  <dl id="l_pupilmasks">
  <dt><b>pupilmasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pupilmasks' Line='pupilmasks' -->
  <dd>List of masks identifying pixels to ignore in the pupil image.
  This mask is primarily intended to restrict the amplitude calculation
  to the region of the pupil pattern.  Pixels to ignore have
  non-zero mask values.  The same options for specifying the masks apply
  as for the <i>masks</i> parameter.  Keyword references will sought in the
  pupil pattern image header.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">"sdiff"</span> (sdiff|sflat)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = "sdiff" (sdiff|sflat)' -->
  <dd>Output type from the choices <span style="font-family: monospace;">"sdiff"</span> and <span style="font-family: monospace;">"sflat"</span>.  The first one scales
  and subtracts the pupil pattern and the second flattens the input
  by the pupil pattern.
  </dd>
  </dl>
  <dl id="l_ncblk">
  <dt><b>ncblk = 5, nlblk = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncblk' Line='ncblk = 5, nlblk = 5' -->
  <dd>Moving average block sizes for the input and pupil images.
  The block average size for columns and for lines are specified separately.
  </dd>
  </dl>
  <dl id="l_extfit">
  <dt><b>extfit = <span style="font-family: monospace;">"im[2367]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extfit' Line='extfit = "im[2367]"' -->
  <dd>Extensions to use for fitting the pupil amplitude.  A null string matches
  all extension names.  Otherwise the parameter is a comma separated list of
  patterns which match the entire extension name.  Thus, a list of extension
  names may be given or the pattern matching characters <span style="font-family: monospace;">'?'</span> for any
  character or [] for a set of characters.  The set may include ranges in
  ascii order by using hyphens; i.e. 1-3 matches the characters 1, 2, and 3.
  The default value is for the KPNO Mosaic at the Mayall telescope.
  All the selected extensions in the input files must also exist in the
  pupil and mask files.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>Filename for appending log information.  If no name is specified then no
  log is written.  Note that there is no need to use <span style="font-family: monospace;">"STDOUT"</span> since the
  same information is written when the <i>verbose</i> parameter is set.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>If set to yes, log information is written to the standard output.  Note
  that this is the same information as written to the logfile specified
  by the <i>logfile</i> parameter.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  RMPUPIL determines the pupil amplitude that minimizes the weighted mean
  difference between an input image and a fringe image given in equation 1.
  The input images, specified by the <i>input</i> parameter, may be individual
  images (which includes images selected from multiextension files as
  explicit image extensions) or multiextension files specified by a root
  filename.  In the latter case the image extension names selected by the
  <i>extfit</i> parameter are used for computing a global pupil amplitude for
  all the extensions.
  </p>
  <p>
  The output of this task are pupil corrected images or multiextension
  files.  When the input is a multiextension file the output is a
  multiextension file with all the same extensions.  Note that all the
  extensions in the input are output regardless of which extensions are
  selected for fitting.
  </p>
  <p>
  The statistic used to compute the scale is
  </p>
  <div class="highlight-default-notranslate"><pre>
  (1)  &lt;(((A - &lt;A&gt;) - s (P - &lt;P&gt;)) (P - &lt;P&gt;))&gt; = 0
  </pre></div>
  <p>
  where
  </p>
  <div class="highlight-default-notranslate"><pre>
  A           Input image               (<i>input</i> parameter)
  B           Input image background    (<i>background</i> parameter)
  P           Pupil image               (<i>pupil</i> parameter)
  s           Pupil amplitude scale factor
  </pre></div>
  <p>
  The solution of equation 1 is determined over all pixels in the image or
  extensions selected by the <i>extfit</i> parameter which are not flagged in
  the pixel masks specified by the <i>masks</i> and <i>pupilmasks</i>
  parameters.  For multiextension files equation 1 is also solved separately
  for each extension and estimates of the pupil amplitude are shown in the
  log output (see examples 2 and 3).  However, the final pupil amplitude is
  not the average of these values but the solution over all pixels.  To treat
  image extensions as independent images the various file lists must be
  explicit images rather than multiextension file rootnames (see example 3).
  </p>
  <p>
  The fitting defined by equation 1 is improved by smoothing when the data
  and pupil pattern include noise, such as occurs when it is derived from
  observational data.  The images may be smoothed by a moving block average
  with block sizes specified by the parameters <i>ncblk</i> and <i>nlblk</i>.
  </p>
  <p>
  There are two types of output from the task selected by the <i>outtype</i>
  parameter.  When the type is <span style="font-family: monospace;">"sdiff"</span> the output is <span style="font-family: monospace;">"A - s * P"</span>.  When
  the type is <span style="font-family: monospace;">"sflat"</span> the output is <span style="font-family: monospace;">"A / (f * P + 1)"</span> where
  </p>
  <div class="highlight-default-notranslate"><pre>
  (2)  f = s / b = s / (&lt;A&gt; - s * &lt;P&gt;)
  </pre></div>
  <p>
  The quantity b is an estimate of the background outside the pupil pattern.
  The derived quantities f and b are printed in the log output under the
  keywords <span style="font-family: monospace;">"flatscale"</span> and <span style="font-family: monospace;">"flatbkg"</span>.
  </p>
  <p>
  While the observed pupil pattern is basically a scattered (additive) light
  effect it must be removed in a two step process when it also appears in
  the flat field data.  In the first step the pattern is removed from the
  flat field data using the <span style="font-family: monospace;">"sflat"</span> option.  This separates the underlying
  relative responses of the pixels.  After this corrected flat field is
  applied to the object data the pupil pattern is then removed as additive
  light using the <span style="font-family: monospace;">"sdiff"</span> option.  Generally the pupil pattern image is
  derived before each step.  A pupil pattern is first derived from data which
  has not been flat fielded, in other words from the flat field data itself.
  Then, after the object data has been flat fielded by the corrected flat
  field, a new pupil pattern is extracted from a sky flat field produced
  from the flat fielded object data.
  </p>
  <p>
  A key to obtaining the best match between the pupil pattern and the input
  data is to use masks for the input and the pattern.  The mask for the
  input data identifies bad data and objects in the input image.  The task
  <b>nproto.objmasks</b> is recommended for creating the masks.  When removing
  the pattern from flat field data the mask may be absent or identify regions
  where the flat field response significantly distorts the pattern, such
  as regions of very low or non-linear response or dust patterns.
  </p>
  <p>
  The pattern mask restricts the data used to determine the pupil amplitude
  to where the pupil pattern is located.  The two masks can be combined into
  one mask but it may be easier to use two separate masks since the pattern
  mask will often be independent of the data or even the date of observation.
  </p>
  <p>
  The masks specified by the <i>masks</i> and <i>pupilmasks</i> parameters may be
  in any of the supported masks formats.  As of IRAF V2.12 this includes
  pixel list (.pl) files and FITS <span style="font-family: monospace;">"type=mask"</span> extensions.  When the input is
  a multiextension file, the selected extension names are appended to the
  mask filename to select masks with the same extension name.  If a mask file
  of the form <span style="font-family: monospace;">"name[ext]"</span> is not found the task will treat the filename as a
  directory of pixel list files and select the filename corresponding to the
  extension name; i.e. <span style="font-family: monospace;">"name/ext.pl"</span>.
  </p>
  <p>
  In addition to the pupil corrected image, log output to the terminal is
  produced when <i>verbose</i> is <span style="font-family: monospace;">"yes"</span> and log output to a specified file
  is produced by setting <i>logfile</i>.  The output is the same for both.
  Because this task is a simple script calling the task <b>patfit</b>
  the log output contains some additional information not described here.
  See the help page for <b>patfit</b> for details.
  </p>
  <p>
  The output image will also contain a record of the operation performed
  under the keyword RMPUPIL as in the following example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  RMPUPIL  = 'o262 - 0.80696 pupil'
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Pupil removal from a single image, <span style="font-family: monospace;">"o262"</span>.
  The input image is processed to produce a mask, <span style="font-family: monospace;">"objmask262"</span>, of the
  objects and bad pixels (see <b>nproto.objmasks</b>).  A pupil mask, <span style="font-family: monospace;">"pupilmask"</span>,
  has been created at the same time as the pupil pattern image, <span style="font-family: monospace;">"pupil"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rmpupil o262 fo262 pupil objmask262 pupilmask=pupilmask
  RMPUPIL: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262
    pattern = pupil
    weight = pupil
      ncblk = 5
      nlblk = 5
    input background = &lt;input&gt;
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262
    pattern mask = pupilmask
    output = fo262
    outtype = sdiff
    &lt;input&gt; = 7650.
    &lt;pattern&gt; = 0.1554
    &lt;weight&gt; = 0.1554
    scale = 0.807
      fo262 = o262 - 0.80696 pupil
  </pre></div>
  <p>
  2.  The same example but with multiextension files.  In this
  case the object mask may either be a multiextension file of mask type
  extensions (V2.12 and later) or a directory <span style="font-family: monospace;">"objmask262"</span> with files im1.pl,
  im2.pl, etc.  This shows fitting the pupil only in the set of extensions
  where parts of the pupil pattern are found and then creating an
  output with all the extensions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rmpupil o262 fo262 pupil objmask262 pupilmask=pupilmask
  RMPUPIL: NOAO/IRAF V2.11EXPORT ... 15-Jan-2002
    input = o262
    pattern = pupil
    weight = pupil
      ncblk = 5
      nlblk = 5
    input background = &lt;input&gt;
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262
    pattern mask = pupilmask
    output = fo262
    outtype = sdiff
      o262[im2]: 0.8103
      o262[im3]: 0.8235
      o262[im6]: 0.8365
      o262[im7]: 0.7584
    &lt;input&gt; = 7650.
    &lt;pattern&gt; = 0.5208
    &lt;weight&gt; = 0.5208
    scale = 0.8095
      fo262[im1] = o262[im1] - 0.80953 pupil[im1]
      fo262[im2] = o262[im2] - 0.80953 pupil[im2]
      fo262[im3] = o262[im3] - 0.80953 pupil[im3]
      fo262[im4] = o262[im4] - 0.80953 pupil[im4]
      fo262[im5] = o262[im5] - 0.80953 pupil[im5]
      fo262[im6] = o262[im6] - 0.80953 pupil[im6]
      fo262[im7] = o262[im7] - 0.80953 pupil[im7]
      fo262[im8] = o262[im8] - 0.80953 pupil[im8]
  </pre></div>
  <p>
  3.  The same multextension example treating the extensions as
  independent images.  Note that in this case the mask is actually
  objmask262/im1.pl but is referenced as objmask262[im1] (the other
  form could also be used).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dpar rmpupil
  rmpupil.input = "o262[im2],o262[im3],o262[im6],o262[im7]"
  rmpupil.output = "fo262[im2],fo262[im3,append],...
  rmpupil.pupil = "pupil[im2],pupil[im3],...
  rmpupil.masks = "objmask262[im2],objmask262[im3],...
  rmpupil.patternmasks = "pupilmask[im2],pupilmask[im3],...
  rmpupil.outtype = "sdiff"
  rmpupil.ncblk = 5
  rmpupil.nlblk = 5
  rmpupil.extfit = ""
  rmpupil.logfile = "logfile"
  rmpupil.verbose = yes
  rmpupil.mode = "ql"
  # EOF
  cl&gt; rmpupil
  List of input images (o262[im2],o262[im3],...
  List of output corrected images (fo262[im2],fo262[im3,append],...
  Pupil or list of pupil patterns (pupil[im2],...
  List of object/bad data masks (objmask262[im2],...
  RMPUPIL: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262[im2]
    pattern = pupil[im2]
    weight = pupil[im2]
      ncblk = 5
      nlblk = 5
    input background = &lt;input&gt;
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262[im2]
    pattern mask = pupilmask[im2]
    output = fo262[im2]
    outtype = sdiff
    &lt;input&gt; = 7340.
    &lt;pattern&gt; = 0.1587
    &lt;weight&gt; = 0.1587
    scale = 0.8088
      fo262[im2] = o262[im2] - 0.80883 pupil[im2]
  RMPUPIL: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262[im3]
    pattern = pupil[im3]
    weight = pupil[im3]
      ncblk = 5
      nlblk = 5
    input background = &lt;input&gt;
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262[im3]
    pattern mask = pupilmask[im3]
    output = fo262[im3,append]
    outtype = sdiff
    &lt;input&gt; = 7299.
    &lt;pattern&gt; = -0.3147
    &lt;weight&gt; = -0.3147
    scale = 0.7948
      fo262[im3,append] = o262[im3] - 0.79481 pupil[im3]
  ...
  </pre></div>
  <p>
  Note that in this case an output multiextension file is built from the
  individual outputs by using the <span style="font-family: monospace;">"append"</span> syntax of the FITS image kernel.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nproto.objmasks, patfit, rmfringe, irmpupil
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
