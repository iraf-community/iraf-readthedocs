.. _darksub:

darksub: Scale and subtract a dark count image
==============================================

**Package: generic**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  darksub input output darkimage
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images from which to subtract the dark count image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output dark count subtracted images.  The output images may
  be the same as the input images.  The input and output image lists should
  contain the same number of images.
  </dd>
  </dl>
  <dl id="l_darkimage">
  <dt><b>darkimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='darkimage' Line='darkimage' -->
  <dd>Dark count image to be scaled and subtracted from the input images.
  </dd>
  </dl>
  <dl id="l_exposure">
  <dt><b>exposure = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exposure' Line='exposure = ""' -->
  <dd>Header parameter name from which to obtain the exposure times.
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = "1"' -->
  <dd>The pixel datatype of the dark subtracted images.  The default (<span style="font-family: monospace;">"1"</span>)
  is the pixel datatype of the original image.  The other choices are
  <span style="font-family: monospace;">"short"</span>, <span style="font-family: monospace;">"integer"</span>, <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"real"</span>, and <span style="font-family: monospace;">"double"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print log of operations performed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The dark count image is scaled by the ratio of the input image exposure to the
  dark count image exposure and subtracted from each of the input images.
  The exposures are obtained from the image headers under the specified
  name.  The output images may have the same names as the input images.
  A temporary image is used for the scaled dark count image and the original
  image is not modified.  The pixel datatype of the output images is
  specified by the parameter <i>pixtype</i>.  The default (<span style="font-family: monospace;">"1"</span>) uses the
  datatype of the input image.  A log of the operations performed may be
  printed on the standard output when the verbose options is specified.
  </p>
  <p>
  Note that this task can be used to subtract any type of image from a set
  of images in which the subtracted image must be scaled to a given exposure.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To subtract the dark count image 'dark' from obs1, obs2, and obs3:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; darksub obs1,obs2 obs1,obs2 dark exp="exposure"
  Tue 18:50:56 08-Apr-86
    obs1 = obs1 - 5.0049997336067 * dark
  Tue 18:51:05 08-Apr-86
    obs2 = obs2 - 5.009999733075 * dark
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imarith
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
