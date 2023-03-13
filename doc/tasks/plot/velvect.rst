.. _velvect:

velvect: Plot representation of a velocity field
================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  velvect uimage vimage
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_uimage">
  <dt><b>uimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='uimage' Line='uimage' -->
  <dd>Name of image containing u components of the velocity field.
  </dd>
  </dl>
  <dl id="l_vimage">
  <dt><b>vimage </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vimage' Line='vimage ' -->
  <dd>Name of image containing v components of the velocity field.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = stdgraph</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = stdgraph' -->
  <dd>Output device for plot.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>Title to be centered over the plot.  By default, it will be the title
  from the image header of the <b>uimage</b>.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append to an old plot?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print warning messages?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>velvect</i> draws a representation of a two-dimensional velocity
  field by drawing arrows from each data location.  The length of the arrow
  is proportional to the strength of the field at that location and the direction
  of the arrow indicates the direction of the flow at that location.  The
  two images <i>uimage</i> and <i>vimage</i> contain the velocity field to be
  plotted.  The vector at the point (i,j) has:
  </p>
  <div class="highlight-default-notranslate"><pre>
  magnitude = sqrt (uimage(i,j)**2 + vimage(i,j)**2)
  direction = atan2 (vimage(i,j), uimage(i,j))
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Make a vector plot from the two images <span style="font-family: monospace;">"crab.blue"</span> and <span style="font-family: monospace;">"crab.red"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; velvect crab.blue crab.red
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  
