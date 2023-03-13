.. _skygroup:

skygroup: Group a list containing RA and Dec into spatial sublists
==================================================================

**Package: nproto**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  A list with RA and Dec in the first two columns followed by user data
  is grouped into sublist based on spatial proximity.  A separation parameter
  defines the grouping by looking for gaps in both RA and Dec that are
  bigger than the specified amount.  The output sublists may or may not
  include the RA and Dec columns.  A typical example of user data might be
  image names.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  skygroup input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input tabular text file containing RA and Dec in the first two whitespace
  separated columns and user data in the remaining columns.  The RA may
  be in hours or degrees while the Dec must be in degrees.  The RA values
  must lie in the range 0h to 24h or 0d to 360d and the Dec values
  must lie in the range -90d to 90d.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output root filename.  The root filename itself will contain a list of
  the sublists.  The sublists will have _NNN appended to the root name
  where NNN is a three digit number.  If there are more than 999 sublists
  the number of digits will increase.  A check is made for any pre-existing
  filenames with this root, sequence pattern, and optional extension and
  an error will result if any are found.
  </dd>
  </dl>
  <dl id="l_extn">
  <dt><b>extn = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extn' Line='extn = ""' -->
  <dd>Optional output extension.  This string is appended to the output files
  noted previously.  Note that an period must be given explicitly if a
  <span style="font-family: monospace;">".XXX"</span> style extension is desired.
  </dd>
  </dl>
  <dl id="l_sep">
  <dt><b>sep = 60 (arcsec)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sep' Line='sep = 60 (arcsec)' -->
  <dd>The maximum separation in arcseconds in RA and Dec, applied separately, which
  defines the start of a new group.
  </dd>
  </dl>
  <dl id="l_raunit">
  <dt><b>raunit = <span style="font-family: monospace;">"hr"</span> (hr|deg)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raunit' Line='raunit = "hr" (hr|deg)' -->
  <dd>The input RA unit where <span style="font-family: monospace;">"hr"</span> is hours and <span style="font-family: monospace;">"deg"</span> is degrees.
  </dd>
  </dl>
  <dl id="l_keepcoords">
  <dt><b>keepcoords = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keepcoords' Line='keepcoords = yes' -->
  <dd>Keep the input coordinate columns in the output lists?  If no then only
  the user data will be placed in the output lists.  This option allows
  taking a list of RA, Dec, and filenames and producing only lists of
  filenames to be used as @files.
  </dd>
  </dl>
  <dl id="l_raformat">
  <dt><b>raformat = <span style="font-family: monospace;">"%.2h"</span>, decformat = <span style="font-family: monospace;">"%.1h"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raformat' Line='raformat = "%.2h", decformat = "%.1h"' -->
  <dd>The format for printing the RA and Dec in the output lists if
  <i>keepcoords</i> is yes.  See the help for <b>printf</b> for the formats.
  Note that the raformat may be given in %H format to convert input RA
  in degrees into output hours.  The default produces sexagesimal format
  keeping the RA in the same units as the input.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task groups a list of user data with RA and Dec coordinates
  into sublists where all points in a group have at least one member with
  celestial distance in RA or Dec separately less than or equal to the
  specified separation.  In other words, groups are defined by gaps in RA
  and Dec.
  </p>
  <p>
  The input format is a text table where each line consists of an RA,
  a Dec, and arbitrary user data.  Whitespace separates these three parts.
  The RA and Dec have certain restrictions on units and ranges as described
  in the parameters.  However, the RA may be given either in hours or degrees
  and may be output in hours if given in degrees.
  </p>
  <p>
  The output is a set of sublists as well as a file containing the set
  of sublist filenames.  The sublists contain the input user data with
  or without the input coordinates.
  </p>
  <p>
  The grouping algorithm is summarized as follows.  The input list is
  sorted by declination.  The declination ordered list is traversed
  to form groups with consecutive declination intervals less than or
  equal to the specified separation.  These groups are then
  sorted in RA and these are traversed to form the final groups with
  consecutive RA intervals less than or equal to the specified separation.
  Note that the RA intervals are actually computed by <b>skysep</b> and
  make use of both the RA and Dec.
  </p>
  <p>
  A challenge is dealing with the wrap around in RA at the zero meridian.
  This is handled by duplicating points near 0 beyond 24h or 360d.  This is
  the reason the input is required to only be in a specific range.  This
  duplication can result in entries appearing in more than one output group.
  A merging step handles this situation.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. A set of images is to be grouped based on their FITS tangent point
  coordinates.  Note this make most sense when the tangent point pixel
  coordinates are the same in the image.  The image will then be grouped
  to find those that overlap by some amount.  If the images have 10 arc
  minute fields of view and we want to group those that overlap by at least
  50% then the separation parameter should be something like 5 arc minutes.
  We want to the output to a list of only the file names which will then
  be passed on to an image stacking program.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect *.fits crval1,crval2,title yes &gt; coords
  cl&gt; skygroup coords group extn=".lis" sep=300 rau=deg keep-
  cl&gt; type group.lis
  group_001.lis
  group_002.lis
  ...
  cl&gt; type group_001.lis
  obj4325.fits
  obj4329.fits
  ...
  cl&gt; count @group.lis
  cl&gt; count @group
        1       3      85 group_001.lis
        2       6     170 group_002.lis
      102     306    8670 group_003.lis
      133     399   11438 group_004.lis
       31      93    2666 group_005.lis
        7      21     595 group_006.lis
        5      15     425 group_007.lis
      281     843   24049 Total
  </pre></div>
  <p>
  The CRVAL values are for the RA and Dec world axes respectively.  Because
  the FITS reference values must be in degrees the input RA unit is specified
  as degrees.  Because we want only the output file names we use keepcoords=no.
  The output lists will be group_001.lis, group_002.lis, etc.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  skysep, astradius, astcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
