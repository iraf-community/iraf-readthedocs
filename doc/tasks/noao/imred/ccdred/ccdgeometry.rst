.. _ccdgeometry:

ccdgeometry: Discussion of CCD coordinate/geometry keywords
===========================================================

**Package: ccdred**

.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <b>ccdred</b> package maintains and updates certain geometry
  information about the images.  This geometry is described by four image
  header parameters which may be present.  These are defined below by the
  parameter names used in the package.  Note that these names may be
  different in the image header using the image header translation
  feature of the package.
  </p>
  <dl id="l_DATASEC">
  <dt><b>DATASEC</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='DATASEC' Line='DATASEC' -->
  <dd>The section of the image containing the CCD data.  If absent the
  entire image is assumed to be data.  Only the pixels within the
  data section are modified during processing.  Therefore, there may be
  additional calibration or observation information in the image.
  If after processing, the data section is the entire image it is
  not recorded in the image header.
  </dd>
  </dl>
  <dl id="l_CCDSEC">
  <dt><b>CCDSEC</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='CCDSEC' Line='CCDSEC' -->
  <dd>The section of the CCD to corresponding to the data section.  This
  refers to the physical format, columns and lines, of the detector.  This is
  the coordinate system used during processing to relate calibration
  data to the image data; i.e. image data pixels are calibrated by
  calibration pixels at the same CCD coordinates regardless of image pixel
  coordinates.  This allows recording only parts of the CCD during data
  taking and calibrating with calibration frames covering some or all of
  the CCD.  The CCD section is maintained during trimming operations.
  Note that changing the format of the images by image operators outside
  of the <b>ccdred</b> package will invalidate this coordinate system.
  The size of the CCD section must agree with that of the data section.
  If a CCD section is absent then it defaults to the data section such
  that the first pixel of the data section has CCD coordinate (1,1).
  </dd>
  </dl>
  <dl id="l_BIASSEC">
  <dt><b>BIASSEC</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='BIASSEC' Line='BIASSEC' -->
  <dd>The section of the image containing prescan or overscan bias information.
  It consists of a strip perpendicular to the readout axis.  There may be
  both a prescan and overscan but the package currently only uses one.
  This parameter may be overridden during processing by the parameter
  <i>ccdproc.biassec</i>.  Only the part of the bias section along the
  readout is used and the length of the bias region is determined by
  the trim section.  If one wants to limit the region of the bias
  strip used in the fit then the <i>sample</i> parameter should be used.
  </dd>
  </dl>
  <dl id="l_TRIMSEC">
  <dt><b>TRIMSEC</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='TRIMSEC' Line='TRIMSEC' -->
  <dd>The section of the image extracted during processing when the trim
  operation is selected (<i>ccdproc.trim</i>).  If absent when the trim
  operation is selected it defaults to the data section; i.e. the processed
  image consists only of the data section.  This parameter may be overridden
  during processing by the parameter <i>ccdproc.trimsec</i>.  After trimming
  this parameter, if present, is removed from the image header.  The
  CCD section, data section, and bias section parameters are also modified
  by trimming.
  </dd>
  </dl>
  <p>
  The geometry is as follows.  When a CCD image is recorded it consists
  of a data section corresponding to part or all of the CCD detector.
  Regions outside of the data section may contain additional information
  which are not affected except by trimming.  Most commonly this consists
  of prescan and overscan bias data.  When recording only part of the
  full CCD detector the package maintains information about that part and
  correctly applies calibrations for that part of the detector.  Also any
  trimming operation updates the CCD coordinate information.  If the
  images include the data section, bias section, trim section, and ccd
  section the processing may be performed entirely automatically.
  </p>
  <p>
  The sections are specified using the notation [c1:c2,l1:l2] where c1
  and c2 are the first and last columns and l1 and l2 are the first and
  last lines.  Currently c1 and l1 must be less than c2 and l2
  respectively and no subsampling is allowed.  This may be added later.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION'  -->
  
