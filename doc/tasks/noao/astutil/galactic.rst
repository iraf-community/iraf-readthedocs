.. _galactic:

galactic: Convert ra, dec to galactic coordinates
=================================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  galactic files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The name of a file (or a file list or template) containing the coordinates
  to be converted.
  </dd>
  </dl>
  <dl id="l_in_coords">
  <dt><b>in_coords = <span style="font-family: monospace;">"equatorial"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='in_coords' Line='in_coords = "equatorial"' -->
  <dd>Type of input coordinates.  May be either <span style="font-family: monospace;">"equatorial"</span> (RA and DEC) or
  <span style="font-family: monospace;">"galactic"</span> (l and b).
  </dd>
  </dl>
  <dl id="l_print_coords">
  <dt><b>print_coords = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='print_coords' Line='print_coords = yes' -->
  <dd>If <b>print_coords</b> = yes, the RA, DEC and epoch (as well as lII and bII) 
  will be listed on the output file.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Program <b>galactic</b> is used to convert between equatorial and
  galactic coordinates.  It converts in either direction based on the
  specified input coordinates.  Coordinates are read from the input file
  as RA and DEC or galactic longitude and latitude pairs, one pair per
  input line.  Each coordinate pair may optionally be followed by the
  epoch of the equatorial coordinates, in which case the coordinates are
  precessed to 1950.0 (the epoch of definition for the galactic center)
  before conversion for equatorial to galactic or to the specified epoch
  for galactic to equatorial.  Coordinates may be entered in either
  decimal or sexagesimal notation.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert the given RA and DEC coordinates to galactic coordinates.  When
  the epoch is specified as other than 1950.0, precess before converting.
  The lines input by the user are marked:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; galactic STDIN                              [input]
  12:30:10.12 10:18:27.5 1930.                    [input]
  12:30:10.12   10:18:27.5  1930.00     288.4695   72.2884
  12:30 10:18                                     [input]
  12:30:00.00   10:18:00.0  1950.00     287.4598   72.3202
  12.5  10:18                                     [input]
  12:30:00.00   10:18:00.0  1950.00     287.4598   72.3202
  (eof=&lt;ctrl/z&gt;)                                  [input]
  </pre></div>
  <p>
  2. The following is equivalent, except that coordinate input is taken from
  the file <span style="font-family: monospace;">"coords"</span>, rather than from the terminal:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; galactic coords                             [input]
  12:30:10.12   10:18:27.5  1930.00     288.4695   72.2884
  12:30:00.00   10:18:00.0  1950.00     287.4598   72.3202
  12:30:00.00   10:18:00.0  1950.00     287.4598   72.3202
  </pre></div>
  <p>
  3. If image headers contain the coordinates, in this case RA, DEC, and EPOCH,
  then one can get the galactic coordinates for the image by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect *.imh ra,dec,epoch yes | galactic STDIN
  </pre></div>
  <p>
  (Consult the help for the task <b>hselect</b> for information about selecting
  fields from image headers.)
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  
