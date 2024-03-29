.. _mkmsc:

mkmsc: Make multiextension mosaic format from flat formats
==========================================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  MKMSC creates a multiextension format, suitable for use with the MSCRED
  package, from images with multiple amplifier readouts recorded as sections
  of a single image.  These <span style="font-family: monospace;">"flat"</span> formats occur for both mosaics of CCDs and
  multiamplifier readouts from a single CCD.  Examples of this format are the
  NOAO QUAD format, the ESO FORS format, and the Keck mosaic format.  The
  regions and keywords are defined in a simple description file.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkmsc input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be converted.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of multiextension mosaic files to be created.  If no list is specified
  the output names will be the same as the input names otherwise the output
  list much match the input list in number.  If an output name is the same
  as the input name, the output multiextension file will replace the input
  image upon successful conversion.  If the output file exists it is skipped
  with a warning.
  </dd>
  </dl>
  <dl id="l_description">
  <dt><b>description = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='description' Line='description = ""' -->
  <dd>Description file to use.  See the DESCRIPTION section for the format.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print processing information?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKMSC creates a multiextension format, suitable for use with the MSCRED
  package, from images with multiple amplifier readouts recorded as sections
  of a single image.  These <span style="font-family: monospace;">"flat"</span> formats occur for both mosaics of CCDs and
  multiamplifier readouts from a single CCD.  Examples of this format are the
  NOAO QUAD format, the ESO FORS format, and the Keck mosaic format.  The
  regions and keywords are defined in a simple description file.
  </p>
  <p>
  The first column is an extension keyword and the second is the keyword
  value or reference to the value of a keyword in the input images.  The
  structure is shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  keyword(extname) [!keyword|value]
  </pre></div>
  <p>
  The <span style="font-family: monospace;">"keyword"</span> is either one of the standard keywords described later or any
  keyword to be added to the output extension.  The keyword is case
  insensitive.  The <span style="font-family: monospace;">"extname"</span> is the exentsion name to which it applies.  The
  set of unique extension names defines the set of possible output
  extensions.  The second column is either a reference to a keyword in the
  input images, beginning with <span style="font-family: monospace;">'!'</span> and followed by the keyword, or a value.
  If the value contains whitespace it must be quoted.
  </p>
  <p>
  The regions of the input image to be mapped to extensions are given by the
  image section keywords DATASEC, BIASSEC, and TRIMSEC.  DATASEC is required
  otherwise no extension will be created.  The sections refer to regions
  of the input image.  In the output extension the data section will be in the
  first columns and the bias section will follow regardless of where the
  bias section is in the input.  The trim section is used for display and
  processing to select the region of the data section that is to be used.
  </p>
  <p>
  The keywords CCDSEC and DETSEC are sections which must match the data section
  in unbinned pixel size.  These keywords are always in unbinned pixels in
  MSCRED.  The CCD section is used to match calibration pixels and the
  detector section is used to define how the regions will be displayed and
  how multiple amplifiers are related.  For multiple amplifiers from a
  single CCD the detector section is optional.
  </p>
  <p>
  When there are multiple amplifiers from the same CCD the keyword CCDNAME
  should be defined with the same value.  Merging of multiple amplifiers
  into a single CCD image in MSCRED occurs when extensions have the
  same CCDNAME.  The keyword AMPNAME may also be defined to identify
  the amplifier.  In a mosaic the amplifier name can be the same for
  the same amplifier in each CCD.
  </p>
  <p>
  MSCRED uses an amplifier identifier keyword to match extensions.
  This keyword must be unique for each extension.
  If no amplifier ID is specified the extension name will be used.  However,
  since the extension name can be changed as needed it is a good idea
  to have a separate keyword.  In MSCRED the default keyword when there is
  no instrument keyword translation is AMPID.  Often times the keyword
  IMAGEID is used.
  </p>
  <p>
  All other keywords are simply added to the output extension.  Note that
  each extension will start with a copy of the keywords in the input image,
  so added keywords should be used either for keywords that differ between
  each extension or to change a keyword from the value in the input image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  CTIO ARCON QUAD FORMAT
  </p>
  <p>
  The follwing description file may be used with the CTIO quad format,
  both with 2 or 4 amplifiers.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; page mscred$lib/mkmsc/quad.dat
  imageid(im1)    1
  ampid(im1)      11
  datasec(im1)    !DSEC11
  biassec(im1)    !BSEC11
  trimsec(im1)    !TSEC11
  ccdsec(im1)     !CSEC11
  detsec(im1)     !CSEC11
  ccdname(im1)    !DETECTOR
  ampname(im1)    Amp11
  rdnoise(im1)    !GTRON11
  gain(im1)       !GTGAIN11
  
  imageid(im2)    2
  ampid(im2)      12
  datasec(im2)    !DSEC12
  biassec(im2)    !BSEC12
  trimsec(im2)    !TSEC12
  ccdsec(im2)     !CSEC12
  detsec(im2)     !CSEC12
  ccdname(im2)    !DETECTOR
  ampname(im2)    Amp12
  rdnoise(im2)    !GTRON12
  gain(im2)       !GTGAIN12
  
  imageid(im3)    3
  ampid(im3)      21
  datasec(im3)    !DSEC21
  biassec(im3)    !BSEC21
  trimsec(im3)    !TSEC21
  ccdsec(im3)     !CSEC21
  detsec(im3)     !CSEC21
  ccdname(im3)    !DETECTOR
  ampname(im3)    Amp21
  rdnoise(im3)    !GTRON21
  gain(im3)       !GTGAIN21
  
  imageid(im4)    4
  ampid(im4)      22
  datasec(im4)    !DSEC22
  biassec(im4)    !BSEC22
  trimsec(im4)    !TSEC22
  ccdsec(im4)     !CSEC22
  detsec(im4)     !CSEC22
  ccdname(im4)    !DETECTOR
  ampname(im4)    Amp22
  rdnoise(im4)    !GTRON22
  gain(im4)       !GTGAIN22
  ms&gt; mkmsc quad0008 mef0008 desc=mscred$lib/mkmsc/quad.dat verbose+
    Reading description file mscred$lib/mkmsc/quad.dat
    Create mef0008[im1][833,769]: OIIICont 14s
      quad0008[1:779,1,769] -&gt; mef0008[im1][1:779,1:769]
      quad0008[790:843,1,769] -&gt; mef0008[im1][780:833,1:769]
    Create mef0008[im2][833,769]: OIIICont 14s
      quad0008[908:1686,1,769] -&gt; mef0008[im2][1:779,1:769]
      quad0008[844:897,1,769] -&gt; mef0008[im2][780:833,1:769]
    Create mef0008[im3][833,769]: OIIICont 14s
      quad0008[1:779,770,1538] -&gt; mef0008[im3][1:779,1:769]
      quad0008[790:843,770,1538] -&gt; mef0008[im3][780:833,1:769]
    Create mef0008[im4][833,769]: OIIICont 14s
      quad0008[908:1686,770,1538] -&gt; mef0008[im4][1:779,1:769]
      quad0008[844:897,770,1538] -&gt; mef0008[im4][780:833,1:769]
  </pre></div>
  <p>
  Note that this description file works with dual readout because only the
  keywords DSEC which are present will result in extensions being created.
  </p>
  <p>
  ESO VLT FORS1 FORMAT
  </p>
  <p>
  The ESO VLT FORS1 data uses a format which is very similar to that of
  the CTIO format.  The following description file may be used based on
  an example derived from the archive file FORS.2001-04-19T04:18:55.409.fits.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; type mscred$lib/mkmsc/fors.dat
  imageid(im1)    1
  ampid(im1)      A
  datasec(im1)    !DSECA
  biassec(im1)    !BSECA
  trimsec(im1)    !TSECA
  ccdsec(im1)     !CSECA
  detsec(im1)     !CSECA
  ccdname(im1)    FORS
  ampname(im1)    AmpA
  
  imageid(im2)    2
  ampid(im2)      B
  datasec(im2)    !DSECB
  biassec(im2)    !BSECB
  trimsec(im2)    !TSECB
  ccdsec(im2)     !CSECB
  detsec(im2)     !CSECB
  ccdname(im2)    FORS
  ampname(im2)    AmpB
  
  imageid(im3)    3
  ampid(im3)      C
  datasec(im3)    !DSECC
  biassec(im3)    !BSECC
  trimsec(im3)    !TSECC
  ccdsec(im3)     !CSECC
  detsec(im3)     !CSECC
  ccdname(im3)    FORS
  ampname(im3)    AmpC
  
  imageid(im4)    4
  ampid(im4)      D
  datasec(im4)    !DSECD
  biassec(im4)    !BSECD
  trimsec(im4)    !TSECD
  ccdsec(im4)     !CSECD
  detsec(im4)     !CSECD
  ccdname(im4)    FORS
  ampname(im4)    AmpD
  ms&gt; mkmsc f109.7 "" desc=mscred$lib/mkmsc/fors.dat
    Reading description file mscred$lib/mkmsc/fors.dat
    Create f109.7[im1][1040,1024]: PG1323-086
      f109.7[17:1040,1,1024] -&gt; f109.7[im1][1:1024,1:1024]
      f109.7[1:16,1,1024] -&gt; f109.7[im1][1025:1040,1:1024]
    Create f109.7[im2][1040,1024]: PG1323-086
      f109.7[1041:2064,1,1024] -&gt; f109.7[im2][1:1024,1:1024]
      f109.7[2065:2080,1,1024] -&gt; f109.7[im2][1025:1040,1:1024]
    Create f109.7[im3][1040,1024]: PG1323-086
      f109.7[17:1040,1025,2048] -&gt; f109.7[im3][1:1024,1:1024]
      f109.7[1:16,1025,2048] -&gt; f109.7[im3][1025:1040,1:1024]
    Create f109.7[im4][1040,1024]: PG1323-086
      f109.7[1041:2064,1025,2048] -&gt; f109.7[im4][1:1024,1:1024]
      f109.7[2065:2080,1025,2048] -&gt; f109.7[im4][1025:1040,1:1024]
  </pre></div>
  <p>
  This example shows in-place conversion.
  </p>
  <p>
  KECK MOSAIC DEVELOPMENT FORMAT
  </p>
  <p>
  The following was derived from a sample development flat format for a two CCD
  mosaic.  It differs from the above two examples in that the overscan
  and prescan regions are not contiguous with the data regions.  All the
  prescan regions are placed before the data regions and all the overscan
  regions (used for the bias regions) are placed after all the data regions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; type mscred$lib/mkmsc/keck.dat
      ampid(im1)      1
      datasec(im1)    [205:1228,1:4096]
      biassec(im1)    [4301:4380,1:4096]
      ccdsec(im1)     [1:1024,1:4096]
      detsec(im1)     [1:1024,1:4096]
      ccdname(im1)    "CCD 1"
      ampname(im1)    "AMP 1"
  
      ampid(im2)      2
      datasec(im2)    [1229:2252,1:4096]
      biassec(im2)    [4381:4460,1:4096]
      ccdsec(im2)     [1025:2048,1:4096]
      detsec(im2)     [1025:2048,1:4096]
      ccdname(im2)    "CCD 1"
      ampname(im2)    "AMP 2"
  
      ampid(im3)      3
      datasec(im3)    [2253:3276,1:4096]
      biassec(im3)    [4461:4540,1:4096]
      ccdsec(im3)     [1:1024,1:4096]
      detsec(im3)     [2049:3072,1:4096]
      ccdname(im3)    "CCD 2"
      ampname(im3)    "AMP 1"
  
      ampid(im4)      4
      datasec(im4)    [3277:4300,1:4096]
      biassec(im4)    [4541:4620,1:4096]
      ccdsec(im4)     [1024:2048,1:4096]
      detsec(im4)     [3073:4096,1:4096]
      ccdname(im4)    "CCD 2"
      ampname(im4)    "AMP 2"
      ms&gt; mkmsc obj0574 "" desc=mscred$lib/mkmsc/keck.dat verbose+
        Reading description file mscred$lib/mkmsc/keck.dat
        Create obj0574[im1][1104,4096]:
          obj0574[205:1228,1,4096] -&gt; obj0574[im1][1:1024,1:4096]
          obj0574[4301:4380,1,4096] -&gt; obj0574[im1][1025:1104,1:4096]
        Create obj0574[im2][1104,4096]:
          obj0574[1229:2252,1,4096] -&gt; obj0574[im2][1:1024,1:4096]
          obj0574[4381:4460,1,4096] -&gt; obj0574[im2][1025:1104,1:4096]
        Create obj0574[im3][1104,4096]:
          obj0574[2253:3276,1,4096] -&gt; obj0574[im3][1:1024,1:4096]
          obj0574[4461:4540,1,4096] -&gt; obj0574[im3][1025:1104,1:4096]
        Create obj0574[im4][1104,4096]:
          obj0574[3277:4300,1,4096] -&gt; obj0574[im4][1:1024,1:4096]
          obj0574[4541:4620,1,4096] -&gt; obj0574[im4][1025:1104,1:4096]
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MKMSC">
  <dt><b>MKMSC - V4.6: December 7, 2001</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKMSC' Line='MKMSC - V4.6: December 7, 2001' -->
  <dd>This task is new in this release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
