.. _quadjoin:

quadjoin: Rejoin single amplifier images produced by quadsplit
==============================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  quadjoin input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Root name of images to be joined.  Extensions based on the AMPLIST
  keyword are applied to the root name.  This task does not
  allow a list of input root names.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Output image name.  If one is not given then the input root name is used.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = no' -->
  <dd>Delete subimages on completion?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Images in split <span style="font-family: monospace;">"quadformat"</span> (see help topic <b>quadformat</b> and
  <b>quadsplit</b>) are rejoined into <span style="font-family: monospace;">"quadformat"</span>.  The input images
  have a common root name and then an extension given by the amplifier
  labels in the AMPLIST keyword are added.  The output name may be specified
  or the input root name may be used.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To join a split set of images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; dir quad0072*
  quad0072.11.imh     quad0072.21.imh
  quad0072.12.imh     quad0072.22.imh
  qu&gt; quadjoin quad0072 delete+
  qu&gt; dir quad0072*
  quad0072.imh
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  quadformat, quadsplit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
