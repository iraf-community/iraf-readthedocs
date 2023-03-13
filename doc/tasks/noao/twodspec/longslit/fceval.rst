.. _fceval:

fceval: Evaluate coordinates using the FITSCOORDS solutions
===========================================================

**Package: longslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fceval input output fitnames
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input text file of pixel coordinates.  This may be <span style="font-family: monospace;">"STDIN"</span> to read
  coordinates from the terminal or pipe.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output text file of pixel coordinates and fitted coordinates.  This may
  be <span style="font-family: monospace;">"STDOUT"</span> to write coordinates to the terminal or pipe.
  </dd>
  </dl>
  <dl id="l_fitnames">
  <dt><b>fitnames  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitnames' Line='fitnames  ' -->
  <dd>Names of the user coordinate maps to evaluate.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database containing the coordinate maps.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task transforms pixel coordinates to the world coordinates fit with
  FITCOORDS.  When there is no map for an axis the identify transform is
  used.  If there are more the one map for an axis the average of the mapped
  coordinates is output.  This is the same behavior as TRANSFORM.
  </p>
  <p>
  The input file consists of two columns giving the x and y pixel values
  in the frame of the untransformed image data.  The output is a file
  with four columns giving the input x any y pixel values and the
  user coordinates fit by FITCOORDS.
  </p>
  <p>
  Two typical uses for this task are to look up world coordinates for
  points in the untransformed data and to generate transformations using
  GEOMAP and GEOTRAN.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Evaluate a wavelength and slit position fit where the input pixel coordinates
  are entered interactively and the output is written to the terminal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fceval STDIN STDOUT arcfit,std
  1 1
  1. 1. 20.60425149463117 4202.47202514205
  60 1
  60. 1. 79.60425149463118 4203.316616448186
  1 512
  1. 512. 19.15606081299484 7356.089801036373
  60 512
  60. 512. 78.15606081299485 7355.042495319318
  </pre></div>
  <p>
  In this case the first axis corresponds to the spatial dimension and
  the second to the dispersion dimension.  The arcfit was created using
  Angstroms and so the units of the last column is Angstroms.
  </p>
  <p>
  2. One use of this task is to generate the inverse transformation from
  that produced by TRANSFORM.  The steps are: 1) produce a grid of
  coordinates using LISTPIX and FCEVAL, 2) convert the user coordinates to
  pixel coordinates in the transformed data using WCSCTRAN, 3) fit a
  transformation using GEOMAP, and 4) transform the data with GEOTRAN.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; listpix orig[*:5,*:5] wcs=physical verb- |
  &gt;&gt;&gt; fceval STDIN STDOUT arcfit,std |
  &gt;&gt;&gt; wcsctran STDIN coords trans world logical columns="3 4"
  cl&gt; geomap coords geomap.db 1 61 1 512
  cl&gt; geotran trans origNEW geomap.db coords flux+
  </pre></div>
  <p>
  This example uses pipes to eliminate intermediate files.  But these
  files can be useful for understanding the process.  LIXTPIX is used to
  generate a grid of points with some subsampling.  Be sure to use <span style="font-family: monospace;">"physical"</span>
  for the coordinate system otherwise the grid of x and y values will be
  for the subsection.  The order of the columns will be appropriate for
  GEOMAP to compute the inverse transformation.  By reversing the order
  of the columns one could generate a transformation similar to that
  produced by TRANSFORM in order to use features in GEOTRAN not provided
  by TRANSFORM.  However, the world coordinate system information will
  not be automatically set.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fitcoords, transform, geomap, geotran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
