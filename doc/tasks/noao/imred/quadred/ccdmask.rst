.. _ccdmask:

ccdmask: Make a bad pixel mask from CCD data
============================================

**Package: quadred**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  ccdmask image mask
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>CCD image to use in defining bad pixels.  Typically this is
  a flat field image or, even better, the ratio of two flat field
  images of different exposure levels.
  </dd>
  </dl>
  <dl id="l_mask">
  <dt><b>mask</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mask' Line='mask' -->
  <dd>Pixel mask name to be created.  A pixel list image, .pl extension,
  is created so no extension is necessary.
  </dd>
  </dl>
  <dl id="l_ncmed">
  <dt><b>ncmed = 7, nlmed = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncmed' Line='ncmed = 7, nlmed = 7' -->
  <dd>The column and line size of a moving median rectangle used to estimate the
  uncontaminated local signal.  The column median size should be at least 3
  pixels to span single bad columns.
  </dd>
  </dl>
  <dl id="l_ncsig">
  <dt><b>ncsig = 15, nlsig = 15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncsig' Line='ncsig = 15, nlsig = 15' -->
  <dd>The column and line size of regions used to estimate the uncontaminated
  local sigma using a percentile.  The size of the box should contain
  of order 100 pixels or more.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 6, hsigma = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 6, hsigma = 6' -->
  <dd>Positive sigma factors to use for selecting pixels below and above
  the median level based on the local percentile sigma.
  </dd>
  </dl>
  <dl id="l_ngood">
  <dt><b>ngood = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngood' Line='ngood = 5' -->
  <dd>Gaps of undetected pixels along the column direction of length less
  than this amount are also flagged as bad pixels.
  </dd>
  </dl>
  <dl id="l_linterp">
  <dt><b>linterp = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linterp' Line='linterp = 2' -->
  <dd>Mask code for pixels having a bounding good pixel separation which is
  smaller along lines; i.e.  to use line interpolation along the narrower
  dimension.
  </dd>
  </dl>
  <dl id="l_cinterp">
  <dt><b>cinterp = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cinterp' Line='cinterp = 3' -->
  <dd>Mask code for pixels having a bounding good pixel separation which is
  smaller along columns; i.e.  to use columns interpolation along the narrower
  dimension.
  </dd>
  </dl>
  <dl id="l_eqinterp">
  <dt><b>eqinterp = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='eqinterp' Line='eqinterp = 2' -->
  <dd>Mask code for pixels having a bounding good pixel separation which is
  equal along lines and columns.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Ccdmask</b> makes a pixel mask from pixels deviating by a specified
  statistical amount from the local median level.  The input images may be of
  any type but this task was designed primarily for detecting column oriented
  CCD defects such as charge traps that cause bad columns and non-linear
  sensitivities.  The ideal input is a ratio of two flat fields having
  different exposure levels so that all features which would normally flat
  field properly are removed and only pixels which are not corrected by flat
  fielding are found to make the pixel mask.  A single flat field may also be
  used but pixels of low or high sensitivity may be included as well as true
  bad pixels.
  </p>
  <p>
  The input image is first subtracted by a moving box median.  The median is
  unaffected by bad pixels provided the median size is larger that twice
  the size of a bad region.  Thus, if 3 pixel wide bad columns are present
  then the column median box size should be at least 7 pixels.  The median
  box can be a single pixel wide along one dimension if needed.  This may be
  appropriate for spectroscopic long slit data.
  </p>
  <p>
  The median subtracted image is then divided into blocks of size
  <i>nclsig</i> by <i>nlsig</i>.  In each block the pixel values are sorted and
  the pixels nearest the 30.9 and 69.1 percentile points are found; this
  would be the one sigma points in a Gaussian noise distribution.  The
  difference between the two count levels divided by two is then the local
  sigma estimate.  This algorithm is used to avoid contamination by the bad
  pixel values.  The block size must be at least 10 pixels in each dimension
  to provide sufficient pixels for a good estimate of the percentile sigma.  The
  sigma uncertainty estimate of each pixel in the image is then the sigma
  from the nearest block.
  </p>
  <p>
  The deviant pixels are found by comparing the median subtracted residual to
  a specified sigma threshold factor times the local sigma above and below
  zero (the <i>lsigma</i> and <i>hsigma</i> parameters).  This is done for
  individual pixels and then for column sums of pixels (excluding previously
  flagged bad pixels) from two to the number of lines in the image.  The sigma
  of the sums is scaled by the square root of the number of pixels summed so
  that statistically low or high column regions may be detected even though
  individual pixels may not be statistically deviant.  For the purpose of
  this task one would normally select large sigma threshold factors such as
  six or greater to detect only true bad pixels and not the extremes of the
  noise distribution.
  </p>
  <p>
  As a final step each column is examined to see if there are small
  segments of unflagged pixels between bad pixels.  If the length
  of a segment is less than that given by the <i>ngood</i> parameter
  all the pixels in the segment are also marked as bad.
  </p>
  <p>
  The bad pixel mask is created with good pixels identified by zero values
  and the bad pixels by non-zero values.
  The nearest good pixels along the columns and lines for
  each bad pixel are located and the separation along the columns and lines
  between those pixels is computed.  The smaller separation is used to select
  the mask value.  If the smaller separation is along lines the <i>linterp</i>
  value is set, if the smaller separation is along columns the <i>cinterp</i>
  value is set, and if the two are equal the <i>eqinterp</i> value is set.
  The purpose of this is to allow interpolating across bad pixels using the
  narrowest dimension.  The task <b>fixpix</b> can select the type of pixel
  replacement to use for each mask value.  So one can chose, for example,
  line interpolation for the linterp values and the eqinterp values, and
  column interpolation for the cinterp values.
  </p>
  <p>
  In addition to this task, pixel mask images may be made in a variety of
  ways.  Any task which produces and modifies image values may be used.  Some
  useful tasks are <b>imexpr, imreplace, imcopy, text2mask</b> and
  <b>mkpattern</b>.  If a new image is specified with an explicit <span style="font-family: monospace;">".pl"</span>
  extension then the pixel mask format is produced.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Two flat fields of exposures 1 second and 3 seconds are taken,
  overscan and zero corrected, and trimmed.  These are then used
  to generate a CCD mask.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith flat1 / flat2 ratio
  cl&gt; ccdmask ratio mask
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_CCDMASK">
  <dt><b>CCDMASK V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDMASK' Line='CCDMASK V2.11' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imreplace, imexpr, imcopy, imedit, fixpix, text2mask
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
