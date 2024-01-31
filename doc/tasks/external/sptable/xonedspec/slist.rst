.. _slist:

slist: List spectrum header parameters
======================================

**Package: xonedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  slist images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images to be listed.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be selected from the images for listing.  A null
  list selects all apertures.  See <b>ranges</b> for the syntax of
  this list.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>If set to yes, then a multiline listing of the header elements is given.
  If set to no, then a single line per spectrum is given.  The contents
  of the listing depend on the format.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task lists header information from apertures in a list of input
  images.  There is a short one line per spectrum listing and a more
  extended listing selected by the <i>long_header</i> parameter.
  </p>
  <p>
  In both short and long outputs the aperture information consists of
  lines with the following whitespace separated fields: the image line,
  the aperture number, the beam number, the dispersion type, the
  wavelength of the first pixel, the wavelength interval per pixel,
  the number of valid pixels, and the aperture title.  The dispersion
  type is an integer with a value of -1 if not dispersion corrected,
  0 if dispersion corrected to a linear wavelength sampling, 1 if
  dispersion corrected to a log wavelength sampling, and 2 if dispersion
  corrected to a nonlinear sampling.  The wavelength per pixel is
  an approximation based on the wavelength endpoints divided by the
  number of pixels in the case of a nonlinear dispersion function.
  Also the wavelengths refer to the actual pixels taking any image sections
  into account and so may differ from the coordinate system information in
  the header which is defined for the original physical coordinates.
  The aperture titles may be identical with the image title if individual
  aperture titles are not defined.
  </p>
  <p>
  In the short output format the image title is given first followed
  by the above described information.  This format is compact and
  suitable for easy use in other programs (see the example below).
  The long output format is blocked by image and gives the image name
  and title on the first line, the exposure time, universal time,
  and siderial time on the second line, the right ascention, declination,
  hour angle, and airmass on the third line, and then the individual
  aperture informations on the remaining lines.  If some of the header
  information is missing a value of INDEF is printed.  The keywords used
  are EXPTIME/ITIME/EXPOSURE (in that order) for the exposure time,
  and UT, ST, RA, DEC, HA, and AIRMASS for the remaining values.
  </p>
  <p>
      demoobj.ms: Hydra artificial image
  	EXPTIME = 2133.33 UT = 9:10:09.0    ST = 20:09:34.0
  	RA = 1:34:02.00   DEC = 30:37:03.0  HA = INDEF    AIRMASS = 2.3
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  List short header for an object and arc from a Hydra multifiber reduction
  for fibers 36 to 39.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; slist demoobj.ms,demoarc1.ms ap=36-39
  demoobj.ms 1 37 0 0 5785.85 6.140271 256 Sky fiber
  demoobj.ms 2 38 1 0 5785.85 6.140271 256 SS313
  demoobj.ms 3 39 1 0 5785.85 6.140271 256 SS444
  demoarc1.ms 1 36 2 0 5785.85 6.140271 256 Arc fiber
  demoarc1.ms 2 37 0 0 5785.85 6.140271 256 Sky fiber
  demoarc1.ms 3 38 1 0 5785.85 6.140271 256 SS313
  demoarc1.ms 4 39 1 0 5785.85 6.140271 256 SS444
  </pre></div>
  <p>
  Note that fiber 37 is the first image line in demoobj.ms and teh second image
  line in demoarc.ms.  The dispersion is the same in all fibers by design.
  </p>
  <p>
  2.  List long headers for the two images of example 1 but restricted to
  apertures 38 and 39.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; slist demoobj.ms,demoarc1.ms ap=38,39 l+
  demoobj.ms: Hydra artificial image
      EXPTIME = 2133.33 UT = 9:10:09.0    ST = 20:09:34.0
      RA = 1:34:02.00   DEC = 30:37:03.0  HA = INDEF    AIRMASS = 2.3
      2 38 1 0 5785.85 6.140271 256 SS313
      3 39 1 0 5785.85 6.140271 256 SS444
  demoarc1.ms: Hydra artificial image
      EXPTIME = 2133.33 UT = 9:10:09.0    ST = 20:09:34.0
      RA = 1:34:02.00   DEC = 30:37:03.0  HA = INDEF    AIRMASS = 2.3
      3 38 1 0 5785.85 6.140271 256 SS313
      4 39 1 0 5785.85 6.140271 256 SS444
  </pre></div>
  <p>
  The other header parameters are the same because this is artificial
  data using the same template header.
  </p>
  <p>
  3.  Dump the set of image headers on a printer in long format.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; slist *.ms.imh l+ | lprint
  </pre></div>
  <p>
  4.  The short form of SLIST may be used to get some of the aperture
  information for use in a script.  The following simply prints the
  image line corresponding to a specified aperture.  In a real application
  something more complex would be done.
  </p>
  <div class="highlight-default-notranslate"><pre>
  procedure example (images, aperture)
  
  string  images          {prompt="List of images"}
  int     aperture        {prompt="Aperture"}
  
  begin
          string temp, image
          int     line
  
          # Use SLIST to print to a temporary file.
          temp = mktemp ("example")
          slist (images, aperture=aperture, long=no, &gt; temp)
  
          # Scan each line and print the line number.
          list = temp
          while (fscan (list, image, line) != EOF)
              print (image, ": ", line)
          list = ""
          delete (temp, verify=no)
  end
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SLIST">
  <dt><b>SLIST V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SLIST' Line='SLIST V2.10' -->
  <dd>This task was revised to be relevant for the current spectral image
  formats.  The old version is still available in the IRS/IIDS package.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imheader, hselect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
