.. _gcombine:

gcombine: Combine a set of GEIS images into one image
=====================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  gcombine input output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A set of multigroup format (GEIS) images, or, a set of OIF images as a
  special case of GEIS images having only one group, are combined by weighted 
  averaging or medianing.  Pixels may be rejected from the combining by 
  using masks, threshold levels, and rejection algorithms.  The images 
  must be properly scaled to a common exposure level and flux offset
  to a common mean zero level before rejection (except for thresholding) 
  and combining.  
  </p>
  <p>
  The input images to be combined are specified by a list.  The images must 
  all have the same number of groups, dimensions, and sizes.
  </p>
  <p>
  A list of input mask images, specified by the `masks' parameter, can be used
  to mask bad pixels before thresholding and rejection operations. The 
  mask images should have the same number of groups, dimensionality, and 
  size as the input images. A good example of the mask image is a DQF file 
  associated with the HST science data. We consider masks as a boolean
  type, i.e., a mask value of zero indicates the pixel is good, while
  any non-zero mask value indicates the pixel should be excluded.
  </p>
  <p>
  A list of input error images, specified by the `errmap' parameter, can
  be used for the `errclip' algorithm and to compute the pixel-wise weights
  when the parameter, `weight', is chosen as <span style="font-family: monospace;">"pixelwise"</span>. The input error 
  images should have the same number of groups, dimensionality, and 
  size as the input images.
  </p>
  <p>
  The parameter `groups' may  be used to specify a range of groups.
  The default value of `groups' is set to <span style="font-family: monospace;">"*"</span> indicating combining
  will be done for all groups of images.  A group range may be
  specified by a set of three integers, indicating the beginning
  group, the ending group, and the increment, e.g., 3-11x2 meaning a
  range of groups starting from group No. 3 through group No. 11 with
  a step of 2 (note: a default step is 1).  Several ranges of groups
  may be specified as range lists separated by a delimiter, i.e., a
  <span style="font-family: monospace;">","</span> or a blank. This range list, however, will be overridden if the
  input file(s) itself already includes a group specification. 
  </p>
  <p>
  The output image header is a copy of the first image in the combined set.
  In addition, the number of images combined is recorded under the keyword
  NCOMBINE, image header keywords selected by the `expname' and `darkname' 
  parameters are updated as an average of the input header keywords, 
  and some information produced in the log file is also put into the image 
  header HISTORY records. The output pixel type is set by the parameter 
  `outtype'.  If left blank then the input datatype of highest precision 
  is used. 
  </p>
  <p>
  One can use the parameter, `rej_cnt', to specify an output <span style="font-family: monospace;">"rejection 
  count"</span> image. This image counts the number of points rejected by
  masking, thresholding and rejection algorithms altogether at each
  pixel of the output combined image. When all the points are rejected
  at a given pixel of the output image, the value of the corresponding 
  pixel in the `rej_cnt' image is equal to the number of input images.
  In this case, and only in this case, a blank value defined by the 
  parameter `blank', will be assigned to that pixel and that pixel in the 
  output image is considered being bad.
  </p>
  <p>
  The 'rej_list' parameter can be used to generate a set of <span style="font-family: monospace;">"rejection
  images"</span>. Each rejection image contains information about what pixels were
  rejected in the corresponding input image. A rejected pixel is signaled
  with the value zero; an accepted pixel is signaled with the value 32767.
  These particular values were chosen to support the DQ file building
  operation in task 'mscombine', and can be converted to any desired 
  value using task 'imcalc' on the rejection image.
  </p>
  <p>
  The parameter `out_err' can be used to specify an output error image. 
  This error image contains the estimated error in the average or median
  of the combined image.
  </p>
  <p>
  An outline of the steps taken by the program is given below and the
  following sections elaborate on the steps.
  </p>
  <div class="highlight-default-notranslate"><pre>
  o   Set the input image scales, flux offsets, and weights
  o   Write the log file output and put it into the output image header
      history
  </pre></div>
  <p>
  For each output image line:
  </p>
  <div class="highlight-default-notranslate"><pre>
  o   Get input image lines
  o   Reject masked pixels
  o   Reject pixels outside the threshold limits
  o   Reject pixels using the specified algorithm
  o   Combine remaining pixels using the weighted average or median
  o   Compute errors of remaining pixels about the combined values
  o   Write the combined image, rej_cnt image, and error image lines.
  </pre></div>
  <p>
  SCALES, ZEROS, AND WEIGHTS
  </p>
  <p>
  In order to combine images with rejection of pixels based on deviations
  from some average or median they must be scaled to a common level.  
  This is done as shown in the following equation:
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  d(i) = D(i) / S(i) - Z(i),                              (1)
  </pre></div>
  <p>
  where d(i) is the scaled intensity, D(i) the original intensity, S(i)
  the scale factor, and Z(i) the zero level offset for the i'th image.
  The scale factor is normalized to the mean of the scales, i.e.,
  </p>
  <div class="highlight-default-notranslate"><pre>
  S(i) = S_o(i) / &lt;S_o&gt;,                                  (2)
  </pre></div>
  <p>
  where S_o(i) is the scale factor specified by the parameter, `scale',
  for the i'th image, and &lt;S_o&gt; is the mean of them. The zero offset is
  given as
  </p>
  <div class="highlight-default-notranslate"><pre>
  Z(i) = Z_o(i) / S(i) - &lt;Z&gt;,                             (3)
  </pre></div>
  <p>
  where Z_o(i) is the zero specified by the parameter, `zero', for the i'th
  image, and &lt;Z&gt; = &lt;Z_o / S&gt; is taken as the mean sky level.
  </p>
  <p>
  The parameters, `scale' and `zero' may take the values <span style="font-family: monospace;">"none"</span> for no scaling
  or zeroing, <span style="font-family: monospace;">"mode"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mean"</span> to scale by statistics of the 
  image section, <span style="font-family: monospace;">"exposure"</span> (for intensity scaling only) to scale by the 
  exposure time keyword in the image header, any other image header keyword 
  specified by the keyword name prefixed by the character <span style="font-family: monospace;">'!'</span>, and the 
  name of a file containing the scale factors for the input image prefixed 
  by the character <span style="font-family: monospace;">'@'</span>. 
  </p>
  <p>
  Examples of the possible parameter values are shown below where
  <span style="font-family: monospace;">"myval"</span> is the name of an image header keyword and <span style="font-family: monospace;">"scales.dat"</span> is
  a text file containing a list of scale factors.
  </p>
  <div class="highlight-default-notranslate"><pre>
  scale = none            No scaling
  zero = mean             Intensity offset by the mean
  scale = exposure        Scale by the exposure time
  zero = !myval           Intensity offset by an image keyword
  scale = @scales.dat     Scales specified in a file
  </pre></div>
  <p>
  The image statistics are computed by sampling a uniform grid of points with
  the smallest grid step that yields less than 500x500 pixels; sampling is used
  to reduce the time needed to compute the statistics.  If one wants to
  restrict the sampling to a region of the image the `statsec' parameter
  is used.  This parameter has the standard syntax for an image section.
  The statistics are as indicated by their names. Masked pixels are excluded 
  from the computations as well as during the rejection and combining operations.
  </p>
  <p>
  The <span style="font-family: monospace;">"exposure"</span> option in the intensity scaling uses the value of the
  image header keyword specified by the `expname' keyword.  As implied
  by the parameter name, this is typically the image exposure time since
  intensity levels are linear with the exposure time in CCD detectors.
  Note that the exposure keyword is also updated in the final image
  as the average of the input values.  Thus, if one wants to
  use a nonexposure time keyword and keep the exposure time updating
  feature, the image header keyword syntax is available; i.e. !&lt;keyword&gt;.
  </p>
  <p>
  Scaling values may be defined as a list of values in a text file.  The file
  name is specified by the standard @file syntax.  The list consists of one
  value per line.  The order of the list is assumed to be the same as the
  order of the input images.  It is a fatal error if the list is incomplete
  and a warning if the list appears longer than the number of input images.
  Because the scale and zero levels are adjusted, only the relative
  values are important.
  </p>
  <p>
  If `combine' = <span style="font-family: monospace;">"average"</span> and `weight' is NOT specified as <span style="font-family: monospace;">"pixelwise"</span>,
  a <span style="font-family: monospace;">"uniform"</span> weighting scheme is assumed and the uniform weights
  are specified in the same way as the scale factors.  If `combine' = 
  <span style="font-family: monospace;">"average"</span> but `weight' = <span style="font-family: monospace;">"pixelwise"</span>, then the weight is the reciprocal of
  the sigma**2, where the sigma is the scaled error taken from the input error
  image. In addition the NCOMBINE keyword, if present, will be used in 
  the uniform weights. The uniform weights, normalized to unity, are printed in 
  the log output, while only the input error image names are logged when
  the pixel-wise weighting scheme is chosen.
  </p>
  <p>
  These weights are only used for the final weighted average and output
  error image. They are not necessarily the same as those might be used  
  in the various rejection algorithms.
  </p>
  <p>
  MASKS
  </p>
  <p>
  The mask images specified by the parameter, `masks', are always treated as
  of a boolean type: a zero value indicates a good pixel, while all non-zero
  mask values indicate a bad pixel.
  </p>
  <p>
  THRESHOLD REJECTION
  </p>
  <p>
  In addition to rejecting masked pixels, pixels in the unscaled input
  images which are below or above the thresholds given by the parameters
  `lthreshold' and `hthreshold' are rejected.  Values of INDEF
  mean that no threshold value is applied.  Threshold rejection may be used
  to exclude very bad pixel values or as an alternative way of masking
  images.  In the latter case one can use a task like `imedit', `imreplace',
  or `stsdas.toolbox.imgtools.pixedit' to set parts of the images to be 
  excluded to some very low or high magic value.
  </p>
  <p>
  REJECTION ALGORITHMS
  </p>
  <p>
  The `reject' parameter selects a type of rejection operation to
  be applied to pixels not masked or thresholded.  If no rejection
  operation is desired the value <span style="font-family: monospace;">"none"</span> is specified.
  </p>
  <p>
  MINMAX
  A specified fraction of the highest and lowest pixels are rejected.
  The fraction is specified as the number of high and low pixels, the
  `nhigh' and `nlow' parameters, when data from all the input images
  surviving masking and thresholding.  If pixels have been rejected by 
  masking or thresholding, then a matching fraction of the remaining 
  pixels, truncated to an integer, are used.  Thus,
  </p>
  <div class="highlight-default-notranslate"><pre>
  nl = n * nlow/nimages + 0.001
  nh = n * nhigh/nimages + 0.001
  </pre></div>
  <p>
  where n is the number of pixels surviving masking and
  thresholding, nimages is the number of input images, nlow and nhigh
  are task parameters and nl and nh are the final number of low and
  high pixels rejected by the algorithm.  The factor of 0.001 is to
  adjust for rounding of the ratio.
  </p>
  <p>
  As an example with 10 input images and specifying two low and one high
  pixels to be rejected, the fractions to be rejected are 0.2 and 0.1
  and the number rejected as a function of n is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  n   0  1  2  3  4  5  6  7  8  9 10
  nl  0  0  0  0  0  1  1  1  1  1  2
  nh  0  0  0  0  0  0  0  0  0  0  1
  </pre></div>
  <p>
  CCDCLIP
  If the noise characteristics of input images are known to be well represented
  by a noise model for a CCD with known read out noise, gain, and
  sensitivity noise parameters, the sigma in the data can be evaluated 
  based on the noise model. A noise model can be described by
  </p>
  <div class="highlight-default-notranslate"><pre>
  sigma = [(rn/g) ** 2 + &lt;I&gt;/g + (s*&lt;I&gt;) ** 2] ** 1/2, (4)
  </pre></div>
  <p>
  where &lt;I&gt; is the estimated signal intensity, rn the read out noise in 
  electrons, g the gain in electrons per data value, s the sensitivity noise 
  given as a fraction, and ** is the exponentiation operator. To get the
  best estimate of the <span style="font-family: monospace;">"true"</span> signal level, one uses the average (`mclip' 
  = no) or the median (`mclip' = yes) scaled back to the original levels
  as the expected &lt;I&gt; for the un-scaled images in Eq. (4). This yields
  an estimate of the sigma in the un-scaled data (sigma_original). 
  Then the sigma in the data of the scaled images will be 
  (sigma_original / scale).
   
  The task `wfpc.noisemodel' provides a way to demonstrate how a noise model
  would fit the data with user-specified parameters (though that task expresses 
  the read out noise in data numbers and the sensitivity noise parameter as a 
  percentage). 
  </p>
  <p>
  The read out noise is specified by the `rdnoise' parameter.  The value
  may be a numeric value to be applied to all the input images or an image
  header keyword containing the value for each image.  Similarly, the
  parameter `gain' specifies the gain as either a value or image header
  keyword and the parameter `snoise' specifies the sensitivity
  noise parameter as either a value or image header keyword.
  </p>
  <p>
  The algorithm operates on each output pixel independently.  It starts by
  taking the median or unweighted average (excluding the minimum and maximum)
  of the unrejected pixels provided there are at least two input pixels.  The
  expected sigma is computed as above.  All pixels with deviations more
  than `lsigma' times this sigma below or `hsigma' times this sigma
  above the median or average are rejected.  The process is then iterated
  until no further pixels are rejected.  If the average is used as the
  estimator of the true value then after the first round of rejections the
  highest and lowest values are no longer excluded.
  </p>
  <p>
  In the case of only two images to combine, special care has been taken.
  It is expected that all values of the good pixels in the two images 
  correlate strongly with each other within the uncertainties in these
  data values, while possible outliers, if they are assumed not to appear
  at the same location of the two images, would fall far away from this 
  correlation line. This fact leads us to believe that outliers can be 
  identified by their large deviations from the correlation line. Instead
  of drawing scatter diagrams, the algorithm operates based on the
  pixel values and their noises. If both the unscaled pixel values are
  within threshold times of the read out noise, no rejection needs to be
  done. If both of them are below `lsigma' times the readout noise, or 
  one of them is above `hsigma' and the other is below `lsigma' times of 
  the readout noise, the one with the larger absolute value is excluded.  
  If both of them are above `lsigma' times the readout noise, the
  deviation of the larger one from the smaller one is compared to the
  expected noise, which accounts for the errors in both of them.
  If this deviation exceeds the `hsigma' times of the expected noise, 
  the larger one is rejected.  NB: Since the information in neighboring
  pixels around a pixel under test is utilized only in a global way as shown
  by the correlation line, there may be chances that a bad pixel is not
  rejected, or a possibly better pixel (with a larger value) is rejected 
  while the other with a smaller value but above `lsigma' times of the
  readout noise, which could merely be a data dropout, may be retained.
  However these chances, especially of the latter case, are expected to
  be very slim, users are warned about the possiblity.
  </p>
  <p>
  If there are different CCD noise parameters for the input images
  (as might occur using the image header keyword specification) then
  the sigmas are computed for each pixel from each image using the
  same estimated true value.
  </p>
  <p>
  After rejection the number of retained pixels is checked against the
  `nkeep' parameter.  If there are fewer pixels retained than specified
  by this parameter, the pixels with the smallest absolute deviations
  are added back.  If there is more than one pixel with the same
  absolute deviation (for example the two pixels about an average
  or median of two will have the same deviations) they are all added
  back even if this means more than `nkeep' pixels are retained.
  Note that the `nkeep' parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  There are occasions when bright stars appear in the images, the CCDCLIP
  might cut off the tops of the bright stars especially if the images
  are shifted by a fraction of a pixel.  This difficulty in distinguishing
  tops of the bright stars from cosmic ray events can somewhat be overcome
  by specifying a non-zero sensitivity noise parameter. 
  </p>
  <p>
  This is the best clipping algorithm to use if the CCD noise parameters are
  adequately known.  The parameters affecting this algorithm are `reject'
  to select this algorithm, `mclip' to select the median or average for
  the center of the clipping, `nkeep' to limit the number of pixels
  rejected, the CCD noise parameters `rdnoise', `gain' and `snoise',
  `lsigma' and `hsigma' to select the clipping thresholds.
  </p>
  <p>
  CCDCRREJ
  This algorithm is identical to <span style="font-family: monospace;">"ccdclip"</span> except that only pixels above
  the average are rejected based on the `hsigma' parameter.  This
  is appropriate for rejecting cosmic ray events and works even with
  two images.
  </p>
  <p>
  RSIGCLIP
  This sigma clipping algorithm computes at each output pixel the median or
  weighted average excluding the highest and lowest values and the robust
  estimate of the sigma about the median or average. 
  </p>
  <p>
  The <span style="font-family: monospace;">"R"</span> in RSIGCLIP stands for <span style="font-family: monospace;">"robust"</span>. One tries to compute a sigma, robust 
  against the effects of unidentified outliers on the estimate of the sigma 
  iteself. The sigma is computed from the data and corrected for the Poisson 
  scaling effect. The final sigma is given by
  </p>
  <div class="highlight-default-notranslate"><pre>
  sig(i)**2 = &lt;sig&gt;**2 * sum [S(i)/&lt;d(i)&gt;] / n *
              S(i)/&lt;d(i)&gt;,                        (5)
  </pre></div>
  <p>
  where &lt;d(i)&gt; is the average of the scaled data, S(i) / &lt;d(i)&gt; is the
  Poisson scaling factor, and the average sigma &lt;sig&gt; is given as
  </p>
  <div class="highlight-default-notranslate"><pre>
  &lt;sig&gt;**2 = sum [w(i) * (d(i) - &lt;d(i)&gt;)**2] /
             sum [w(i)] * n / (n-1),              (6)
  </pre></div>
  <p>
  where w(i) is the weight. The weights for pixels not far from the mean are
  equal to S(i)/&lt;d(i)&gt;, which is Poisson scaling factor used in Eq (5), while
  much smaller weights are assigned to the points farthest from the 
  mean: The weight of S(i)/d(i) is used for points on the high side from 
  the mean, and the weight of 0.001*S(i)/&lt;d(i)&gt; is applied to points on the 
  low side from the mean. An outlier, if present, will get the negligible weight 
  and therefore the least influence on the &lt;sig&gt;**2 and on sig(i)**2. 
  </p>
  <p>
  At least three images are required for the option. The more images one
  has, the better the RSIGCLIP works. 
  </p>
  <p>
  Values deviating from the expected signal level by more than the specified 
  sigma threshold factors are rejected.  These steps are
  repeated, except that after the first time the average includes all values,
  until no further pixels are rejected or there are fewer than two pixels.
  </p>
  <p>
  After rejection the number of retained pixels is checked against the
  `nkeep' parameter.  If there are fewer pixels retained than specified
  by this parameter, the pixels with the smallest absolute deviations
  are added back.  If there is more than one pixel with the same
  absolute deviation (for example the two pixels about an average
  or median of two will have the same deviations) they are all added
  back even if this means more than `nkeep' pixels are retained.
  Note that the `nkeep' parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  The parameters affecting this algorithm are `reject' to select
  this algorithm, `mclip' to select the median or average for the
  center of the clipping, `nkeep' to limit the number of pixels
  rejected, `lsigma' and `hsigma' to select the
  clipping thresholds.
  </p>
  <p>
  RSIGCRREJ
  This algorithm is identical to <span style="font-family: monospace;">"rsigclip"</span> except that only pixels above
  the average are rejected based on the `hsigma' parameter.  This
  is appropriate for rejecting cosmic ray events and works even with
  two images.
  </p>
  <p>
  AVSIGCLIP
  The averaged sigma clipping algorithm assumes that the sigma about the
  median or mean (average excluding the lowest and highest values) is 
  proportional to the square root of the median or mean at each point,
  at least for the un-scaled images.  This is described by the equation:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sig_o**2 = A * I_o,                             (7)
  </pre></div>
  <p>
  where sig_o is the standard deviation, I_o the <i>estimated</i> signal level
  in the un-scaled images, and A the <i>estimated</i> proportionality
  constant. This noise model is valid for images whose values are 
  proportional to the number of photons recorded.  In effect this algorithm 
  estimates a detector gain for each line with no read out noise component when
  information about the detector noise parameters is not known or
  available.  Thus the proportionality constant, A, can be obtained by
  </p>
  <div class="highlight-default-notranslate"><pre>
  A = &lt;sig_o**2 / I_o&gt;,                           (8)
  </pre></div>
  <p>
   
  </p>
  <p>
  The average &lt;&gt; is taken over all pixels in an image line. 
  </p>
  <p>
  After A is obtained, the estimated final sigma is simply given 
  </p>
  <div class="highlight-default-notranslate"><pre>
  sigma_final = A * sqrt {[d(i) + Z(i)] / S(i)}.  (9)
  </pre></div>
  <p>
  	
  Since all points along an image line are used in Eq (8), the unidentified 
  outliers would have somewhat reduced effects on the estimate of the sigma.
  </p>
  <p>
  Pixels with deviations from the mean or median exceeding the specified 
  thresholds times the sigma_final, are rejected.  If any values are rejected 
  the median or mean (this time not excluding the extreme values) is 
  recomputed and further values rejected. 
  </p>
  <p>
  After rejection the number of retained pixels is checked against the
  `nkeep' parameter.  If there are fewer pixels retained than specified
  by this parameter the pixels with the smallest absolute deviations
  are added back.  If there is more than one pixel with the same
  absolute deviation (for example the two pixels about an average
  or median of two will have the same deviations) they are all added
  back even if this means more than `nkeep' pixels are retained.
  Note that the `nkeep' parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  This algorithm works well for even a few input images.  It works better if
  the median is used though this is slower than using the average.  Note that
  if the images have a known read out noise and gain (the proportionality
  factor above) then the <span style="font-family: monospace;">"ccdclip"</span> algorithm is superior.  The two algorithms
  are related in that the average sigma proportionality factor is an estimate
  of the gain.
  </p>
  <p>
  The parameters affecting this algorithm are `reject' to select
  this algorithm, `mclip' to select the median or average for the
  center of the clipping, `nkeep' to limit the number of pixels
  rejected, `lsigma' and `hsigma' to select the
  clipping thresholds.
  </p>
  <p>
  AVSIGCRREJ
  This algorithm is identical to <span style="font-family: monospace;">"avsigclip"</span> except that only pixels above
  the average are rejected based on the `hsigma' parameter.  This
  is appropriate for rejecting cosmic ray events and works even with
  two images.
  </p>
  <p>
  ERRCLIP
  The ERRCLIP algorithm is used when a list of input error images are
  provided. In this case, the noise characteristics of the input images are
  well represented by the noise values stored in each pixels of the error
  images. In other words, the noise is already given on the pixel-by-pixel
  basis. No model is needed any more for estimating the noise. It also becomes
  obvious that the sigma does not have to be estimated from the data, where
  outliers often skew the statistics at the first place.  The trimmed
  mean or median is used to represent the expected signal level.
  </p>
  <p>
  Values deviating from the expected signal level by more than the specified 
  sigma threshold factors are rejected.  These steps are repeated. After
  rejection the number of retained pixels is checked against the
  `nkeep' parameter.  If there are fewer pixels retained than specified
  by this parameter, the pixels with the smallest absolute deviations
  are added back.  If there is more than one pixel with the same
  absolute deviation (for example the two pixels about an average
  or median of two will have the same deviations) they are all added
  back even if this means more than `nkeep' pixels are retained.
  Note that the `nkeep' parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  In the case of only two images to combine, special care has been taken,
  similarly as seen in the CCDCLIP. If both the pixel values are
  within threshold times of their noises, no rejection needs to be
  done. If both of them are below `lsigma' times the noise, or 
  one of them is above `hsigma' and the other is below `lsigma' times of 
  the noise, the one with the larger absolute value is excluded.  
  If both of them are above `lsigma' times the noise, the
  deviation of the larger one from the smaller one is compared to the
  expected noise, which accounts for the errors in both of them.
  If this deviation exceeds the `hsigma' times of the expected noise, 
  the larger one is rejected.
  </p>
  <p>
  The parameters affecting this algorithm are `reject' to select
  this algorithm, `mclip' to select the median or average for the
  center of the clipping, `nkeep' to limit the number of pixels
  rejected, `lsigma' and `hsigma' to select the
  clipping thresholds.
  </p>
  <p>
  ERRCRREJ
  This algorithm is identical to <span style="font-family: monospace;">"errclip"</span> except that only pixels above
  the average are rejected based on the `hsigma' parameter.  This
  is appropriate for rejecting cosmic ray events and works even with
  two images.
  </p>
  <p>
  COMBINING
  </p>
  <p>
  After all the steps of masking pixels, threshold rejection, scaling, 
  and applying a rejection algorithms, the remaining pixels are combined.
  The pixels may be combined by computing the median or by computing a 
  weighted average.
  </p>
  <p>
  OUTPUT ERROR IMAGE
  </p>
  <p>
  An optional output <span style="font-family: monospace;">"error image"</span> may be produced.  The output error is 
  the error in the average or median.  It serves to provide an estimate of
  the noise in the combined image on the pixel to pixel basis, similar to
  the input error image which gives the noise in the input image. 
  </p>
  <p>
  In general, the combined image can be considered to be a weighted average
  of the input data, i.e.,
  </p>
  <div class="highlight-default-notranslate"><pre>
  &lt;I&gt; = Sum [W(i) * I(i)] / Sum [W(i)],                   (10)
  </pre></div>
  <p>
  where W(i) is the weight which should normally be proportional to the
  reciprocal of the variances in the data, and the sums run over all 
  the remaining good pixels. From Eq. (10), the estimated error in the
  resultant image of &lt;I&gt; is given by
  </p>
  <div class="highlight-default-notranslate"><pre>
  sigma_in_mean**2 = Sum {sigma(i)**2 * [D&lt;I&gt;/DI(i)]**2}, (11)
  </pre></div>
  <p>
  where D&lt;I&gt;/DI(i) is the partial derivative of the resultant image with
  respect to the i'th data, and sigma(i) is the uncertainty associated
  with the i'th data. The partial derivatives can be evaluated from Eq. (10).
  If the input error images are available then the sigma (i) is taken 
  directly from these error images. If they are not available, the error
  in the data can be estimated from the input images. If the number of
  images is small, say, less than 10, the sigma(i) is estimated from the 
  noise model corrected for the effects of the scaling.  When the number 
  of images is large enough, or, when the noise model is not available 
  even though the number of images may be small, a weighted average sigma 
  is computed from the good pixels. 
  </p>
  <p>
  We emphasize that an error image associated with any image is considered
  more favorable than a noise model in keeping track of the noise
  characteristics of the image. The noise model is, however, a very
  good alternative to the error image when either the error image is
  not available or capacity to store an extra error image is a concern. 
  </p>
  <p>
  A good estimate of the noise in the combined image can also be useful
  if one is forced to combine a large set of images in more than one
  pass.  In this case, the noise images generated at each pass, when combining
  the subsets of the input images separately, can be used as the input 
  error images for the next pass of combining the subsets together.  
  We believe that the noise characteristics can be best preserved by 
  means of producing the noise images at every stage of the operations. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>List of input images to combine. They can be either single group (OIF) or
  multi-group (GEIS) images, but the number of groups, the dimensionality
  and the size of all the input images must be consistent with each other.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string]' -->
  <dd>Output combined image.
  </dd>
  </dl>
  <dl>
  <dt><b>(groups = <span style="font-family: monospace;">"*"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(groups = "*") [string]' -->
  <dd>List of ranges of groups in the input images. The default is <span style="font-family: monospace;">"*"</span>, meaning
  to operate for all groups. Any other ranges of groups can also be
  specified (for legitimate range specifications, see the DESCRIPTION section)
  </dd>
  </dl>
  <dl>
  <dt><b>(masks = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(masks = "") [string]' -->
  <dd>List of input mask images.
  </dd>
  </dl>
  <dl>
  <dt><b>(errmap = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(errmap = "") [string]' -->
  <dd>List of input error images. 
  </dd>
  </dl>
  <dl>
  <dt><b>(rej_cnt = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rej_cnt = "") [string]' -->
  <dd>Output <span style="font-family: monospace;">"rejection counts"</span> image.  This image indicates how many points are
  rejected at a given pixel of the combined image.
  </dd>
  </dl>
  <dl>
  <dt><b>(rej_list = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rej_list = "") [string]' -->
  <dd>List with output rejection images. This list must be paired with the input
  list.
  </dd>
  </dl>
  <dl>
  <dt><b>(out_err = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(out_err = "") [string]' -->
  <dd>Output error image to indicate the uncertainties in the combined image.
  </dd>
  </dl>
  <dl>
  <dt><b>(nsmod_e = yes) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nsmod_e = yes) [bool]' -->
  <dd>Use noise models to compute output <span style="font-family: monospace;">"error"</span> image when the number of input
  images is less than 10?
  </dd>
  </dl>
  <dl>
  <dt><b>(logfile = <span style="font-family: monospace;">"STDOUT"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(logfile = "STDOUT") [string]' -->
  <dd>Output log file.  If it is an empty string then no log information will be
  produced. The special filename <span style="font-family: monospace;">"STDOUT"</span> prints log information to the screen.
  </dd>
  </dl>
  <dl>
  <dt><b>(reject = <span style="font-family: monospace;">"none"</span>) </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(reject = "none") ' -->
  <dd>[Allowed values: none | minmax | ccdclip | ccdcrrej |
  rsigclip | rsigcrrej | avsigclip | avsigcrrej|
  errclip | errcrrej]
  <br>
  Type of rejection operation performed on the pixels remaining after masking 
  and thresholding.  The algorithms are described in the
  DESCRIPTION section.  The rejection choices are:
  <div class="highlight-default-notranslate"><pre>
        none - No rejection
      minmax - Reject the nlow and nhigh pixels
     ccdclip - Reject pixels using CCD noise models
    ccdcrrej - Reject only positively deviant pixels using noise models
    rsigclip - Reject pixels using a robust sigma clipping algorithm
   rsigcrrej - Reject only positively deviant pixels using robust sigmas
   avsigclip - Reject pixels using an averaged sigma clipping algorithm
  avsigcrrej - Reject only positively deviant pixels using avsigclip
     errclip - Reject pixels using sigma based on input error images
    errcrrej - Reject only positively deviant pixels using error images
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(combine = <span style="font-family: monospace;">"average"</span>) [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(combine = "average") [string] ' -->
  <dd>[Allowed values: average | median]
  <br>
  Type of combining operation performed on the final set of pixels (after
  masking, thresholding, and rejection).  The choices are
  <span style="font-family: monospace;">"average"</span> or <span style="font-family: monospace;">"median"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(weight = <span style="font-family: monospace;">"none"</span>) [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(weight = "none") [string] ' -->
  <dd>[Allowed values: none | pixelwise | mode | median | mean |
  exposure | @&lt;file&gt; | !&lt;keyword&gt;]
  <br>
  Type of weighting scheme used when combine = <span style="font-family: monospace;">"average"</span>. The choices are 
  shown by the allowed values above.  It is important to note that allowed
  weighting schemes, except for <span style="font-family: monospace;">"none"</span>, can be divided into two major 
  categories: one is the <span style="font-family: monospace;">"pixelwise"</span> weighting and all the rest belong to the
  uniform weighting.  While the weights in the uniform weighting scheme are 
  constant for all pixels of each input image, the reciprocal of the variance 
  at a given pixel is used as the weight for that pixel in the pixel-wise 
  (<span style="font-family: monospace;">"pixelwise"</span>) weighting scheme.  In the case of <span style="font-family: monospace;">"pixelwise"</span> weighting, 
  one must specify an input error map with the parameter <span style="font-family: monospace;">"errmap"</span>, 
  associated with each input image.  In the case of uniform weighting, 
  the weights can be the <span style="font-family: monospace;">"mode"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mean"</span> of the 
  specified statistics section, the <span style="font-family: monospace;">"exposure"</span> time, values given in a <span style="font-family: monospace;">"file"</span>,
  or values in a user-specified image header <span style="font-family: monospace;">"keyword"</span>. When specified in a 
  file the weights must be one per line in the order of the input images. 
  When nsmod_w = <span style="font-family: monospace;">"yes"</span>, the choices of <span style="font-family: monospace;">"mode"</span>, <span style="font-family: monospace;">"median"</span>, and <span style="font-family: monospace;">"mean"</span> will 
  mean to use these values for computing a global variance for each of the 
  input images and the reciprocal of the variances will then be used as the 
  weights for the input images.
  <br>
  </dd>
  </dl>
  <dl>
  <dt><b>(nsmod_w = yes) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nsmod_w = yes) [bool]' -->
  <dd>Use the noise model to compute the variances from mode, median or mean for
  uniform weights?
  </dd>
  </dl>
  <dl>
  <dt><b>(outtype = <span style="font-family: monospace;">"r"</span>) [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outtype = "r") [string] ' -->
  <dd>[Allowed values: s | i | l | r | d]
  <br>
  Output image pixel data type. The pixel data types are <span style="font-family: monospace;">"double"</span>, <span style="font-family: monospace;">"real"</span>,
  <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"integer"</span>, and <span style="font-family: monospace;">"short"</span> with highest precedence first. If none is 
  specified then the highest precedence data type of the input images is used.
  </dd>
  </dl>
  <dl>
  <dt><b>(blank = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(blank = 0.) [real]' -->
  <dd>Output value to be used when all points are considered as bad at a given 
  pixel of the combined image.
  </dd>
  </dl>
  <dl>
  <dt><b>(scale = <span style="font-family: monospace;">"none"</span>) [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(scale = "none") [string] ' -->
  <dd>[Allowed values: none | mode | median | mean |
  exposure | @&lt;file&gt; | !&lt;keyword&gt;]
  <br>
  Scaling factor to bring the input images to a common exposure level.  The 
  choices are <span style="font-family: monospace;">"none"</span>, dividing by the <span style="font-family: monospace;">"mode"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mean"</span> of the 
  specified statistics section, dividing by the <span style="font-family: monospace;">"exposure"</span> time in the image 
  header, dividing by the values in a specified <span style="font-family: monospace;">"file"</span>, or dividing by values 
  in a user-specified image header <span style="font-family: monospace;">"keyword"</span>.  When specified in a file the 
  scales must be one per line in the order of the input images.
  </dd>
  </dl>
  <dl>
  <dt><b>(zero = <span style="font-family: monospace;">"none"</span>) [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(zero = "none") [string] ' -->
  <dd>[Allowed values: none | mode | median | mean |
  @&lt;file&gt; | !&lt;keyword&gt;]
  <br>
  Zero flux offset to bring the input images to a common zero level.  The 
  choices are <span style="font-family: monospace;">"none"</span>, shift by the <span style="font-family: monospace;">"mode"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mean"</span> of the specified 
  statistics section, shift by values given in a <span style="font-family: monospace;">"file"</span>, or shift by values 
  in a user-specified image header <span style="font-family: monospace;">"keyword"</span>.  When specified in a file the 
  zero values must be one per line in the order of the input images.
  </dd>
  </dl>
  <dl>
  <dt><b>(statsec = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(statsec = "") [string]' -->
  <dd>Section of images to use in computing image statistics for scaling and
  weighting.  If a null section is given then the entire region of the input is
  sampled.
  </dd>
  </dl>
  <dl>
  <dt><b>(expname = <span style="font-family: monospace;">"EXPTIME"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(expname = "EXPTIME") [string]' -->
  <dd>Image header keyword to be used with the exposure scaling and weighting
  options.  Also if an exposure keyword is specified, an <span style="font-family: monospace;">"effective
  exposure time"</span> will be computed and that keyword will be added to the 
  output image. The effective exposure time is defined as an average 
  of the scaled input exposure values.
  </dd>
  </dl>
  <dl>
  <dt><b>(darkname = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(darkname = "") [string]' -->
  <dd>Image header keyword of the dark time.  If a dark time keyword is specified,
  an <span style="font-family: monospace;">"effective dark time"</span> will be computed and that keyword will be added to 
  the output image. The effective dark time is defined as an average of 
  the scaled input dark time values.
  </dd>
  </dl>
  <p style="text-align:center">Algorithm Parameters
  
  </p>
  <dl>
  <dt><b>(lthreshold = INDEF, hthreshold = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lthreshold = INDEF, hthreshold = INDEF) [real]' -->
  <dd>Low and high thresholds (floors and ceilings) to be applied to the input 
  pixels.  This is done before any scaling, rejection, and combining.  
  If they are specified as INDEF, the thresholding will not be applied.
  </dd>
  </dl>
  <dl>
  <dt><b>(nlow = 1,  nhigh = 1) [integer] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nlow = 1,  nhigh = 1) [integer] ' -->
  <dd>The number of low and high pixels to be rejected by the <span style="font-family: monospace;">"minmax"</span> algorithm.
  These numbers are converted to fractions of the total number of input images
  so that if no rejections by masking and thresholding have taken place, 
  the specified number of low and high pixels will be rejected, while if 
  pixels have been rejected by masking and thresholding, then the fraction 
  of the remaining pixels, truncated to an integer, will be used to do
  this operation of the <span style="font-family: monospace;">"minmax"</span> rejection.
  </dd>
  </dl>
  <dl>
  <dt><b>(nkeep = 1) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nkeep = 1) [integer]' -->
  <dd>The minimum number of pixels to retain or the maximum number to reject
  when using the clipping algorithms (ccdclip, crreject, sigclip,
  avsigclip, or errclip).  When given as a positive value, this is the minimum
  number to keep.  When given as a negative value, the absolute value is
  the maximum number to reject.  The latter is in addition to pixels
  rejected by masking and thresholding.
  </dd>
  </dl>
  <dl>
  <dt><b>(mclip = yes) [bool] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(mclip = yes) [bool] ' -->
  <dd>Use the median as the estimate for the true intensity rather than the
  average with high and low values excluded in the <span style="font-family: monospace;">"ccdclip"</span>, <span style="font-family: monospace;">"ccdcrrej"</span>,
  <span style="font-family: monospace;">"rsigclip"</span>, <span style="font-family: monospace;">"rsigcrrej"</span>, <span style="font-family: monospace;">"avsigclip"</span>, <span style="font-family: monospace;">"avsigcrrej"</span>, <span style="font-family: monospace;">"errclip"</span>, and 
  <span style="font-family: monospace;">"errcrrej"</span> algorithms? 
  </dd>
  </dl>
  <dl>
  <dt><b>(lsigma = 3., hsigma = 3.) [real] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lsigma = 3., hsigma = 3.) [real] ' -->
  <dd>Low and high sigma clipping factors for the <span style="font-family: monospace;">"ccdclip"</span>,  <span style="font-family: monospace;">"ccdcrrej"</span>,
  <span style="font-family: monospace;">"rsigclip"</span>, <span style="font-family: monospace;">"rsigcrrej"</span>, <span style="font-family: monospace;">"avsigclip"</span>, <span style="font-family: monospace;">"avsigcrrej"</span>, <span style="font-family: monospace;">"errclip"</span>, and 
  <span style="font-family: monospace;">"errcrrej"</span> algorithms.  After the algorithm estimates a 
  <span style="font-family: monospace;">"sigma"</span>, it will compare the deviation of a pixel value about the average
  or median with the products of (lsigma * sigma) and of (hsigma * sigma) to 
  reject outliers on both ends, except that the <span style="font-family: monospace;">"lsigma"</span> is ignored for the
  various CR rejection algorithms.
  </dd>
  </dl>
  <dl>
  <dt><b>(rdnoise = <span style="font-family: monospace;">"13."</span>, gain = <span style="font-family: monospace;">"7.5"</span>, snoise = <span style="font-family: monospace;">"0.0"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rdnoise = "13.", gain = "7.5", snoise = "0.0") [string]' -->
  <dd>CCD readout noise in electrons, gain in electrons/DN, and sensitivity noise
  as a fraction.  These parameters are needed when (1) the noise model is
  used to compute output error image (nsmod_e = yes); (2) the <span style="font-family: monospace;">"ccdclip"</span> and 
  <span style="font-family: monospace;">"ccdcrrej"</span> rejection algorithms are chosen; (3) the weights are
  computed based on the noise model (nsmod_w = yes).  The values may be 
  either numeric as shown in the above, or an image header keyword,
  which defines the value in the image header.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To average and median images for all groups without any other features:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gcombine obj* avg combine=average weight=none \
  &gt;&gt;&gt; reject=none
  cl&gt; gcombine obj* med combine=median reject=none
  </pre></div>
  <p>
  2.  To reject cosmic rays and combine for groups 2 and 5 respectively
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gcombine obs1,obs2 Obs groups="2,5" reject=ccdcrrej \
  &gt;&gt;&gt; rdnoise=13.0, gain=7.5, snoise=0.1
  </pre></div>
  <p>
  3.  To apply a mask image with good pixels marked with a zero value and
  bad pixels marked with a non-zero value:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gcombine u20ltu0*t.c0h final groups="1-2,4" \
  &gt;&gt;&gt; masks="u20ltu0*t.c1h" combine="median"
  </pre></div>
  <p>
  4.  To scale image by the exposure time and then adjust for varying
  sky brightness and make a weighted average:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gcombine u20ltu0*t.c0h final groups="*" \
  &gt;&gt;&gt; masks="u20ltu0*t.c1h" reject="avsigclip" \
  &gt;&gt;&gt; combine="average" weight="exposure" \
  &gt;&gt;&gt; scale="exposure" zero="mode" mclip="no" \
  &gt;&gt;&gt; expname="EXPTIME" darkname="DARKTIME" \
  &gt;&gt;&gt; statsec="[350:550,220:320]"
  </pre></div>
  <p>
  5.  To combine separately two sets of images listed in @set1 and 
  @set2 first while rejecting bad pixels using the CCDCLIP. And 
  then to combine the resultant two output images, gcom1 and gcom2 
  together to form the final combined image, gcom.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gcombine @set1 gcom1 groups="*" \
  &gt;&gt;&gt; masks="@msk1" out_err="err1" reject="ccdclip" \
  &gt;&gt;&gt; combine="average" weight="exposure" \
  &gt;&gt;&gt; scale="exposure" zero="mode" \
  &gt;&gt;&gt; expname="EXPTIME" darkname="DARKTIME" statsec=""
  
  cl&gt; gcombine @set2 gcom2 groups="*" \
  &gt;&gt;&gt; masks="@msk2" out_err="err2" reject="ccdclip" \
  &gt;&gt;&gt; combine="average" weight="exposure" \
  &gt;&gt;&gt; scale="exposure" zero="mode" \
  &gt;&gt;&gt; expname="EXPTIME" darkname="DARKTIME" statsec=""
  
  cl&gt; gcombine gcom* final groups="*" \
  &gt;&gt;&gt; errmap="err*" reject="none" \
  &gt;&gt;&gt; combine="average" weight="pixelwise" \
  &gt;&gt;&gt; scale="exposure" zero="mode" \
  &gt;&gt;&gt; expname="EXPTIME" \
  &gt;&gt;&gt; darkname="DARKTIME" statsec=""
  </pre></div>
  <p>
  6. In the above example, suppose the first set of images are long
  exposures and the second set are short exposures. Pixels at
  positions of tops of bright sources might have been saturated, but
  the faint, extended features are well revealed. The tops of the
  bright sources are not saturated in the second set, however.
  So one hopes that the final combined image would retain both the
  brightest and the faintest features. To do so, it would be useful 
  to set a proper <span style="font-family: monospace;">"blank"</span> value for the image resulting from combining 
  the first set of long exposure images. Say, one sets the
  <span style="font-family: monospace;">"blank"</span> value equal to -10000.0. In the final pass, one could 
  then use the <span style="font-family: monospace;">"thresholding"</span> operation to set the parameter, 
  <span style="font-family: monospace;">"lthreshold"</span> value to -9999.999. This way, the saturated pixels
  in the long exposure image will be excluded by the <span style="font-family: monospace;">"thresholding"</span>
  operation when combined with the short exposure image. 
  This will ensure that the pixel values of the tops of the 
  final image be only the values taken from the resultant 
  image of the second set of short exposure, which is now scaled to
  have the same exposure level as the first set of long exposure. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gcombine @set1 gcom1 groups="*" \
  &gt;&gt;&gt; masks="@msk1" out_err="err1" reject="ccdclip" \
  &gt;&gt;&gt; combine="average" weight="exposure" \
  &gt;&gt;&gt; blank=-10000.0 scale="exposure" zero="mode" \
  &gt;&gt;&gt; expname="EXPTIME" darkname="DARKTIME" statsec=""
  
  cl&gt; gcombine @set2 gcom2 groups="*" \
  &gt;&gt;&gt; masks="@msk2" out_err="err2" reject="ccdclip" \
  &gt;&gt;&gt; combine="average" weight="exposure" \
  &gt;&gt;&gt; scale="exposure" zero="mode" \
  &gt;&gt;&gt; expname="EXPTIME" darkname="DARKTIME" statsec=""
  
  cl&gt; gcombine gcom* final groups="*" \
  &gt;&gt;&gt; errmap="err*" reject="none" \
  &gt;&gt;&gt; combine="average" weight="pixelwise" \
  &gt;&gt;&gt; scale="exposure" zero="mode" \
  &gt;&gt;&gt; expname="EXPTIME" \
  &gt;&gt;&gt; darkname="DARKTIME" statsec="" \
  &gt;&gt;&gt; lthreshold=-9999.999
  </pre></div>
  <p>
  7.  To combine two images, s1 and s2, using the 
  ERRCLIP algorithm, one can even make noise maps, e1 and e2,
  out of s1 and s2. Put s1 and s2 into @s.lis and e1 and e2
  into @e.lis, then run gcombine with the ERRCLIP. In the following
  it is assumed that the readout noise is 1.73 DN and the gain
  is 7.5.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcalc s1 e1 "if im1 &lt;= 0. then 1.73 else sqrt \
  &gt;&gt;&gt; (im1 / 7.5 + 2.99)"
  cl&gt; imcalc s2 e2 "if im1 &lt;= 0. then 1.73 else sqrt \
  &gt;&gt;&gt; (im1 / 7.5 + 2.99)"
  cl&gt; gcombine @s.lis final errmap="@e.lis" groups="*" \
  &gt;&gt;&gt; reject="errclip" combine="average"  \
  &gt;&gt;&gt; weight="pixelwise" scale="exposure" zero="mode" \
  &gt;&gt;&gt; expname="EXPTIME" statsec="[350:550,220:320]"
  </pre></div>
  </section>
  <section id="s_limitations">
  <h3>Limitations</h3>
  <p>
  This task is currently limited to a maximum number of images (120) which
  may be open at one time, imposed by the IRAF virtual operating system.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The task may fail to produce the expected results in the error and mask
  output files, when the number of input files is exactly 10 and depending
  on particular combinations of input parameters.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by CY Zhang. It was based on the (IRAF V2.10) 
  'images.imcombine' task written by F. Valdes (NOAO), the STSDAS 'wfpc.combine'
  task by R. Shaw (STScI), the STSDAS 'wfpc.crrej' by JC Hsu (STScI), and the 
  'mdscombine' task by K. Ratnatunga (JHU). The 
  'gcombine' task is enhanced to be able to deal with the GEIS images more 
  flexibly. In addition to the masking operation using mask images, including 
  the DQF images for HST data, error maps can be used to reject bad pixels 
  with the ERRCLIP algorithm, and to do <span style="font-family: monospace;">"pixel-wise"</span> weighted average. The 
  RSIGCLIP algorithm in 'gcombine' is enhanced to be able to obtain the robust
  estimates of the mean and the clipping sigma.
  To support the 'mstools.mscombine' task, 'gcombine' was enhanced by
  I. Busko (STScI) to generate a set of <span style="font-family: monospace;">"rejection images"</span>.
  </p>
  </section>
  <section id="s_help">
  <h3>Help</h3>
  <p>
  For assistance using this or any other tasks, please contact help@stsci.edu 
  or call the help desk at 410-338-1082.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  images.combine, mstools.mscombine, wfpc.combine, wfpc.crrej, 
  wfpc.noisemodel, xtools.ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'LIMITATIONS' 'BUGS' 'REFERENCES' 'HELP' 'SEE ALSO'  -->
  
