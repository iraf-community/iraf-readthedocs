.. _maskfix:

maskfix: Fix bad pixel in images using a bad pixel mask
=======================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  maskfix inlist bpmasks bpvalue
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input images in which the bad pixels are to be fixed.
  </dd>
  </dl>
  <dl id="l_bpmasks">
  <dt><b>bpmasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmasks' Line='bpmasks' -->
  <dd>The list of bad pixel masks corresponding to inlist. Bad pixel masks are
  assumed to be the same size as the input images and to consist entirely
  of 0's and 1's with bad pixel values equal to badval. The number of bad pixel
  masks must be 1 or equal to the number of input images.
  </dd>
  </dl>
  <dl id="l_badval">
  <dt><b>badval</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badval' Line='badval' -->
  <dd>The input mask bad pixel value which must be 0 or 1.
  </dd>
  </dl>
  <dl id="l_forcefix">
  <dt><b>forcefix = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcefix' Line='forcefix = no' -->
  <dd>If forcefix = yes then all bad pixels in inlist are replaced. If forcefix = no
  and the input images contain the keyword <span style="font-family: monospace;">"MASKFIX"</span> then maskfix assumes that
  the bad pixels have already been fixed and no further pixel editing is done.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MASKFIX replaces bad pixels in <i>inlist</i> by linearly interpolating across
  bad columns within each image line. The bad pixels are assumed to be those
  pixels in the bad pixel masks <i>bpmasks</i> which have a value of <i>badval</i>.
  </p>
  <p>
  MASKFIX writes the keyword <span style="font-family: monospace;">"MASKFIX"</span> to the input image header when it
  completes replacing the bad pixels. If <i>forcefix</i> = no and the keyword
  <span style="font-family: monospace;">"MASKFIX"</span> already exists in the input image header then no further image
  editing is done. If <i>forcefix</i> = yes bad pixel replacement is performed
  regardless of the presence or absence of <span style="font-family: monospace;">"MASKFIX"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Replace bad pixels in an image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; maskfix demo01.sub.imh demo.pl 0
  </pre></div>
  <p>
  1. Replace bad pixels in a list of images using a single bad pixel mask.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; maskfix @sslist demo.pl 0
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
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
