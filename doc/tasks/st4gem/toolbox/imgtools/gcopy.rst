.. _gcopy:

gcopy: Generic multi-group copy utility.
========================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gcopy input output groups
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Gcopy is an extension to the 'imcopy' command allowing all the groups
  or a group list to be copied to the output file.
  </p>
  <p>
  Gcopy allows the specification of image section for the input file to be
  effective for all the groups in the group list. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>Images to be copied. 
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string] ' -->
  <dd>Output image or directory.
  If it is desired that the output file be created with more groups than
  specified from the input file, simply append [1/n] to the output filename
  where n is the number of groups in the output file
  If a group number is specified as part of the output filename, the copying
  will begin at that output group.
  If the remaining number of groups in the output file is less than the
  specified number of input groups, gcopy will copy as many as possible and
  print a warning message that not all groups were copied.
  </dd>
  </dl>
  <dl id="l_groups">
  <dt><b>groups = <span style="font-family: monospace;">"ALL"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groups' Line='groups = "ALL" [string]' -->
  <dd>Specify the list of groups from the input image to be copied to the output
  image; this list follows the syntax of the ranges utilities; i.e. things
  like 1,2,3; 1-9 or 9,7,13,1-4 are acceptable.
  The default (<span style="font-family: monospace;">"ALL"</span>) value means that all the groups from the input file will
  be copied.
  Note that the current implementation does not preserve the order of the
  specified groups.
  Groups are always copied in the order of increasing group number and 
  duplicate group numbers are eliminated.
  For example, specifying 3,2,1 will result in groups 1,2,3 being copied
  in that order. Likewise specifying the same group number more than
  once will not cause it to be copied more than once (i.e.,  1,1,1 results
  in group 1 copied only once. 
  </dd>
  </dl>
  <dl id="l_i2toi4">
  <dt><b>i2toi4 = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i2toi4' Line='i2toi4 = no' -->
  <dd>Specify if you want to convert group parameter values datatype from
  INTEGER*2 (not longer supported) to INTEGER*4.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print each operation as it takes place?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. For a fast copy of all the groups:
  </p>
  <p>
  	im&gt; gcopy image.hhh imagecopy.hhh
  </p>
  <p>
  2. To copy groups 1,3,5 of a 10 groups geis file. The output file
     will have a GCOUNT of 3.
  </p>
  <p>
  	im&gt; gcopy g10.hhh g3.hhh groups=<span style="font-family: monospace;">"1,3,5"</span>
  </p>
  <p>
  3. Copy several multigroup Geis files to an output directory using a
     section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  im&gt; gcopy g1.hhh[*,20:40],g2.c3h[120:256,30:56] \
        mydir/ gr="1,2,4"
  </pre></div>
  <p>
  4. Copy all groups to a new output file, but create the output file with
     more groups than in the input image (to be 
  </p>
  <p>
  	im&gt; gcopy image.hhh imagecopy.hhh[1/10] groups=<span style="font-family: monospace;">"1-4"</span>
  </p>
  <p>
  5. Copy group 3 of the input image to group 7 of the output image.
  </p>
  <p>
  	im&gt; gcopy image.hhh[3] imagecopy.hhh[7]
  </p>
  <p>
  6. Copy all groups of the input file to the output file starting at group
     5 of the output file.
  </p>
  <p>
  	im&gt; gcopy image.hhh imagecopy.hhh[5]
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was developed by Nelson Zarate following the 'imcopy' task and 
  extended to multigroup.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  IT will not copy 'imh' files. What's more, with the most recent fix
  to allow file level copies of one GEIS file to another
  with different file extensions, if one tries
  'gcopy test.c0h test2.imh' the task will run without complaint and
  produce test.imh and test.imd but these will be GEIS files and not
  'imh' files. This will be fixed in the future.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'BUGS' 'SEE ALSO'  -->
  
