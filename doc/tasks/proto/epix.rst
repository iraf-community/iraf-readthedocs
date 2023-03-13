.. _epix:

epix: Edit pixels in an image
=============================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  epix image_name x y new_value
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image_name">
  <dt><b>image_name</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image_name' Line='image_name' -->
  <dd>Name of image or image section to be edited.
  </dd>
  </dl>
  <dl id="l_xcoord">
  <dt><b>xcoord, ycoord</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcoord' Line='xcoord, ycoord' -->
  <dd>The coordinates of the pixel to be edited.
  </dd>
  </dl>
  <dl id="l_new_value">
  <dt><b>new_value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_value' Line='new_value' -->
  <dd>The new value of the pixel.
  </dd>
  </dl>
  <dl id="l_boxsize">
  <dt><b>boxsize = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boxsize' Line='boxsize = 3' -->
  <dd>The width of a square subraster surrounding the pixel to be edited over which
  the rejection mean and the median will be computed.
  </dd>
  </dl>
  <dl id="l_ksigma">
  <dt><b>ksigma = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ksigma' Line='ksigma = 0.0' -->
  <dd>The pixel rejection threshold for the iterative rejection algorithm used
  to compute the mean.  If zero, a rejection threshold will be computed based
  on the size of the sample using Chauvenet's relation.
  </dd>
  </dl>
  <dl id="l_edit_image">
  <dt><b>edit_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit_image' Line='edit_image = yes' -->
  <dd>Set the pixel value to <i>new_value</i>?  If editing is disabled the mean
  and median may still be computed, and the subraster may still be printed.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the values of the pixels in the subraster surrounding the image,
  and compute the rejection mean and the median.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A subraster <i>boxsize</i> pixels square is extracted centered on the pixel
  (xcoord,ycoord).  If the <i>verbose</i> flag is enabled the values
  of the pixels in the subraster are printed on the standard output along with
  the rejection mean and median of the subraster.  If <i>edit_image</i> is yes
  the program will ask for the <i>new_value</i> and edit the image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Replace the specified pixels with a value of zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epix M92 400 87 0.0
  cl&gt; epix M92 45 300 0.0
  cl&gt; epix M92 207 300 0.0
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
