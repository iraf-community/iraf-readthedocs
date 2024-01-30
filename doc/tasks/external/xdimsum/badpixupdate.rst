.. _badpixupdate:

badpixupdate: Update bad pixel mask to include bad pixels detected by xzap
==========================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  badpixupdate inlist nrepeats bpmask
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input bad pixel masks normally produced by the cosmic
  ray correction tasks xzap or xnzap. The masks in inlist are assumed to
  consist entirely of 1's and 0's with the candidate bad pixels set to 1.
  </dd>
  </dl>
  <dl id="l_nrepeats">
  <dt><b>nrepeats</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nrepeats' Line='nrepeats' -->
  <dd>If the same pixel is bad in nrepeats or more candidate bad pixel masks
  then it is set to 0 in bpmask.
  </dd>
  </dl>
  <dl id="l_bpmask">
  <dt><b>bpmask</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmask' Line='bpmask' -->
  <dd>The name of the bad pixel mask to be updated. Bpmask is assumed to consist
  entirely of 1's and 0's with bad pixels set to 0.0. Note that the pixels
  in bpmask are defined in the opposite sense to those in inlist.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  BADPIXUPDATE sums the candidate bad pixel masks in <i>inlist</i>, detects
  which pixels are bad <i>nrepeats</i> or more images, sets those pixels to
  be bad in <i>bpmask</i>. The input candidate bad pixel masks are normally
  the output of the cosmic ray detection tasks XZAP or XNZAP and are assumed
  to consist entirely of 1's and 0's with 1 defined to be bad. The output
  bad pixel mask is usually the bad pixel mask common to all the input images
  and is assumed to consist entirely of 1's and 0's with 0 defining a bad
  pixel.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Search a list of cosmic ray masks computed by xnzap, detect pixel
  with more than 3 <span style="font-family: monospace;">"cosmic ray"</span> hits and set those pixel to be bad
  in the bad pixel mask demo.pl.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type crmlist
  demo01.sub.crm.pl
  demo02.sub.crm.pl
  demo25.sub.crm.pl
  
  cl&gt; badpixupdate @crmlist 3 demo.pl
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
  xzap,xnzap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
