.. _wcsedit:

wcsedit: Edit an image wcs parameter
====================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wcsedit image parameter value axes1
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images for which the WCS is to be edited.  Image sections are
  ignored.  If the image does not exist a data-less image header is first
  created with the default WCS of dimensionality given by the <span style="font-family: monospace;">"wcsdim"</span>
  parameter.
  </dd>
  </dl>
  <dl id="l_parameter">
  <dt><b>parameter</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameter' Line='parameter' -->
  <dd>The WCS parameter to be edited. The WCS parameters recognized by
  WCSEDIT are: 1) the FITS WCS
  parameters crpix, crval, cd  and, 2) the IRAF WCS parameters ltv, ltm, wtype,
  axtype, units, label, and format.  Only one WCS parameter may be edited at a
  time.
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>The new parameter value. The numerical parameters crpix, crval, cd, ltv, and
  ltm will not be updated if WCSEDIT is unable to decode the parameter value
  into a legal floating point number.
  </dd>
  </dl>
  <dl id="l_axes1">
  <dt><b>axes1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='axes1' Line='axes1' -->
  <dd>The list of principal axes for which <i>parameter</i> is to be edited.
  Axes1 can
  be entered as a list of numbers separated by commas, e.g. <span style="font-family: monospace;">"1,2"</span> or as a
  range, e.g. <span style="font-family: monospace;">"1-2"</span>.
  </dd>
  </dl>
  <dl id="l_axes2">
  <dt><b>axes2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='axes2' Line='axes2' -->
  <dd>The list of dependent axes for which <i>parameter</i> is to be edited.
  Axes2 can
  be entered as a list of numbers separated by commas, e.g. <span style="font-family: monospace;">"1,2"</span> or as a
  range, e.g. <span style="font-family: monospace;">"1-2"</span>. The axes2 parameter is only required if
  <i>parameter</i> is <span style="font-family: monospace;">"cd"</span> or <span style="font-family: monospace;">"ltm"</span>.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"world"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "world"' -->
  <dd>The WCS to be edited.  The options are: the builtin systems <span style="font-family: monospace;">"world"</span> or
  <span style="font-family: monospace;">"physical"</span>, or a named system, e.g. <span style="font-family: monospace;">"image"</span> or <span style="font-family: monospace;">"multispec"</span>. The builtin system
  <span style="font-family: monospace;">"logical"</span> may not be edited.
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>If <i>wcs</i> is <span style="font-family: monospace;">"world"</span> the default WCS is edited. The default WCS
  is either 1) the value of the environment variable <span style="font-family: monospace;">"defwcs"</span> if
  set in the user's IRAF environment (normally it is undefined) and present
  in the image header,
  2) the value of the <span style="font-family: monospace;">"system"</span>
  attribute in the image header keyword WAT0_001 if present in the
  image header or, 3) the <span style="font-family: monospace;">"physical"</span> coordinate system.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>If <i>wcs</i> is <span style="font-family: monospace;">"physical"</span>, WCS is the pixel coordinate system of
  the original image, which may be different from the pixel coordinate system
  of the current image, if the current image is the result of an
  imcopy or other geometric transformation operation. In the <span style="font-family: monospace;">"physical"</span>
  coordinate system the ltv, ltm and the axis attribute
  parameters wtype, axtype, units, label, and format may be edited, but the FITS
  parameters crval, crpix, and cd cannot.
  </dd>
  </dl>
  <dl>
  <dt><b>name</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='name' Line='name' -->
  <dd>A user supplied wcs name.
  If the named WCS does not exist in the image, a new one of that
  name initialized to the identity transform, will be opened for editing, and
  the old WCS will be destroyed. This option should only be used for creating
  a totally new FITS WCS.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_wcsdim">
  <dt><b>wcsdim = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsdim' Line='wcsdim = 2' -->
  <dd>WCS dimensionality when creating a new data-less image header.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Edit the WCS interactively?
  </dd>
  </dl>
  <dl id="l_commands">
  <dt><b>commands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='commands' Line='commands = ""' -->
  <dd>The interactive editing command prompt.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken in interactive or non-interactive mode?
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update the image header in non-interactive mode? A specific command  exists
  to do this in interactive mode.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  WCSEDIT modifies the WCS of an existing image or creates a data-less image
  header of the dimensionality given by the <i>wcsdim</i> parameter.
  </p>
  <p>
  In non-interactive mode WCSEDIT replaces the current value of the WCS
  parameter <i>parameter</i> with the new value <i>value</i> in the headers of
  <i>images</i> and prints a summary of the new WCS on the terminal.  If
  <i>verbose</i> is <span style="font-family: monospace;">"no"</span> the summary is not printed.  If <i>verbose</i> is
  <span style="font-family: monospace;">"yes"</span> and <i>update</i> is <span style="font-family: monospace;">"no"</span>, the result of the editing operation
  is printed on the terminal but the header is not modified.
  </p>
  <p>
  The WCS parameter <i>parameter</i> may be one of: crval, crpix, cd, ltv, ltm,
  wtype, axtype, units, label, or format in either upper or lower case.
  The WCS array parameters crpix, crval, ltv, wtype, axtype, units, label,
  and format
  may be edited for more than one axis at a time by setting <i>axes1</i> to a
  range of axes values. The WCS matrix parameters cd and ltm may be edited for
  more than one axis at a time by setting both <i>axes1</i> and <i>axes2</i> to
  a range of values. In this case, if no <i>axes2</i> values are entered,
  <i>axes2</i> = <span style="font-family: monospace;">""</span>, the
  diagonal elements of the cd and ltm matrices specified by <i>axes1</i> are
  edited. A single non-diagonal element of the cd or ltm matrices can be
  edited by setting <i>axis1</i> and <i>axis2</i> to a single number.
  </p>
  <p>
  The user can create a new WCS from scratch by setting
  <i>wcs</i> to a name different from the name of the WCS in the image header.
  A new WCS with the same dimension as the image and initialized
  to the identity transformation  is presented to the user for editing.
  IF THE USER UPDATES THE IMAGE HEADER AFTER EDITING THE NEW WCS, ALL
  PREVIOUS WCS INFORMATION IS LOST.
  </p>
  <p>
  In interactive mode, WCSEDIT displays the current WCS
  on the terminal if <i>verbose</i> = <span style="font-family: monospace;">"yes"</span>, and prompts the user for 
  an editing command.  The supported editing commands are shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
                        BASIC  COMMANDS
  
  ?               Print the WCSEDIT commands
  show            Print out the current WCS
  update          Quit WCSEDIT and update the image WCS
  quit            Quit WCSEDIT without updating the image WCS
  
                PARAMETER DISPLAY AND EDITING COMMANDS
  
  crval  [value axes1]            Show/set the FITS crval parameter(s)
  crpix  [value axes1]            Show/set the FITS crpix parameter(s)
  cd     [value axes1 [axes2]]    Show/set the FITS cd parameter(s)
  ltv    [value axes1]            Show/set the IRAF ltv parameter(s)
  ltm    [value axes1 [axes2]]    Show/set the IRAF ltm parameter(s)
  wtype  [value axes1]            Show/set the FITS/IRAF axes transform(s)
  axtype [value axes1]            Show/set the FITS/IRAF axis type(s)
  units  [value axes1]            Show/set the IRAF units(s)
  label  [value axes1]            Show/set the IRAF axes label(s)
  format [value axes1]            Show/set the IRAF axes coordinate format(s)
  </pre></div>
  </section>
  <section id="s_the_wcs_parameters">
  <h3>The wcs parameters</h3>
  <p>
  Below is a list of the WCS parameters as they appear encoded in the in the
  IRAF image header. Parameters marked with E can be edited directly with
  WCSEDIT. Parameters marked with U should be updated automatically by WCSEDIT
  if the proper conditions are met. The remaining parameters cannot be edited
  with WCSEDIT. A brief description of the listed parameters is given below.
  For a detailed description of the meaning of these parameters, the user
  should consult the two documents listed in the REFERENCES section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  WCSDIM          WCS dimension (may differ from image)
  
  CTYPEn   U      coordinate type
  CRPIXn   E      reference pixel
  CRVALn   E      world coords of reference pixel
  CDi_j    E      CD matrix
  
  CDELTn   U      CDi_i if CD matrix not used (input only)
  CROTA2   U      rotation angle if CD matrix not used
  
  LTVi     E      Lterm translation vector
  LTMi_j   E      Lterm rotation matrix
  
  WATi_jjj U      WCS attributes for axis I (wtype,axtype,units,label,format)
  WAXMAPii        WCS axis map
  </pre></div>
  <p>
  The WCSDIM and WAXMAP parameters cannot be edited by WCSEDIT, unless a
  new WCS is created in which case WCSDIM is set to
  the dimension of the input image and the axis map is deleted.
  The FITS parameters CRPIX, CRVAL, and CD
  define the transformation between the world coordinate system and the pixel
  coordinate system of the image and may be edited directly.  The more general
  FITS CD matrix notation supersedes the FITS CDELT/CROTA notation if both are
  present on input, and is used by preference on output.  The FITS parameter
  CTYPE cannot be edited directly by WCSEDIT but is correctly updated on
  output using the current values of the WCS parameters wtype and axtype
  parameters, if there was a pre-existing FITS header in the image.  On input
  IRAF currently recognizes the following values of the FITS parameter CTYPE:
  RA---TAN and DEC--TAN (the tangent plane sky projection), RA---SIN and
  DEC--SIN (the sin sky projection), RA---ARC and DEC--ARC (the arc sky
  projection), LINEAR, and MULTISPEC, from which it derives the correct values
  for wtype and axtype.
  </p>
  <p>
  The LTV and LTM are IRAF parameters which define the transformation between
  the
  current image pixel coordinate system and the original pixel coordinate system,
  if the current image was derived from a previous
  image by a geometric transformation, e.g. IMCOPY or IMSHIFT.
  Both parameters may be edited directly by WCSEDIT, but with the exception
  of resetting the LTV vector to 0 and the LTM matrix to the identity
  matrix it is not usually desirable to do so. The task WCSRESET can also
  be used for this purpose.
  </p>
  <p>
  The WATi_jjj parameters are not directly accessible by WCSEDIT but the five
  axis attributes which are encoded under these keywords (wtype, axtype,
  units, label, and format) may be edited.
  The IRAF WCS code currently
  recognizes the following values for <span style="font-family: monospace;">"wtype"</span>: <span style="font-family: monospace;">"linear"</span>, <span style="font-family: monospace;">"tan"</span>, <span style="font-family: monospace;">"sin"</span>,
  <span style="font-family: monospace;">"arc"</span>, and <span style="font-family: monospace;">"multispec"</span>.  If <span style="font-family: monospace;">"wtype"</span> is not defined or cannot
  be decoded by the WCS code <span style="font-family: monospace;">"linear"</span> is assumed.
  Axtype should be <span style="font-family: monospace;">"ra"</span> or <span style="font-family: monospace;">"dec"</span> if wtype is one of the sky projections
  <span style="font-family: monospace;">"tan"</span>, <span style="font-family: monospace;">"sin"</span> or <span style="font-family: monospace;">"arc"</span>, otherwise it should be undefined.
  WCSEDIT will combine the values of <span style="font-family: monospace;">"wtype"</span> and <span style="font-family: monospace;">"axtype"</span> on output to
  produce the correct value of the FITS keyword CTYPE.
  The <span style="font-family: monospace;">"label"</span> and <span style="font-family: monospace;">"units"</span> parameter may be set to any string constant.
  Format must be set to a legal IRAF format as described in the section
  below.
  </p>
  </section>
  <section id="s_formats">
  <h3>Formats</h3>
  <p>
  A  format  specification has the form <span style="font-family: monospace;">"%w.dCn"</span>, where w is the field
  width, d is the number of decimal places or the number of digits  of
  precision,  C  is  the  format  code,  and  n is radix character for
  format code <span style="font-family: monospace;">"r"</span> only.  The w and d fields are optional.  The  format
  codes C are as follows:
      
  </p>
  <div class="highlight-default-notranslate"><pre>
  b       boolean (YES or NO)
  c       single character (c or '\c' or '\0nnn')
  d       decimal integer
  e       exponential format (D specifies the precision)
  f       fixed format (D specifies the number of decimal places)
  g       general format (D specifies the precision)
  h       hms format (hh:mm:ss.ss, D = no. decimal places)
  m       minutes, seconds (or hours, minutes) (mm:ss.ss)
  o       octal integer
  rN      convert integer in any radix N
  s       string (D field specifies max chars to print)
  t       advance To column given as field W
  u       unsigned decimal integer
  w       output the number of spaces given by field W
  x       hexadecimal integer
  z       complex format (r,r) (D = precision)
  
  Conventions for w (field width) specification:
  
      W =  n      right justify in field of N characters, blank fill
          -n      left justify in field of N characters, blank fill
          0n      zero fill at left (only if right justified)
  absent, 0       use as much space as needed (D field sets precision)
  
  Escape sequences (e.g. "\n" for newline):
  
  \b      backspace   (not implemented)
       formfeed
  \n      newline (crlf)
  \r      carriage return
  \t      tab
  \"      string delimiter character
  \'      character constant delimiter character
  \\      backslash character
  \nnn    octal value of character
  
  Examples
  
  %s          format a string using as much space as required
  %-10s       left justify a string in a field of 10 characters
  %-10.10s    left justify and truncate a string in a field of 10 characters
  %10s        right justify a string in a field of 10 characters
  %10.10s     right justify and truncate a string in a field of 10 characters
  
  %7.3f       print a real number right justified in floating point format
  %-7.3f      same as above but left justified
  %15.7e      print a real number right justified in exponential format
  %-15.7e     same as above but left justified
  %12.5g      print a real number right justified in general format
  %-12.5g     same as above but left justified
  
  %h          format as nn:nn:nn.n
  %15h        right justify nn:nn:nn.n in field of 15 characters
  %-15h       left justify nn:nn:nn.n in a field of 15 characters
  %12.2h      right justify nn:nn:nn.nn
  %-12.2h     left justify nn:nn:nn.nn
  
  %H          / by 15 and format as nn:nn:nn.n
  %15H        / by 15 and right justify nn:nn:nn.n in field of 15 characters
  %-15H       / by 15 and left justify nn:nn:nn.n in field of 15 characters
  %12.2H      / by 15 and right justify nn:nn:nn.nn
  %-12.2H     / by 15 and left justify nn:nn:nn.nn
  
  \n          insert a newline
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Detailed documentation for the IRAF world coordinate system interface MWCS
  can be found in the file <span style="font-family: monospace;">"iraf$sys/mwcs/MWCS.hlp"</span>. This file can be
  formatted and printed with the command <span style="font-family: monospace;">"help iraf$sys/mwcs/MWCS.hlp fi+ |
  lprint"</span>.  Details of the FITS header world coordinate system interface can
  be found in the document <span style="font-family: monospace;">"World Coordinate Systems Representations Within the
  FITS Format"</span> by Hanisch and Wells, available from our anonymous ftp
  archive.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Change the default output coordinate formats for an image with a defined
  FITS tangent plane projection in its header, for the RA axis (axis 1), and the
  DEC axis (axis 2) to %H and %h respectively. Then display the image and use
  rimcursor to produce a coordinate list of objects whose coordinates are
  printed as hh:mm:ss.s and dd:mm:ss.s respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image format %H 1
  cl&gt; wcsedit image format %h 2
  cl&gt; display image 1
  cl&gt; rimcursor wcs=world &gt; coordlist
      ... mark the coordinates
  </pre></div>
  <p>
  2. Change the default sky projection for an image with a defined tangent
  plane projection to one with a sin projection.  Note that wtype for both
  axis1 and axis2 must be changed to <span style="font-family: monospace;">"sin"</span>. Check the results first before
  doing the actual update.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image wtype sin 1-2 update-
  cl&gt; wcsedit image wtype sin 1-2
  </pre></div>
  <p>
  3. Change the diagonal elements of the FITS cd matrix to 2.0. The off
  diagonal elements are 0.0. This is equivalent to resetting the image scale.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image cd 2.0 1-2 ""
  </pre></div>
  <p>
  4. Set the value of the FITS cd matrix elements, cd[2,1] and cd[1,2] to 0.0. 
  This removes any rotation/skew from the WCS definition.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image cd 0.0 2 1
  cl&gt; wcsedit image cd 0.0 1 2
  </pre></div>
  <p>
  5. Change the FITS crval value for axis 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image crval 47.85 2
  </pre></div>
  <p>
  6. Create a totally new WCS for an image, deleting the previous WCS
  and set the diagonal elements of the cd matrix to 0.68. 0.68 is the
  scale of the 36 inch telescope at KPNO.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image cd 1.5 1-2 wcs="kpno9m"
  </pre></div>
  <p>
  7. Interactively edit the WCS of an image. with an existing FITS header.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image interactive+
  
      ... summary of current WCS is printed on terminal
  
      wcsedit: ?
  
      ... user types in ? to see list of wcsedit commands
  
      wcsedit: cd 2.0 1-2
  
      ... user changes the scale of the WCS
  
      wcsedit: format %0.3f 1-2
  
      ... user changes format so the coordinates will be printed
          out with 3 decimals of precision by any tasks which
          can read the WCS format parameter such as rimcursor
          and listpixels
  
      wcsedit: show
  
      ... user checks the new wcs
  
      wcsedit: update
  
      ... user quits editor and updates the image header
  </pre></div>
  <p>
  8. Open and edit a new WCS for an image. Any pre-existing WCS will
  be destroyed, assuming that the default wcs is not <span style="font-family: monospace;">"newwcs"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsedit image wcs=newwcs intera+
  
      wcsedit: ....
      wcsedit: ....
  
      ... edit in the desired values
  
      wcsedit: update
  
      ... update the image header.
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The IRAF WCS code supports the dimensional reduction of images,
  for example creating an image with smaller dimensions than its parent, but
  may not be fully compatible with FITS when this occurs.
  In this case user may need to fix up an illegal or
  incorrect WCS with HEDIT or HFIX bypassing the WCS code used by WCSEDIT.
  </p>
  <p>
  WCSEDIT does not permit the user to edit any parameters encoded in the
  WATi_jjj keywords other than the five listed: wtype, axtype, units, label,
  and format. For example WCSEDIT cannot be used to edit the <span style="font-family: monospace;">"speci"</span> parameters
  used by the IRAF spectral reductions code <span style="font-family: monospace;">"multispec"</span> format. The spectral
  reduction code itself should be used to do this, although hfix can
  be used to fix a serious problem should it arise.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  wcsreset,hedit,hfix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'THE WCS PARAMETERS' 'FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
