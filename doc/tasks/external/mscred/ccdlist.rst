.. _ccdlist:

ccdlist: List mosaic processing information
===========================================

**Package: mscred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccdlist images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of mosaic exposures to be listed.  A subset of the these may be
  selected using the CCD image type parameter.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = ""' -->
  <dd>CCD type to be listed.  If no type is specified then all the types are
  listed.  If a CCD type is specified then only images of that type are
  listed.  See <b>ccdtypes</b> for a list of the package image types.
  </dd>
  </dl>
  <dl id="l_extname">
  <dt><b>extname = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extname' Line='extname = ""' -->
  <dd>Comma delimited list of patterns matching the extension names to be listed.
  The null string, <span style="font-family: monospace;">""</span>, selects all extension names.  Otherwise a pattern
  must match the full name.  For example the pattern <span style="font-family: monospace;">"[1-8]"</span> matches
  <span style="font-family: monospace;">"5"</span> but not <span style="font-family: monospace;">"im5"</span>.  One form of pattern is an exact match so that
  a parameter value of <span style="font-family: monospace;">"im1,im12"</span> matches both <span style="font-family: monospace;">"im1"</span> and <span style="font-family: monospace;">"im12"</span>, but not
  <span style="font-family: monospace;">"im11"</span>.  Typically the parameter would be <span style="font-family: monospace;">""</span> to select all extensions or
  just the name of the first extension since all extensions should have the
  same filter, type, title, and processing status.
  </dd>
  </dl>
  <dl id="l_names">
  <dt><b>names = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='names' Line='names = no' -->
  <dd>List the image names only?  Used with the CCD image type parameter to make
  a list of the images of the specified type.
  </dd>
  </dl>
  <dl id="l_long">
  <dt><b>long = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long' Line='long = no' -->
  <dd>Long format listing?  The images are listed in a long format containing some
  image parameters and the processing history.
  </dd>
  </dl>
  <dl id="l_ccdproc">
  <dt><b>ccdproc (pset)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdproc' Line='ccdproc (pset)' -->
  <dd>CCD processing parameter set.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Information from the specified input mosaic exposures is listed on the standard
  output.  A specific CCD type may be selected from the input exposures by
  the parameter <i>ccdtype</i>.  There are three list formats; the default one
  line per image format, an image name only format, and a multi-line long
  format.  The default one line format consists of the image name, image
  size, image pixel type, CCD image type, amplifier ID (if defined), subset
  ID (if defined), processing flags, and title.  This format contains the
  same information as that produced by <b>imheader</b> as well as CCD specific
  information.  The processing flags identifying the processing operations
  performed on the image are given by the following single letter codes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  X - Crosstalk correction
  B - Bad pixel replacement
  O - Overscan bias subtraction
  T - Trimming
  Z - Zero level subtraction
  D - Dark count subtraction
  F - Flat field calibration
  </pre></div>
  <p>
  The long format has the same first line as the default format plus additional
  instrument information such as the exposure time and the full processing
  history.  In addition to listing the completed processing, the operations
  not yet done (as specified by the <b>ccdproc</b> parameters) are also
  listed.
  </p>
  <p>
  The image name only format is intended to be used to generate lists of
  images of the same CCD image type.  These lists may be used as <span style="font-family: monospace;">"@"</span> file
  lists in IRAF tasks.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To list the default format for extension im1 of all images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.fits extname=im1
  ccd001.fits[im1][544,512][short][unknown][1][V]:FOCUS L98-193
  ccd007.fits[im1][544,512][short][object][1][V]:N2968 V 600s
  ccd015.fits[im1][544,512][short][object][1][B]:N3098 B 500s
  ccd024.fits[im1][544,512][short][object][1][R]:N4036 R 600s
  ccd045.fits[im1][544,512][short][flat][1][V]:dflat 6v+blue 5s
  ccd066.fits[im1][544,512][short][flat][1][B]:dflat 6v+blue 5s
  ccd103.fits[im1][544,512][short][flat][1][R]:dflat 6v+blue 5s
  ccd104.fits[im1][544,512][short][zero][1][]:bias
  ccd105.fits[im1][544,512][short][dark][1][]:dark 3600s
  </pre></div>
  <p>
  2. To list all extensions of one mosaic exposure which has been processed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist obj092
      obj092[im1][128,256][real][object][1][R][XBOTZF]:NGC1569
      obj092[im2][128,256][real][object][2][R][XBOTZF]:NGC1569
      obj092[im3][128,256][real][object][3][R][XBOTZF]:NGC1569
      obj092[im4][128,256][real][object][4][R][XBOTZF]:NGC1569
      obj092[im5][127,256][real][object][5][R][XBOTZF]:NGC1569
      obj092[im6][127,256][real][object][6][R][XBOTZF]:NGC1569
      obj092[im7][127,256][real][object][7][R][XBOTZF]:NGC1569
      obj092[im8][127,256][real][object][8][R][XBOTZF]:NGC1569
  </pre></div>
  <p>
  These exposures have not been processed.
  </p>
  <p>
  3. To restrict the listing to just the object images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.fits extname=im1 ccdtype=object
  ccd007.fits[im1][544,512][short][object][1][V]:N2968 V 600s
  ccd015.fits[im1][544,512][short][object][1][B]:N3098 B 500s
  ccd024.fits[im1][544,512][short][object][1][R]:N4036 R 600s
  </pre></div>
  <p>
  4. The long list for image <span style="font-family: monospace;">"ccd007"</span> is obtained by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist ccd007 extname=im1 l+
  ccd007[im1][544,512][short][object][1][V]:N2968 R 600s
      exptime = 200. darktime = 200.
      [TO BE DONE] Overscan strip is [520:540,*]
      [TO BE DONE] Trim image section is [3:510,3:510]
      [TO BE DONE] Flat field correction
  </pre></div>
  <p>
  5. After processing the images have the short listing:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.fits extname=im1 ccdtype=object
  ccd007.fits[im1][508,508][real][object][1][V][OTF]:N2968 V 600s
  ccd015.fits[im1][508,508][real][object][1][B][OTF]:N3098 B 500s
  ccd024.fits[im1][544,512][short][object][1][R][OTF]:N4036 R 600s
  </pre></div>
  <p>
  The processing indicated is overscan subtraction, trimming, and flat fielding.
  </p>
  <p>
  6. The long listing for <span style="font-family: monospace;">"ccd007"</span> after processing is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist ccd007 extname=im1 l+
  ccd007[im1][508,508][real][object][1][V][OTF]:N2968 R 600s
      exptime = 200. darktime = 200.
      Jun  2 18:18 Overscan section is [520:540,*] with mean=481.8784
      Jun  2 18:18 Trim data section is [3:510,3:510]
      Jun  2 18:19 Flat field image is FlatV with scale=138.2713
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_CCDLIST">
  <dt><b>CCDLIST - MSCRED</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDLIST' Line='CCDLIST - MSCRED' -->
  <dd>Modified to work with multiextension mosaic exposures.
  </dd>
  </dl>
  <dl id="l_CCDLIST">
  <dt><b>CCDLIST V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDLIST' Line='CCDLIST V2.11' -->
  <dd>Added amplifier field in listing.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdtypes ccdgroups
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
