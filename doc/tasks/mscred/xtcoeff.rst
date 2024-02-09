.. _xtcoeff:

xtcoeff: Compute crosstalk coefficients
=======================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  Crosstalk coefficients between pairs of source and victim CCDs, specified
  as extensions in an MEF file, are computed.  The output is a file suitable
  for use with XTALKCOR or CCDPROC.  There is an option to examine and
  interact with the data.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  xtcoeff input output victim source
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of mosaic exposures in multiextension format (MEF).  The crosstalk
  coefficient for a pair of extensions is computed combining all the input
  exposures.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Optional output crosstalk file.  The format of this file is that used by
  <b>xtalkcor</b> or <b>ccdproc</b> provided each victim extension is specified
  once and only once (and generally in the same order as in the input MEF
  file).  One may include more than one source extension for each victim
  extension.  If the <i>verbose</i> option is set the same information in the
  crosstalk file will also be written to the terminal.
  </dd>
  </dl>
  <dl id="l_victim">
  <dt><b>victim = <span style="font-family: monospace;">"im1,im2,im3,im4,im5,im6,im7,im8"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='victim' Line='victim = "im1,im2,im3,im4,im5,im6,im7,im8"' -->
  <dd>List of victim extension names in the MEF input files.  This list is
  matched with the list of source extension names specified by the
  <i>source</i> parameter.  A crosstalk coefficient will be measured for each
  extension specified in the list.  The same extension may be specified more
  than once to compare with source extensions that should not contribute to
  the crosstalk.  Large lists may be specified with an @file.
  If the specified @file is not found in the current directory it is sought
  in xtcoeff$.  Use <span style="font-family: monospace;">"page xtcoeff$README"</span> for available lists.
  </dd>
  </dl>
  <dl id="l_source">
  <dt><b>source = <span style="font-family: monospace;">"im2,im1,im4,im3,im6,im5,im8,im7"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='source' Line='source = "im2,im1,im4,im3,im6,im5,im8,im7"' -->
  <dd>List of source extension names in the MEF input files.  This list is
  matched with the list of victim extension names specified by the
  <i>victim</i> parameter.  The same extension may be specified more than
  once.  Large lists may be specified with an @file.
  If the specified @file is not found in the current directory it is sought
  in xtcoeff$.  Use <span style="font-family: monospace;">"page xtcoeff$README"</span> for available lists.
  </dd>
  </dl>
  <dl id="l_vbkg">
  <dt><b>vbkg = <span style="font-family: monospace;">""</span>, sbkg = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vbkg' Line='vbkg = "", sbkg = ""' -->
  <dd>List of victim and source backgrounds.  If not specified then a simple
  percentile background for each line is used.  The values may be full
  images, <span style="font-family: monospace;">"maps"</span> which are reduced scale images typically produced by
  <b>ace</b> or <b>objmasks</b>, or constants.  The image/map files must have
  the same extensions as in the input data.  Note that if one file contains
  the backgrounds for all the extensions then the victim and source
  background files may be the same.  A good victim background is important
  while the default percentile source background is normally adequate.
  </dd>
  </dl>
  <dl id="l_masks">
  <dt><b>masks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masks' Line='masks = ""' -->
  <dd>List of object masks for each input image.  Typically this will be produced
  by a task like <b>objmasks</b>.  The masks must have extensions matching
  the victim extensions.
  </dd>
  </dl>
  <dl id="l_smin">
  <dt><b>smin = 20000, smax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='smin' Line='smin = 20000, smax = INDEF' -->
  <dd>Range of pixel values in the source extension that are used in measuring
  the crosstalk.  These values should be those which cause a crosstalk
  visible above the background in the victim extension.  Typically these will
  be values near and above saturation.  The number of pixels considered has
  an impact on the computation speed and memory so the values should also be
  such as to select only a small percent of the data in the source
  extension.  A value of INDEF for the maximum selects all source pixels
  above the minimum value.  The minimum value should be explicitly specified
  but a value of INDEF defaults to 10000.
  </dd>
  </dl>
  <dl id="l_medfactor">
  <dt><b>medfactor = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='medfactor' Line='medfactor = 0.5' -->
  <dd>Median factor for defining the backgrounds when background
  images/maps/constants are not specified.  The background for each pair of
  source and victim pixels is computed by taking the Nth brightest pixel in
  the same line.  N is computed as the <i>medfactor</i> parameter times the
  number of pixels in the line.  A value of 0.5 selects the standard median
  (half the pixel values are above and half below).  This factor may be
  adjusted from 0.5 to account for biases from objects by considering pairs
  of extensions where no crosstalk is expected and adjusting this factor to
  make the crosstalk coefficients scatter around zero.
  </dd>
  </dl>
  <dl id="l_maxcoeff">
  <dt><b>maxcoeff = 0.01</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxcoeff' Line='maxcoeff = 0.01' -->
  <dd>A coefficient estimate is computed for each pair of source and victim
  pixels as (victim-background)/source.  To reject victim pixels which
  have contaminating objects other than the crosstalk ghosts at that
  position, all estimates above this value are rejected immediately.  Note
  that computation of the final coefficient from all the individual estimates
  uses iterative rejection.  However, grossly invalid values will
  adversely affect the iterative rejection.  This parameter value need
  only be set approximately.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 3, low = 3., high = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 3, low = 3., high = 3.' -->
  <dd>The number of rejection fitting iterations and the lower and upper sigma
  thresholds used when combining the individual pixel coefficient estimates
  into a final estimate.  These parameters are from <b>icfit</b>.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>The determination of a single coefficient from all the
  estimates of the individual pixels consists of fitting a constant function
  (effectively an average) with iterative rejection.  When this parameter
  is yes the pixel coefficient estimates are plotted against the source
  pixel values and the <b>icfit</b> interactive fitting routine is entered.
  This allows interactive examination of the data, rejection of points, and
  selection of sample regions.  When this parameter is no the same fitting
  routine is used in non-interactive mode.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the measurement results to the terminal?
  </dd>
  </dl>
  <dl id="l_clobber">
  <dt><b>clobber</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clobber' Line='clobber' -->
  <dd>This is a query parameter which is typically not set before hand.  It is
  used only when the specified output crosstalk file already exists.  If it
  is not specified on the command line then a query will occur if the output
  crosstalk file exists.  To avoid a query and force a specific action
  specify the parameter on the command line.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XTCOEFF measures crosstalk coefficients relating the signals from pairs
  of extensions in multiextension format (typically pairs of CCDs in raw
  mosaic exposures).  The coefficient is defined by the relation
  </p>
  <div class="highlight-default-notranslate"><pre>
  &lt;(V - V_b) / (S - S_b)&gt;
  </pre></div>
  <p>
  where V is the victim image, V_b is the background in the victim image,
  S is the source image, and S_b is the background in the source image.
  The average is computed over the source pixels between <i>smin</i> and
  <i>smax</i> and the victim pixels not in an object <i>mask</i>
  (if one is specified).
  </p>
  <p>
  The pairs of extensions are specified by the parameters <i>victim</i>
  and <i>source</i>.  The lists may be comma separate extension names
  (note that extension positions may also be used) or an @file.  When
  the <b>mscred</b> package is loaded the logical directory xtcoeff$ is
  defined.  This may be reset by the user if desired.  If a specified
  @file is not found the directory prefix xtcoeff$ is added.  This allows
  using a library of @files without having to use the directory path.
  To check the contents use
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; dir xtcoeff
  ms&gt; page xtcoeff$README
  </pre></div>
  <p>
  The second command depends on there being a descriptive file in the
  directory.
  </p>
  <p>
  Each combination of extension names is applied to the <i>input</i>,
  <i>vbkg</i>, <i>sbkg</i>, and <i>masks</i> files.  The last three are
  optional.  the victim and source backgrounds may be in the same
  multiextension file.  The object masks, if specified, will also usually
  be multiextension files of <span style="font-family: monospace;">"pixel mask"</span> extensions.  The backgrounds
  and object masks are typically produced by the task <b>objmasks</b>.
  </p>
  <p>
  The coefficient for a particular pair of extensions is estimated by
  collecting measurements of
  </p>
  <div class="highlight-default-notranslate"><pre>
  (V - V_b) / (S - S_b)
  </pre></div>
  <p>
  for all source values within the range specified by <i>smin</i> and
  <i>smax</i> and victim values not in the object mask (if specified).
  Contaminating objects in the victim are also roughly excluded by requiring
  that a measurement by below the value specified by <i>maxcoeff</i>.
  An iterative rejection of outliers also minimizes the effects of
  contaminating objects.
  </p>
  <p>
  If no background file or constant is specified by the <i>vbkg</i>
  or <i>sbkg\R parameters a background estimate is computed for
  each line by taking the Nth brightest value.  N is computed
  by taking the specified fImedfactor</i> value times the number of pixels
  in the line.  A value of 0.5 for the factor is the classical median but
  the value may be adjusted to compensate for biases from objects.  This
  can be done by using source extensions which are known not to contribute
  crosstalk and running this task with adjustments to the factor until
  the coefficient values are zero within the uncertainties of the calculation.
  </p>
  <p>
  A good victim background is very important in computing the crosstalk
  coefficients.  Therefore, it is strongly recommended that a background
  be determined externally.  The source background is not very critical
  and the line median is adequate, though computing a background normally
  is done over all extensions so a source background will generally be
  available if the victim background is determined.
  </p>
  <p>
  The set of coefficients from individual pairs of pixels are combined into a
  single coefficient estimate by fitting a constant to the coefficients
  verses the source pixel value.  This is equivalent to computing the
  average.  However, a fitting algorithm is used to allow examining the data
  graphically to check for trends away from the assumed crosstalk relation
  given earlier.  The fitting approach also allows using the standard ICFIT
  routines for examining the data interactively if the <i>interactive</i>
  parameter is set.  During interactive fitting, points may be explicitly
  deleted and sample regions in the source intensity axes may be defined.
  The fitting, both interactive and non-interactive, includes iterative
  rejection of outlyers.  The iterative rejection is is controled by the
  parameters <i>niterate</i>, <i>low</i>, and <i>high</i> which are the number
  of iterations and the sigma clipping factors.
  </p>
  <p>
  The output of this program includes a banner with the input used and
  a table with the victim extension, the source extension, the estimated
  coefficient value, the estimated uncertainty in the coefficient, and
  the number of sigma from zero (the absolute value of the ratio of the
  coefficient and the uncertainty).  The latter two values are in parentheses
  and will be ignored by the calibration tasks that uses the crosstalk
  file.  The output is may be written to a specified file, if one is given
  with the <i>output</i> parameter, and to the terminal, if the <i>verbose</i>
  parameter is set to yes.  If the specified file exists you are given
  the option to clobber the file or exit the program.
  </p>
  <p>
  The output is in a format which may be used by the calibration tasks
  <i>xtalkcor</i> or <i>ccdproc</i>.  Normally CCDPROC is used and it calls
  XTALKCOR if the correction is selected and it has not been done yet.
  It is applied before any other calibration.  Note that the crosstalk
  calibration file must consist of each extension in the MEF file given
  only once and in the order in the file.  The second column is the
  extension to be scaled and subtracted, followed by the crosstalk
  coefficient.  If only the input extension is given it will be copied
  to the output calibrated exposure without a crosstalk correction.
  See the help for <b>xtalkcor</b> for more.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following examples use some data (not taken specifically for this
  purpose) from the NOAO Mosaic2 camera.  Pairs of CCDs are controlled
  by a single box of electronics.  Unfortunately there is crosstalk from
  those pairs in this data.  One would probably want to have several exposures
  to combine and then the list of exposures would include them all.
  </p>
  <p>
  There are some standard extension lists in the xtcoeff$ logical directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; show xtcoeff
  mscred$lib/xtcoeff/
  ms&gt; dir xtcoeff
  README       snoao16ref   snoao8ref    vnoao16ref   vnoao8ref
  snoao16      snoao8       vnoao16      vnoao8
  ms&gt; type xtcoeff$README
  This directory contains extension lists for use with the XTCOEFF task.
  The lists are paired with the <span style="font-family: monospace;">'v'</span> files being for the victim and the
  <span style="font-family: monospace;">'s'</span> files being for the source.
  
  vnoao8/snoao8           NOAO Mosaics with 8 amplifiers
                          All pairs sharing the same Arcon box
  
  vnoao8ref/snoao8ref     NOAO Mosaics with 8 amplifiers
                          All pairs not sharing the same Arcon box
  
  vnoao16/snoao16         NOAO Mosaics with 16 amplifiers
                          All pairs sharing the same Arcon box
  
  vnoao16ref/snoao16ref   NOAO Mosaics with 16 amplifiers
                          All pairs not sharing the same Arcon box
  </pre></div>
  <p>
  1. Check coefficients when there is no crosstalk by pairing the extensions
  where no crosstalk is expected.  The @files used in this example contain
  all combinations which are not expected to have crosstalk.  The @files
  are just the two columns of extensions shown in the output.  No output
  crosstalk file is specified.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; xtcoeff
  List of mosaic exposures: obj110
  Output crosstalk file:
  List of victim extensions (im1,im2,im3,im4,im5,im6,im7,im8): @vnoao8ref
  List of source extensions (im2,im1,im4,im3,im6,im5,im8,im7): @snoao8ref
  
  # XTCOEFF: NOAO/IRAF V2.11.3EXPORT valdes@puppis Fri 10:06:12 18-Aug-2000
  #   Images: obj110
  
  im1     im3     -0.000007 (0.000010,  0.6)
  im1     im4      0.001422 (0.000295,  4.8)
  im1     im5     -0.000014 (0.000014,  1.0)
  im1     im6      0.000017 (0.000013,  1.3)
  im1     im7      0.000031 (0.000012,  2.5)
  im1     im8      0.000006 (0.000018,  0.4)
  im2     im3     -0.000014 (0.000010,  1.4)
  im2     im4      0.000128 (0.000072,  1.8)
  im2     im5     -0.000010 (0.000015,  0.7)
  im2     im6      0.000008 (0.000012,  0.6)
  im2     im7     -0.000005 (0.000013,  0.4)
  im2     im8      0.000026 (0.000020,  1.4)
  im3     im1      0.000005 (0.000006,  0.8)
  im3     im2      0.000065 (0.000013,  5.1)
  im3     im5      0.000085 (0.000015,  5.6)
  im3     im6     -0.000041 (0.000015,  2.7)
  im3     im7      0.000136 (0.000015,  9.1)
  im3     im8      0.000013 (0.000022,  0.6)
  im4     im1      0.000008 (0.000006,  1.3)
  im4     im2      0.000013 (0.000013,  1.0)
  im4     im5      0.000048 (0.000014,  3.4)
  im4     im6     -0.000018 (0.000018,  1.0)
  im4     im7      0.000036 (0.000013,  2.7)
  im4     im8     -0.000018 (0.000021,  0.9)
  im5     im1      0.000012 (0.000005,  2.2)
  im5     im2      0.000019 (0.000011,  1.8)
  im5     im3      0.000007 (0.000011,  0.6)
  im5     im4      0.002339 (0.000709,  3.3)
  im5     im7     -0.000006 (0.000010,  0.5)
  im5     im8      0.000027 (0.000020,  1.3)
  im6     im1     -0.000020 (0.000006,  3.1)
  im6     im2     -0.000023 (0.000013,  1.8)
  im6     im3      0.000015 (0.000013,  1.2)
  im6     im4      0.000038 (0.000057,  0.7)
  im6     im7     -0.000014 (0.000014,  1.0)
  im6     im8      0.000024 (0.000024,  1.0)
  im7     im1      0.000000 (0.000006,  0.1)
  im7     im2      0.000005 (0.000014,  0.4)
  im7     im3      0.000008 (0.000012,  0.7)
  im7     im4     -0.000017 (0.000064,  0.3)
  im7     im5      0.000023 (0.000014,  1.7)
  im7     im6     -0.000015 (0.000012,  1.2)
  im8     im1     -0.000002 (0.000005,  0.4)
  im8     im2     -0.000020 (0.000012,  1.7)
  im8     im3     -0.000030 (0.000011,  2.7)
  im8     im4     -0.000030 (0.000057,  0.5)
  im8     im5      0.000002 (0.000014,  0.2)
  im8     im6     -0.000022 (0.000014,  1.5)
  </pre></div>
  <p>
  2.  In the above example we want to examine the 9.9 sigma case interactively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; xtcoeff interactive+
  List of mosaic exposures (obj110):
  Output crosstalk file (xtalk.dat): ""
  List of victim extensions (@vnoao8ref): im3
  List of source extensions (@snoao8ref): im7
  
  # XTCOEFF: NOAO/IRAF V2.11.3EXPORT valdes@puppis Fri 10:21:55 18-Aug-2000
  #   Images: obj110
  
  </pre></div>
  <p>
  An ICFIT graph is shown.  It is likely most of the power is coming from one
  saturated source star where the victim has a faint object.  Set a
  sample region (with the <span style="font-family: monospace;">'s'</span> key) to exclude the clump of points at high
  source values and refit with <span style="font-family: monospace;">'f'</span>.  The fit is still above zero but with
  high scatter.  Finish with <span style="font-family: monospace;">'q'</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  im3     im7      0.000104 (0.000031,  3.4)
  </pre></div>
  <p>
  The 3.4 sigma is probably not significant compared to the real crosstalk
  shown in the next example.
  </p>
  <p>
  3. Now pair the extensions where crosstalk is expected and record the
  results to a crosstalk file.  The xtalk.dat file already exists so this
  example illustrates the clobber parameter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; unlearn xtcoeff
  ms&gt; xtcoeff
  List of mosaic exposures: obj110
  Output crosstalk file: xtalk.dat
  List of victim extensions (im1,im2,im3,im4,im5,im6,im7,im8): @vnoao8
  List of source extensions (im2,im1,im4,im3,im6,im5,im8,im7): @snoao8
  Warning: Operation would overwrite existing file (xtalk.dat)
  Clobber existing crosstalk file? (no): yes
  
  # XTCOEFF: NOAO/IRAF V2.11.3EXPORT valdes@puppis Fri 10:15:45 18-Aug-2000
  #   Images: obj110
  
  im1     im2      0.001546 (0.000010, 153.7)
  im2     im1      0.000426 (0.000006, 75.1)
  im3     im4      0.001613 (0.000091, 17.8)
  im4     im3      0.001672 (0.000014, 116.4)
  im5     im6      0.000098 (0.000015,  6.6)
  im6     im5      0.001382 (0.000016, 86.1)
  im7     im8      0.000244 (0.000022, 11.2)
  im8     im7      0.001696 (0.000011, 161.1)
  </pre></div>
  <p>
  Most of the coefficients are highly significant.  If one wanted to assume
  there was no crosstalk in some of the pairs, which speeds applying the
  calibration step,  the file could be edited to one of the following forms.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # XTCOEFF: NOAO/IRAF V2.11.3EXPORT valdes@puppis Fri 10:15:45 18-Aug-2000
  #   Images: obj110
  
  im1     im2      0.001546 (0.000010, 153.7)
  im2     im1      0.000426 (0.000006, 75.1)
  im3     im4      0.001613 (0.000091, 17.8)
  im4     im3      0.001672 (0.000014, 116.4)
  im5
  im6     im5      0.001382 (0.000016, 86.1)
  im7
  im8     im7      0.001696 (0.000011, 161.1)
  </pre></div>
  <p>
  or
  </p>
  <div class="highlight-default-notranslate"><pre>
  # XTCOEFF: NOAO/IRAF V2.11.3EXPORT valdes@puppis Fri 10:15:45 18-Aug-2000
  #   Images: obj110
  
  im1     im2      0.001546 (0.000010, 153.7)
  im2     im1      0.000426 (0.000006, 75.1)
  im3     im4      0.001613 (0.000091, 17.8)
  im4     im3      0.001672 (0.000014, 116.4)
  im5     im6      0              # 0.000098 (0.000015,  6.6)
  im6     im5      0.001382 (0.000016, 86.1)
  im7     im8      0              # 0.000244 (0.000022, 11.2)
  im8     im7      0.001696 (0.000011, 161.1)
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_XTCOEFF">
  <dt><b>XTCOEFF - MSCRED V4.8: September 3, 2002</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='XTCOEFF' Line='XTCOEFF - MSCRED V4.8: September 3, 2002' -->
  <dd>The previous version underestimated the crosstalk coefficients because
  of using a crude victim background and no source background.  The new
  versions provides for input of backgrounds as well as object masks.
  </dd>
  </dl>
  <dl id="l_XTCOEFF">
  <dt><b>XTCOEFF - MSCRED V4.0: August 22, 2000</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='XTCOEFF' Line='XTCOEFF - MSCRED V4.0: August 22, 2000' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  xtalkcor, ccdproc, icfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
