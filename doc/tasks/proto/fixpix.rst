.. _fixpix:

fixpix: Fix bad pixels by linear interpolation from nearby pixels
=================================================================

**Package: proto**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  fixpix images masks
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of two dimensional images to be <span style="font-family: monospace;">"fixed"</span> (modified) by
  linear interpolation.
  </dd>
  </dl>
  <dl id="l_masks">
  <dt><b>masks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masks' Line='masks' -->
  <dd>List of bad pixel masks, images, or files (collectively called masks)
  identifying the bad pixels.  The list of masks must either match the
  list of input images in number or a single mask may be specified to apply
  to all images.  The special name <span style="font-family: monospace;">"BPM"</span> may be specified to select a mask
  specified by the header keyword <span style="font-family: monospace;">"BPM"</span> in the input image.  The possible
  mask formats are given in the DESCRIPTION section.
  </dd>
  </dl>
  <dl id="l_linterp">
  <dt><b>linterp = <span style="font-family: monospace;">"INDEF"</span>, cinterp = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linterp' Line='linterp = "INDEF", cinterp = "INDEF"' -->
  <dd>Normally interpolation is performed across the narrowest dimension spanning
  the bad pixels with interpolation along image lines if the two dimensions are
  equal.  However specific values in the mask may be used to
  identify the desired interpolation direction.  The value in the mask
  specifying line interpolation is given by the <i>linterp</i> parameter and
  the value specifying column interpolation is given by the <i>cinterp</i>
  parameter.  Any values which are do not match one of these parameters
  results in interpolation along the narrowest dimension.  Note that a
  text file mask always has 2 for pixels with narrow dimension along
  lines and 3 for pixels with narrow dimension along columns.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If this parameter is set to yes a line identifying each image and
  associated mask is printed.  If the <i>pixels</i> parameter is
  set then a list of the pixels modified is also printed.
  </dd>
  </dl>
  <dl id="l_pixels">
  <dt><b>pixels = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixels' Line='pixels = no' -->
  <dd>List the pixels modified?  This is only done if this parameters and
  the <i>verbose</i> parameter are set.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Pixels in a list of images identified by bad pixel masks, images, or text
  files (collectively called masks here) are replaced by linear interpolation
  along lines or columns using the nearest good pixels.  The list of input
  images, specified by the <i>images</i> parameter, are matched with a list of
  masks, specified by the <i>masks</i> parameter.  The list of masks must
  match the list of input images or a single mask name may be given to apply
  to all input images.  The special mask name <span style="font-family: monospace;">"BPM"</span> may be used to
  select a mask name given in the input image header under the keyword
  <span style="font-family: monospace;">"BPM"</span>.
  </p>
  <p>
  There are three types of masks which may be used.  The preferred type
  is a bad pixel mask given as a <span style="font-family: monospace;">"pixel list"</span> image.  Pixel list images
  have the extension <span style="font-family: monospace;">".pl"</span> signifying a special compact file of integer
  values ideal for identifying sets of pixels.  For a bad pixel mask the
  good pixels have a value of zero and bad pixels have positive integer
  values.
  </p>
  <p>
  The second type is any image format.  The image will be internally
  converted to a bad pixel mask.  Note that real image values will be
  truncated to integers.  Again good pixels will have values of zero and bad
  pixels will have positive values.
  </p>
  <p>
  The final format is a text file with lines giving the integer coordinates
  of a single pixel or a rectangular region.  A single pixel is specified by
  a column and line number.  A region is specified by a starting column, an
  ending column, a starting line, and an ending line.  Internally this file
  is turned into a bad pixel mask of the size of the input image with values
  of zero for non-specified pixels, a value of two for pixels with narrowest
  interpolation direction along lines, and three for pixels with narrowest
  interpolation direction along columns.
  </p>
  <p>
  As noted previously, bad pixels are <span style="font-family: monospace;">"fixed"</span> by replacing them with values
  by linear interpolation to the nearest pixels not identified as bad.
  Normally interpolation is performed across the narrowest dimension spanning
  bad pixels with interpolation along image lines if the two dimensions are
  equal.  However specific values in the mask may be used to identify the
  desired interpolation direction.  The value in the mask specifying line
  interpolation is given by the <i>linterp</i> parameter and the value
  specifying column interpolation is given by the <i>cinterp</i> parameter.
  Any values which are do not match one of these parameters results in
  interpolation along the narrowest dimension.  Note that a text file mask
  always has 1 for pixels with narrow dimension along lines and 2 for pixels
  with narrow dimension along columns.
  </p>
  <p>
  The <i>verbose</i> allows printing a line giving the task name, the
  image name, and the mask name.  In addition, if the <i>pixels</i>
  parameter is set the pixels modified are listed.  The list of pixels
  consists of the column and line of the pixel, the original
  and replaced pixel values, and the column and line of the one or two
  pixels used for the interpolation.  If the bad pixel region has no
  pixels at one end, that is there are bad pixels all the way to one edge
  of the image, then the single pixel used is printed.
  </p>
  <p>
  Normally the input images and the masks will have the same dimension.
  However, this task matches bad pixels in the masks with the input images
  based on physical coordinates.  Thus, the mask image may be bigger or
  smaller than the input image and image sections may be used with either
  the input images or the bad pixel mask or image mask images.  If the
  input image is the result of extracting a subsection of a bigger image
  the coordinates of the pixels will be those of the original image
  and the matching coordinates of the mask will be applied.  This has
  the effect of allowing image sections to be applied to images having
  a bad pixel mask specified in the image and still having the bad pixel
  mask be valid.
  </p>
  <p>
  Mask images may be made in a variety of ways.  Any task which produces
  and modifies image values may be used.  Some useful tasks are
  <b>imexpr, imreplace, imcopy,</b> and <b>mkpattern</b>.  If a new image
  is specified with the explicit <span style="font-family: monospace;">".pl"</span> extension then the pixel mask
  format is produced.  Two other ways to make masks are with the
  tasks <b>text2mask</b> and <b>ccdmask</b>.  The former uses an input
  text file consisting of rectangular region.  This is the old
  <span style="font-family: monospace;">"fixpix"</span> format.  The task <b>ccdmask</b> is specialized to make a mask
  of bad pixels from flat fields or, even better, from the ratio of
  two flat fields of different exposure levels.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  A list of images have bad pixel masks defined in the image header.
  To replace the bad pixels by interpolation along the narrowest
  dimension:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fixpix obj* BPM
  </pre></div>
  <p>
  2.  A simple mask of 0s and 1s defines bad columns in spectral data
  with dispersion along the lines.  To interpolate along the lines:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fixpix spec00*h ccdmask linterp=1 v+
  FIXPIX: image spec001.imh with mask ccdmask
  FIXPIX: image spec002.imh with mask ccdmask
  ...
  </pre></div>
  <p>
  3.  A text file of bad pixels is used and the modified pixels are printed
  with:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type mask.dat
  1 2 1 1
  25 26 25 25
  26 27 27 27
  49 50 50 50
  10 10
  20 21 20 20
  cl&gt; fixpix myimage mask.dat v+ p+
  FIXPIX: image myimage with mask mask.dat
     1    1       1.       1.   1    2
     2    1       1.       1.   2    2
    10   10       1.       1.   9   10  11   10
    20   20       1.       1.  20   19  20   21
    21   20       1.       1.  21   19  21   21
    25   25       1.       1.  25   24  25   26
    26   25       1.       1.  26   26  26   28
    26   27       1.       1.  26   26  26   28
    27   27       1.       1.  27   26  27   28
    49   50       1.       1.  49   49
    50   50       1.       1.  50   49
  </pre></div>
  <p>
  4.  Because a text file input automatically sets the mask values to
  2 or 3 you may need to set the linterp and cinterp parameters to
  force the direction.  In particular, to apply FIXPIX to a 1D image,
  say a spectrum, if you have regions described by ranges in columns
  the mask interpolation values will be assigned as 3.  This means
  it is trying to interpolation between line 0 and line 2 which is
  obviously not what is intended.  To make this work set linterp to
  3:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fixpix myimage mask.dat linterp=3
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_FIXPIX">
  <dt><b>FIXPIX V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='FIXPIX' Line='FIXPIX V2.11' -->
  <dd>This task replaces the old task (now obsolete.ofixpix) and works with the
  more general pixel mask facilities.  It also provides greater flexibility
  in choosing the interpolation direction.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  epix, imedit, ccdproc, text2mask, obsolete.ofixpix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
