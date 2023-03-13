.. _package:

package: CCD image reduction package
====================================

**Package: ccdred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccdred
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_pixeltype">
  <dt><b>pixeltype = <span style="font-family: monospace;">"real real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixeltype' Line='pixeltype = "real real"' -->
  <dd>Output pixel datatype and calculation datatype.  When images are processed
  or created the output pixel datatype is determined by this parameter if the
  specified datatype is of equal or higher precision otherwise the input
  image datatype is preserved.  For example if the output datatype is
  specified as <span style="font-family: monospace;">"input"</span> then input images which are <span style="font-family: monospace;">"short"</span> or <span style="font-family: monospace;">"ushort"</span> will
  be output as integer but any real datatype input images will remain real.
  The allowed types and order of precision are <span style="font-family: monospace;">"short"</span>, <span style="font-family: monospace;">"ushort"</span>, <span style="font-family: monospace;">"int"</span>,
  <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"real"</span>, or <span style="font-family: monospace;">"double"</span>, for short signed integer, short unsigned
  integer, integer, long integers, and real or double floating point.  Note
  that if short input images are processed into real images the disk space
  required will generally increase.  The calculation datatypes may only be
  short and real with a default of real if none is specified.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print log information to the standard output?
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>Text log file.  If no filename is specified then no log file is kept.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>Log metacode plot file for the overscan bias vector fits.  If no filename
  is specified then no metacode plot file is kept.
  </dd>
  </dl>
  <dl id="l_backup">
  <dt><b>backup = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='backup' Line='backup = ""' -->
  <dd>Backup prefix for backup images.  If no prefix is specified then no backup
  images are kept when processing.  If specified then the backup image
  has the specified prefix.
  </dd>
  </dl>
  <dl id="l_instrument">
  <dt><b>instrument = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='instrument' Line='instrument = ""' -->
  <dd>CCD instrument translation file.  This is usually set with
  <b>setinstrument</b>.
  </dd>
  </dl>
  <dl id="l_ssfile">
  <dt><b>ssfile = <span style="font-family: monospace;">"subsets"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ssfile' Line='ssfile = "subsets"' -->
  <dd>Subset translation file used to define the subset identifier.  See
  <b>subsets</b> for more.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Interactive graphics output device when fitting the overscan bias vector.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  The default is the standard graphics cursor.
  </dd>
  </dl>
  <dl id="l_version">
  <dt><b>version = <span style="font-family: monospace;">"June 1987"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='version' Line='version = "June 1987"' -->
  <dd>Package version.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The CCD reduction package is loaded when this command is entered.  The
  package contains parameters which affect the operation of the tasks it
  defines.  When images are processed or new image are created the output
  pixel datatype is that specified by the parameter <b>pixeltype</b>.  Note
  that CCD processing replaces the original image by the processed image so
  the pixel type of the CCD images may change during processing.  The output
  pixel type is not allowed to change to a lower precision but it is common
  for input short images to be processed to real images.  Processing images
  from short to real pixel datatypes will generally increase the amount of
  disk space required (a factor of 2 on most computers).
  </p>
  <p>
  The tasks produce log output which may be printed on the standard
  output (the terminal unless redirected) and appended to a file.  The
  parameter <i>verbose</i> determines whether processing information
  is printed.  This may be desirable initially, but when using background
  jobs the verbose output should be turned off.  The user may look at
  the end of the log file (for example with <b>tail</b>) to determine
  the status of the processing.
  </p>
  <p>
  The package was designed to work with data from many different observatories
  and instruments.  In order to accomplish this an instrument translation
  file is used to define a mapping between the package parameters and
  the particular image header format.  The instrument translation file
  is specified to the package by the parameter <i>instrument</i>.  This
  parameter is generally set by the task <b>setinstrument</b>.  The other
  file used is a subset file.  This is generally created and maintained
  by the package and the user need not do anything.  For more sophisticated
  users see <b>instruments</b> and <b>subsets</b>.
  </p>
  <p>
  The package has very little graphics
  output.  The exception is the overscan bias subtraction.  The bias
  vector is logged in the metacode plot file if given.  The plot file
  may be examined with the tasks in the <b>plot</b> package such as
  <b>gkimosaic</b>.  When interactively fitting the overscan vector
  the graphics input and output devices must be specified.  The defaults
  should apply in most cases.
  </p>
  <p>
  Because processing replaces the input image by the processed image it
  may be desired to save the original image.  This may be done by
  specifying a backup prefix with the parameter <i>backup</i>.  For
  example, if the prefix is <span style="font-family: monospace;">"orig"</span> and the image is <span style="font-family: monospace;">"ccd001"</span>, the backup
  image will be <span style="font-family: monospace;">"origccd001"</span>.  The prefix may be a directory but it must
  end with <span style="font-family: monospace;">'/'</span> or <span style="font-family: monospace;">'$'</span> (for logical directories).
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdproc, instruments, setinstrument, subsets
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'SEE ALSO'  -->
  
