.. _imdelete:

imdelete: Delete a list of images
=================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imdelete images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images to be deleted.
  </dd>
  </dl>
  <dl id="l_go_ahead">
  <dt><b>go_ahead </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='go_ahead' Line='go_ahead ' -->
  <dd>Delete the image?
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Verify the delete operation for each image.
  </dd>
  </dl>
  <dl id="l_default_action">
  <dt><b>default_action = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='default_action' Line='default_action = yes' -->
  <dd>The default action for the verify query.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMDELETE takes as input a list of IRAF images specified by <i>images</i> and
  deletes both the header and pixel files. In <i>verify</i> mode IMDELETE
  queries the user for the appropriate action to be taken for each IRAF image.
  </p>
  <p>
  If the <i>images</i> parameter is a URL, it will be accessed and put into 
  the file cache, then immediately deleted.  To simply remove a file from
  the cache, use the <i>fcache</i> command instead.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Delete a list of images
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imdelete fits*
  </pre></div>
  <p>
  2. Delete a list of images using verify
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imdel fits* ver+
  cl&gt; Delete file <i>'fits1'</i> ? (yes): yes
  cl&gt; Delete file <i>'fits2'</i> ? (yes): yes
  cl&gt; Delete file <i>'fits3'</i> ? (yes): yes
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
  imcopy, fcache
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
