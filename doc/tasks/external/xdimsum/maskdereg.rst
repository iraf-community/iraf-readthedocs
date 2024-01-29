.. _maskdereg:

maskdereg: Deregister master object mask to individual object masks
===================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  maskdereg omask sections outlist
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_omask">
  <dt><b>omask</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omask' Line='omask' -->
  <dd>The input object mask for the combined image. Omask is usually created by the
  mkmask task for the combined image created by the xnregistar task. The input
  object mask is assumed to consist entirely of 1's and 0's with object
  regions set to 1.
  </dd>
  </dl>
  <dl id="l_sections">
  <dt><b>sections</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sections' Line='sections' -->
  <dd>The input sections or corners file usually written by the xnregistar task.
  Sections contains the name of the original input images, the x and y
  coordinates of the lower left corner of the input image in the combined 
  image, and the x and y coordinates of the upper right corner of the input
  image in the combined image, in columns 1 through 5 respectively.
  </dd>
  </dl>
  <dl id="l_outlist">
  <dt><b>outlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outlist' Line='outlist' -->
  <dd>The list of output image masks or the string appended to the input image names
  in <i>sections</i> to create the output individual mask names. 
  </dd>
  </dl>
  <dl id="l_y2n_angle">
  <dt><b>y2n_angle = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y2n_angle' Line='y2n_angle = 0.0' -->
  <dd>The angle in degrees from the image y axis to the north axis measured from north
  through east. Y2n_angle is used to reorient the input object mask before
  creating the individual output object masks.
  </dd>
  </dl>
  <dl id="l_rotation">
  <dt><b>rotation = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rotation' Line='rotation = yes' -->
  <dd>Is the rotation of the input image north axis to the east axis counter-clockwise
   ?  Y2n_angle is used to reorient the input object mask before creating the
  individual output object masks.
  </dd>
  </dl>
  <dl id="l_mkcrmask">
  <dt><b>mkcrmask = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkcrmask' Line='mkcrmask = no' -->
  <dd>Create object masks for comparison with the cosmic ray masks or for
  use with the second pass sky subtraction task xslm ?
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Write the names of the output object masks to the headers of the input images.
  If mkcrmask is <span style="font-family: monospace;">"no"</span> the object mask name keyword is <span style="font-family: monospace;">"OBJMASK"</span>, if mkcrmask is
  <span style="font-family: monospace;">"yes"</span> it is <span style="font-family: monospace;">"CROBJMAS"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MASKDEREG creates individual object masks for the original input images
  using the object mask <i>omask</i> for the combined image  written by the
  MKMASK task and the sections file <i>sections</i> written by the XNREGISTAR
  task.
  </p>
  <p>
  The sections file contains the name of the original input image, the x and y
  coordinates of the lower left corner of the input image in the combined image,
  and the x and y coordinates of the upper right corner of the input image in
  the combined image, in columns 1 through 5.
  </p>
  <p>
  The output object masks are assigned names of the form input image name //
  outlist if outlist begins with a <span style="font-family: monospace;">"."</span>, e.g. <span style="font-family: monospace;">"demo01.msk.pl"</span> if outlist =
  <span style="font-family: monospace;">".msk"</span>, and the original image name is <span style="font-family: monospace;">"demo01.fits"</span>.
  All object masks are assumed to consist entirely of 0's and 1's with the
  object regions assigned values of 1.
  </p>
  <p>
  By default XNREGISTAR orients the combined image to within 45 degrees
  of north pointing up and east pointing left. Therefore the input object
  mask created by MKMASK will normally have this orientation is well. The
  parameters <i>y2n_angle</i> and <i>rotation</i> are used to reorient the
  input object mask so that the orientation of the individual output object
  masks matches the orientation of the original images.
  </p>
  <p>
  If <i>update</i> is <span style="font-family: monospace;">"yes"</span> then the name of output object mask is written
  into the header of the original input image.  If <i>mkcrmask</i> is <span style="font-family: monospace;">"no"</span>
  the object mask keyword is <span style="font-family: monospace;">"OBJMASK"</span>, otherwise it is <span style="font-family: monospace;">"CROBJMAS"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create individual object masks from a combined image mask.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; maskdereg mosaic.msk mosaic.corners ".obm" y2n_angle=0.0 \
      rotation+ mkcrmask- update+
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
  xnregistar,mkmask,orient
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
