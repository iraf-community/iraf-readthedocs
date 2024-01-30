.. _fxconvert:

fxconvert: Convert between IRAF image types.
============================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  fxconvert input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Images to be copied.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output images or directory.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print each operation as it takes place?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Fxconvert is a take from the 'imcopy' task but with the capability to
  convert many 'imh' images for example to 'fits' images onto an output
  directory.
  Each of the input images, which may be given as a general image template
  including sections, is copied to the corresponding output image list,
  which may also be given as an image template, or the output directory.
  If the output is a list of images then the number of input images must be
  equal to the number of output images and the input and output images are paired
  in order.  If the output image name exists and contains a section then the
  input image (provided it is the same size as the section) will be copied
  into that section of the input image.  If the output image name does not
  have a section specification and if it is the same as the input image name
  then the input image is copied to a temporary file which replaces the input
  image when the copy is successfully concluded.  Note that these are the only
  cases where clobber checking is bypassed; that is, if an output image name
  is not equal to the input image name or a subsection of an existing image
  and the file already exists then a clobber error will occur if
  clobber checking is in effect.
  </p>
  <p>
  The verbose options prints for each copy lines of the form:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  input image -&gt; output image
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. For a simple copy of an image. Since we are not putting extension, 
  we need to which kind of image we want as output:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  cl&gt; reset imtype=fits
  cl&gt; flpr             # Necessary when changing imtype value
  cl&gt; fxconvert image imagecopy
  
  </pre></div>
  <p>
  2. To copy a portion of an image:
  </p>
  <p>
  	cl&gt; fxconvert image[10:20,*] subimage.fits
  </p>
  <p>
  3. To copy several images. The 'imtype' setting is necessary to dot it only
  once until another image type is desire as output. After the reset, a 
  'flprc' command is necessary for the change to take effect.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  cl&gt; reset imype=fits
  cl&gt; flprc
  cl&gt; fxconvert image1,image2,frame10 a,b,c
  
  </pre></div>
  <p>
  4. To trim an image:
  </p>
  <p>
  	cl&gt; fxconvert image[10:20,*] image
  </p>
  <p>
  In the above example the specified section of the input image replaces the
  original input image.  To trim several images using an image template:
  </p>
  <p>
  	cl&gt; fxconvert frame*[1:512,1:512] frame*
  </p>
  <p>
  In this example all images beginning with <span style="font-family: monospace;">"frame"</span> are trimmed to 512 x 512.
  </p>
  <p>
  5. To copy a set of images to a new directory. Notice that the output
  image type will be whatever the value of imtype is, and it will not
  necessarily be the input type.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fxconvert image* directory
                  or
  cl&gt; fxconvert image* directory$
                  or
  cl&gt; fxconvert image* osdirectory
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"osdirectory"</span> is an operating system directory name (i.e. /user/me
  in UNIX).
  </p>
  <p>
  6. To copy a section of an image in an already existing image of
  sufficient size to contain the input section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fxconvert image[1:512,1:512] outimage[257:768,257:768]
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The distinction between copying to a section of an existing image
  and overwriting a input image is rather inobvious.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO' 'BUGS'  -->
  
