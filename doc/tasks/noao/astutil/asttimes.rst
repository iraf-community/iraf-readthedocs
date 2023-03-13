.. _asttimes:

asttimes: Compute UT, Julian day, epoch, and sidereal time
==========================================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  asttimes
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files = ""' -->
  <dd>List of files containing local dates and times for which the astronomical
  dates and times are desired.  If no input files are specified then task
  parameters are used.
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = yes' -->
  <dd>Print header and observatory information to output?
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">")_.observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = ")_.observatory"' -->
  <dd>Observatory for  which times are to be computed.  The default is a
  redirection to look in the parameters for the parent package for a value.
  The final value of this parameter may be one of the
  observatories in the observatory database, <span style="font-family: monospace;">"observatory"</span> to select the
  observatory defined by the environment variable <span style="font-family: monospace;">"observatory"</span> or the
  parameter <b>observatory.observatory</b>, or <span style="font-family: monospace;">"obspars"</span> to select the
  current parameters set in the <b>observatory</b> task.  See help for
  <b>observatory</b> for additional information.
  </dd>
  </dl>
  <dl id="l_year">
  <dt><b>year, month, day, time</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='year' Line='year, month, day, time' -->
  <dd>If no input files are specified then the date and time for which the
  astronomical date and time is computed are given by these parameters.
  If the year is less than 100 then the century is assumed to be 1900.
  The month is specified as an integer between 1 and 12, and the local
  time for the specified time zone is in hours (sexagesimal format is
  acceptable).
  </dd>
  </dl>
  <dl id="l_ut">
  <dt><b>ut, epoch, jd, lmst</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ut' Line='ut, epoch, jd, lmst' -->
  <dd>If no input files are specified then the universal time, J2000 Julian epoch,
  Julian day, and local mean sidereal time (at the specified longitude)
  are recorded in these parameters for possible reference as CL
  variables.  This is in addition to the usual printed output.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The astronomical quantities of universal time, J2000 Julian epoch, Julian day,
  and local mean sidereal time at the specified observatory are computed and
  printed for the given dates and times.  To compute parameters for a
  location not specified in the observatory database use the observatory name
  <span style="font-family: monospace;">"obspars"</span> which will use the values defined by the parameters
  <i>observatory.longitude</i> and <i>observatory.timezone</i>.  The input
  dates and times may be taken from files containing the year, month (as an
  integer between 1 and 12), day, and local time (sexagesimal notation is
  acceptable) in the specified time zone.  If no files are specified then task
  parameters are used.  The output consists of a printed table with optional
  header and the input data and derived astronomical data.  In addition, if
  the input date and time is from the task parameters then the astronomical
  times are recorded in the user's parameter file (provided the task is not
  run as a background job).  These parameters may then be used as CL
  parameters.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. For use directly without data files set the date and time using
  the parameter editor, with explicit assignments, or on the command line:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; asttimes year=1987 month=10 day=28 time=15:30 obs=kpno
  # ASTTIMES: Observatory parameters for Kitt Peak National Observatory
  #       timezone = 7
  #       longitude = 111:36.0
  ##YR MON   DAY          ZT         UT      EPOCH           JD       LMST
  1987  10 28 WED 15:30:00.0 22:30:00.0 1987.82324 2447097.4375 17:30:31.8
  cl&gt; =asttimes.lmst
  17.508823973881
  </pre></div>
  <p>
  2. To make a table using a CL loop:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; asttimes.observatory="kpno"
  cl&gt; asttimes.year=1987
  cl&gt; asttimes.month=10
  cl&gt; asttimes.time=0
  cl&gt; for (i=10; i&lt;16; i+=1) {
  &gt;&gt;&gt; asttimes (day=i, header=no)
  &gt;&gt;&gt; }
  1987  10 10 SAT  0:00:00.0  7:00:00.0 1987.77219 2447078.7917  0:47:01.0
  1987  10 11 SUN  0:00:00.0  7:00:00.0 1987.77493 2447079.7917  0:50:57.5
  1987  10 12 MON  0:00:00.0  7:00:00.0 1987.77766 2447080.7917  0:54:54.1
  1987  10 13 TUE  0:00:00.0  7:00:00.0 1987.78040 2447081.7917  0:58:50.7
  1987  10 14 WED  0:00:00.0  7:00:00.0 1987.78314 2447082.7917  1:02:47.2
  1987  10 15 THU  0:00:00.0  7:00:00.0 1987.78588 2447083.7917  1:06:43.8
  </pre></div>
  <p>
  In practice the output would be directed to a file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  &gt;&gt;&gt; asttimes (day=i, header=no, &gt;&gt;"table")
  </pre></div>
  <p>
  3. To use an input file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; asttimes f=dates &gt; table
  cl&gt; type table
  # ASTTIMES: Observatory parameters for Kitt Peak National Observatory
  #       timezone = 7
  #       longitude = 111:36.0
  ##YR MON   DAY          ZT         UT      EPOCH           JD       LMST
  1987  10 28 WED 22:00:00.0  5:00:00.0 1987.82398 2447097.7083  0:01:35.8
  1987  10 28 WED 23:00:00.0  6:00:00.0 1987.82409 2447097.7500  1:01:45.7
  1987  10 29 THU  0:00:00.0  7:00:00.0 1987.82421 2447097.7917  2:01:55.5
  1987  10 29 THU  1:00:00.0  8:00:00.0 1987.82432 2447097.8333  3:02:05.4
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_ASTTIMES">
  <dt><b>ASTTIMES V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='ASTTIMES' Line='ASTTIMES V2.10.3' -->
  <dd>The epoch was changed from day of the year divided by 365.25 to the
  precise J2000 Julian epoch definition.  In addition to changing
  the output value this fixes incorrect values JD and LMST around the
  new year.
  The times are now always printed in the proper 24 hour interval instead
  of using negative or values greater than 24 to indicate the day difference
  with Greenwich.
  The header parameter now suppress printing the observatory information.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  observatory
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
