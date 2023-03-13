.. _imrename:

imrename: Rename one or more images
===================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imrename oldnames newnames
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_oldnames">
  <dt><b>oldnames</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oldnames' Line='oldnames' -->
  <dd>An image template specifying the names of the images to be renamed.
  </dd>
  </dl>
  <dl id="l_newnames">
  <dt><b>newnames</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newnames' Line='newnames' -->
  <dd>Either an image template specifying the new names for the images,
  or the name of the directory to which the images are to be renamed (moved).
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If verbose output is enabled a message will be printed on the standard output
  recording each rename operation.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <b>imrename</b> task renames one or more images.  The ordinary <i>rename</i>
  task cannot be used to rename images since an image may consist of more than
  one file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Rename the image <span style="font-family: monospace;">"pix"</span> to <span style="font-family: monospace;">"wfpc.1"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imrename pix wfpc.1
  </pre></div>
  <p>
  2. Rename all the <span style="font-family: monospace;">"nite1*"</span> images as <span style="font-family: monospace;">"nite1_c"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imrename nite1.*.imh nite1%%_c%.*.imh
  </pre></div>
  <p>
  3. Move the images in logical directory <span style="font-family: monospace;">"dd"</span> to the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imrename dd$*.imh .
  </pre></div>
  <p>
  4. Move the pixel files associated with the images in the current directory
  to a subdirectory <span style="font-family: monospace;">"pix"</span> of the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reset imdir = HDR$pix/
  cl&gt; imrename *.imh .
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy, imdelete, imheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
