.. _adumpim:

adumpim: Image survey access debugging task
===========================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  adumpim imsurvey output ra dec size
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_imsurvey">
  <dt><b>imsurvey</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imsurvey' Line='imsurvey' -->
  <dd>The name of the image survey to be queried. Image survey names have the form
  survey@site, e.g. <span style="font-family: monospace;">"dss2@cadc"</span>. The image survey address and query format are
  stored in a record called imsurvey in the image survey configuration file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output query results file. The query results are written
  to the output file without modification, but at present they are implicitly
  assumed to be in fits format. Users should append a <span style="font-family: monospace;">".fits"</span> extension to
  the output file name if they wish the output file to be visible to IRAF
  as a FITS image.
  </dd>
  </dl>
  <dl id="l_ra">
  <dt><b>ra  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ra' Line='ra  ' -->
  <dd>The right ascension of the field center in the units expected by the image
  survey query. The value of ra replaces the default value of the ra query
  parameter.
  </dd>
  </dl>
  <dl id="l_dec">
  <dt><b>dec  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dec' Line='dec  ' -->
  <dd>The declination of the field center in the units expected by the image
  survey query.  The value of dec replaces the default value of the dec query
  parameters. It may be necessary to add or remove a leading + sign from
  in order to make the query function correctly.
  </dd>
  </dl>
  <dl id="l_size">
  <dt><b>size</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='size' Line='size' -->
  <dd>The field size in units expected by the image survey query. The value of size
  replaces the default value of the width, xwidth, ywidth, hwidth, hxwidth,
  and hywidth query
  parameters as appropriate.
  </dd>
  </dl>
  <dl id="l_imdb">
  <dt><b>imdb = <span style="font-family: monospace;">")_.imdb"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imdb' Line='imdb = ")_.imdb"' -->
  <dd>The image survey configuration file. The name of the image survey configuration
  file defaults to the value of the imdb package parameter.  The default
  configuration file is <span style="font-family: monospace;">"astcat$lib/imdb.dat"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Adumpim is a simple image survey access debugging task which queries the
  image survey <i>imsurvey</i>, captures the results, and writes them
  to the file <i>output</i> without modification.
  </p>
  <p>
  The user must supply values for the query parameters ra, dec, and one or
  more of the size query parameters width, xwidth, ywidth, hwidth, xhwidth,
  or yhwidth, by
  specifying appropriate values for the <i>ra</i>, <i>dec</i>, and <i>size</i>
  parameters in the units expected by the image survey query. These values are
  treated as strings and passed directly to the image survey query without
  coordinate transformations or units conversions.
  </p>
  <p>
  The image survey configuration file <i>imdb</i> contains a record for each
  supported <i>imsurvey</i>. This record contains the image survey address,
  the query format, and the output format. The default image survey configuration
  file is <span style="font-family: monospace;">"astcat$lib/imdb.dat"</span>.
  </p>
  <p>
  The output of adumpim can be used to refine the image survey record in the
  image survey configuration file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the supported image surveys, select an image survey to query, make
  the query and capture the results. The aslist task is used  to list
  the supported image surveys and the query and output formats for the selected
  image survey as shown below. The query format tells the user that the input
  ra and dec must be in sexagesimal hours and degrees and in the J2000
  coordinate system that the size parameter is a radius in minutes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aslist *
  dss2@cadc
  
  cl&gt; aslist dss2@cadc verb+
  Scanning image surveys database astcat$lib/imdb.dat
  Listing the supported image surveys
  dss2@cadc
  wcs dss
  nwcs 10
        wxref INDEF INDEF d pixels
        wyref INDEF INDEF d pixels
        wxmag INDEF 1.009 d arcsec/pixel
        wymag INDEF 1.009 d arcsec/pixel
        wxrot INDEF 180.0 d degrees
        wyrot INDEF 0.0 d degrees
       wraref OBJCTRA INDEF d hms
      wdecref OBJCTDEC INDEF d dms
        wproj INDEF tan c INDEF
      wsystem INDEF J2000 c INDEF
  nkeys 13
      observat INDEF Palomar c INDEF
      esitelng INDEF +116:51:46.80 d degrees
      esitelat INDEF +33:21:21.6 d degrees
      esitealt INDEF 1706 r meters
       esitetz INDEF 8 r INDEF
       emjdobs INDEF INDEF c INDEF
      edatamin INDEF INDEF r ADU
      edatamax INDEF INDEF r ADU
         egain INDEF INDEF r e-/ADU
      erdnoise INDEF INDEF r e-
       ewavlen INDEF INDEF r angstroms
         etemp INDEF INDEF r degrees
        epress INDEF INDEF r mbars
  
  cl&gt; adumpim dss2@cadc m51.fits 13:29:53.27 +47:11:48.4 10.0
  
  cl&gt; imheader m51.fits
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  aslist, agetim
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
