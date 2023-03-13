.. _suntoiraf:

suntoiraf: Convert Sun rasters into IRAF images
===============================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  suntoiraf input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_names">
  <dt><b>names</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='names' Line='names' -->
  <dd>List of raster files to be converted.  The output image names will be
  the same as the individual input file names with a <span style="font-family: monospace;">".imh"</span> appended
  (assuming that you are using the Old Image Format).  Rasterfiles with
  an extension of `.ras', will have the extension omitted.  The images will
  appear in the same directory as the raster files, typically the <b>Unix</b>
  login directory when the task is used within an imtool R_DISPOSE string.
  </dd>
  </dl>
  <dl id="l_apply_lut">
  <dt><b>apply_lut = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apply_lut' Line='apply_lut = yes' -->
  <dd>Apply the lookup table translation to each pixel?  If <b>apply_lut</b> =
  no, the pixel values will be taken directly from the raster file.  If
  <b>apply_lut</b> = yes, an NTSC weighted translation from the rasterfile's
  color lookup table will be applied to each pixel to convert to grayscale.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = no' -->
  <dd>Delete the rasterfile after making the image?  This is useful for making
  automated (Unix or IRAF) scripts for producing photographic or other hardcopy.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print informative information while the transformation is occurring?
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>List the rasterfile header information instead?
  </dd>
  </dl>
  <dl id="l_yflip">
  <dt><b>yflip = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yflip' Line='yflip = yes' -->
  <dd>Flip the output image top to bottom?  Rasterfiles are stored in reverse
  vertical order from IRAF images.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Suntoiraf</b> will convert Sun raster files into IRAF images.  This is
  useful, for example, to make <b>solitaire</b> photographic prints or
  other hardcopy from an <b>imtool</b> window (see IMTOOL HINTS, below).
  </p>
  <p>
  For general use, <b>suntoiraf</b> will convert non-run-length-encoded
  Sun rasterfiles into IRAF images.  The output image will have the same
  name as the input rasterfile, but with a `.imh' (or other IRAF image
  extension) appended.  If the rasterfile has an extension of `.ras', this
  extension will be omitted from the image name.
  </p>
  <p>
  If <b>apply_lut</b> = no, the (typically 8 bit) pixel values will be
  copied directly to the output with no interpretation.  If <b>apply_lut</b>
  = yes, the NTSC equalization weighting will be applied to the RGB lookup
  table to convert the color rasterfile to a grayscale image.  The weights
  are 0.299, 0.587, and 0.114 for the red, green, and blue LUT entries,
  respectively.
  </p>
  <p>
  Various options are available to tailor the operation of the task to
  your (or your script's) precise liking.  If <b>delete</b> = yes, the
  input raster file will be removed from the disk after the image
  conversion.  This is useful in script applications.  If <b>verbose</b> =
  yes, a running commentary will be presented, otherwise the operation of
  the task is silent except for error messages.  If <b>listonly</b> = yes,
  the task will report information about each input rasterfile, rather
  than converting it.  If <b>yflip</b> = yes, the storage order of the
  lines of the output image will be inverted from the input rasterfile.
  Since the display convention is inverted for rasterfiles relative to
  IRAF images, this will result in an upright output image.  On the other
  hand, if <b>yflip</b> = no, the storage order will be preserved at the
  expense of the output orientation appearing inverted.
  </p>
  </section>
  <section id="s_imtool_hints">
  <h3>Imtool hints</h3>
  <p>
  One possible first step in making a hardcopy is to create the raster files
  from the imtool window.  The recommended way to do this is to select <span style="font-family: monospace;">"Imcopy"</span>
  from the imtool frame menu.  If the menu is popped up by positioning the
  cursor on the right hand side of the window frame (and away from the edge
  of the screen), the menu won't overlay the window, possibly contaminating
  the hardcopy.  The resulting raster file will save not only the pixels from
  the imtool buffer but also the lookup table information.
  </p>
  <p>
  Another way to generate an imtool screendump is to use the &lt;F7&gt; function
  key, but this requires care because of the possibility of catching cursor
  fallout in the solitaire.  If you do use the &lt;F7&gt; function key, position the
  cursor to minimize its visual impact.  The cursor will appear in the
  hardcopy (solitaire) unless it happens to blink out at the moment that
  the hardcopy is made.
  </p>
  <p>
  A possibly confusing choice is the <span style="font-family: monospace;">"Save"</span> option in the imtool setup menu.
  This is inappropriate because no lookup table information is preserved.
  </p>
  <p>
  Only the portion of the frame buffer that is displayed in the window
  will be snapped - what you see is what you get.
  </p>
  <p>
  If you have to adjust the contrast and brightness of the image very
  much by using the right mouse button, you may want to redisplay the
  image using a different Z1 and Z2.  This will preserve the grayscale
  resolution in cases in which the <span style="font-family: monospace;">"effective"</span> Z1 and Z2 are much
  different than the <span style="font-family: monospace;">"actual"</span> Z1 and Z2.
  </p>
  <p>
  In the setup menu try:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Show colorbar:      No
  Background color:   black
  </pre></div>
  <p>
  The choice of the background color may have an effect on any graphics
  in the frame.
  </p>
  <p>
  If you use the <b>imttodmd</b> shell script available at NOAO/Tucson,
  the pixel files for the images will be created in the IRAF directory
  `tmp$', which is typically the UNIX directory `/tmp/'.  If you have
  trouble with this directory filling up, the pixel files may be placed
  into another directory by setting the UNIX environment variable `tmp'
  to the desired pathname:
  </p>
  <div class="highlight-default-notranslate"><pre>
  % setenv tmp '/scr1/v13/pixels/'
  </pre></div>
  <p>
  *before* starting up IMTOOL (IN THE PARENT SHELL OF THE IMTOOL).
  Note that if this is set when IRAF is entered, all IRAF temporary
  files will end up in this directory.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  These are rather specific to NOAO/Tucson, but may suggest ways that the
  task may be useful to you.
  </p>
  <p>
  To configure imtool for one button solitaire operation:
  </p>
  <p>
  The Unix shell script, <span style="font-family: monospace;">"/ursa/iraf/extern/nlocal/lib/imttodmd"</span> (on
  Ursa and its kin) can be used to make imtool solitaire prints.  The
  script may move to /usr/local/bin in the future and would thus be
  available like any other unix command.  Imttodmd is meant to be
  called directly by the imtool.  For example, place these lines in
  your `.login' file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  setenv R_RASTERFILE 'snap.%d'
  setenv R_DISPOSE '/ursa/iraf/extern/nlocal/lib/imttodmd %s'
  </pre></div>
  <p>
  More recent versions of imtool also allow setting these strings from
  the setup panel.
  </p>
  <p>
  The parent shell of the imtool must have these variables defined in
  its environment prior to starting imtool.  If you aren't sure what
  this means, the simplest thing to do is to edit these lines into
  your <b>.login</b>, log off of the workstation <b>completely</b>, and
  log back into Unix, Sunview, and IRAF.
  </p>
  <p>
  Pressing &lt;F7&gt; will send snaps directly to the solitaire queue, leaving
  no intermediate files.  Only the windowed portion of the frame buffer
  will be snapped.  The necessary files will twinkle in and out of
  existence in the current working directory of the imtool, typically
  your Unix login directory.  Your windows will be frozen until the
  solitaire is safely on its way, at which time the screen will beep.
  This should take on the order of half a minute for a 512 square
  imtool on a lightly loaded system.  If faster response is needed,
  the script may be run in the background:
  </p>
  <div class="highlight-default-notranslate"><pre>
  setenv R_DISPOSE    '/ursa/iraf/extern/nlocal/lib/imttodmd %s &amp;'
  </pre></div>
  <p>
  Care should be taken in this case to avoid having too many
  (<b>too many is typically more than one</b>) background job running
  at once.
  </p>
  <p>
  To make one-button snap files and solitaires:
  </p>
  <p>
  The <b>imttodmd</b> script has various options for leaving the
  intermediate files around.  To leave the snap images in your
  directory and also make solitaires (i.e., if you are highly
  suspicious by nature) set the variable:
  </p>
  <div class="highlight-default-notranslate"><pre>
  setenv R_DISPOSE    '/ursa/iraf/extern/nlocal/lib/imttodmd -image %s'
  </pre></div>
  <p>
  To only make the images, with no solitaire output:
  </p>
  <div class="highlight-default-notranslate"><pre>
  setenv R_DISPOSE    '/ursa/iraf/extern/nlocal/lib/imttodmd -nocrt %s'
  </pre></div>
  <p>
  This will allow you to run a single CRTPICT job after collecting all
  the snap files.
  </p>
  <p>
  To make solitaires from an imtool window, the old way:
  </p>
  <p>
  Enter this from the UNIX shell, <b>before starting suntools</b>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  % setenv R_RASTERFILE "frame.%d"
  </pre></div>
  <p>
  Start suntools, login to iraf and load the noao, tv and local
  packages.  Display an image and press the &lt;F7&gt; function key to
  create a raster file named <span style="font-family: monospace;">"frame.N"</span>, where N is an index number
  generated by imtool.  This raster file will be appear in your
  <b>UNIX</b> login directory.
  </p>
  <p>
  Dump the raster files to the solitaire queue:
  </p>
  <div class="highlight-default-notranslate"><pre>
  lo&gt; suntoiraf frame.*
  lo&gt; crtpict frame.*.i.imh ztrans=min_max z1=5 z2=260
      (The z1 &amp; z2 values were empirically determined.)
  </pre></div>
  <p>
  *** Don't forget to clean up! ***
  </p>
  <div class="highlight-default-notranslate"><pre>
  lo&gt; imdelete frame.*.i.imh
  lo&gt; delete frame.*
  </pre></div>
  <p>
  The solitaires should be ready the next day in the basket by the
  main computer lab.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  irafil, binfil, and the UNIX man page for imtool
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'IMTOOL HINTS' 'EXAMPLES' 'SEE ALSO'  -->
  
