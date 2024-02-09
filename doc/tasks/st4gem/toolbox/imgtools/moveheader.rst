.. _moveheader:

moveheader: Combine the header and pixels from two images,
==========================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  moveheader hdrimage piximage outimage
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task takes the header from one image and the pixels from one or
  more other images and places them in a new image.  The group
  parameters from the first image are also copied to the third image
  since logically, if not physically, they are part of the header.  If
  the second image contains header parameters with the same name as
  those in the first image, the values of the second image will be
  retained in the third image.  The same applies to group parameters.
  If an image name does not contain agroup specification, then all
  groups within the image will be copied.  Otherwise, only the specified
  group will be copied.  If the pixels are copied from more than one
  images, the groups of each of the images are concatenated. The number
  of groups copied from the header image must either be one or equal to
  the number of groups in the pixel image.  In the first case, the group
  parameters from the one group in the header image are copied into each
  group in the output image.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_hdrimage">
  <dt><b>hdrimage [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hdrimage' Line='hdrimage [file name]' -->
  <dd>The name of the image whose header is to be copied to the new file.
  </dd>
  </dl>
  <dl id="l_piximage">
  <dt><b>piximage [file template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='piximage' Line='piximage [file template]' -->
  <dd>The name of the image or images containing the pixels that will be copied 
  to the new file.
  </dd>
  </dl>
  <dl id="l_outimage">
  <dt><b>outimage [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outimage' Line='outimage [file name]' -->
  <dd>The name of the output image created from 'hrdimage' and 'piximage'.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Copy the header from a file called 'y00v7701r.d0h' and the pixels 
  from one called 'yblack.hhh' creating a new image 'yblack.d0h'. The 
  images 'y00v7701r.d0h' and 'yblack.hhh' must have the same number of 
  groups:
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; moveheader y00v7701r.d0h yblack.hhh yblack.d0h
  </pre></div>
  <p>
  2. Do the same thing as in the previous example, but this time, copy 
  only the third group:
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; moveheader y00v7701r.d0h[3] yblack.hhh[3] yblack.d0h
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  eheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
