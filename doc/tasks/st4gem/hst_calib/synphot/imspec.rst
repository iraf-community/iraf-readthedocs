.. _imspec:

imspec: Convert an image to a synphot spectrum or vice versa.
=============================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imspec input output
  </p>
  </section>
  <section id="s_description_">
  <h3>Description </h3>
  <p>
  This task will convert a one-dimensional image into an ST4GEM table that
  can be used by the other 'synphot' tasks, or convert a 'synphot' table
  to a one-dimensional image. The type of conversion performed is
  determined automatically from the type of the input file.  More than
  one file may be converted at a time by using a list of input and
  output files. An optional wavelength image may be supplied along with
  the input and output files. If the input file is an image and no
  wavelength image is supplied, the wavelengths are computed from the
  world coordinate system in the input image. If a wavelength image is
  supplied, the world coordinate system in the input image is ignored
  and the wavelengths are copied from the wavelength image, which are
  assumed to be in a one-to-one correspondence with the fluxes in the
  input image. If the input file is a table and a wavelength image is
  specified, the flux column in the input table is copied to the output
  image and the wavelength column is copied to the wavelength image.
  </p>
  <p>
  You can optionally specify the length of the output file by
  setting the parameter 'olength'. The length of an image is its number
  of pixels and the length of a table is the number of rows. If the
  output file is a table, the flux units can be set by the parameter
  'form'. If an input table has INDEF values, these will be replaced in
  the output image by the value specified in the parameter 'badpix'.
  </p>
  <p>
  If a wavelength image is supplied, the wavelengths must be in
  monotonic order. If no wavelength image is supplied, the input image
  must be one-dimensional and have a linear world coordinate system.  An
  input table must contain two columns, labeled WAVELENGTH and FLUX (or
  FLUX1). All other columns will be ignored. The values in the
  wavelength column must be in monotonic order. If wavelength and flux
  units are specified in the table, they must be units supported by the
  synphot package.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>List of input files. Files may be either images or tables. This task
  will determine the type of each input file and create an output file
  of the opposite type. Only one group can be copied from each input
  file. If the group is not specified in the file name, the first group
  will be copied.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string]' -->
  <dd>List of output files. The number of output files must match the number
  of input files. The type of the output file will be determined from
  the corresponding input file.
  </dd>
  </dl>
  <dl>
  <dt><b>(wave = <span style="font-family: monospace;">" "</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wave = " ") [file name]' -->
  <dd>The name of the wavelength file. If this name is blank (the default),
  no wavelength file will be used. If wavelength files are used, the
  number of wavelength files must match the number of input and output
  files. If a wavelength file is used and the input file is an image,
  the world coordinates of the input image are ignored and the
  wavelengths are copied from the wavelength image. If a wavelength file
  is used and the input file is a table, the wavelength column from the
  table is used to create the wavelength image.
  </dd>
  </dl>
  <dl>
  <dt><b>(inform = <span style="font-family: monospace;">"counts"</span>) [string, allowed values: obmag | stmag |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inform = "counts") [string, allowed values: obmag | stmag |' -->
  <dd>vegamag | counts | mjy | jy | fnu | flam | photnu | photlam]
  The flux units of the input spectrum. If the input spectrum is a
  table, the flux units will be read from the flux column units and this
  parameter will be ignored unless the column units are blank.
  </dd>
  </dl>
  <dl>
  <dt><b>(outform = <span style="font-family: monospace;">"counts"</span>) [string, allowed values: obmag | stmag |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outform = "counts") [string, allowed values: obmag | stmag |' -->
  <dd>vegamag | counts | mjy | jy | fnu | flam | photnu | photlam]
  The flux units of the output spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>(olength = INDEF) [integer] [min = 1, max = INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(olength = INDEF) [integer] [min = 1, max = INDEF]' -->
  <dd>Length of the output file.
  If this parameter is set to INDEF (the default), the length of the
  output file will be the same as the length of the input file.
  Otherwise, the length of the output file will be that specified by
  this parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(badpix = 0.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(badpix = 0.0) [real]' -->
  <dd>The value of this parameter will be used to replace flux values from
  the input table when they are INDEF.
  </dd>
  </dl>
  <dl>
  <dt><b>(refdata = <span style="font-family: monospace;">""</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refdata = "") [pset name]' -->
  <dd>Parameter set for reference data for tasks in the synphot package. The
  only parameter in this pset used by this task is 'area', the HST
  telescope area in cm^2.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Copy a 'synphot' table to an image. Set the length of the output
  image to 512 pixels:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; imspec crrefer$calspec/eta_uma_002.tab eta_uma.hhh olength=512
  </pre></div>
  <p>
  2.Copy a set of FOS spectra into tables with the same rootname as the
  input file, but an extension of '.tab'.  Use the FOS wavelength images
  (<span style="font-family: monospace;">"c0h"</span> images) to determine the wavelength array in the output table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; imspec y*.c1h y*.%c1h%tab% wave=y*.c0h
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ttools.imtab, ttools.tabim
  </p>
  <p>
  Type <span style="font-family: monospace;">"help synphot opt=sys"</span> for a description of table formats.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION ' 'PARAMETERS' 'EXAMPLES' 'SEE ALSO'  -->
  
