headers: Tools for modifying image headers.
===========================================

.. toctree:: :maxdepth: 1

.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  There are several tasks in this package for examining and 
  editing image headers---particularly GEIS format image headers. 
  Type <span style="font-family: monospace;">"help geis"</span> for more information about the data structure for 
  HST data.  The `headers' package is implicitly loaded when 
  ST4GEM is loaded.  Placing these tasks in a separate 
  package merely serves (in this case) to emphasize the logical 
  relationship between them, and to make the package menu small and 
  informative.  A quick summary is given in Table 1 below, followed 
  by a few highlights.  Utilities for examining, editing, and 
  reformatting images can be found in the `toolbox.imgtools' package. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  
                Table 1.  Image Header Utility Tasks
  +--------------------------------------------------------------+
  | Task        | Description                                    |
  +--------------------------------------------------------------+
  | hdiff       | Display differences between two headers        |
  +--------------------------------------------------------------+
  </pre></div>
  </section>
  <section id="s_header_examination">
  <h3>Header examination</h3>
  <p>
  There are three tasks for examining the image header contents.  The 
  `iminfo' task prints the values of some generally useful keywords 
  that are found in most astronomical image headers, such as the 
  image size, the integration time, the RA &amp; Dec, UT and ST, etc.  
  For HST data this task will print various, instrument-specific 
  information, such as the filter(s)/grating(s) used, the instrument 
  operating mode, etc.  The two more general tasks are `hdiff', which 
  prints the names and values of keywords that differ between pairs 
  of images, and `hcheck' which will print the values of specified 
  keywords based upon a user-specified condition.  `hcheck' is quite 
  general and is very useful for finding keyword values that are, 
  e.g., out of range, or missing altogether.  
  </p>
  </section>
  <section id="s_group_format_images">
  <h3>Group format images</h3>
  <p>
  Users should be aware that modifications to GPB keywords must be 
  performed explicitly on each group in multi-group GEIS files; the 
  default is to operate on only the first image group.  To learn the 
  syntax for operating on individual image groups, type <span style="font-family: monospace;">"help geis"</span>. 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  toolbox.imgtools.  
  </p>
  <p>
  Type <span style="font-family: monospace;">"help geis"</span> for more information about GEIS format files.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'INTRODUCTION' 'HEADER EXAMINATION' 'GROUP FORMAT IMAGES' 'SEE ALSO'  -->
  
