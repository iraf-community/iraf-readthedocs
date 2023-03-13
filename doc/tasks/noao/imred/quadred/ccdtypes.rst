.. _ccdtypes:

ccdtypes: Description of the CCD image types
============================================

**Package: quadred**

.. raw:: html

  <section id="s_ccdtypes">
  <h3>Ccdtypes</h3>
  <p>
  The following CCD image types may be specified as the value of the parameter
  <i>ccdtype</i>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ""      - (the null string) all image types
  object  - object images
  zero    - zero level images such as a bias or preflash
  dark    - dark count images
  flat    - flat field images
  illum   - iillumination images
  fringe  - fringe correction images
  other   - other image types defined in the translation file
  none    - images without an image type parameter
  unknown - image types not defined in the translation file
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <b>ccdred</b> package recognizes certain standard CCD image types
  identified in the image header.  The tasks may select images of a
  particular CCD image type from image lists with the parameter
  <i>ccdtype</i> and also recognize and take special actions for
  calibration images.
  </p>
  <p>
  In order to make use of CCD image type information the header keyword
  identifying the image type must be specified in the instrument
  translation file.  This entry has the form
  </p>
  <p>
  	imagetyp keyword
  </p>
  <p>
  where keyword is the image header keyword.  This allows the package to
  access the image type string.  There must also be a translation between
  the image type strings and the CCD types as recognized by the package.
  This information consists of lines in the instrument translation file
  of the form
  </p>
  <p>
  	header	package
  </p>
  <p>
  where header is the exact string given in the image header and package
  is one of the types recognized by the package.  The image header string
  can be virtually anything and if it contains blanks it must be
  quoted.  The package image types are those given above except for
  the null string, <span style="font-family: monospace;">"none"</span>, and <span style="font-family: monospace;">"unknown"</span>.  That is, these types may
  be specified as a CCD image type in selecting images but not as a translations
  of image type strings.
  </p>
  <p>
  There may be more than one image type that maps to the same package
  type.  In particular other standard CCD image types, such as comparison
  spectra, multiple exposure, standard star, etc., should be mapped to
  object or other.  There may also be more than one type of flat field, i.e. dome
  flat, sky flat, and lamp flat.  For more on the instrument translation
  file see the help for <b>instruments</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The example entries in the instrument translation file are from the 1986
  NOAO CCD image header format produced by the CAMERA format tape writer.
  </p>
  <div class="highlight-default-notranslate"><pre>
  imagetyp                    data-typ
  
  'OBJECT (0)'                object
  'DARK (1)'                  dark
  'PROJECTOR FLAT (2)'        flat
  'SKY FLAT (3)'              other
  'COMPARISON LAMP (4)'       other
  'BIAS (5)'                  zero
  'DOME FLAT (6)'             flat
  </pre></div>
  <p>
  The image header keyword describing the image type is <span style="font-family: monospace;">"data-typ"</span>.
  The values of the image type strings in the header contain blanks so they
  are quoted.  Also the case of the strings is important.  Note that there
  are two types of flat field images and two types of other images.
  </p>
  <p>
  2. One way to check the image types is with the task <b>ccdlist</b>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh
  Zero.imh[504,1][real][zero][1][OT]:FOCUS L98-193
  Flat1.imh[504,1][real][flat][1][OTZ]:dflat 6v+blue 5s
  ccd002.imh[504,504][real][unknown][1][OTZF]:FOCUS L98-193
  ccd003.imh[544,512][short][object][1]:L98-193
  ccd004.imh[544,512][short][object][1]:L98-193
  ccd005.imh[544,512][short][object][1]:L98-193
  oldformat.imh[544,512][short][none][1]:M31 V
  </pre></div>
  <p>
  The unknown type has a header image type of <span style="font-family: monospace;">"MUL (8)"</span>.  The old format
  image does not have any header type.
  </p>
  <p>
  3. To select only images of a particular type:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh ccdtype=object
  ccd003.imh[544,512][short][object][1]:L98-193
  ccd004.imh[544,512][short][object][1]:L98-193
  ccd005.imh[544,512][short][object][1]:L98-193
  cl&gt; ccdlist *.imh ccdtype=unknown
  ccd002.imh[504,504][real][unknown][1][OTZF]:FOCUS L98-193
  cl&gt; ccdlist *.imh ccdtype=none
  oldformat.imh[544,512][short][none][1]:M31 V
  </pre></div>
  <p>
  4. To process images with <b>ccdproc</b>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdproc *.imh
  cl&gt; ccdproc *.imh ccdtype=object
  </pre></div>
  <p>
  In the first case all the images will be processed (the default value of
  <i>ccdtype</i> is <span style="font-family: monospace;">""</span>).  However, the task recognizes the calibration
  images, such as zero level and flat fields, and processes them appropriately.
  In the second case only object images are processed and all other images
  are ignored (except if needed as a calibration image).
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  instruments
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'CCDTYPES' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
