.. _hdtoi:

hdtoi: Apply DTOI transformation to density image
=================================================

**Package: dtoi**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hdtoi input output database
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output image names.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>Name of text database describing HD curve.
  </dd>
  </dl>
  <dl id="l_fog">
  <dt><b>fog = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fog' Line='fog = ""' -->
  <dd>Value of fog level, read from database if unspecified.
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = <span style="font-family: monospace;">"mean"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = "mean"' -->
  <dd>Option for calculating fog density when <b>fog</b> is a file list, can be
  either <span style="font-family: monospace;">"mean"</span> or <span style="font-family: monospace;">"median"</span>.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = 3.0' -->
  <dd>If <b>fog</b> is a file name, and <b>option</b> = <span style="font-family: monospace;">"mean"</span>, the mean fog density
  is iteratively calculated using this rejection criteria.
  </dd>
  </dl>
  <dl id="l_floor">
  <dt><b>floor = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='floor' Line='floor = 0.0' -->
  <dd>Value assigned to levels below fog, can be either 0.0 or -1.0.  
  </dd>
  </dl>
  <dl id="l_ceiling">
  <dt><b>ceiling = 30000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ceiling' Line='ceiling = 30000.' -->
  <dd>The final intensities are scaled to this value, such that a saturated
  input density equals <b>ceiling</b> on output.
  </dd>
  </dl>
  <dl id="l_datatype">
  <dt><b>datatype = <span style="font-family: monospace;">"r"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datatype' Line='datatype = "r"' -->
  <dd>Datatype of output image pixels.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print log of processing to STDOUT.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>hdtoi</i> transforms one image to another as described by the 
  <b>database</b>.  There is only one HD curve per run; the same 
  transformation is applied to all input images.
  </p>
  <p>
  The fog value can be obtained in three ways: read from the database, read
  as a floating point number, or calculated from a list of fog images.  If 
  parameter <b>fog</b> is not specified, the fog value is read from 
  <b>database</b>.  If <b>fog</b> is specified, it can be entered
  as either a floating point number or as a list of file names.  If the
  value cannot be read as a number, it is assumed to be a file name.  In that
  case, the density of each file in the fog list is calculated and the 
  average of these values is subtracted from <b>input</b> before processing.
  The algorithm used to calculate the fog density is selected by the
  <b>option</b> parameter, and is either a <span style="font-family: monospace;">"mean"</span> or <span style="font-family: monospace;">"median"</span> calculation.
  The fog density can be the mean value after pixels more than the specified
  number of sigma have been rejected, or the median value of all the fog spot
  pixels.
  </p>
  <p>
  The fog value is subtracted from the input image before the transformation
  takes place.  It is possible that some density values will fall below
  the fog level; these values are handled in one of two ways.  Values
  below the fog value are set equal to 0.0 when <b>floor</b> = 0.0.  If 
  <b>floor</b> = -1.0, the resulting intensity = -1 * intensity (abs (value)).
  </p>
  <p>
  A scaling factor is applied to the final intensities, as typically
  they will be &lt; 1.0.  The <b>ceiling</b> parameter is used to specify what
  value a saturated density is transformed to; all intensities are scaled
  to this upper limit.  The precision of the transformation is unaffected by 
  this parameter, although caution must be used if the output image pixel
  type is an integer.  The user is responsible for choosing
  a <b>ceiling</b> that avoids the truncation of significant digits.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Convert three density images to intensity images as described in database db1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hdtoi denin* intim1,intim2,intim3 db1
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Task <b>hdtoi</b> requires 20 cpu seconds to transform a 512 square image, with
  a 12 bit data range, on a VAX 750
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  spotlist, dematch, hdfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  
