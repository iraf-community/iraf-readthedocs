imgtools: Tools for manipulating & examining images and bad pixel lists.
========================================================================

.. toctree:: :maxdepth: 1

   addmasks
   imcalc
   iminsert
   improject
   rd2xy
   xy2rd
   xyztable
   xyztoim
.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  There are several tasks within this package for examining, editing, 
  reformatting, and operating on masks and images, and GEIS format 
  images in particular.  Type <span style="font-family: monospace;">"help geis"</span> for more information about 
  the data structure for HST data. The `mstools' subpackage contains
  tasks that handle the IMSETs found in STIS and NICMOS data files.
  </p>
  <p>
  The `imgtools' package is 
  implicitly loaded when the `stsdas' package is loaded.  Placing 
  these tasks in a separate package merely serves (in this case) to 
  emphasize the logical relationship between them, and to make the 
  package menu small and informative.  A quick summary is given in 
  Table 1 below, followed by a few highlights.  Utilities for 
  comparing, examining, and editing image headers can be found in the 
  `toolbox.headers' package.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  
                Table 1.  Image Utility Tasks
  +--------------------------------------------------------------+
  | Task        | Description                                    |
  +--------------------------------------------------------------+
  | addmasks    | Combine several masks or bad pixel lists       |
  | imcalc      | Perform general image arithmetic               |
  | iminsert    | Insert one image into another                  |
  | improject   | Project image along one axis                   |
  | rd2xy       | Translate RA/Dec to pixel coordinates          |
  | xy2rd       | Translate pixel coordinates to RA &amp; Dec        |
  +--------------------------------------------------------------+
  </pre></div>
  </section>
  <section id="s_image_and_mask_arithmetic">
  <h3>Image and mask arithmetic</h3>
  <p>
  The `imcalc' task is useful for performing arithmetic and logical 
  operations involving multiple images and masks, but producing only 
  one output image.  This task is complimentary to the IRAF 
  `images.imarith' task, which only performs arithmetic on pairs of 
  images, but can operate successively on multiple of pairs.  The 
  `imcalc' task has a much larger set of available arithmetic, 
  logical, and trigonometric operations from which to choose, and it 
  will perform the specified operation(s) on all groups of multi-group 
  images.  
  </p>
  <p>
  While the `imcalc' task works perfectly well for image masks, the 
  `addmasks' task provides additional flexibility for image masks.  
  In addition, `addmasks' can operate on masks stored in 
  binary TABLES.  Masks are used to encode some sort of information 
  about the corresponding image values, but there are many ways to 
  code that information.  `addmasks' can combine masks using logical 
  <span style="font-family: monospace;">"or"</span> or <span style="font-family: monospace;">"and"</span> if the values are bit-encoded, or using a 
  user-specified precedence or simple addition if they are not.  
  </p>
  </section>
  <section id="s_image_editing_and_browsing">
  <h3>Image editing and browsing</h3>
  <p>
  There are four tasks in `imgtools' for editing the contents of an 
  image.  The `pixedit' screen editor is the most general utility, in 
  that it allows the user to change individual pixel values, but it 
  is somewhat cumbersome for some purposes.  The `imfill' task allows 
  entire regions of an image to be replaced with a particular value, 
  and the `iminsert' task can add, multiply, or replace part of an 
  image with another image section.  The `boxinterp' task can 
  interpolate over regions from the surrounding area.  
  </p>
  <p>
  Simple listings of pixel values can be done with `listarea' or 
  `pixlocate'.  `listarea' differs from `images.listpix' in that the 
  printed values are formatted as a 2-D array, as modified by the 
  screen (or page) width.  
  </p>
  </section>
  <section id="s_image_reformatting">
  <h3>Image reformatting</h3>
  <p>
  There are two related tasks for altering the image structure.  The 
  `stack' task will stack multiple images, creating one of higher 
  dimension, while `improject' projects an image along one axis, 
  creating an output image with one less dimension.  Another task, 
  `moveheader', can create a new image from the header of one input 
  image, and the pixels from one or more others.  
  </p>
  </section>
  <section id="s_group_format_images">
  <h3>Group format images</h3>
  <p>
  If you use non-ST4GEM tasks in the IRAF environment for your 
  analysis, be aware that operations must be performed explicitly on 
  each group in multi-group GEIS files; the default is usually to 
  operate on only the first group.  (To learn the syntax for 
  operating on individual image groups, type <span style="font-family: monospace;">"help geis"</span>.)  On the 
  other hand, many ST4GEM tasks either perform the specified 
  operation on all groups, or make some explicit provision (usually 
  in the task parameters) to define the group(s) on which they 
  operate.  
  </p>
  <p>
  A few tasks are specifically designed to make common operations on 
  multi-group data much less tedious.  These tasks are patterned 
  after IRAF tasks but incorporate a <span style="font-family: monospace;">"groups"</span> parameter, which is a 
  range list for specifying the groups upon which to operate.  A few 
  of them also incorporate a <span style="font-family: monospace;">"g_accum"</span> parameter in those cases where 
  it makes sense to accumulate a result over all groups within a 
  file.  Two tasks are available at present: `gcopy', and 
  `gstatistics'.  Others, including `gcombine', and 
  `ghistogram', are planned for the near future.  
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  hst_calib.ctools, convfile, headers, tools.  
  </p>
  <p>
  Type <span style="font-family: monospace;">"help geis"</span> for more information about GEIS format files.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'INTRODUCTION' 'IMAGE AND MASK ARITHMETIC' 'IMAGE EDITING AND BROWSING' 'IMAGE REFORMATTING' 'GROUP FORMAT IMAGES' 'SEE ALSO'  -->
  
