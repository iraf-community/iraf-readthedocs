.. _package:

package: Package parameters and general description of package
==============================================================

**Package: apextract**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apextract
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 2' -->
  <dd>Image axis along which the spectra dispersion run.  The dispersion axis
  is 1 when the dispersion is along lines so that spectra are horizontal
  when displayed normally.  The dispersion axis is 2 when the dispersion
  is along columns so that spectra are vertical when displayed normally.
  This parameter is superseded when the dispersion axis is defined in
  the image header by the parameter DISPAXIS.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database for storing aperture definitions.  Currently the database is
  a subdirectory of text files with prefix <span style="font-family: monospace;">"ap"</span> followed by the entry name,
  usually the image name.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print detailed processing and log information?  The output is to the
  standard output stream which is the user's terminal unless redirected.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>Text logfile of operations performed.  If a file name is specified
  log and history information produced by all the tasks in the package
  is appended to the file.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>Binary plot metacode file of aperture locations, traces, rejected points,
  etc.  If a file name is given metacode plots are appended.  The contents
  of the file may be manipulated with the tasks in the <b>plot</b> package.
  The most common is <b>gkimosaic</b>.  Special plotfile names may be used
  to select only particular plots or plots not normally output.  These are
  debugall, debugfitspec, debugaps, debugspec, debugfits, debugtrace,
  and debugclean which plot everything, the fitted spectrum, the apertures,
  the extracted spectrum, profile fit plots, the trace, and the rejected
  points during cleaned extraction.
  </dd>
  </dl>
  <dl id="l_version">
  <dt><b>version = <span style="font-family: monospace;">"APEXTRACT V3.0: August 1990"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='version' Line='version = "APEXTRACT V3.0: August 1990"' -->
  <dd>Version of the package.  This is the third major version of the package.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The primary function of the <b>apextract</b> package is the extraction of
  spectra from two dimensional formats to one dimensional formats.  In
  other words, the pixels at each wavelength are summed, possibly
  subtracting a background or sky from other pixels at that wavelength,
  to produce a vector of spectral fluxes as a function of wavelength.
  It has become common to have many spectra in one two dimensional
  image produced by instruments using echelles, fibers, and aperture
  masks.  Thus, the package provides many features for the efficient
  extractions of multiple spectra as well as single spectra.  There are
  also some additional, special purpose tasks for modeling spectra
  and using the aperture definitions, described below,
  to create masks and modified flat field images.
  </p>
  <p>
  The package assumes that one of the image axes is the dispersion axis,
  specified by the <i>dispaxis</i> package parameter or image header
  parameter of the same name, and the other is the spatial axes.
  This means that all pixels at the same column or line (the
  orientation may be in either direction) are considered to be at the
  same wavelength.  Even if this is not exactly
  true the resolution loss is generally quite small and the simplicity and
  absence of interpolation problems justify this approach.  The
  alternatives are to rotate the image with <b>rotate</b> or use the more
  complex <b>longslit</b> package.  Though extraction is strictly along
  lines and columns the position of the spectrum along the spatial axis
  is allowed to shift smoothly with wavelength.  This accounts for small
  misalignments and distortions.
  </p>
  <p>
  The two dimensional regions occupied by the spectra are defined by
  digital apertures having a fixed width but with spatial position smoothly
  varying with wavelength.  The apertures have a number of attributes.
  The aperture definitions are created and modified by the tasks in this
  package and stored in a database specified by the parameter <i>database</i>.
  The database is currently a directory containing simple text files
  in a human readable format.  The elements of an aperture definition
  are as follows.
  </p>
  <p style="text-align:center">Elements of an Aperture Definition
  
  </p>
  <dl id="l_aperture">
  <dt><b>aperture</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='aperture' Line='aperture' -->
  <dd>An integer aperture identification number.  The aperture number
  must be unique within a set of apertures.  The aperture number is
  the primary means of referencing an aperture and the resulting
  extracted spectra.  The aperture numbers are part of the extracted
  spectra image headers.  The numbers may be any integer and in any order
  but the most typical case is to have sequential numbers beginning
  with 1.
  </dd>
  </dl>
  <dl id="l_beam">
  <dt><b>beam</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='beam' Line='beam' -->
  <dd>An integer beam number.  The beam number need not be unique; i.e.
  several apertures may have the same beam number.  The beam numbers are
  recorded in the image headers of the extracted spectra.  The beam
  number is often used to identify types of spectra such as object,
  sky, arc, etc.
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='center' Line='center' -->
  <dd>A pair of numbers specifying the center of the aperture along the spatial
  and dispersion axes in the two dimensional image.  The center along
  the dispersion is usually defined as the middle of the image.  The
  rest of the aperture parameters are defined relative to the aperture
  center making it easy to move apertures.
  </dd>
  </dl>
  <dl id="l_low">
  <dt><b>low, high</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='low' Line='low, high' -->
  <dd>Pairs of numbers specifying the lower and upper limits of the
  aperture relative to the center along the spatial and dispersion axes.
  The lower limits are usually negative and the upper limits positive
  but there is no actual restriction; i.e. the aperture can actually
  be offset from the center position.  Currently the dispersion
  aperture limits are such that the entire length of the image along the
  dispersion axis is used.  In the future this definition can be
  easily used for objective prism spectra.
  </dd>
  </dl>
  <dl id="l_curve">
  <dt><b>curve, axis</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='curve' Line='curve, axis' -->
  <dd>An IRAF <span style="font-family: monospace;">"curfit"</span> function specifying a shift to be added to the center
  position along the spatial axis, given by the axis parameter which is
  the complement of the dispersion axis parameter <i>dispaxis</i>, as a
  function of the dispersion coordinate.  This trace function is one of
  the standard IRAF <b>icfit</b> types; a legendre polynomial, a chebyshev
  polynomial, a linear spline, or a cubic spline.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='background' Line='background' -->
  <dd>Background definition parameters.  For the <span style="font-family: monospace;">"average"</span> background subtraction
  option only the set of background sample regions (defined relative to
  the aperture center) are used.  For the <span style="font-family: monospace;">"fit"</span> option the parameters
  are those used by the <b>icfit</b> package for fitting a function to
  the points in the background sample regions.
  </dd>
  </dl>
  <p>
  This information as well as the image (or database entry) name are stored
  in a text file, with name given by the prefix <span style="font-family: monospace;">"ap"</span> followed by the entry
  name, in the database directory.  An example with the special entry  name
  <span style="font-family: monospace;">"last"</span>, stored in the file <span style="font-family: monospace;">"database$aplast"</span>, is given below. The <span style="font-family: monospace;">"begin"</span>
  line marks the beginning of an aperture definition.
  </p>
  <p style="text-align:center">Sample Aperture Database Entry
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Fri 17:43:41 03-Aug-90
  begin   aperture last 1 70.74564 256.
          image   last
          aperture        1
          beam    1
          center  70.74564 256.
          low     -5. -255.
          high    5. 256.
          background
                  xmin -100.
                  xmax 100.
                  function chebyshev
                  order 1
                  sample -10:-6,6:10
                  naverage -3
                  niterate 0
                  low_reject 3.
                  high_reject 3.
                  grow 0.
          axis    1
          curve   5
                  2.
                  1.
                  1.
                  512.
                  0.
  </pre></div>
  <p>
  There are a number of logical functions which may be performed to
  create, modify, and use the aperture definitions.  These functions
  are:
  </p>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Automatically find a specified number of spectra and assign default
  apertures.  Apertures may also be inherited from another image or
  defined using an interactive graphical interface called the <i>aperture
  editor</i>.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Recenter apertures on the image spectrum profiles.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Resize apertures based on spectrum profile width.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Interactively define or adjust aperture definitions using a graphical
  interface called the <i>aperture editor</i>.  All function may also
  be performed from this editor and, so, provides an alternative
  method of processing and extracting spectra.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Trace the positions of spectra profiles from a starting image line
  or column to other image lines or columns and fit a smooth function.
  The trace function is used to shift the center of the apertures
  at each dispersion point in the image.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Extract the flux in the apertures into one dimensional spectra in various
  formats.  This includes possible background subtraction, variance
  weighting, and bad pixel rejection.
  </dd>
  </dl>
  <p>
  The package is logically organized around these functions.  Each
  function has a task devoted to it.  The description of the parameters
  and algorithms for each function are organized according to these
  tasks; namely under the help topics <b>apdefault, apfind, aprecenter,
  apresize, apedit, aptrace</b>, and <b>apsum</b>.  However, each task has
  parameters to allow selecting some or all of the other functions, hence
  it is not necessary to use the individual tasks and often it is more
  convenient to use just the extraction task for all operations.  It is
  also possible to perform all the functions from within a graphical
  interface called the aperture editor.  This is usually only used to
  define and modify aperture definitions but it also has the capability
  to trace spectra and extract them.
  </p>
  <p>
  Each of the functions has many different options and parameters.  When
  broken down into individual tasks the parameters are also sorted by
  their function though there are then some mutual interdependencies.
  This parameter decomposition was what was available prior to the
  addition of the task <b>apall</b>.  This is the central task of the
  package which performs any and all of the functions required for the
  extraction of spectra and also collects all the parameters into one
  parameter set.  It is recommended that <b>apall</b> be used because it
  collects all the parameters in one place eliminating confusion over
  where a particular parameter is defined.
  </p>
  <p>
  In summary, the package consists of a number of logical functions which
  are documented by the individual tasks named for that function, but the
  functions are also integrated into each task and the aperture editor to
  providing many different ways for the user to choose to perform the
  functions.
  </p>
  <p>
  The package menu and help summary is shown below.
  </p>
  <p style="text-align:center">The APEXTRACT Package Tasks
  
  </p>
  <div class="highlight-default-notranslate"><pre>
    apall        apedit       apflatten    aprecenter   apsum
    apdefault    apfind       apmask       apresize     aptrace
    apdemos      apfit        apnormalize  apscatter
  
         apall - Extract 1D spectra (all parameters in one task)
     apdefault - Set the default aperture parameters and apidtable
       apdemos - Various tutorial demonstrations
        apedit - Edit apertures interactively
        apfind - Automatically find spectra and define apertures
         apfit - Fit 2D spectra and output the fit, difference,
                 or ratio
     apflatten - Remove overall spectral and profile shapes from
                 flat fields
        apmask - Create and IRAF pixel list mask of the apertures
   apnormalize - Normalize 2D apertures by 1D functions
    aprecenter - Recenter apertures
      apresize - Resize apertures
     apscatter - Fit and subtract scattered light
         apsum - Extract 1D spectra
       aptrace - Trace positions of spectra
  
               Additional topics
  
  apbackground - Background subtraction algorithms
     apextract - Package parameters and general description of
                 package
    approfiles - Profile determination algorithms
    apvariance - Extractions, variance weighting, cleaning, and
                 noise model
  </pre></div>
  <p>
  The extracted spectra are recorded in one, two, or three dimensional
  images depending on the <i>format</i> and <i>extras</i> parameters.  If
  the <i>extras</i> parameter is set to yes the formats are three
  dimensional with each plane in the third dimension containing
  associated information for the spectra in the first plane.  See
  <b>apsum</b> for further details.  When <i>extras</i>=no only the
  extracted spectra are output.
  </p>
  <p>
  If the format parameter is <span style="font-family: monospace;">"onedspec"</span> the output extractions are one
  dimensional images with names formed from an output rootname and an
  aperture number extension; i.e. root.0001 for aperture 1.  There will
  be as many output images as there are apertures for each input image,
  all with the same output rootname but with different aperture
  extensions.  This format is provided to be compatible with the original
  format used by the <b>onedspec</b> package.
  </p>
  <p>
  If the format parameter is <span style="font-family: monospace;">"echelle"</span> or <span style="font-family: monospace;">"multispec"</span> the output aperture
  extractions are put into a two dimensional image with a name formed from
  the output rootname and the extension <span style="font-family: monospace;">".ec"</span> or <span style="font-family: monospace;">".ms"</span>.  Each line in
  the output image corresponds to one aperture.  Thus in this format
  there is one output image for each input image.  These are the preferred
  output formats for reasons of compactness, ease of handling, and efficiency.
  These formats are compatible with the <b>onedspec</b>, <b>echelle</b>, and
  <b>msred</b> packages.  The format is a standard IRAF image with
  specialized image header keywords.  Below is an example of the keywords.
  </p>
  <p style="text-align:center">MULTISPEC/ECHELLE Format Image Header Keywords
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; imhead test.ms
  test.ms[512,2,4][real]: Title
      BANDID1 = 'spectrum - background fit, weights variance, clean yes'
      BANDID2 = 'spectrum - background fit, weights none, clean no'
      BANDID3 = 'background - background fit'
      BANDID4 = 'sigma - background fit, weights variance, clean yes'
      APNUM1  = '1 1 87.11 94.79'
      APNUM2  = '2 1 107.11 114.79'
      APID1   = 'Galaxy center'
      APID2   = 'Galaxy edge'
      WCSDIM  =                    3
      CTYPE1  = 'PIXEL   '
      CTYPE2  = 'LINEAR  '
      CTYPE3  = 'LINEAR  '
      CRVAL1  =                   1.
      CRPIX1  =                   1.
      CD1_1   =                   1.
      CD2_2   =                   1.
      CD3_3   =                   1.
      LTM1_1  =                   1.
      LTM2_2  =                   1.
      LTM3_3  =                   1.
      WAT0_001= 'system=equispec
      WAT1_001= 'wtype=linear label=Pixel
      WAT2_001= 'wtype=linear
      WAT3_001= 'wtype=linear
  </pre></div>
  <p>
  The BANDIDn keywords describe the various elements of the 3rd dimension.
  Except for the first one the other bands only occur when <i>extras</i> is
  yes and when sky subtraction and/or variance and cleaning are done.  The
  relation between the line and the aperture numbers is given by the header
  parameters APNUMn where n is the line and the value gives extraction and
  coordinate information about the spectrum.  The first field is the aperture
  number and the second is the beam number.  After dispersion calibration of
  echelle format spectra the beam number becomes the order number.  The other
  two numbers are the aperture limits at the line or column at which the
  aperture was defined.
  The APID keywords provide an optional title for each extracted spectrum
  in addition to the overall image title.
  </p>
  <p>
  The rest of the keywords are part of the IRAF World Coordinate System
  (WCS).  If the image being extracted has been previously calibrated
  (say with <b>longslit.transform</b>) then the dispersion coordinates
  will be carried in CRVAL1 and CD1_1.
  </p>
  <p>
  There is one other value for the format parameter, <span style="font-family: monospace;">"strip"</span>.  This produces
  two dimensional extractions rather than one dimensional extractions.
  Each aperture is output to a two dimensional image with a width set by the
  nearest integer which includes the aperture.  The output names are
  generated in the same way as for <span style="font-family: monospace;">"onedspec"</span> format.  The aperture is
  shifted by interpolation so that it is exactly aligned with the image
  columns.  If not variance weighting the actual image data is output
  with appropriate shifting while for variance weighting and/or cleaning
  the profile model is output (similar to <b>apfit</b> except for being
  aligned).  This format is that provided in the previous version of
  the package by the <b>apstrip</b> task.  It is now relegated to a
  special case.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION'  -->
  
