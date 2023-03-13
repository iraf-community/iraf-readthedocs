.. _ccdgroups:

ccdgroups: Group CCD images into image lists
============================================

**Package: ccdred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccdgroups images output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of CCD images to be grouped.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output root group filename.  The image group lists will be put in files
  with this root name followed by a number.
  </dd>
  </dl>
  <dl id="l_group">
  <dt><b>group = <span style="font-family: monospace;">"ccdtype"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='group' Line='group = "ccdtype"' -->
  <dd>Group type.  There are currently four grouping types:
  <dl>
  <dt><b>ccdtype</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ccdtype' Line='ccdtype' -->
  <dd>Group by CCD image type.
  </dd>
  </dl>
  <dl>
  <dt><b>subset</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='subset' Line='subset' -->
  <dd>Group by subset parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>position</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='position' Line='position' -->
  <dd>Group by position in right ascension (in hours) and declination (in degrees).
  The groups are defined by a radius parameter (in arc seconds).
  </dd>
  </dl>
  <dl>
  <dt><b>title</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='title' Line='title' -->
  <dd>Group by identical titles.
  </dd>
  </dl>
  <dl>
  <dt><b>date</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='date' Line='date' -->
  <dd>Group by identical dates.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 60.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 60.' -->
  <dd>Grouping radius when grouping by positions.  This is given in arc seconds.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = ""' -->
  <dd>CCD image types to select from the input image list.  If null (<span style="font-family: monospace;">""</span>) then
  all image types are used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input images, possible restricted to a particular CCD image type,
  are grouped into image lists.  The <span style="font-family: monospace;">"ccdtype"</span> or <span style="font-family: monospace;">"subset"</span> groups
  produce output image lists with the given root name and the CCD type
  or subset as an extension (without a period).  For the other group
  types the
  image lists have file names given by
  the root output name and a numeric extension (without a period).
  If the package parameter <i>ccdred.verbose</i> is yes then the
  image name and output group list is printed for each image.  The image lists can
  be used with the @ list feature for processing separate groups of observations.
  Note that grouping by CCD image type and subset is often not necessary since
  the <b>ccdred</b> tasks automatically use this information (see
  <b>ccdtypes</b> and <b>subsets</b>).
  </p>
  <p>
  Besides CCD image type and subsets there are currently three ways to
  group images.  These are by position in the sky, by title, and by
  date.  Further groups may be added as suggested.  The title grouping is
  useful if consistent titles are used when taking data.  The date
  grouping is useful if multiple nights of observations are not organized
  by directories (it is recommended that data from separate nights be
  kept in separate directories).  The position grouping finds
  observations within a given radius on the sky of the first member of
  the group (this is not a clustering algorithm).  The right ascension
  and declination coordinates must be in standard units, hours and
  degrees respectively.  The grouping radius is in arc seconds.  This
  grouping type is useful for making sets of data in which separate
  calibration images are taken at each position.
  </p>
  <p>
  The date, title, and coordinates are accessed through the instrument
  translation file.  The standard names used are <span style="font-family: monospace;">"date-obs"</span>, <span style="font-family: monospace;">"title"</span>, <span style="font-family: monospace;">"ra"</span>,
  and <span style="font-family: monospace;">"dec"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. For each object 5 exposures were taken to be combined in order to remove
  cosmic rays.  If the titles are the same then (with ccdred.verbose=yes):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdgroups *.imh group group=title ccdtype=object
  ccd005.imh  --&gt; group1
  ccd006.imh  --&gt; group1
  ccd007.imh  --&gt; group1
  ccd008.imh  --&gt; group1
  ccd009.imh  --&gt; group1
  ccd012.imh  --&gt; group2
  ccd013.imh  --&gt; group2
  ccd014.imh  --&gt; group2
  ccd015.imh  --&gt; group2
  ccd016.imh  --&gt; group2
  [... etc ...]
  cl&gt; combine @group1 obj1 proc+
  cl&gt; combine @group2 obj2 proc+
  [... etc ...]
  </pre></div>
  <p>
  Note the numeric suffixes to the output root name <span style="font-family: monospace;">"group"</span>.
   
  2. CCD observations were made in groups with a flat field, the object, and
  a comparison spectrum at each position.  To group and process this data:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdgroups *.imh obs group=position &gt;&gt; logfile
  cl&gt; ccdproc @obs1
  cl&gt; ccdproc @obs2
  cl&gt; ccdproc @obs3
  </pre></div>
  <p>
  Since no flat field is specified for the parameter <i>ccdproc.flat</i>
  the flat field is taken from the input image list.
  </p>
  <p>
  3. If for some reason you want to group by date and position it is possible
  to use two steps.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdgroups *.imh date group=date
  cl&gt; ccdgroups @data1 pos1
  cl&gt; ccdgroups @data2 pos2
  </pre></div>
  <p>
   
  4. To get groups by CCD image type:
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdgroups *.imh "" group=ccdtype
  ccd005.imh  --&gt; zero
  ccd006.imh  --&gt; zero
  ccd007.imh  --&gt; zero
  ccd008.imh  --&gt; dark
  ccd009.imh  --&gt; flat
  ccd012.imh  --&gt; flat
  ccd013.imh  --&gt; object
  ccd014.imh  --&gt; object
  ccd015.imh  --&gt; object
  ccd016.imh  --&gt; object
  [... etc ...]
  </pre></div>
  <p>
   
  Note the use of a null root name and the extension is the standard
  CCDRED types (not necessarily those used in the image header).
   
  5. To get groups by subset:
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdgroups *.imh filt group=subset
  ccd005.imh  --&gt; filt
  ccd006.imh  --&gt; filtB
  ccd007.imh  --&gt; filtB
  ccd008.imh  --&gt; filtB
  ccd009.imh  --&gt; filtV
  ccd012.imh  --&gt; filtV
  ccd013.imh  --&gt; filtV
  ccd014.imh  --&gt; filtB
  ccd015.imh  --&gt; filtB
  ccd016.imh  --&gt; filtB
  [... etc ...]
  </pre></div>
  <p>
   
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdlist, ccdtypes, instruments, subsets
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
