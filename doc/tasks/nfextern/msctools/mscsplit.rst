.. _mscsplit:

mscsplit: Split MEF files into separate images
==============================================

**Package: msctools**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  This task splits MEF files into separate images.  The output images have
  names of the form rootname_N where rootname is a user specified output
  rootname and N is the extension number.  The primary images or global
  headers are also created.  The output of this task can be used with MSCJOIN
  to recreate an MEF file with the same structure and extension names.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mscsplit input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input MEF files to be split.  If the list includes image type
  extensions then the extension must be specified in the <i>mefext</i> parameter.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output root names.  If no output rootname is given then the input
  name is used as the rootname.  The output split images will have the
  specified rootname with suffix <span style="font-family: monospace;">"_N"</span> where N is the extension number.
  </dd>
  </dl>
  <dl id="l_mefext">
  <dt><b>mefext = <span style="font-family: monospace;">".fits"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mefext' Line='mefext = ".fits"' -->
  <dd>MEF filename extension.  This is used to identify the part of the input
  name to strip off to form the rootname for the output if no rootname is
  specified.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = no' -->
  <dd>Delete MEF files after splitting?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print processing information?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MSCSPLIT takes multiextension format (MEF) files and separates them into
  separate images.  The output is designed to be used with MSCJOIN to
  recreate an MEF file with the same structure and extension names.  Typically
  this task is used to allow operating on the extension images separately
  after which the MEF file is recreated.
  </p>
  <p>
  A list of input MEF files is given and each file is separated into images
  with names of the form rootname_N where rootname is a user specified output
  rootname and N is the extension number.  The primary image, extension
  number 0, is also created.  The output rootname list may be left blank in
  which case the input MEF file name is used as the rootname.
  </p>
  <p>
  If the input MEF file is not found or the output files exist then a warning
  is printed and the task proceeds to the next input file.
  </p>
  <p>
  The <i>delete</i> parameter may be used to delete the input MEF file
  after splitting.  This is useful in conjunction with MSCJOIN to later
  recreate the MEF file.
  </p>
  <p>
  The output separate images may be displayed with MSCDISPLAY if the
  parameter \Imimpars.exttmplt is of the form <span style="font-family: monospace;">"_![1-9]*.*"</span> and
  the rootname does not match an MEF file.  Other display oriented tasks
  such as MSCZERO and MSCEXAM will also work with this format.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Split an MEF file and delete it after splitting.  Then do some
  operations that modify the images.  Display the separate images
  with MSCDISPLAY.  Finally recreate the MEF file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscsplit obj012 del+ verb+
  obj012[0] -&gt; obj012_0
  obj012[im1] -&gt; obj012_1
  obj012[im2] -&gt; obj012_2
  obj012[im3] -&gt; obj012_3
  obj012[im4] -&gt; obj012_4
  obj012[im5] -&gt; obj012_5
  obj012[im6] -&gt; obj012_6
  obj012[im7] -&gt; obj012_7
  obj012[im8] -&gt; obj012_8
  cl&gt; imedit obj012_3 ""
  cl&gt; mscdisplay obj012 1 exttmplt="![1-9]*.*"
  file template: obj012_![1-9]*.*
  cl&gt; mscjoin obj012 del+ verb+
  obj012_0 -&gt; obj012
  obj012_1.fits -&gt; obj012[append,inherit]
  obj012_2.fits -&gt; obj012[append,inherit]
  obj012_3.fits -&gt; obj012[append,inherit]
  obj012_4.fits -&gt; obj012[append,inherit]
  obj012_5.fits -&gt; obj012[append,inherit]
  obj012_6.fits -&gt; obj012[append,inherit]
  obj012_7.fits -&gt; obj012[append,inherit]
  obj012_8.fits -&gt; obj012[append,inherit]
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCSPLIT">
  <dt><b>MSCSPLIT - V3.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCSPLIT' Line='MSCSPLIT - V3.2' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mscjoin, fitsutil
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
