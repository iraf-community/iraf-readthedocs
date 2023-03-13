.. _im3dtran:

im3dtran: 3d image transpose (used for rotates as well)
=======================================================

**Package: vol**

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
  <dd>Input 3d image (datacube).
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Transposed datacube.
  </dd>
  </dl>
  <dl id="l_len_blk">
  <dt><b>len_blk = 128</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='len_blk' Line='len_blk = 128' -->
  <dd>Size in pixels of linear internal subraster.  IM3DTRAN will try to transpose
  a subraster up to len_blk cubed at one time.  Runtime is much faster with
  larger <b>len_blk</b>, but the task may run out of memory.
  </dd>
  </dl>
  <dl id="l_new_x">
  <dt><b>new_x = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_x' Line='new_x = 3' -->
  <dd>New x axis = old axis (1=x, 2=y, 3=z).  Default (3) replaces new x with old z.
  </dd>
  </dl>
  <dl id="l_new_y">
  <dt><b>new_y = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_y' Line='new_y = 2' -->
  <dd>New y axis = old axis.  Default (2) is identity.
  </dd>
  </dl>
  <dl id="l_new_z">
  <dt><b>new_z = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_z' Line='new_z = 1' -->
  <dd>New z axis = old axis.  Default (1) replaces new z with old x.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IM3DTRAN is very similar to IMAGES.IMTRANSPOSE, except that it can accomplish
  3d image transposes.  In 3 dimensions, it is necessary to specify which old
  axes map to the new axes.  In all cases, IM3DTRAN maps old axis element 1 to
  new axis element 1, i.e. it does not flip axes, just transposes them.
  </p>
  <p>
  If one wants to use IM3DTRAN to rotate a datacube 90 degrees in any direction,
  it is necessary to use a combination of flip and transpose (just like in the
  2d case).  For example, let the original datacube be visualized with its
  origin at the lower left front when seen by the viewer, with the abscissa
  being the x axis (dim1), ordinate the y axis (dim2), and depth being the
  z axis (dim3), z increasing away from the viewer or into the datacube [this
  is a left-handed coordinate system].  One then wants to rotate the datacube
  by 90 degrees clockwise about the y axis when viewed from +y (the <span style="font-family: monospace;">"top"</span>);
  this means the old z axis becomes the new x axis, and the old x axis becomes
  the new z axis, while new y remains old y.  In this case the axis that must
  be flipped prior to transposition is the <b>x axis</b>; see Example 1.
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
  <div class="highlight-default-notranslate"><pre>
  1.  For an input datacube with columns = x = abscissa, lines = y = ordinate,
      and bands = z = depth increasing away from viewer, and with the image
      origin at the lower left front, rotate datacube 90 degrees clockwise
      around the y axis when viewed from +y (top):
  
      cl&gt; im3dtran input[-*,*,*] output 3 2 1
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  [Not available yet]
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  [Not available yet]
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  pvol i2sun
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  
