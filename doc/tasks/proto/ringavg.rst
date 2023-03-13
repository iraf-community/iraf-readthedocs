.. _ringavg:

ringavg: Compute pixel averages in concentric rings about given center
======================================================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ringavg image xc yc
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Image to be used.
  </dd>
  </dl>
  <dl id="l_xc">
  <dt><b>xc, yc</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xc' Line='xc, yc' -->
  <dd>Pixel coordinate for center of rings.
  </dd>
  </dl>
  <dl id="l_r1">
  <dt><b>r1 = 0, r2 = 10, dr = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='r1' Line='r1 = 0, r2 = 10, dr = 1' -->
  <dd>Rings to be measured.  <i>r1</i> is the inner radius of the first ring,
  <i>r2</i> is the outer radius of the last bin, and <i>dr</i> is the widths
  of the rings.  The values are in units of pixels.
  </dd>
  </dl>
  <dl id="l_labels">
  <dt><b>labels = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='labels' Line='labels = yes' -->
  <dd>Print column labels for the output?
  </dd>
  </dl>
  <dl id="l_vebar">
  <dt><b>vebar = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vebar' Line='vebar = no' -->
  <dd>If <i>vebar</i> is yes then the standard deviation and standard error will
  be printed as negative values for use with <b>graph</b>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Pixels are binned into a series of concentric rings centered on a given
  position in the input image.  The rings are defined by an inner radius
  for the first ring, an outer radius for the last ring, and the width
  of the rings.  The statistics of the pixel values in each ring are then 
  computed and list to the standard output.  The output lines consist
  of the inner and outer ring radii, the number of pixels, the average value,
  the standard deviation of the value (corrected for population size), and
  the standard error.  The parameter <i>label</i> selects whether to include
  column labels.
  </p>
  <p>
  If the ring average are to be plotted with the task <b>graph</b> using
  the option to plot error bars based on the standard deviation or standard
  error then the <i>vebar</i> parameter may be set to write the values as
  negative values are required by that task.
  </p>
  <p>
  This task is a script and so users may copy it and modify it as desired.
  Because it is a script it will be very slow if r2 becomes large.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the ring averages with labels and output to the terminal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ringavg pwimage 17 17
  #  R min    R max     Npix    Average    Std Dev    Std Err
      0.00     1.00        5      7.336       9.16      4.096
      1.00     2.00        8     0.2416     0.2219    0.07844
      2.00     3.00       16     0.3994     0.5327     0.1332
      3.00     4.00       20    0.06211    0.05491    0.01228
      4.00     5.00       32     0.0987    0.08469    0.01497
      5.00     6.00       32    0.06983    0.06125    0.01083
      6.00     7.00       36     0.0641     0.0839    0.01398
      7.00     8.00       48    0.06731    0.05373   0.007755
      8.00     9.00       56    0.06146    0.07601    0.01016
      9.00    10.00       64    0.05626    0.05846   0.007308
  </pre></div>
  <p>
  2.  Plot the ring averages with standard errors used for error bars.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ringavg pwimage 17 17 label- vebar+ | fields STDIN 2,4,6 |
  &gt;&gt;&gt; graph point+ marker=vebar
  </pre></div>
  <p>
  3.  Plot ring averages for galaxy in dev$pix.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ringavg dev$pix 256 256 r2=100 dr=5 label- | fields STDIN 2,4 |
  &gt;&gt;&gt; graph logy+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  pradprof, psfmeasure, radprof
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
