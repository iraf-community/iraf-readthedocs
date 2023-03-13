.. _pairmass:

pairmass: Plot airmass vs time for a given coordinate
=====================================================

**Package: obsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pairmass
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_ra">
  <dt><b>ra</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ra' Line='ra' -->
  <dd>The right ascension of the object in hours.
  </dd>
  </dl>
  <dl id="l_dec">
  <dt><b>dec</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dec' Line='dec' -->
  <dd>The declination of the object in degrees.
  </dd>
  </dl>
  <dl id="l_epoch">
  <dt><b>epoch=INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='epoch' Line='epoch=INDEF' -->
  <dd>The epoch of the coordinates in years.
  </dd>
  </dl>
  <dl id="l_year">
  <dt><b>year</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='year' Line='year' -->
  <dd>The year of the observation.
  </dd>
  </dl>
  <dl id="l_month">
  <dt><b>month</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='month' Line='month' -->
  <dd>The month of the observation (a number from 1 to 12).
  </dd>
  </dl>
  <dl id="l_day">
  <dt><b>day</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='day' Line='day' -->
  <dd>The day of the month of the observation.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "observatory"' -->
  <dd>The observatory identifier in the observatory database.  See the
  help for <b>observatory</b> task for more information.
  </dd>
  </dl>
  <dl id="l_timesys">
  <dt><b>timesys = <span style="font-family: monospace;">"Standard"</span> (Universal|Standard|Siderial)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='timesys' Line='timesys = "Standard" (Universal|Standard|Siderial)' -->
  <dd>Time system for the plot or output list.  The choices are
  <span style="font-family: monospace;">"Universal"</span> for universal time, <span style="font-family: monospace;">"Standard"</span> for standard time (where
  the time zone is determined from the observatory database), and <span style="font-family: monospace;">"Siderial"</span>
  for the siderial time.
  </dd>
  </dl>
  <dl id="l_resolution">
  <dt><b>resolution=4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resolution' Line='resolution=4' -->
  <dd>The number of UT points per hour for which to calculate the airmass.
  </dd>
  </dl>
  <dl id="l_listout">
  <dt><b>listout=no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listout' Line='listout=no' -->
  <dd>List, rather than plot, the airmass versus time?  Only airmasses
  below that given by the <i>wy2</i> parameters are listed.
  </dd>
  </dl>
  </section>
  <section id="s_plot_parameters">
  <h3>Plot parameters</h3>
  <dl id="l_wx1">
  <dt><b>wx1=-7., wx2=7., wy1=0., wy2=5.</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='wx1' Line='wx1=-7., wx2=7., wy1=0., wy2=5.' -->
  <dd>The range of window (user) coordinates to be included in the plot.
  If the range of values in x or y = 0, the plot is automatically
  scaled from the minimum to maximum data values along that axis.
  The times are available from -24 hours to 48 hours so one can use
  negative numbers to plot hours from midnight or in actual hours.
  </dd>
  </dl>
  <dl id="l_pointmode">
  <dt><b>pointmode = no</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='pointmode' Line='pointmode = no' -->
  <dd>Plot individual points instead of a continuous line?
  </dd>
  </dl>
  <dl id="l_marker">
  <dt><b>marker=<span style="font-family: monospace;">"box"</span></b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='marker' Line='marker="box"' -->
  <dd>If <b>pointmode</b> = yes, the marker drawn at each point is set with this
  parameter.  The acceptable choices are <span style="font-family: monospace;">"point"</span>, <span style="font-family: monospace;">"box"</span>, <span style="font-family: monospace;">"plus"</span>, <span style="font-family: monospace;">"cross"</span>,
  <span style="font-family: monospace;">"circle"</span>, <span style="font-family: monospace;">"hebar"</span>, <span style="font-family: monospace;">"vebar"</span>, <span style="font-family: monospace;">"hline"</span>, <span style="font-family: monospace;">"vline"</span>, and <span style="font-family: monospace;">"diamond"</span>.
  </dd>
  </dl>
  <dl id="l_szmarker">
  <dt><b>szmarker = 0.005</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='szmarker' Line='szmarker = 0.005' -->
  <dd>The size of the marker drawn when <b>pointmode</b> = yes.  A value of 0
  (zero) indicates that the task should read the size from the input list.
  </dd>
  </dl>
  <dl id="l_logx">
  <dt><b>logx = no, logy = no</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='logx' Line='logx = no, logy = no' -->
  <dd>Draw the x or y axis in log units, versus linear?
  </dd>
  </dl>
  <dl id="l_xlabel">
  <dt><b>xlabel=<span style="font-family: monospace;">"default"</span></b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='xlabel' Line='xlabel="default"' -->
  <dd>Label for the X-axis.  The value <span style="font-family: monospace;">"default"</span> uses the specified time system.
  </dd>
  </dl>
  <dl id="l_ylabel">
  <dt><b>ylabel=<span style="font-family: monospace;">"Airmass"</span></b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='ylabel' Line='ylabel="Airmass"' -->
  <dd>Labels for the Y-axis.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title=<span style="font-family: monospace;">"default"</span></b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='title' Line='title="default"' -->
  <dd>Title for plot.  If not changed from <span style="font-family: monospace;">"default"</span>, a title string consisting
  of the date, observatory, and  object position is used.
  </dd>
  </dl>
  <dl id="l_vx1">
  <dt><b>vx1=0., vx2=0., vy1=0., vy2=0.</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='vx1' Line='vx1=0., vx2=0., vy1=0., vy2=0.' -->
  <dd>NDC coordinates (0-1) of the plotting device viewport.  If not set
  by the user, a suitable viewport which allows sufficient room for all
  labels is used.
  </dd>
  </dl>
  <dl id="l_majrx">
  <dt><b>majrx=5, minrx=5, majry=5, minry=5</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='majrx' Line='majrx=5, minrx=5, majry=5, minry=5' -->
  <dd>The number of major and minor divisions along the x or y axis.
  </dd>
  </dl>
  <dl id="l_round">
  <dt><b>round = no</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='round' Line='round = no' -->
  <dd>Round axes up to nice values?
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = yes</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='fill' Line='fill = yes' -->
  <dd>Fill the plotting viewport regardless of the device aspect ratio?
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append to an existing plot?
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device=<span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PLOT PARAMETERS' Level=0 Label='device' Line='device="stdgraph"' -->
  <dd>Output device.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The airmass is plotted over a specified set of hours for a given
  observatory.  The observatory is specified by an identifier as given
  in the observatory database.  See the help for <span style="font-family: monospace;">"observatory"</span> for more
  information about the database and identifiers.
  </p>
  <p>
  The results can be shown in universal, standard, or siderial time.
  The standard time simply adds the time zone from the observatory
  database tothe universal time and so there is no explicit facility
  for daylight savings time.  The times are computed in the range
  -24 hours to +48 hours.  By setting the <i>wx1</i> and <i>wx2</i>
  parameters one can plot either in hours relative to 0 in the specified
  time system or as positive hours.  This simple task does not support
  axis labeling which wraps around.
  </p>
  <p>
  The list output prints date, observatory, object coordinates, and
  the time system.  This is followed by the time sorted between 0 and 24
  and the airmasses.  The list only includes airmasses below the
  value specified by <i>wy2</i>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To plot the airmass for M82 from Kitt Peak for Groundhog's Day in 1992:
  </p>
  <div class="highlight-default-notranslate"><pre>
  pairmass ra=9:51:42 dec=69:56 epoch=1950 year=1992 month=2 day=2
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  observatory, airmass, setairmass, graph
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'PLOT PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
