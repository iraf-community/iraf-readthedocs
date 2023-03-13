.. _imaccess:

imaccess: Test if an image exists
=================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bool = imaccess (image)
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The name of the image whose existence is to be tested.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Imaccess</i> is a boolean intrinsic function returning true (<span style="font-family: monospace;">"yes"</span>) if the
  named image exists.  The function will return false (<span style="font-family: monospace;">"no"</span>) if the image doesn't
  exist, or if no image extension is supplied and the image name is ambiguous.
  <i>Imaccess</i> can only be called as a function in an expression, not as a task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the header of an image if it exists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (imaccess ("dev$wpix"))
      imheader ("dev$wpix",long+)
  else
      error (11, "Image not found")
  </pre></div>
  <p>
  2. Tell if a image exists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; = imaccess ("dev$pix")
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  An optional second argument should be added to test whether the named file
  can be accessed for reading or writing.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  
