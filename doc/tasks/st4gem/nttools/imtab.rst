.. _imtab:

imtab: Copy an image to a table column.
=======================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imtab input outtable colname
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task copies data from an image to a table.
  Pixel values are read from the image line by line
  and written to a column in increasing row number.
  The image may be of any dimension,
  but a single column is written.
  If the table already exists then columns will be added to it;
  names of new columns must not conflict with existing names.
  If the table does not exist it will be created.
  </p>
  <p>
  The number of names in the 'input' list must be the same as
  the number of names in the 'outtable' list,
  unless 'outtable' is <span style="font-family: monospace;">"STDOUT"</span>.
  </p>
  <p>
  Information about the image dimension and axis lengths will not be kept
  in keywords, but there is an option to write the image pixel numbers
  to columns of the table.
  The pixel coordinates may be just the pixel numbers,
  or they may be world coordinates at the pixel locations.
  </p>
  <p>
  A history record will be added to the table giving
  the name of the data column and the name of the image.
  If pixel coordinates are written to the table,
  another history record is written that also gives
  the column name for the image data
  and gives the column names for the pixel coordinates.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input = <span style="font-family: monospace;">""</span> [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input = "" [file name template]' -->
  <dd>The names of the images to be written to the tables.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable = <span style="font-family: monospace;">""</span> [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable = "" [file name template]' -->
  <dd>The names of the output tables.
  If outtable = <span style="font-family: monospace;">"STDOUT"</span> or if the output has been redirected,
  the values will be written to the standard output.
  If the output table is of type text (e.g. STDOUT),
  the data values will be in the first column.
  If the pixel coordinates are also printed,
  they will be in the following columns.
  </dd>
  </dl>
  <dl id="l_colname">
  <dt><b>colname = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='colname' Line='colname = "" [string]' -->
  <dd>A column of this name will be created in the output table,
  and the values of the image will be written to this column.
  The same column name will be used for all output tables.
  </dd>
  </dl>
  <dl>
  <dt><b>(pname = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pname = "") [string]' -->
  <dd>If 'pname' is not null,
  the pixel coordinates will also be written to columns of the table.
  The names of these columns will be the value of 'pname' with the
  numbers 1, 2, 3, etc appended,
  corresponding to the sample number, line number, band number, etc.
  This may be especially useful for a multi-dimensional input image,
  since all the data values are written to one column.
  The same column names will be used for all output tables.
  See also 'wcs' and 'formats'.
  If 'pname' is null (or blank) the pixel numbers will not be written.
  </dd>
  </dl>
  <dl>
  <dt><b>(wcs = <span style="font-family: monospace;">"logical"</span>) [string, allowed values:  logical | physical | world]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wcs = "logical") [string, allowed values:  logical | physical | world]' -->
  <dd>This parameter is only gotten if 'pname' is not null.
  In this case, the user has the option of which coordinate system
  should be used when writing pixel coordinates to the table.
  The <span style="font-family: monospace;">"logical"</span> coordinates are simply the pixel numbers
  of the image or image section.
  The <span style="font-family: monospace;">"physical"</span> coordinates are also pixel numbers,
  but they can differ from logical coordinates
  if an image section has been taken.
  Physical coordinates have the same origin and sampling as the original image.
  The <span style="font-family: monospace;">"world"</span> coordinates are coordinates such as wavelength, time,
  or right ascension and declination.
  The translation from logical to world coordinates is given by
  header keywords CRVAL1, CRPIX1, CD1_1, CTYPE1, etc.
  The number of pixel coordinates written by 'imtab' differs from
  the number written by 'listpixels' when wcs = <span style="font-family: monospace;">"physical"</span> or <span style="font-family: monospace;">"world"</span>
  and an image section was used that reduces the dimension of the image.
  'imtab' gives one pixel coordinate column for each dimension
  of the original image, while 'listpixels' gives one pixel coordinate
  for each dimension of the image section.
  Type <span style="font-family: monospace;">"help mwcs$MWCS.hlp fi+"</span> for extensive information on coordinate systems.
  </dd>
  </dl>
  <dl>
  <dt><b>(formats) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(formats) [string]' -->
  <dd>The print formats to use for the pixel coordinates, one format
  per axis, with the individual formats separated by whitespace.
  This parameter is only gotten if 'pname' is not null.
  If the formats are not given, a default format is assigned.
  See the help for 'listpixels' for extensive information on formats.
  These formats are saved in the descriptors for the table columns,
  so these formats will be used if the table is printed.
  If the output table is text rather than binary,
  these formats will be used to write the coordinates to the text table.
  </dd>
  </dl>
  <dl>
  <dt><b>(tbltype = <span style="font-family: monospace;">"default"</span>) [string, allowed values: default | row |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tbltype = "default") [string, allowed values: default | row |' -->
  <dd>column | text ]
  If the output table does not already exist,
  you can specify whether the table should be created in row or column
  ordered format.
  As an alternative to a binary table,
  tbltype = <span style="font-family: monospace;">"text"</span> means the output will be a plain text file.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Copy image <span style="font-family: monospace;">"hr465_flux.imh"</span> to table <span style="font-family: monospace;">"hr465.tab"</span>, column <span style="font-family: monospace;">"flux"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; imtab hr465_flux.imh hr465.tab flux
  </pre></div>
  <p>
  2.  Copy the 2-D image <span style="font-family: monospace;">"ir27.hhh"</span> to column <span style="font-family: monospace;">"ir27"</span> of table <span style="font-family: monospace;">"map.tab"</span>,
  saving the pixel numbers in columns <span style="font-family: monospace;">"pix1"</span> and <span style="font-family: monospace;">"pix2"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; imtab ir27.hhh map.tab ir27 pname="pix"
  </pre></div>
  <p>
  3.  Copy the 1-D section [257:257,129:384] of
  x0y70206t.d0h to column <span style="font-family: monospace;">"x0y70206"</span> of table <span style="font-family: monospace;">"focus.tab"</span>.
  Also write the right ascension and declination
  (<span style="font-family: monospace;">"world"</span> coordinates) to columns <span style="font-family: monospace;">"p1"</span> and <span style="font-family: monospace;">"p2"</span> respectively
  using HH:MM:SS.d and DD:MM:SS.d formats.
  We use <span style="font-family: monospace;">"%12.1H"</span> for right ascension and <span style="font-family: monospace;">"%12.1h"</span> for declination.
  The capital <span style="font-family: monospace;">"H"</span> in the format means that the values will be divided by 15
  to convert from degrees to hours before formatting in sexagesimal.
  Note that we get two columns of pixel coordinates even though
  the image section is only 1-D.
  Physical or world coordinates will be 2-D in this case
  because the original image <span style="font-family: monospace;">"x0y70206t.d0h"</span> is 2-D.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; imtab x0y70206t.d0h[257:257,129:384] focus.tab x0y70206 \
  &gt;&gt;&gt; pname="p" wcs="world" formats="%12.1H %12.1h"
  </pre></div>
  <p>
  4.  Use the same image as in the previous example,
  but print the values on the standard output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; imtab x0y70206t.d0h[257:257,129:384] STDOUT x0y70206 \
  &gt;&gt;&gt; pname="p" wcs="world" formats="%12.1H %12.1h"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Phil Hodge.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  The 'tabim' task copies a column of a table to an image.
  The 'listpixels' task in the 'images' package writes data values and
  pixel coordinates to the standard output.
  The parameters 'wcs' and 'formats' are the same in 'imtab' and 'listpixels'.
  For detailed information on the distinction between logical, physical and
  world coordinates, type <span style="font-family: monospace;">"help mwcs$MWCS.hlp fi+"</span>.
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables option=sys"</span> for a higher-level description of
  the tables package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
