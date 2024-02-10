.. _xlist:

xlist: Create image sublists used by xslm
=========================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xlist inlist outlist start finish exclude
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The input image list.
  </dd>
  </dl>
  <dl id="l_outlist">
  <dt><b>outlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outlist' Line='outlist' -->
  <dd>The output image list.
  </dd>
  </dl>
  <dl id="l_start">
  <dt><b>start</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start' Line='start' -->
  <dd>The sequence number of the first image in the input list to include in the
  output list.
  </dd>
  </dl>
  <dl id="l_finish">
  <dt><b>finish</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='finish' Line='finish' -->
  <dd>The sequence number of the first image in the input list to include in the
  output list.
  </dd>
  </dl>
  <dl id="l_exclude">
  <dt><b>exclude</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exclude' Line='exclude' -->
  <dd>The sequence number of the image  in the input image list that lies
  between start and finish to exclude from the output list.
  </dd>
  </dl>
  <dl id="l_suffix">
  <dt><b>suffix = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='suffix' Line='suffix = ""' -->
  <dd>The prefix to append to the selected input image names before they are written
  to the output list.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XLIST creates an output images list <i>outlist</i> consisting of images 
  <i>start</i> to <i>finish</i> in the input image list <i>inlist</i>.
  If <i>exclude</i> is between start and finish the input image with that
  sequence number will be excluded from the output image list. The string
  <i>suffix</i> will be appended to the input image names before they are
  written to the output image list.
  </p>
  <p>
  XLIST is a simple script task currently used by the XSLM and MASKDEREG
  tasks to create subsets image lists sky subtraction and object mask
  combination.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Assemble the list of 6 nearest images to be used to create a sky image for 
  image number 13 in the demo image sequence.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type inlist
  demo01
  demo02
  demo03
  demo24
  demo25
  
  cl&gt; xlist inlist outlist 10 16 13
  
  cl&gt; type outlist
  demo10
  demo11
  demo12
  demo14
  demo15
  demo16
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
  
