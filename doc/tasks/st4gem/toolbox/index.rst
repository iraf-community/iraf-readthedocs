toolbox: General tools packages.
================================

.. toctree:: :maxdepth: 1

   headers/index
   imgtools/index
   tools/index
.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  There are seven packages within this package that contain general 
  utility tasks for examining, editing, reformatting, and operating 
  on images and tables.  All of these packages are implicitly loaded 
  when the `st4gem' package is loaded.  Placing 
  these tasks in separate packages merely serves (in this case) to 
  emphasize the logical relationship between them, and to make the 
  individual package menus manageable.  A quick summary is given in 
  Table 1 below; a more detailed summary can be found in the 
  following sections.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  
                Table 1.  General Tools Packages
  +-------------------------------------------------------------+
  | Package  | Description                                      |
  +-------------------------------------------------------------+
  | headers  | Tools for examining and editing image headers    |
  | imgtools | General image and mask manipulation tools        |
  | tools    | General utilities                                |
  +-------------------------------------------------------------+
  </pre></div>
  </section>
  <section id="s_headers">
  <h3>Headers</h3>
  <p>
  The `headers' package provides utilities for comparing, examining, 
  and editing image headers.  These tasks are particularly useful for 
  GEIS format images, where the image descriptors that are specific 
  to particular groups are stored in the binary portion of the data.  
  Type <span style="font-family: monospace;">"help geis"</span> for more information about this data structure.  
  </p>
  </section>
  <section id="s_imgtools">
  <h3>Imgtools</h3>
  <p>
  The `imgtools' tasks are useful for performing operations on images 
  and masks, such as calculations involving multiple images, editing 
  the contents of an image, or examining the image statistics.  There 
  are also utilities for stacking multiple images in to one of higher 
  dimension (and vice versa), retrieving world coordinates of pixels, 
  and pixel mask utilities. 
  </p>
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
  `gstatistics'.  Others, including `gcalc', `gcombine', and 
  `ghistogram', are planned for the near future.  
  </p>
  </section>
  <section id="s_tools">
  <h3>Tools</h3>
  <p>
  The `tools' package offers general utilities such diverse needs as 
  precessing coordinates, converting between time formats, creating 
  unique file names, and making an `apropos' database file.  
  </p>
  </section>
  <section id="s_other_general_utilities">
  <h3>Other general utilities</h3>
  <p>
  Most of the general plotting and analysis tools that users need to 
  display, analyze and interpret their HST data are available within 
  other packages, such as the `graphics', or `analysis' packages.  
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  headers, imgtools, tools
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'INTRODUCTION' 'HEADERS' 'IMGTOOLS' 'TOOLS' 'OTHER GENERAL UTILITIES' 'SEE ALSO'  -->
  
