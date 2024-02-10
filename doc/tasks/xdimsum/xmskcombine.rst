.. _xmskcombine:

xmskcombine: Combine bad pixel, cosmic ray, holes, and object masks
===================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xmkscombine inlist bpmask crmasks hmasks omasks rmasks
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The input sky subtracted image list. 
  </dd>
  </dl>
  <dl id="l_bpmask">
  <dt><b>bpmask </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmask' Line='bpmask ' -->
  <dd>The input bad pixel mask common to all the input sky subtracted images.
  The bad pixel mask is assumed to consist of 1's and 0's where 0 defines
  a bad pixel. If no bad pixel mask is defined a virtual bad pixel mask
  consisting entirely of 1's is assumed.
  </dd>
  </dl>
  <dl id="l_crmasks">
  <dt><b>crmasks </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmasks' Line='crmasks ' -->
  <dd>The list of input cosmic ray masks normally produced by the xzap or xnzap
  tasks. The cosmic ray mask is assumed to consist of 1's and 0's where 1
  defines a cosmic ray. Crmasks may define a list masks which has the same
  length as inlist, or an image keyword containing the name of the cosmic ray
  mask. The default keyword name  written by xzap and xnzap  is <span style="font-family: monospace;">"CRMASK"</span>.
  If no cosmic ray mask is defined a virtual cosmic ray mask consisting
  entirely of 0's is defined.
  </dd>
  </dl>
  <dl id="l_hmasks">
  <dt><b>hmasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hmasks' Line='hmasks' -->
  <dd>The list of input holes masks normally produced by the xslm task. The holes
  mask is assumed to consist of 1's and 0's where 0 defines a hole or undefined
  pixel in the input image sky subtracted image which contains no good data.
  Hmasks may define a list of masks which has the same length as inlist or an
  image keyword containing the name of the holes mask. The default keyword name
  written by xslm  is <span style="font-family: monospace;">"HOLES"</span>. If no holes mask is defined a virtual holes mask
  consisting entirely of 1's is defined.
  </dd>
  </dl>
  <dl id="l_omasks">
  <dt><b>omasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omasks' Line='omasks' -->
  <dd>The list of input object masks normally produced by the mkmask / maskdereg
  tasks. The objects mask is assumed to consist of 1's and 0's where 1 defines
  and object and 0 defines the sky. Omasks may define a list of masks which has
  the same length as inlist or an image keyword containing the name of the object
  mask. The default keyword name written by maskdereg is <span style="font-family: monospace;">"OBJMASK"</span>. If no objects
  mask is defined a virtual objects mask consisting entirely of 0's is defined.
  Object masks are only used if <i>nprev_omask</i> &gt; 0.
  </dd>
  </dl>
  <dl id="l_rmasks">
  <dt><b>rmasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmasks' Line='rmasks' -->
  <dd>The list of output rejection masks or the string appended to the input sky
  subtracted image name to create the output rejection mask name. New rejection
  masks are not created if only the bad pixel mask <i>bpmask</i> is defined.
  Rejection masks consist entirely of 0's and 1's with 0's defining the bad
  pixels and are suitable for input to the XNREGISTAR task. The name of the
  rejection mask is written to the REJMASK keyword in the input image.
  </dd>
  </dl>
  <dl id="l_nprev_omask">
  <dt><b>nprev_omask = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nprev_omask' Line='nprev_omask = 0' -->
  <dd>The number of previous object masks to combine to create an objects mask.
  By default no object masks are defined. If nprev_omask is 1 then the
  object mask of the previous image is used to mask the current image,
  if <i>nprev_omask</i> = 2 then the 2 previous object masks are used, etc.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XMSKCOMBINE combines the bad pixel mask <i>bpmask</i>, the cosmic ray
  masks <i>crmasks</i> (normally written by the XZAP or XNZAP tasks), the holes
  masks <i>hmasks</i> (normally written by the XSLM task), and the previous object
  masks <i>omasks</i> (normally written by the MKMASK and MASKDEREG tasks)
  into combined rejection masks <i>rmasks</i> corresponding
  to the sky subtracted images in <i>inlist</i>.
  </p>
  <p>
  The final combined mask  which is suitable for input to the XNREGISTAR
  tasks consists entirely of 0's and 1's where 0's define the bad pixels.
  </p>
  <p>
  Users may befine their own <i>crmasks</i>, <i>hmasks</i>, and <i>omasks</i> lists
  or set these parameters to the  appropriate input image header keyword,
  normally CRMASK, HMASK, and OBJMASK respectively.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Combine the first pass bad pixel mask. Note that in this no new masks
  are written because the rejection mask is equal to the bad pixel mask. The
  bad pixel mask name is written to the REJMASK keyword.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type simlist
  demo01.sub.im
  demo02.sub.imh
  demo03.sub.imh
  ...
  ...
  demo24.sub.imh
  demo25.sub.imh
  
  cl&gt; xmskcombine @simlist demo.pl "" "" "" ".rjm"
  </pre></div>
  <p>
  2. Combine the first pass bad pixel mask and the cosmic ray masks. The
  rejection mask name is written to the REJMASK keyword.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type simlist
  demo01.sub.im
  demo02.sub.imh
  demo03.sub.imh
  ...
  ...
  demo24.sub.imh
  demo25.sub.imh
  
  cl&gt; xmskcombine @simlist demo.pl CRMASK "" "" ".rjm"
  </pre></div>
  <p>
  3. Combine the bad pixel, cosmic ray, holes, and previous object masks. The
  rejection mask name is written to the REJMASK keyword.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type simlist
  demo01.sub.im
  demo02.sub.imh
  demo03.sub.imh
  ...
  ...
  demo24.sub.imh
  demo25.sub.imh
  
  cl&gt; xmskcombine @simlist demo.pl CRMASK HOLES OBJMASK ".rjm"
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
  xslm,xzap,xnzap,mkmask,mkdereg,xnregistar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
