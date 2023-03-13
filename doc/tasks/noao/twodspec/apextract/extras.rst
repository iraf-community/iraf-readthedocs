.. _extras:

extras: Information about the extra information in 3D images
============================================================

**Package: apextract**

.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  When one dimensional spectra are extracted by the tasks in the
  <b>apextract</b> package the user may specify that additional
  extra associated information be extracted at the same time.  This
  information is produced when the <i>extras</i> parameter is <span style="font-family: monospace;">"yes"</span>.
  </p>
  <p>
  The associated information is recorded as additional <span style="font-family: monospace;">"bands"</span> (the IRAF term
  for the third dimension of a three dimensional image) of the output
  extracted spectral image.  Extracted spectra are currently stored as IRAF
  images with dispersion information given in the image header.  The
  image axes for such images are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  1 (columns) - dispersion axis
  2 (lines)   - spectrum axis (each line is a separate spectrum)
  3 (bands)   - extras axis (each band is associated data)
  </pre></div>
  <p>
  The lengths of the second and third axes, that is the number of
  lines and bands, may be one or more.  If there is only one band
  the image will be two dimensional and if there is only one line
  and one band the image will be one dimensional.  Note that the
  <i>format</i> parameter controls whether multiple apertures are
  written to separate images or to a single image.  Thus, if
  the format is <span style="font-family: monospace;">"onedspec"</span> this means that the second dimension
  will always be of length one and, if the <i>extras</i> parameter
  is no, the output images will be one dimensional.
  </p>
  <p>
  The associated data in the image bands depends on which extraction
  options are performed.  The various types of data are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  The primary spectrum flux values.
  Simple aperture sum if variance weighting or cleaning was done.
  Background spectrum if background subtraction was done.
  Sigma spectrum if variance weighting or cleaning was done.
  </pre></div>
  <p>
  The primary spectrum is always the first band and will be the cleaned
  and/or variance weighted and/or background subtracted spectrum.  The
  simple aperture sum spectrum allows comparing against the results of the
  variance weighting or pixel rejection options.  When background
  subtraction is performed the subtracted background is recorded in
  one of the bands.  When variance weighting or pixel rejection is
  performed the software generates an estimate of the uncertainty
  in the extracted flux as a sigma.
  </p>
  <p>
  The identity of the various bands is given by the image header
  keywords BANDIDn (where n is the band number).  This also serves
  to document which extraction options were used.
  </p>
  <p>
  For more information get help under the topic <span style="font-family: monospace;">"apextract.package"</span>.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apextract.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'SEE ALSO'  -->
  
