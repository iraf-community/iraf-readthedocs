.. _xdshifts:

xdshifts: Compute shifts using image display and centroiding techniques
=======================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xdshifts inlist refim shiftlist cradius
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input images for which offsets are to be computed.
  </dd>
  </dl>
  <dl id="l_refim">
  <dt><b>refim</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refim' Line='refim' -->
  <dd>The reference image which defines the origin of the offsets. The reference
  images must be one of the images in the input image list. If refim is
  undefined the first input image is the reference image.
  </dd>
  </dl>
  <dl id="l_shiftlist">
  <dt><b>shiftlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shiftlist' Line='shiftlist' -->
  <dd>The output offsets file suitable for input to the xnregistar task. The output
  file contains the input image name, the x offset in pixels, the y offset in
  pixels, and the default exposure time which is always 1 in columns 1 through 4.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius' -->
  <dd>The centroiding radius in pixels.
  </dd>
  </dl>
  <dl id="l_datamin">
  <dt><b>datamin = INDEF, datamax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamin' Line='datamin = INDEF, datamax = INDEF' -->
  <dd>The lower and upper bad data limits used by the centroiding algorithm.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = INDEF' -->
  <dd>The mean background level for the centroiding algorithm.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 3' -->
  <dd>The maximum number of iterations performed by the centroiding algorithm.
  </dd>
  </dl>
  <dl id="l_maxshifts">
  <dt><b>maxshifts = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxshifts' Line='maxshifts = 5' -->
  <dd>The maximum difference in pixels between the final computed offset and
  the offset predicted by displaying the images and marking reference stars
  in each image.
  </dd>
  </dl>
  <dl id="l_chkshifts">
  <dt><b>chkshifts = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='chkshifts' Line='chkshifts = no' -->
  <dd>Edit the lists of input image reference stars, the list of registration
  stars, and the final offsets interactively?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XDSHIFTS computes the offsets required to mosaic the images in the input
  image list <i>inlist</i> to the reference image <i>refim</i> using the
  image display and the IMEXAMINE and IMCENTROID tasks and writes the results
  to the output file <i>shiftlist</i>.
  </p>
  <p>
  XDSHIFTS calls IMEXAMINE 3 times to perform the following functions:
  </p>
  <div class="highlight-default-notranslate"><pre>
  o display the images so that the user can select a reference star
    common to all the images
  
  o display the images so that the user can mark the position of the
    reference star in each image and create a reference star list
  
  o display the reference image so that the user can mark the positions
    of several registration stars that will be used to a registration star
    list
  </pre></div>
  <p>
  The IMEXAMINE <span style="font-family: monospace;">'p'</span> and <span style="font-family: monospace;">'n'</span> keystroke commands or the <span style="font-family: monospace;">":select &lt;image&gt;"</span> commands
  are used to select which image to display.  The IMEXAMINE <span style="font-family: monospace;">'a'</span> or <span style="font-family: monospace;">'r'</span> keystroke
  command are used to mark and centroid the stars using pixels within
  <i>cradius</i> of the current best position. The <span style="font-family: monospace;">'q'</span> keystroke terminates the
  current invocation of IMEXAMINE. More details on how IMEXAMINE computes the
  centroids and how to use the many features of IMEXAMINE can be found in the
  IMEXAMINE help page. If <i>chkshifts</i> is yes the user is given
  the opportunity to edit the reference star list and the registration star list.
  </p>
  <p>
  Given the input image list, the reference image, the reference star list, the
  registration star list, and the centroiding parameters <i>cradius</i>,
  <i>datamin</i>, <i>datamax</i>, <i>background</i>, <i>niterate</i>, and
  <i>maxshifts</i>, XDSHIFTS calls the IMCENTROID task to recenter the
  registration objects and compute the offsets of each input image relative to
  the reference image <i>refim</i>. Detailed descriptions of the IMCENTROID task
  algorithms can be found in the IMCENTROID help page. If <i>chkshifts</i> is yes
  then the user is given the opportunity to  edit the offsets file before
  it is finally output.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the offsets file for the 25 sky subtracted demo images. Go ahead
  and register the images with xnregistar. The output image will appear in
  demo.mosaic and the output exposure map will appear in exp_demo.mosaic.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type simlist
  demo01.sub.imh
  demo02.sub.imh
  demo03.sub.imh
  demo24.sub.imh
  demo25.sub.imh
  
  cl&gt; xdshifts @simlist "" offsets 5.0
  
  
  
  
  
  cl&gt; xnregistar offsets demo.pl "" "" mosaic mosaic.exp mosaic.corners
  
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
  imexamine,imcentroid
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
