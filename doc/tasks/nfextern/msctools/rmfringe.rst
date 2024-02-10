.. _rmfringe:

rmfringe: Remove fringe pattern
===============================

**Package: msctools**

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
  <dl id="l_fringe">
  <dt><b>fringe</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fringe' Line='fringe' -->
  <dd>List of fringe images or multiextension files.  The list must either match
  the input list or be a single file to be used for all the input files.
  The fringe pattern is assumed to have a flat mean background.  This is
  usually zero though this task will determine and ignore any constant
  mean in the data.
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
  <dl id="l_fringemasks">
  <dt><b>fringemasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fringemasks' Line='fringemasks' -->
  <dd>List of masks identifying pixels to ignore in the fringe image.
  This mask is primarily intended to restrict the amplitude calculation
  to the region of the fringe pattern.  Pixels to ignore have
  non-zero mask values.  The same options for specifying the masks apply
  as for the <i>masks</i> parameter.  Keyword references will sought in the
  fringe pattern image header.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = ""' -->
  <dd>List of backgrounds for the input data.  If no list is given then the mean
  of the data, excluding masked pixels, is used for the background.  The list
  may be either a single value which applies to all the input data or match
  the input list in number.  The background may be specifed as an image or
  constant value.  Images are linearly interpolated to the size of the data
  images if the sizes do not match.
  </dd>
  </dl>
  <dl id="l_ncblk">
  <dt><b>ncblk = 5, nlblk = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncblk' Line='ncblk = 5, nlblk = 5' -->
  <dd>Moving average block sizes for the input and fringe images.
  The block average size for columns and for lines are specified separately.
  </dd>
  </dl>
  <dl id="l_extfit">
  <dt><b>extfit = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extfit' Line='extfit = ""' -->
  <dd>Extensions to use for fitting the fringe amplitude.  A null string matches
  all extension names.  Otherwise the parameter is a comma separated list of
  patterns which match the entire extension name.  Thus, a list of extension
  names may be given or the pattern matching characters <span style="font-family: monospace;">'?'</span> for any
  character or [] for a set of characters.  The set may include ranges in
  ascii order by using hyphens; i.e. 1-3 matches the characters 1, 2, and 3.
  All the selected extensions in the input files must also exist in the
  fringe and mask files.
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
  RMFRINGE determines the fringe amplitude that minimizes the weighted mean
  difference between an input image and a fringe image given in equation 1.
  The input images, specified by the <i>input</i> parameter, may be individual
  images (which includes images selected from multiextension files as
  explicit image extensions) or multiextension files specified by a root
  filename.  In the latter case the image extension names selected by the
  <i>extfit</i> parameter are used for computing a global fringe amplitude for
  all the extensions.
  </p>
  <p>
  The output of this task are fringe corrected images or multiextension files
  and log information with the computed fringe amplitude.  When the input is
  a multiextension file the output is a multiextension file with all the same
  extensions.  Note that all extensions are used for the output regardless of
  which extensions are selected for fitting.  The fringe correction is <span style="font-family: monospace;">"A - s
  * (F - &lt;F&gt;)"</span> where the quantities are defined below.
  </p>
  <p>
  The statistic used to compute the scale is
  </p>
  <div class="highlight-default-notranslate"><pre>
  (1)  &lt;(((A - B) - s (F - &lt;F&gt;)) (F - &lt;F&gt;))&gt; = 0
  </pre></div>
  <p>
  where
  </p>
  <div class="highlight-default-notranslate"><pre>
  A           Input image               (<i>input</i> parameter)
  B           Input image background    (<i>background</i> parameter)
  F           Fringe image              (<i>fringe</i> parameter)
  s           Fringe amplitude scale factor
  </pre></div>
  <p>
  The solution of equation 1 is determined over all pimels in the image or
  extensions selected by the <i>extfit</i> parameter which are not flagged in
  the pixel mask specified by the <i>masks</i> parameter.  For multiextension
  files equation 1 is also solved separately for each extension and estimates
  of the fringe scale are shown in the log output (see examples 2 and 3).
  However, the final fringe amplitude is not the average of these values but
  the solution over all pixels.  To treat image extensions as independent
  images the various file lists must be explicit images rather than
  multiextension file rootnames (see example 4).
  </p>
  <p>
  The fitting defined by equation 1 is improved by smoothing when the data
  and fringe pattern include noise, such as occurs when it is derived from
  observational data.  The images may be smoothed by a moving block average
  with block sizes specified by the parameters <i>ncblk</i> and <i>nlblk</i>.
  </p>
  <p>
  There are three types of backgrounds, B, which may be specified.  An image,
  a constant, and the mean value.  The image may be a fully sampled image
  of the same size as the image to which it applies or a smaller sampled
  image that is interpolated to match the size of the image.  If there is a
  background gradient in the input data it is useful to supply a background
  image otherwise the mean may be used by specifying a null string, <span style="font-family: monospace;">""</span>.
  </p>
  <p>
  A key to obtaining the best match between the fringe and the input data is
  to use masks for the input and fringe pattern.  The masks will identify bad
  data and the objects in the input image.  The task <b>nproto.objmasks</b> is
  recommended for creating the object masks.
  </p>
  <p>
  The masks specified by the <b>masks</b> parameter may be in any of the supported
  masks formats.  As of IRAF V2.12 this includes pixel list (.pl) files
  and FITS <span style="font-family: monospace;">"type=mask"</span> extensions.  When the input is a multiextension
  file, the selected extension names are appended to the mask filename to
  select masks with the same extension name.  If a mask file of the form
  <span style="font-family: monospace;">"name[ext]"</span> is not found the task will treat the filename as a directory
  of pixel list files and select the filename corresponding to the
  extension name; i.e. <span style="font-family: monospace;">"name/ext.pl"</span>.
  </p>
  <p>
  In addition to the fringe corrected image, log output to the terminal is
  produced when <i>verbose</i> is <span style="font-family: monospace;">"yes"</span> and log output to a specified file
  is produced by setting <i>logfile</i>.  The output is the same for both.
  Because this task is a simple script calling the task <b>patfit</b>
  the log output contains some additional information not described here.
  See the help page for <b>patfit</b> for details.
  </p>
  <p>
  The output image will also contain a record of the operation performed
  under the keyword RMFRINGE as in the following example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  RMFRINGE  = 'o262 - 0.80696 (fringe - 0.15538)'
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Fringe removal from a single image, <span style="font-family: monospace;">"o262"</span>.  The fringe image, <span style="font-family: monospace;">"fringe"</span>,
  is created by combining many exposures during the night to eliminate the
  objects.  A smooth background, averaged on scales larger than the fringe
  pattern, is subtracted.  The input image is processed to produce a mask,
  <span style="font-family: monospace;">"objmask262"</span>, of the objects and bad pixels (see <b>nproto.objmasks</b>) and
  also a low frequency sky map to account for gradients in the background.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rmfringe o262 fo262 fringe objmask262 background=sky262
  RMFRINGE: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262
    pattern = fringe
    weight = fringe
    input background = sky262
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262
    output = fo262
    outtype = pdiff
    &lt;pattern&gt; = 0.1554
    &lt;weight&gt; = 0.1554
    scale = 0.807
      fo262 = o262 - 0.80696 (fringe - 0.15538)
  </pre></div>
  <p>
  2.  The same fringing example but with multiextension files.  In this
  case the object mask may either be a multiextension file of mask type
  extensions (V2.12 and later) or a directory <span style="font-family: monospace;">"objmask262"</span> with files im1.pl,
  im2.pl, etc.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rmfringe o262 fo262 fringe objmask262 background=sky262
  RMFRINGE: NOAO/IRAF V2.11EXPORT ... 15-Jan-2002
    input = o262
    pattern = fringe
    weight = fringe
    input background = sky262
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262
    output = fo262
    outtype = pdiff
      o262[im1]: 0.8127
      o262[im2]: 0.8103
      o262[im3]: 0.8235
      o262[im4]: 0.8177
      o262[im5]: 0.8161
      o262[im6]: 0.8365
      o262[im7]: 0.7584
      o262[im8]: 0.7979
    &lt;pattern&gt; = 0.5208
    &lt;weight&gt; = 0.5208
    scale = 0.8095
      fo262[im1] = o262[im1] - 0.80953 (fringe[im1]...
      fo262[im2] = o262[im2] - 0.80953 (fringe[im2]...
      fo262[im3] = o262[im3] - 0.80953 (fringe[im3]...
      fo262[im4] = o262[im4] - 0.80953 (fringe[im4]...
      fo262[im5] = o262[im5] - 0.80953 (fringe[im5]...
      fo262[im6] = o262[im6] - 0.80953 (fringe[im6]...
      fo262[im7] = o262[im7] - 0.80953 (fringe[im7]...
      fo262[im8] = o262[im8] - 0.80953 (fringe[im8]...
  </pre></div>
  <p>
  3.  The same fringing example with multiextension files with fitting
  extensions specified.  This artificial example shows fitting one
  set of extensions and outputing a different set.  A more likely situation
  would be fitting a subset of extensions (for speed) but outputing all the
  extensions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rmfringe o262 fo262 fringe objmask262 background=sky262 \
  &gt;&gt;&gt; extfit=im[123]
  RMFRINGE: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262
    pattern = fringe
    weight = fringe
    input background = sky262
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262
    output = fo262
    outtype = pdiff
      o262[im1]: 0.8127
      o262[im2]: 0.8103
      o262[im3]: 0.8235
    &lt;pattern&gt; = 0.1554
    &lt;weight&gt; = 0.1554
    scale = 0.8153
      fo262[im4] = o262[im4] - 0.81534 (fringe[im4]...
      fo262[im5] = o262[im5] - 0.81534 (fringe[im5]...
      fo262[im6] = o262[im6] - 0.81534 (fringe[im6]...
  </pre></div>
  <p>
  4.  The same multextension fringing example treating the extensions as
  independent images.  Note that in this case the mask is actually
  objmask262/im1.pl but is referenced as objmask262[im1] (the other
  form could also be used).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dpar rmfringe
  rmfringe.input = "o262[im1],o262[im2],o262[im3]"
  rmfringe.output = "fo262[im1],fo262[im2,append],...
  rmfringe.fringe = "fringe[im1],fringe[im2],...
  rmfringe.masks = "objmask262[im1],objmask262[im2],objmask262[im3]"
  rmfringe.background = ""
  rmfringe.extfit = ""
  rmfringe.logfile = "logfile"
  rmfringe.verbose = yes
  rmfringe.mode = "ql"
  # EOF
  cl&gt; rmfringe
  List of input images (o262[im1],o262[im2],o262[im3]):
  List of output corrected images (fo262[im1],fo262[im2,append],...
  Fringe or list of fringe patterns (fringe[im1],...
  List of object/bad data masks (objmask262[im1],...
  RMFRINGE: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262[im1]
    pattern = fringe[im1]
    weight = fringe[im1]
    input background = &lt;input&gt;
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262[im1]
    output = fo262[im1]
    outtype = pdiff
    &lt;input&gt; = 7340.
    &lt;pattern&gt; = 0.1587
    &lt;weight&gt; = 0.1587
    scale = 0.8088
      fo262[im1] = o262[im1] - 0.80883 (fringe[im1]...
  RMFRINGE: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262[im2]
    pattern = fringe[im2]
    weight = fringe[im2]
    input background = &lt;input&gt;
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262[im2]
    output = fo262[im2,append]
    outtype = pdiff
    &lt;input&gt; = 7299.
    &lt;pattern&gt; = -0.3147
    &lt;weight&gt; = -0.3147
    scale = 0.7948
      fo262[im2,append] = o262[im2] - 0.79481 (fringe[im2]...
  RMFRINGE: NOAO/IRAF V2.11EXPORT ... 18-Jan-2002
    input = o262[im3]
    pattern = fringe[im3]
    weight = fringe[im3]
    input background = &lt;input&gt;
    pattern background = &lt;pattern&gt;
    weight background = &lt;weight&gt;
    input mask = objmask262[im3]
    output = fo262[im3,append]
    outtype = pdiff
    &lt;input&gt; = 7260.
    &lt;pattern&gt; = 0.634
    &lt;weight&gt; = 0.634
    scale = 0.8185
      fo262[im3,append] = o262[im3] - 0.81849 (fringe[im3]...
  </pre></div>
  <p>
  Note that in this case an output multiextension file is built from the
  individual outputs by using the <span style="font-family: monospace;">"append"</span> syntax of the FITS image kernel.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nproto.objmasks, patfit, rmpupil, irmfringe
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
