.. _imgets:

imgets: Return the value of an image header parameter as a string
=================================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imgets image param
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Name of the image to be accessed.
  </dd>
  </dl>
  <dl id="l_param">
  <dt><b>param</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='param' Line='param' -->
  <dd>Name of the parameter whose value is to be returned.
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value = ""' -->
  <dd>The value of the parameter, returned as a string.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The value of the parameter <i>param</i> of the image <i>image</i> is returned
  as a string in the output parameter <i>value</i>.  The CL type coercion
  functions <i>int</i> and <i>real</i> may be used to decode the returned
  value as an integer or floating point value.  Both standard image header
  parameters and special application or instrument dependent parameters may be
  accessed.  If the parameter cannot be found a warning message is printed and
  the value <span style="font-family: monospace;">"0"</span> is returned.  Parameter names are case sensitive.
  </p>
  <p>
  The following standard image header parameters may be accessed with
  <b>imgets</b>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  i_pixtype                       pixel type (short, real, etc.)
  i_naxis                         number of dimensions
  i_naxis[1-7]                    length of the axes (x=1,y=2)
  i_minpixval                     minimum pixel value or INDEF
  i_maxpixval                     maximum pixel value or INDEF
  i_title                         image title string
  i_pixfile                       pixel storage file name
  </pre></div>
  <p>
  This task is most useful for image parameter access from within CL scripts.
  The task <b>imheader</b> is more useful for just looking at the image header
  parameters.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Fetch the instrument parameter <span style="font-family: monospace;">"HA"</span> (hour angle) from the image header of
  the image <span style="font-family: monospace;">"nite1.1001"</span>, and compute and print the hour angle in degrees:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imgets nite1.1001 HA
  cl&gt; = real(imgets.value) * 15.0
  42.79335
  </pre></div>
  <p>
  2. Print the number of pixels per line in the same image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imgets nite1.1001 i_naxis1
  cl&gt; = int(imgets.value)
  1024
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imheader, hedit, hselect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
