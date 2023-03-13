.. _wcscopy:

wcscopy: Copy the wcs from one image to another
===============================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wcscopy images refimages
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The list of input images which will inherit the wcs of the reference image.
  If the image does not exists a dataless image header is created.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The list of reference images containing the reference wcs. The number of
  reference images must be one or equal to the number of input images.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  WCSCOPY copies the world coordinate system information in the header of the
  reference image <i>reference</i> to the headers of the input images
  <i>images</i>, replacing any existing world coordinate system information
  in the input image headers in the process. WCSCOPY assumes that the
  world coordinate system information in the header of the reference 
  image is accurate and that all the input images have write permission.
  If the input image does not exist a data-less image header is created.
  The WCS is treated as an independent object and
  there is no check made on the dimensionality and sizes of the images.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Information  on  IRAF  world  coordinate  systems including
  more detailed descriptions of the <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>
  coordinate systems can be
  found  in  the  help  pages  for  the  WCSEDIT  and  WCRESET  tasks. 
  Detailed   documentation   for  the  IRAF  world  coordinate  system 
  interface MWCS can be found in  the  file  <span style="font-family: monospace;">"iraf$sys/mwcs/MWCS.hlp"</span>.
  This  file  can  be  formatted  and  printed  with the command <span style="font-family: monospace;">"help
  iraf$sys/mwcs/MWCS.hlp fi+ | lprint"</span>.  Information on the spectral
  coordinates systems and their suitability for use with WCSXYMATCH
  can be obtained by typing <span style="font-family: monospace;">"help specwcs | lprint"</span>.
  Details of  the  FITS  header
  world  coordinate  system  interface  can  be  found in the document
  <span style="font-family: monospace;">"World Coordinate Systems Representations Within  the  FITS  Format"</span>
  by Hanisch and Wells, available from our anonymous ftp archive.
      
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Make sure that the world coordinates systems of a list of input images
  that have been registered to a reference image with the xregister task
  are identical to the world coordinate system of the reference image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xregister @inlist refimage [200:400,200:400] shifts \
      output=@outlist xwindow=21 ywindow=21
  cl&gt; wcscopy @outlist refimage
  </pre></div>
  <p>
  2.  Create a data-less WCS image by specifying a new image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcscopy new dev$wpix
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
  tprecess,imalign,xregister,geomap,register,geotran,wcsmap,wregister,wcsedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
