.. _sptabguide:

sptabguide: Guide to using spectral tables with onedspec and rv
===============================================================

**Package: sptable**

.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  Spectral tables are file formats for one dimensional spectra represented as
  multi-column tables.  These formats include text files and FITS binary
  tables.  In the future this could also include XML tables such as
  VOTABLES. Typically such tables include a column for the dispersion
  coordinates such as wavelength or frequency.  This guide describes how
  spectral tables may be used with the IRAF spectral packages ONEDSPEC
  and RV.
  </p>
  <p>
  Spectral tables provide a very wide range of possible formats,
  particularly since there are minimal standards.  
  </p>
  </section>
  <section id="s_the_spectrum_table_database_and_package_parameters">
  <h3>The spectrum table database and package parameters</h3>
  <p>
  It would be highly inconvenient to require specifying all the details of
  a spectral table in each IRAF task.  Instead these details are specified
  through package parameters; i.e. onedspec and rv.  The principle is that
  one normally will work with one type of format with, possibly, many spectra
  and many tasks.  Setting information for the package allows this to be
  done once in this case.
  </p>
  <p>
  While there can be a wide variety of formats it is common that data
  providers will use one format for spectral data from an observatory,
  instrument, or pipeline.  So a way to simplify describing spectral
  tables is with a database of formats.  This is called a spectrum table
  database.  Users can use the database provided with the IRAF package
  as well as easily customizing thier own version and make additions.
  Because there is no standard for identifying a particular format the
  spectrum table database applies a heuristic that generally works well.
  This heuristic consist of identifying a format by the set of column names,
  including their order, in the file.  This set of column names act like a
  fingerprint that the database translates into the detailed description
  of the table.
  </p>
  </section>
  <section id="s_spectrum_table_package_parameters">
  <h3>Spectrum table package parameters</h3>
  <p>
  The fundamental requirement for defining a spectrum table is the column
  identifications.  Columns are defined by range lists of column numbers.
  A range list is one or more comma separated ranges.  A range may be a
  single number, a pair of hypen separated numbers, and some less common
  variations as described in the help page <span style="font-family: monospace;">"ranges"</span>.  Column numbers are used
  instead of column names in order to allow for more complex situations as
  well as for simple text tables without column names.
  </p>
  <p>
  The simplest spectrum table consists of the most basic type of column,
  the flux values, which might be instrumental numbers or some calibrated
  photon unit.  There can be multiple flux columns, each of which is
  considered a different spectrum.  In these cases the dispersion values
  are just the row numbers which are akin to pixels in an image.  The flux
  columns are specified by the package parameter <span style="font-family: monospace;">"tbspec"</span>.
  </p>
  <p>
  The second basic column type is the dispersion coordinate.  There can
  only be one dispersion column, though one could use the same file with
  different dispersion columns specified as separate spectrum table descriptions.
  The dispersion column is specified by the package parameter <span style="font-family: monospace;">"tbdisp"</span>.
  </p>
  <p>
  There may also be two types of optional associated quantities; an error
  spectrum and an associated spectrum.  These are defined by the parameters
  <span style="font-family: monospace;">"tberr"</span> and <span style="font-family: monospace;">"tbassoc"</span>.  An associated spectrum might be an uncalibrated
  version of the spectrum, a different type of extraction, or even more
  creative types.
  </p>
  <p>
  There are also two parameters specifying the flux units, <span style="font-family: monospace;">"tbfunits"</span>, and
  dispersion units, <span style="font-family: monospace;">"tbdunits"</span>.  Ideally these should be specified by the
  units attribute of named columns.  These parameters are mostly intended for
  the case of simple text tables that don't have named columns.  The units
  understood are found in the help for <span style="font-family: monospace;">"onedspec.package"</span>, <span style="font-family: monospace;">"disptrans"</span>, or
  <span style="font-family: monospace;">"splot"</span>.  For instance, common dispersion units are <span style="font-family: monospace;">"angstroms"</span> and <span style="font-family: monospace;">"nm"</span>.
  </p>
  <p>
  A final convenience package parameter, <span style="font-family: monospace;">"tbextn"</span>, specifies a default
  extension.  Note the period is not included in this parameter.  This allows
  using tasks with names that don't include the extension.  For example,
  if all the spectra are <span style="font-family: monospace;">".fits"</span> or <span style="font-family: monospace;">".txt"</span> you can refer to spec.fits or
  spec.txt as just spec.
  </p>
  </section>
  <section id="s_spectrum_table_database_format">
  <h3>Spectrum table database format</h3>
  <p>
  The spectrum table database is a text file with lines consisting of
  1) a list of column names, 2) an identifier, 3) the dispersion column,
  4) the flux columns, 5) any flux error columns, and 6) and associated
  data columns.  The column fields are range lists and a value of NULL may
  be used if there are no columns of a particular type (though a minimum
  of a single flux column is required).  Each field may not contain blanks.
  Additionally there may be blank and comment lines with <span style="font-family: monospace;">'#'</span> as the comment
  character.  The identifier is not currently used by the tasks.
  </p>
  <p>
  The column names are those understood by the <span style="font-family: monospace;">"nttools"</span> package.  In
  particular, simple text tables without column definitions have column
  names <span style="font-family: monospace;">"C1"</span>, <span style="font-family: monospace;">"C2"</span>, etc.  Note that the matching is case insensitive.
  </p>
  <p>
  Below are some examples:
  </p>
  <div class="highlight-default-notranslate"><pre>
  # A simple ASCII file with a single column.
  C1 SIMPLE_ASCII NULL 1 NULL NULL
  
  # A simple ASCII file with a two columns: dispersion, spectrum.
  C1,C2 SIMPLE_ASCII 1 2 NULL NULL
  
  # Some  simple common defaults.
  WAVE,FLUX SIMPLE_TABLE 1 2 NULL NULL
  FLUX,WAVE1 SIMPLE_TABLE 2 1 NULL NULL
  FLUX,WAVE1,WAVE2 SIMPLE_TABLE 2 1 NULL NULL
  
  # A STIS format.
  WAVE,FLUX,DATA_QUALITY,SIGMA STIS 1 2 NULL NULL
  
  # An IUE format.
  WAVE,FLUX,SIGMA,QUALITY IUE 1 2 NULL NULL
  
  # An STECF format.
  SPORDER,NELEM,WAVELENGTH,GROSS,BACKGROUND,NET,FLUX,ERROR,
  NET_ERROR,DQ,A2CENTER,EXTRSIZE,MAXSRCH,BK1SIZE,BK2SIZE,
  BK1OFFST,BK2OFFST,EXTRLOCY,OFFSET STECF 3 7 8 6
  </pre></div>
  <p>
  Note the last example is shown wrapped to illustrate the complexity
  of the columns but in the database file this would be a single
  line.
  </p>
  <p>
  As mentioned previously, the association between a particular table
  file and its description is through the comma separated list of all
  the column names in order.  So, for instance, all files having just
  the two columns WAVE and FLUX would match the SIMPLE_TABLE entry but
  would not match either WAVELENGTH/FLUX, WAVE/SPECTRUM, or
  WAVE/FLUX/ERR.
  </p>
  <p>
  The spectrum table database is specified by the <span style="font-family: monospace;">"sptabledb"</span> package parameter.
  A default is supplied but the user may copy the file to the working or home
  directory and modify it, or simply create their own as described above.
  </p>
  </section>
  <section id="s_iraf_spectral_tasks">
  <h3>Iraf spectral tasks</h3>
  <p>
  Spectrum tables are understood by the onedspec and rv package tasks.
  These tasks have a spectrum data model which includes the concepts
  of multiple spectra, called apertures, and associated elements, called
  bands.  These may be thought of in the same way as the spectrum image
  formats of onedspec, equispec or multispec, and echelle.  A
  description of these may be found under the topic <span style="font-family: monospace;">"specwcs"</span>.  In
  these formats multiple spectra are stored as rows in a 2D or 3D
  image and as bands in a 3D image.  Note there can be a 3D image with
  a single row.  The main effect of understanding this is that when
  a table has multiple flux, error, and associated columns defined by
  range lists they manifest in the task parameters as apertures and
  bands.
  </p>
  </section>
  <section id="s_physical_file_formats">
  <h3>Physical file formats</h3>
  <p>
  Tables are accessed using the IRAF tables library, which is inherited
  from the STSDAS tables system.  This means that any format understood
  by the nttools package may a spectrum table.  The formats currently
  supported by this library are text tables with and without column
  descriptors, FITS binary tables, and STSDAS tables.  For FITS binary
  tables the FITS extension syntax also applies if there are multiple
  extensions.  Also the row and column selector syntax may be used (see
  below).
  </p>
  <p>
  The most important thing to note, as mentioned earlier, is that simple
  ASCII text tables consisting only of lines with the same number of
  whitespace separated columns may be used and, when necessary, the
  implied column names are C1, C2, etc, which are case insensitive.
  ASCII tables may have headers and column descriptors as supported by the
  tables library and which have lines beginning with <span style="font-family: monospace;">"#k"</span> for keywords and
  <span style="font-family: monospace;">"#c"</span> for columns definitions.  If you want to add column names and units
  see the help for <span style="font-family: monospace;">"tcreate"</span>.
  </p>
  <p>
  Another special case is FITS binary tables with array cells. In this
  case each column would have a one-dimensional array and only one
  row may be present.
  </p>
  <p>
  It should be obvious, but all the vectors must have the same length.
  In other words, for column tables there must be the same number of rows
  while for array cells each array must be the same length.
  </p>
  </section>
  <section id="s_table_selector_syntax">
  <h3>Table selector syntax</h3>
  <p>
  The table selector syntax, see the help topic <span style="font-family: monospace;">"selectors"</span>, allows
  on-the-fly selection of rows and columns.  For simply cutting out a
  dispersion region this could be done with a selector but some of the
  common spectral tasks have this facility; e.g. SPLOT.
  </p>
  <p>
  However, one interesting case is for multi-order (e.g. echelle) spectra in
  a format where there is a just one dispersion, flux, and order column.
  So different orders have to be separated based on the order column.
  For instance, if the order column is called <span style="font-family: monospace;">"order"</span> then
  </p>
  <div class="highlight-default-notranslate"><pre>
  ondspec&gt; splot myechelle.fits[r:order=5]
  </pre></div>
  <p>
  plots order 5.
  </p>
  <p>
  The ONEDSPEC tasks applicable to an echelle do not directly deal with
  this concatenated order format.  Rather, an echelle format requires each
  order to be a separate column.  The table selector syntax and SCOPY could
  be used to convert to the echelle format.  The NTTOOLS package, described
  next, may provide an easier method to convert.
  </p>
  </section>
  <section id="s_nttools_package">
  <h3>Nttools package</h3>
  <p>
  Any spectral table format may be manipulated with the NTTOOLS package, which
  is essentially a version of the STSDAS TABLES package added to the IRAF
  core system.  There are a wide variety of spectral format manipulations
  that can be performed with these tools.  These can include changing
  formats, expressions, and joining, projecting, and merging.  In effect,
  these supplement the more spectroscopy oriented tasks in the ONEDSPEC
  and RV package in a nice symbiosis.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  specwcs, onedspec, rv, ranges, nttools, selectors
  </p>
  
  </section>
  
  <!-- Contents: 'Introduction' 'The Spectrum Table Database and Package Parameters' 'Spectrum Table Package Parameters' 'Spectrum Table Database Format' 'IRAF Spectral Tasks' 'Physical File Formats' 'Table Selector Syntax' 'NTTOOLS Package' 'See Also'  -->
  
