.. _miterstat:

miterstat: Compute image statistics using a mask and iterative rejection
========================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  miterstat inlist
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
  <dl id="l_inmsklist">
  <dt><b>inmsklist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inmsklist' Line='inmsklist' -->
  <dd>The input mask list. Masks are assumed to consist of 0's and 1's with
  the 0's defining the good values. To invert the mask on input prefix
  the name by <span style="font-family: monospace;">'^'</span>.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the statistics. Statsec is ignored
  if the input image name includes a section specification.
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
  <dl id="l_imean">
  <dt><b>imean</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imean' Line='imean' -->
  <dd>The returned image mean estimate.
  </dd>
  </dl>
  <dl id="l_isigma">
  <dt><b>isigma</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='isigma' Line='isigma' -->
  <dd>The returned image standard deviation estimate.
  </dd>
  </dl>
  <dl id="l_imedian">
  <dt><b>imedian</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imedian' Line='imedian' -->
  <dd>The returned image median estimate.
  </dd>
  </dl>
  <dl id="l_imode">
  <dt><b>imode</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imode' Line='imode' -->
  <dd>The returned image mode estimate.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The mean, standard deviation, median, and mode are estimated for each input
  image in <i>inlist</i> using iterative rejection around the mean  and stored
  in the output parameters <i>imean</i>, <i>isigma</i>, <i>imedian</i>, and
  <i>imode</i>. Results for each iteration are printed on the terminal
  if <i>verbose</i> = yes, and for the final result only if <i>show</i> = yes.
  </p>
  <p>
  If <i>statsec</i> is defined and the input image name does not include an
  image section then the statistics are computed inside statsec. If the input
  image name does include an image section statsec is ignored. Initial values
  for the image statistics are computed after rejected data outside the limits
  defined by the <i>lower</i> and <i>upper</i> parameters.  New bad data
  limits are computed using the mean and sigma computed by the previous
  iteration and value of the <i>nsigrej</i> parameter. ITERSTAT terminates if the
  number of iterations &gt;= <i>maxiter</i> or if no new bad pixels are detected.
  </p>
  <p>
  ITERSTAT is a script task which makes repeated calls to IMSTATISTICS to compute
  the actual statistics. More information about the ITERSTAT algorithms can
  be found in the help page for the IMSTATISTICS task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the statistics for an image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; miterstat demo01 demo01.pl
  </pre></div>
  <p>
  2. Compute the statistics for the list of demo images but print only the
  final result.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; miterstat @demo.list @ demo.msklist verbose-
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
  mimstatistics
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
