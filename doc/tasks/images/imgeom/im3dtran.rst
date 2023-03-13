.. _im3dtran:

im3dtran: Transpose a list of 3-D images
========================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  im3dtran input output 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input 3d image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output transposed 3D image. If the output image name is the same as
  the input image name then the original image will be overwritten. The number
  of output images must equal the number of input images.
  </dd>
  </dl>
  <dl id="l_new_x">
  <dt><b>new_x = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_x' Line='new_x = 3' -->
  <dd>The new x axis.  The default (3) replaces new x with old z.
  </dd>
  </dl>
  <dl id="l_new_y">
  <dt><b>new_y = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_y' Line='new_y = 2' -->
  <dd>The new y axis = old axis.  The default (2) does not change the y axis.
  </dd>
  </dl>
  <dl id="l_new_z">
  <dt><b>new_z = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_z' Line='new_z = 1' -->
  <dd>The new z axis.  The default (1) replaces new z with old x.
  </dd>
  </dl>
  <dl id="l_len_blk">
  <dt><b>len_blk = 128</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='len_blk' Line='len_blk = 128' -->
  <dd>The size in pixels of the linear internal subraster. Im3dtran will try to
  transpose a subraster up to len_blk cubed at one time.  Runtime is much
  faster with larger <b>len_blk</b>, but the task may run out of memory.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IM3DTRAN transposes the input images <i>input</i> in 3 dimensions and
  writes the transposed images to <i>output</i>. The 6 possible axis 
  mappings are specified by setting the parameters <i>new_x</i>, <i>new_y</i>,
  and <i>new_z</i>.
  </p>
  <p>
  IM3DTRAN can be used to rotate a datacube 90 degrees in any direction by
  combining the transpose operation with an axis  flip.  For
  example, Consider a datacube is visualized with its origin at the lower
  left front
  when seen by the viewer, with its abscissa being the x axis, its ordinate
  the y axis, and its depth the z axis, with z increasing away from the viewer
  or into the datacube [this
  is a left-handed coordinate system].  To rotate the datacube
  by 90 degrees clockwise about the y axis when viewed from the +y direction;
  the old z axis must become the new x axis, and the old x axis must become
  the new z axis, while the new y axis remains old y axis.  In this case the
  axis that must be flipped prior to transposition is the x axis as shown
  in example 2.
  </p>
  <p>
  The parameter <b>len_blk</b> controls how much memory is used during the
  transpose operation.  <b>len_blk</b> elements are used in each axis at a
  time, or a cube len_blk elements on a side.  If <b>len_blk</b> is too large,
  the task will abort with an <span style="font-family: monospace;">"out of memory"</span> error.  If it is too small,
  the task can take a very long time to run.  The maximum size of len_blk
  depends on how much memory is available at the time IM3DTRAN is run,
  and the size and datatype of the image to be transposed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Transpose axes 1 2 and 3 of a list of input images to axes 2 1 and 3 of
  a list of output images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; im3dtran image1,image2,image3 tr1,tr2,tr3 2 1 3
  </pre></div>
  <p>
  2.  For an input datacube with columns = x = abscissa, lines = y = ordinate,
  and bands = z = depth increasing away from viewer, and with the image
  origin at the lower left front, rotate datacube 90 degrees clockwise
  around the y axis when viewed from +y (top):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; im3dtran input[-*,*,*] output 3 2 1
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imtranspose, imjoin, imstack, imslice
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  
