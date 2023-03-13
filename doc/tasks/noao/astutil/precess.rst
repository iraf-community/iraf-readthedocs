.. _precess:

precess: Precess a list of astronomical coordinates
===================================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  precess files startyear endyear
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The name of a file (or a file list or template) containing the coordinates
  to be precessed.
  </dd>
  </dl>
  <dl id="l_startyear">
  <dt><b>startyear</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='startyear' Line='startyear' -->
  <dd>The default equinox of the input coordinates.
  </dd>
  </dl>
  <dl id="l_endyear">
  <dt><b>endyear</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='endyear' Line='endyear' -->
  <dd>The default target year to which the coordinates will be precessed.
  </dd>
  </dl>
  <dl id="l_stdepoch">
  <dt><b>stdepoch = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='stdepoch' Line='stdepoch = 0' -->
  <dd>If nonzero, coordinates will be output precessed to both <b>endyear</b>
  and the specified standard epoch.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Coordinates are read from the input file as RA and DEC pairs,
  one pair per input line.  Each coordinate pair may optionally be followed
  by the equinox of the input coordinates (if different from the default)
  and the epoch of the output coordinates.
  Coordinates may be entered in either decimal or sexagesimal notation.
  The given coordinates are rotated according to the
  precession rates to the requested year and printed on the standard output.
  Basic data is taken from the Explanation to the American Ephemeris.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Precess coordinate entered interactively from 1950 to 1990, except where
  the dates are specified otherwise on the command line (lines input by the
  user are marked:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; precess STDIN 1950 1990                     [input]
  12:30:10.12 10:18:27.5                          [input]
    12:32:11.79   10:05:13.09  1990.0
  12:30 10:18                                     [input]
    12:32:01.68   10:04:45.51  1990.0
  12:30 -20 1900                                  [input]
    12:34:42.89  -20:29:46.29  1990.0
  12:30 -20 1900 2000                             [input]
    12:35:14.40  -20:33:04.40  2000.0
  (eof=&lt;ctrl/z&gt;)                                  [input]
  </pre></div>
  <p>
  The following is equivalent, except that coordinate input is taken from
  the file <span style="font-family: monospace;">"coords"</span>, rather than from the terminal:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; precess coords 1950 1990                    [input]
    12:32:11.79   10:05:13.09  1990.0
    12:32:01.68   10:04:45.51  1990.0
    12:34:42.89  -20:29:46.29  1990.0
    12:35:14.40  -20:33:04.40  2000.0
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  
