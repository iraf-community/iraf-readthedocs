.. _ccdlist:

ccdlist: List mosaic processing information
===========================================

**Package: msctools**

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
  <dd>CCD images to be listed.  A subset of the these may be selected using the
  CCD image type parameter.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = ""' -->
  <dd>CCD image type to be listed.  If no type is specified then all the images
  are listed.  If an image type is specified then only images
  of that type are listed.  See <b>ccdtypes</b> for a list of the package
  image types.
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
  Information from the specified input images is listed on the standard
  output.  A specific CCD image type may be selected from the input
  images by the parameter <i>ccdtype</i>.  There are three list formats;
  the default one line per image format, an image name only format, and a
  multi-line long format.  The default one line format consists of the
  image name, image size, image pixel type, CCD image type, subset ID (if
  defined), processing flags, and title.  This format contains the same
  information as that produced by <b>imheader</b> as well as CCD specific
  information.  The processing flags identifying the processing operations
  performed on the image are given by the following single letter codes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  B - Bad pixel replacement
  O - Overscan bias subtraction
  T - Trimming
  Z - Zero level subtraction
  D - Dark count subtraction
  F - Flat field calibration
  I - Iillumination correction
  Q - Fringe correction
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
  1. To list the default format for all images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh
  ccd001.imh[544,512][short][unknown][V]:FOCUS L98-193
  ccd007.imh[544,512][short][object][V]:N2968 V 600s
  ccd015.imh[544,512][short][object][B]:N3098 B 500s
  ccd024.imh[544,512][short][object][R]:N4036 R 600s
  ccd045.imh[544,512][short][flat][V]:dflat 6v+blue 5s
  ccd066.imh[544,512][short][flat][B]:dflat 6v+blue 5s
  ccd103.imh[544,512][short][flat][R]:dflat 6v+blue 5s
  ccd104.imh[544,512][short][zero][]:bias
  ccd105.imh[544,512][short][dark][]:dark 3600s
  </pre></div>
  <p>
  These images have not been processed.
  </p>
  <p>
  2. To restrict the listing to just the object images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh ccdtype=object
  ccd007.imh[544,512][short][object][V]:N2968 V 600s
  ccd015.imh[544,512][short][object][B]:N3098 B 500s
  ccd024.imh[544,512][short][object][R]:N4036 R 600s
  </pre></div>
  <p>
  3. The long list for image <span style="font-family: monospace;">"ccd007"</span> is obtained by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist ccd007 l+
  ccd007[544,512][short][object][V]:N2968 R 600s
      exptime = 200. darktime = 200.
      [TO BE DONE] Overscan strip is [520:540,*]
      [TO BE DONE] Trim image section is [3:510,3:510]
      [TO BE DONE] Flat field correction
  </pre></div>
  <p>
  4. After processing the images have the short listing:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh ccdtype=object
  ccd007.imh[508,508][real][object][V][OTF]:N2968 V 600s
  ccd015.imh[508,508][real][object][B][OTF]:N3098 B 500s
  ccd024.imh[544,512][short][object][R][OTF]:N4036 R 600s
  </pre></div>
  <p>
  The processing indicated is overscan subtraction, trimming, and flat fielding.
  </p>
  <p>
  5. The long listing for <span style="font-family: monospace;">"ccd007"</span> after processing is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist ccd007 l+
  ccd007[508,508][real][object][V][OTF]:N2968 R 600s
      exptime = 200. darktime = 200.
      Jun  2 18:18 Overscan section is [520:540,*] with mean=481.8784
      Jun  2 18:18 Trim data section is [3:510,3:510]
      Jun  2 18:19 Flat field image is FlatV.imh with scale=138.2713
  </pre></div>
  <p>
  6. To make a list file containing all the flat field images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh ccdtype=flat name+ &gt; flats
  </pre></div>
  <p>
  This file can be used as an @ file for processing.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdtypes ccdgroups
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
