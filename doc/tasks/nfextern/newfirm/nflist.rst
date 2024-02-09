.. _nflist:

nflist: List image parameters as derived by nfproc
==================================================

**Package: newfirm**

.. raw:: html

  <section id="s_usage___">
  <h3>Usage   </h3>
  <p>
  nflist input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input			</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input			' -->
  <dd>List of NEWFIRM MEF files or image extensions.
  </dd>
  </dl>
  <dl id="l_obstype">
  <dt><b>obstype = <span style="font-family: monospace;">""</span> (dark|flat|sky|object)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obstype' Line='obstype = "" (dark|flat|sky|object)' -->
  <dd>Select a data with a particular OBSTYPE keyword value.  The value may
  be a substring of the keyword value.  Case and whitespace are ignored.
  </dd>
  </dl>
  <dl id="l_showops">
  <dt><b>showops = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='showops' Line='showops = no' -->
  <dd>Show operations to be performed based on the current <b>nfproc</b>
  settings.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  NFLIST list information about the NEWFIRM data in the input list.  When
  <i>showops</i> is no a single line is printed for each image in the input
  list (where input MEF files are expanded into their consitutent images).
  When it is yes the various processing options set for <b>nfproc</b> are
  applied against any processing history in the image headers to indicate
  what operations would be performed by <b>nfproc</b>.
  </p>
  <p>
  The line with the image name has the format
  </p>
  <div class="highlight-default-notranslate"><pre>
  imagename[obstype][imageid][filter][exptime][flags]
  </pre></div>
  <p>
  where obstype is the logical NFPROC observation type (dark, fflat, gflat,
  sky, and object), imageid is the value of the IMAGEID keyword,
  filter is the abbreviated version of the FILTER keyword, exptime is
  the exposure time, and flags are processing history flags from the
  PROCDONE keyword.
  </p>
  <p>
  There are two primary purposes for this task, to give an expanding
  description of the data and to check if NFPROC recognizes the important
  parameters needed for processing.  Note that another useful task checking
  and organizing data is <b>nfgroup</b>.
  </p>
  <p>
  When the input list is very large, say from a directory of data for a
  whole night or set of nights, no output will appear until every image
  is read and so may appear to be stuck.  To speed this up or just to
  reduce the output, a list selecting only a single array (image extension)
  may be used.
  </p>
  <p>
  This task is a simple script using <b>nfproc</b> in list only output mode.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The dataset consists of 35 NEWFIRM exposures in 9 sequences.
  This is the same example dataset illustrating <b>nfgroup</b>.
  There are two dark sequences of different exposure times, one dome flat
  sequence that cycles through two filters, and 6 object sequences in
  two filters.  The science sequences are a combination of offset skys and
  on-field object exposures in an SOOS pattern.
  </p>
  <p>
  1.  List all files but use an image extension to reduce the list and time.
  </p>
  <div class="highlight-default-notranslate"><pre>
  newfirm&gt; nflist nftest*[im1]
  Jan 27  8:13 nflist
  nftest01.fits[im1][dark][1][][5.0][]
  nftest05.fits[im1][dark][1][][60.0][]
  nftest03.fits[im1][dark][1][][5.0][]
  nftest04.fits[im1][dark][1][][60.0][]
  nftest06.fits[im1][dark][1][][60.0][]
  nftest02.fits[im1][dark][1][][5.0][]
  nftest07.fits[im1][fflat][1][J][5.0][]
  nftest09.fits[im1][fflat][1][J][5.0][]
  nftest08.fits[im1][fflat][1][J][5.0][]
  nftest10.fits[im1][fflat][1][Ks][5.0][]
  nftest12.fits[im1][fflat][1][Ks][5.0][]
  nftest11.fits[im1][fflat][1][Ks][5.0][]
  nftest20.fits[im1][sky][1][J][60.0][]
  nftest13.fits[im1][sky][1][J][60.0][]
  nftest16.fits[im1][sky][1][J][60.0][]
  nftest17.fits[im1][sky][1][J][60.0][]
  nftest24.fits[im1][sky][1][J][60.0][]
  nftest21.fits[im1][sky][1][J][60.0][]
  nftest25.fits[im1][sky][1][Ks][60.0][]
  nftest28.fits[im1][sky][1][Ks][60.0][]
  nftest36.fits[im1][sky][1][Ks][60.0][]
  nftest33.fits[im1][sky][1][Ks][60.0][]
  nftest29.fits[im1][sky][1][Ks][60.0][]
  nftest32.fits[im1][sky][1][Ks][60.0][]
  nftest19.fits[im1][object][1][J][60.0][]
  nftest14.fits[im1][object][1][J][60.0][]
  nftest18.fits[im1][object][1][J][60.0][]
  nftest15.fits[im1][object][1][J][60.0][]
  nftest22.fits[im1][object][1][J][60.0][]
  nftest23.fits[im1][object][1][J][60.0][]
  nftest27.fits[im1][object][1][Ks][60.0][]
  nftest26.fits[im1][object][1][Ks][60.0][]
  nftest35.fits[im1][object][1][Ks][60.0][]
  nftest34.fits[im1][object][1][Ks][60.0][]
  nftest30.fits[im1][object][1][Ks][60.0][]
  nftest31.fits[im1][object][1][Ks][60.0][]
  </pre></div>
  <p>
  2.  Limit the list to flat fields.
  </p>
  <div class="highlight-default-notranslate"><pre>
  newfirm&gt; nflist nftest*[im1] obstype='flat'
  Jan 27  8:16 nflist
  nftest07.fits[im1][fflat][1][J][5.0][]
  nftest09.fits[im1][fflat][1][J][5.0][]
  nftest08.fits[im1][fflat][1][J][5.0][]
  nftest10.fits[im1][fflat][1][Ks][5.0][]
  nftest12.fits[im1][fflat][1][Ks][5.0][]
  nftest11.fits[im1][fflat][1][Ks][5.0][]
  </pre></div>
  <p>
  3.  Show the operations to be done.  This depends on the settings of nfproc.
  </p>
  <div class="highlight-default-notranslate"><pre>
  newfirm&gt; nflist nftest*[im1] obstype='flat' show+
  Jan 27  8:19 nflist
  nftest07.fits[im1][fflat][1][J][5.0][]
  nftest07.fits[im1]: Fixpix $I
  $M = nfdat$bpm20090125[im1]
  nftest09.fits[im1][fflat][1][J][5.0][]
  nftest09.fits[im1]: Fixpix $I
  $M = nfdat$bpm20090125[im1]
  nftest08.fits[im1][fflat][1][J][5.0][]
  nftest08.fits[im1]: Fixpix $I
  $M = nfdat$bpm20090125[im1]
  nftest10.fits[im1][fflat][1][Ks][5.0][]
  nftest10.fits[im1]: Fixpix $I
  $M = nfdat$bpm20090125[im1]
  nftest12.fits[im1][fflat][1][Ks][5.0][]
  nftest12.fits[im1]: Fixpix $I
  $M = nfdat$bpm20090125[im1]
  nftest11.fits[im1][fflat][1][Ks][5.0][]
  nftest11.fits[im1]: Fixpix $I
  $M = nfdat$bpm20090125[im1]
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nfproc, nfgroup
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE   ' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
