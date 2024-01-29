.. _xtalkcor:

xtalkcor: Apply crosstalk corrections
=====================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  XTALKCOR reads a file containing coefficients for a simple crosstalk
  interaction between extensions in a mosaic exposure and applies
  the correction.  The correction takes the form
  </p>
  <div class="highlight-default-notranslate"><pre>
  corrected = victim - (scale1 * source1 + scale2 * source2 + ...)
  </pre></div>
  <p>
  where the arithmetic is done on each pixel in the victim image extension
  with the matching pixels in the source image extensions and the scales are
  numerical coefficients.  Alternatively or in addition, bad pixel masks may
  be generated flagging pixels which have corrections greater than a
  specified threshold or which have source pixels greater than a theshold.
  This task may be executed as part of <b>ccdproc</b>.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  xtalkcor input output bpmasks xtalkfiles
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input mosaic exposures to be corrected.  Mosaic files in which
  the the extensions contain the keyword XTALKCOR, indicating file
  has been previously corrected, are silently skipped. 
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output corrected mosaic exposures.  If an empty list is specified
  then no output correction is produced otherwise the output list must
  match the input list.  When <i>split</i>=no the output is a corrected
  multiextension file.  If <i>split</i>=yes each extension in the input
  will be corrected to a separate single image file using the output name
  as the rootname and appending the extension name preceded by <span style="font-family: monospace;">"_"</span>.
  </dd>
  </dl>
  <dl id="l_bpmasks">
  <dt><b>bpmasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmasks' Line='bpmasks' -->
  <dd>List of output bad pixel masks.  The same rules apply as for the <i>output</i>
  parameter except currently splitting is implied since a multiextension format
  is not produced.
  </dd>
  </dl>
  <dl id="l_xtalkfiles">
  <dt><b>xtalkfiles = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xtalkfiles' Line='xtalkfiles = ""' -->
  <dd>List of crosstalk coefficient files or header keywords containing the file
  name.  A header keyword reference is specified by preceding the keyword
  with <span style="font-family: monospace;">'!'</span>.  Note that only the first extension of the input file is used to
  resolve the keyword reference.  The list may consist of a single crosstalk
  file reference, in which case it applies to all the elements of the input
  list, of a list which matches the input list in number.  The format of the
  file has three as explained in the DESCRIPTION section.  This is the same
  format produced by the <b>xtcoeff</b> task.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">"!datasec"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = "!datasec"' -->
  <dd>Section value or keyword to a section value, as indicated by a leading <span style="font-family: monospace;">'!'</span>,
  selecting the part of the image to be corrected.  If no value is specified
  or the keyword doesn't exist then the whole image is used.  This parameter
  is primarily needed if overscan regions to not match after flipping the
  data into amplifier readout order.
  </dd>
  </dl>
  <dl id="l_bpmthreshold">
  <dt><b>bpmthreshold = -10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmthreshold' Line='bpmthreshold = -10.' -->
  <dd>Threshold for identifying pixels in the output bad pixel masks.  A positive
  value flags pixels where any of the contributing source pixels exceeds
  the specified threshold.  A negative value flags pixels where the
  absolute value of the correction exceeds the absolute value of the
  threshold.
  </dd>
  </dl>
  <dl id="l_split">
  <dt><b>split = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='split' Line='split = no' -->
  <dd>Output the corrected extension images as separate single images.  Since
  the procedure produces single images as part of the operation this option
  saves the time needed to rebuild a final multiextension file.
  </dd>
  </dl>
  <dl id="l_fextn">
  <dt><b>fextn = <span style="font-family: monospace;">"fits"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fextn' Line='fextn = "fits"' -->
  <dd>File extension for the input and output exposure files.
  </dd>
  </dl>
  <dl id="l_noproc">
  <dt><b>noproc = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='noproc' Line='noproc = no' -->
  <dd>Do no processing but simply print whether the operation is to be done or
  not based on the presence of an XTALKCOR header keyword?  This is
  intended for use when this task is executed as part of <b>ccdproc</b>.
  </dd>
  </dl>
  <p>
  The following package parameters are also used.
  </p>
  <dl id="l_pixeltype">
  <dt><b>pixeltype</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixeltype' Line='pixeltype' -->
  <dd>The output pixel type for the corrected exposures.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile' -->
  <dd>Log file to record the operations.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose' -->
  <dd>Print processing information to the terminal.
  </dd>
  </dl>
  <dl id="l_im_bufsize">
  <dt><b>im_bufsize</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='im_bufsize' Line='im_bufsize' -->
  <dd>File buffering size in megabytes per read or write operation.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Xtalkcor</b> reads a file containing coefficients for a simple crosstalk
  interaction between extensions in a mosaic exposure and creates a
  corrected copy of the input images and/or a bad pixel mask identifying
  pixels affected by crosstalk.  The corrected images may be in a
  extension file or separate images depending on the <i>split</i> parameter.
  Pixel masks are always separate files in the current version.  The
  output names may be specified as rootnames or as a full list for every
  output file.
  </p>
  <p>
  The crosstalk correction takes the form
  </p>
  <div class="highlight-default-notranslate"><pre>
  corrected = victim - (scale1 * source1 + scale2 * source2 + ...)
  </pre></div>
  <p>
  where the arithmetic is done on each pixel in the victim image extension
  with the matching pixels in the source image extensions and the scales
  are numerical coefficients.  Bad pixel masks may be generated by flagging
  pixels which have corrections greater than a specified threshold or which
  have source pixels greater than a theshold.  This task may be  executed
  as part of <b>ccdproc</b>.
  </p>
  <p>
  The crosstalk occurs during the simultaneous readout of multiple
  amplifiers.  Thus the victim and source pixels must be matched in
  <span style="font-family: monospace;">"amplifier coordinates"</span>.  This version assumes the extensions are matched
  by flips of lines or columns.  The flips are identified by the signs of the
  keywords ATM1_1 for line flips and ATM2_2 for column flips.
  </p>
  <p>
  If the data contain regions, such as overscan regions, which are recorded
  in such a way that after flipping the data into matching amplifier order
  the data do not correctly match then the section keyword must be used.
  The common case is where data is recorded with the overscan in the same
  location in the image extensions though the data sections have been flipped.
  </p>
  <p>
  The crosstalk coefficient file is specified either explicitly or by 
  reference to a header keyword containing the name of the file.  To
  reference a keyword precede the keyword name with <span style="font-family: monospace;">'!'</span>.  Note the only
  the first extension is used to find the referenced keyword.
  </p>
  <p>
  A crosstalk file consists of lines
  </p>
  <div class="highlight-default-notranslate"><pre>
  victim source scale
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"victim"</span> is an extension name for the victim image to be corrected,
  <span style="font-family: monospace;">"source"</span> is the extension name for a source image, and scale is the scale
  coefficient.  When more than one source extension affects a victim
  extension there will be multiple lines.  Any lines where the first three
  fields are not in this format are ignored.  Also any line beginning with
  <span style="font-family: monospace;">'#'</span> is treated as a comment and ignored.  This format is generated by the
  task <b>xtcoeff</b> though it can be created or modified with any text
  editor as well.  Examples are given in the EXAMPLE section.
  </p>
  <p>
  The crosstalk corrected output images will contain the keyword
  XTALKCOR giving the time the correction was applied and the source
  extensions and coefficients used.  Any extension in the input image which
  does not have an entry in the crosstalk file will be copied to the
  crosstalk corrected image without change.  It will also contain the XTALKCOR
  keyword with the time followed by an indication that no crosstalk
  correction was required.  In addtion to the XTALKCOR keyword, the keyword
  XTALKFILE is added giving the name of the crosstalk file used.
  </p>
  <p>
  A bad pixel mask is created when a file name or names is specified for
  the <b>bpmasks</b> parameter.  Currently if only a rootname is specified
  separate pixel list files are produced with the extension appended; i.e. a
  filename of the form root_extension.pl will be produced.  The crosstalk
  affected pixels for each victim extension are flagged either by the
  magnitude of the correction or by source pixel values exceeding a positive
  threshold.  The <i>bpmthreshold</i> parameter specifies the threshold
  and the type of flagging.  A positive value will flag any victim pixel
  in which any of the source pixels exceed the threshold.  Note that only
  one source exceeding the threshold is needed in the case where there are
  multiple sources.  A negative value of the threshold parameter compares
  the magnitude of the correction (computed even if no output corrected file
  is generated) to the absolute value of the specified threshold.  Note that
  the bad pixel mask is not merged with to any other bad pixel mask nor is
  the name added to the header.  This must be done separately if desired.
  </p>
  </section>
  <section id="s_keywords">
  <h3>Keywords</h3>
  <dl id="l_XTALKCOR">
  <dt><b>XTALKCOR</b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='XTALKCOR' Line='XTALKCOR' -->
  <dd>Added to all extensions in an output crosstalk corrected file.
  The value includes a time stamp and the crosstalk coefficients and
  extensions.  If this keyword is present (the value is ignored) in the
  input file then the file will be silently skipped by the task.  To force
  a second round of correction would require this keyword to be manually
  deleted.
  </dd>
  </dl>
  <dl id="l_XTALKFILE">
  <dt><b>XTALKFILE</b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='XTALKFILE' Line='XTALKFILE' -->
  <dd>Added to all extensions in an output crosstalk
  corrected file.  The value is the crosstalk file used.
  </dd>
  </dl>
  <dl id="l_ATM1_1">
  <dt><b>ATM1_1, ATM2_2</b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='ATM1_1' Line='ATM1_1, ATM2_2' -->
  <dd>The sign of these keywords define the amplifier readout direction.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. A crosstalk coeffient file created by <b>xtcoeff</b> is shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; page xtalk.dat
  # XTCOEFF: NOAO/IRAF V2.11.3EXPORT valdes@puppis Fri 10:15:45 18-Aug-2000
  #   Images: obj110
  
  im1     im2      0.001546 (0.000010, 153.7)
  im2     im1      0.000426 (0.000006, 75.1)
  im3     im4      0.001613 (0.000091, 17.8)
  im4     im3      0.001672 (0.000014, 116.4)
  im5
  im6     im5      0.001382 (0.000016, 86.1)
  im7     im8      0.000244 (0.000022, 11.2)
  im8     im7      0.001696 (0.000011, 161.1)
  </pre></div>
  <p>
  Note that the comments and the parts in paraenthesis will be ignored.
  This will cause the following operations to be performed.
  </p>
  <p>
  2.  The above crosstalk correction is applied with the following
  command.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; xtalkcor obj110 xtcor110 xtalkfile=xtalk.dat
  obj110[im1]: Aug 22 10:05 Crosstalk is 0.00155*im2
  obj110[im2]: Aug 22 10:05 Crosstalk is 4.26E-4*im1
  obj110[im3]: Aug 22 10:06 Crosstalk is 0.00161*im4
  obj110[im4]: Aug 22 10:06 Crosstalk is 0.00167*im3
  obj110[im5]: Aug 22 10:07 No crosstalk correction required
  obj110[im6]: Aug 22 10:07 Crosstalk is 0.00138*im5
  obj110[im7]: Aug 22 10:08 Crosstalk is 2.44E-4*im8
  obj110[im8]: Aug 22 10:08 Crosstalk is 0.0017*im7
  </pre></div>
  <p>
  3.  The header information added by the previous example can be
  examined with the following commands.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; imhead xtcor110[im1] l+ |match XTALKCOR
  XTALKCOR= 'Aug 22 10:05 Crosstalk is 0.00155*im2'
  ms&gt; msccmd "hselect $input xtalkcor yes" xtcor110
  "Aug 22 10:05 Crosstalk is 0.00155*im2"
  "Aug 22 10:05 Crosstalk is 4.26E-4*im1"
  "Aug 22 10:06 Crosstalk is 0.00161*im4"
  "Aug 22 10:06 Crosstalk is 0.00167*im3"
  "Aug 22 10:07 No crosstalk correction required"
  "Aug 22 10:07 Crosstalk is 0.00138*im5"
  "Aug 22 10:08 Crosstalk is 2.44E-4*im8"
  "Aug 22 10:08 Crosstalk is 0.0017*im7"
  </pre></div>
  <p>
  Attempting to apply the crosstalk correction again will do nothing because
  of the presence of the XTALKCOR keywords.
  </p>
  <p>
  4.  To execute a correction using a header keyword giving the
  coefficient file use the following modification to example 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; xtalkcor obj110 xtcor110 xtalkfile=!xtalkfil
  </pre></div>
  <p>
  5.  An example of a crosstalk file where there are multiple sources is
  shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; page xtalk.dat
  # XTCOEFF: NOAO/IRAF V2.11.3EXPORT valdes@puppis Fri 10:15:45 18-Aug-2000
  #   Images: obj110
  
  im1     im2      0.001546 (0.000010, 153.7)
  im1     im3      0.000426 (0.000006, 75.1)
  im1     im4      0.001613 (0.000091, 17.8)
  im2     im1      0.001672 (0.000014, 116.4)
  im2     im3      0.001382 (0.000016, 86.1)
  im2     im4      0.000244 (0.000022, 11.2)
  </pre></div>
  <p>
  The correction output would then show
  </p>
  <div class="highlight-default-notranslate"><pre>
  obj614[im1]: Jan  5  9:31 Crosstalk is 0.001546*im2+0.000426*im3+0.001613*im4
  obj614[im2]: Jan  5  9:31 Crosstalk is 0.001672*im1+0.001382*im3+0.000244*im4
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_XTALKCOR">
  <dt><b>XTALKCOR - V5.0: November 16, 2010</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='XTALKCOR' Line='XTALKCOR - V5.0: November 16, 2010' -->
  <dd>The ability to use a section to restrict the correction to a part of the
  input image was added.  This was needed for data where overscan regions
  do not match after flipping the data into amplifier readout order.
  </dd>
  </dl>
  <dl id="l_XTALKCOR">
  <dt><b>XTALKCOR - V4.1: January 6, 2001</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='XTALKCOR' Line='XTALKCOR - V4.1: January 6, 2001' -->
  <dd>Extension changes to support readouts with multiple amplifiers.  The script
  version was replaced by a compiled task which efficiently deals with multiple
  sources and with different amplifier readout directions.  The new version
  supports creation of output bad pixel masks.
  </dd>
  </dl>
  <dl id="l_XTALKCOR">
  <dt><b>XTALKCOR - V3.2: August 27, 1999</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='XTALKCOR' Line='XTALKCOR - V3.2: August 27, 1999' -->
  <dd>The crosstalk file can be specified through a keyword.
  </dd>
  </dl>
  <dl id="l_XTALKCOR">
  <dt><b>XTALKCOR - V3.0: April 1999</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='XTALKCOR' Line='XTALKCOR - V3.0: April 1999' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  xtcoeff, ccdproc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'KEYWORDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
