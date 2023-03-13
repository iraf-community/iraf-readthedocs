.. _sflip:

sflip: Flip data and/or dispersion coordinates in spectra
=========================================================

**Package: specred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sflip input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images containing spectra to be flipped.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Matching list of output image names for flipped spectra.
  If no list is specified then the flipped spectra will replace the input
  spectra.  If the output image name matching an input image name is the
  same then the flipped spectrum will replace the original spectrum.
  </dd>
  </dl>
  <dl id="l_coord_flip">
  <dt><b>coord_flip = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coord_flip' Line='coord_flip = no' -->
  <dd>Flip the dispersion coordinates?  If yes then the relationship between the
  logical pixel coordinates and the dispersion coordinates will be reversed so
  that the dispersion coordinate of the first pixel of the output image will
  correspond to the coordinate of the last pixel in the input image and
  vice-versa for the other endpoint pixel.  The physical coordinates
  will also be flipped.  Only the coordinate system along the dispersion
  axis is flipped.
  </dd>
  </dl>
  <dl id="l_data_flip">
  <dt><b>data_flip = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='data_flip' Line='data_flip = yes' -->
  <dd>Flip the order of the data pixels as they are stored in the image along
  the dispersion axis?  If yes then the first pixel in the input spectrum
  becomes the last pixel in the output spectrum along the dispersion
  axis of the image.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The dispersion coordinate system and/or the data in the spectra specified
  by the input list of images are flipped and stored in the matching output
  image given in the output list of images.  If the output image list is left
  blank or an output image name is the same as an input image name then the
  operation is done so that the flipped spectra in the image replace the
  original spectra.  All of the supported spectrum types are allowed; one
  dimensional images, collections of spectra in multispec format, and two and
  three dimensional spatial spectra in which one axis is dispersion.  In all
  cases the flipping affects only the dispersion axis of the image as
  specified by the DISPAXIS header keyword or the <span style="font-family: monospace;">"dispaxis"</span> parameter.  The
  parameters <i>coord_flip</i> and <i>data_flip</i> select whether the
  coordinate system and data are flipped.  If neither operation is selected
  then the output spectra will simply be copies of the input spectra.
  </p>
  <p>
  Flipping of the coordinate system means that the relation between
  <span style="font-family: monospace;">"logical"</span> pixel coordinates (the index system of the image array)
  and the dispersion and physical coordinate systems is reversed.
  The dispersion coordinate of the first pixel in the flipped spectrum
  will be the same as the dispersion coordinate of the last pixel
  in the original spectrum and vice-versa for the other endpoint.
  </p>
  <p>
  Flipping of the data means that the order in which the pixels are stored
  in the image file is reversed along the image axis corresponding to
  the dispersion.
  </p>
  <p>
  While flipping spectra seems simple there are some subtleties.  If
  both the coordinate system and the data are flipped then plots of
  the spectra in which the dispersion coordinates are shown will appear
  the same as in the original spectra.  In particular the coordinate
  of a feature in the spectrum will remain unchanged.  In contrast
  flipping either the coordinate system or the data will cause features
  in the spectrum to move to opposite ends of the spectrum relative
  to the dispersion coordinates.
  </p>
  <p>
  Since plotting programs often plot the dispersion axis in some standard way
  such as increasing from left to right, flipping both the dispersion
  coordinates and the data will produce plots that look identical even though
  the order of the points plotted will be reversed.  Only if the spectra are
  plotted against logical pixel coordinates will a change be evident.  Note
  also that the plotting programs themselves have options to reverse the
  displayed graph.  So if all one wants is to reverse the direction of
  increasing dispersion in a plot then physically flipping of the spectra is
  not generally necessary.
  </p>
  <p>
  Flipping of both the coordinate system and the data is also equivalent
  to using an image section with a reversed axis.  For example
  a one dimensional spectrum can be flipped in both dispersion coordinates
  and data pixel order by
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcopy spec1[-*] spec2
  </pre></div>
  <p>
  Higher dimensional spectra need appropriate dimensions in the image
  sections.  One advantage of <b>sflip</b> is that it will determine the
  appropriate dispersion axis itself.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  In the following the spectra can be one dimensional, multispec,
  long slit, or spectral data cubes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sflip spec1 spec1f              # Flip data to new image
  cl&gt; sflip spec1 spec1               # Flip data to same image
  cl&gt; sflip spec1 spec1f coord+ data- # Flip coordinates and not data
  cl&gt; sflip spec1 spec1f coord+       # Flip both coordinates and data
  cl&gt; sflip spec* f//spec*            # Flip a list of images
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SFLIP">
  <dt><b>SFLIP V2.10.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SFLIP' Line='SFLIP V2.10.4' -->
  <dd>New in this release.  Note that the V2.9 SFLIP was different in that
  it was script which simply flipped the data.  Coordinate systems were
  not handled in the same way.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy, scopy, dispcor, sapertures
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
