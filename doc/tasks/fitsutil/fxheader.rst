.. _fxheader:

fxheader: List one line of header description per FITS unit
===========================================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxheader input file_list
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name template or device specification]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name template or device specification]' -->
  <dd>The FITS data source.  This is either a template describing a list of disk
  files.
  </dd>
  </dl>
  <dl>
  <dt><b>(long_header = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(long_header = no) [boolean]' -->
  <dd>Print the full FITS header on the standard output?
  </dd>
  </dl>
  <dl>
  <dt><b>(count_lines = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(count_lines = no) [boolean]' -->
  <dd>Precede each line with a count.
  </dd>
  </dl>
  <dl>
  <dt><b>(short_header = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(short_header = yes) [boolean]' -->
  <dd>Print only a short header?  Lists files processed, their 
  dimensions, size of data type and scaling parameter on the standard output.
  </dd>
  </dl>
  <dl>
  <dt><b>(format_file = '') [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(format_file = '') [file name]' -->
  <dd>If you want to define your own output format -- still limited to one
  line per file -- you can create an ASCII text file with some of the
  special keywords, in addition to your own image header keyword that
  you want to see in the display terminal or in the log file.
  The format of the 'format' file is as follow. One column with the
  keywords and a second with the field width and position of the
  values within the columns. The column format is similar to the
  Fortran print formatted statement.
  The following special keywords are available:
  <div class="highlight-default-notranslate"><pre>
  EXT#        -5.5        # (strign) Line counter (if 'long_header=no')
  EXTTYPE     -10.10      # (string) The type of FITS unit
  BITPIX      -5.5        # (string) Bit per pixels and (I,U,R,D,S).
  DIMENS      -10.10      # (string) Output FITS file dimensionality.
  DATATYPE    -8.8        # (string) Input file data type.
  BZERO       -12.6g      # (float)  Scale offset value.
  BSCALE      -12.6g      # (float)  Scale value.
  NBC         -3.3        # (string) Number of cards available to insert
                          # in header before expansion is mandatory.
  </pre></div>
  In addition to these specials keywords, you can add your own that match
  the ones in the input FITS header.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task quickly lists one or a group of FITS files on disk.
  It reads only the header portion of each file, skipping the data.  An
  optional parameter allows the user to list the full FITS header rather
  than a single line per file. For FITS files with extensions, you can specify
  the extension number to get a listing of one FITS unit.
  The keywords below represent the standard single line of 
  information per processed
  file. You can change this by suplying a filename to the parameter 
  'format_file'. Up to 80 characters per line are sent
  to the display terminal.
  </p>
  <p>
  The following information will be listed in short headers by default.
  The first column is a name of an image header keyword or a special name
  the program will process to give you the requested column information.
  </p>
  <div class="highlight-default-notranslate"><pre>
          EXT#       Extension number
          EXTTYPE    Input FITS diskname.
          EXTNAME    EXTNAME value
          BITPIX     Bits per pixels of the input data and
                     the original datatype. (I,R,D,U,S)
          DIMENS     Input FITS file dimensionality.
          BZERO      Zero offset
          BSCALE     Scale factor
  
  Notes: (I,R,D,U,S) refer to Integer, Real, Double, Unsigned and Short
         input data types, respectively. If the 'ieee' parameter is set,
         a minus (-) sign appears between the letter and the bits figure.
  </pre></div>
  <p>
  'DIMENS' is the number of dimensions in the output FITS file; the  
  format is <span style="font-family: monospace;">"NxNxN"</span>
  If the input file is a table, this keyword
  indicates the number of columns (Fields) and the number of rows in the table
  with the suffix F and R (e.g., 27Fx12R).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Catalog a set of FITS extensions and FITS files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  fi&gt; fxheader f1[3],gen.fit[4],bigf
  </pre></div>
  <p>
  2. Catalog a list of FITS files whose root is 'fits' with long output and
  put a line count.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  fi&gt; fxheader fits* long+ count+
  
  </pre></div>
  <p>
  3. Catalog a FITS file with the extension number. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  fi&gt; fxheader yfile.fits[3]
  
  </pre></div>
  <p>
  will list the 3rd extension (The primary FITS unit is [0]).
  </p>
  <p>
  4. To use an alternate format file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  fi&gt; fxheader mef.fits[3] format=home$myformat.mip
  
  </pre></div>
  <p>
  There is also an alternative format file in fitsutil$format_off.mip that will
  list the header and pixel offset in byte units.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The 'NX' and 'NY' fields are 4 characters wide. A <span style="font-family: monospace;">"*"</span> character will be printed if 
  the value in either field is greater than 9999. Use long headers in this case.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tables/fitsio/catfits, rfits
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
