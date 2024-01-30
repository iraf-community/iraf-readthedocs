.. _maskstat:

maskstat: Compute mask statistics using iterative rejection
===========================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  maskstat inlist masks goodvalue
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of images for which the statistics are to be computed. 
  </dd>
  </dl>
  <dl id="l_masks">
  <dt><b>masks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masks' Line='masks' -->
  <dd>The good data masks associated with inlist. Good data masks are assumed
  to consist entirely of 1's and 0's and to be the same size as the images
  in inlist. The number of masks must be one or equal to the number of input
  images.
  </dd>
  </dl>
  <dl id="l_goodvalue">
  <dt><b>goodvalue</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='goodvalue' Line='goodvalue' -->
  <dd>The input mask good data value which must be 1 or 0.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the statistics. If statsec is
  defined the input image and input mask  names must not include an image
  section.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = INDEF' -->
  <dd>The initial lower bad data limit.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = INDEF' -->
  <dd>The initial upper bad data limit.
  </dd>
  </dl>
  <dl id="l_iterstat">
  <dt><b>iterstat = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iterstat' Line='iterstat = no' -->
  <dd>Use the iterstat task to compute the image statistics rather than imstatistics.
  </dd>
  </dl>
  <dl id="l_nsigrej">
  <dt><b>nsigrej = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigrej' Line='nsigrej = 3.0' -->
  <dd>The k-sigma bad data rejection criterion.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 20' -->
  <dd>The maximum number of bad data rejection cycles.
  </dd>
  </dl>
  <dl id="l_show">
  <dt><b>show = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='show' Line='show = yes' -->
  <dd>Print the results for the final iteration ?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the results for each iteration ?
  </dd>
  </dl>
  <dl id="l_mean">
  <dt><b>mean</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mean' Line='mean' -->
  <dd>The returned image mean estimate.
  </dd>
  </dl>
  <dl id="l_msigma">
  <dt><b>msigma</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='msigma' Line='msigma' -->
  <dd>The returned image standard deviation estimate.
  </dd>
  </dl>
  <dl id="l_median">
  <dt><b>median</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='median' Line='median' -->
  <dd>The returned image median estimate.
  </dd>
  </dl>
  <dl id="l_mode">
  <dt><b>mode</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mode' Line='mode' -->
  <dd>The returned image mode estimate.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The mean, standard deviation, median, and mode are estimated for each masked
  input image in <i>inlist</i> and stored in the output parameters <i>mean</i>,
  <i>msigma</i>, <i>median</i>, and <i>mode</i>. <i>Masks</i> defines either a single
  mask to be applied to every input image or an individual mask for every input
  image. If <i>iterstat</i> = yes then the image statistics are computed using
  iterative rejection, otherwise no iterative rejection is performed. Results
  for each iteration are printed on the terminal if <i>verbose</i> = yes, and
  for the final result only if <i>show</i> = yes.
  </p>
  <p>
  If <i>statsec</i> is defined then the statistics are computed inside an
  image section. In that case the input image and mask names must not include an
  image section.  Initial values for the image statistics are computed after
  applying the mask and rejecting data outside the limits defined by the
  <i>lower</i> and <i>upper</i> parameters.  New bad data limits are computed using
  the mean and sigma computed by the previous iteration and value of the
  <i>nsigrej</i> parameter. MASKSTAT terminates if the number of iterations &gt;=
  <i>maxiter</i> or if no new bad pixels are detected.
  </p>
  <p>
  MASKSTAT is a script task which calls ITERSTAT if <i>iterstat</i> = yes or
  IMSTATISTICS if <i>iterstat</i> = no. More information about the ITERSTAT and
  IMSTATISTICS algorithms can be found in the help pages for the ITERSTAT
  and IMSTATISTICS tasks.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the statistics for an image through a mask where the good pixels
  are defined by mask values of 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; maskstat demo01 demo.pl 1
  </pre></div>
  <p>
  2. Repeat the previous example but do the rejection iteratively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; maskstat demo01 demo.pl 1 iterstat+
  </pre></div>
  <p>
  3. Repeat the previous example but operate on a list of images and print
  only the final result.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; maskstat @demo.list demo.pl 1 iterstat+ verbose-
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
  imstatistics, iterstat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
