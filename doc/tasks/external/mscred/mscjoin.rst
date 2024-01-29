.. _mscjoin:

mscjoin: Join separate images into MEF files
============================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  This task joins separate images into MEF files.  The input images must have
  names of the form rootname_N where rootname is a user specified input name
  and N an extension number.  A primary image or global header, extension
  number 0, is required.  The images to be joined into extensions must
  include the keyword <span style="font-family: monospace;">"extname"</span> containing the extension names to be
  created.  MSCSPLIT produces this format.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mscjoin input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input image rootnames to be joined.  Each rootname will be matched
  against images having the form rootname_N where N is the extension number.
  The numbers must be sequential beginning with 0 for the primary image
  or global header.  The images (other than the primary image) must also
  contain the keyword <span style="font-family: monospace;">"extname"</span> giving the extension name to be created
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output MEF names.  If no output name is given then the input
  rootname is used.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = no' -->
  <dd>Delete input images after joining?
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
  MSCJOIN takes input images with names of the form rootname_N where rootname
  is a user specified input name and N is the extension number.  The
  extension numbers must be sequential beginning with 0 for the primary image
  or global header.  The output MEF file is created with the extensions in
  the order given by the extension numbers.  The input images must include
  the keyword <span style="font-family: monospace;">"extname"</span> with the desired extension name.  Typically this task
  is used with MSCSPLIT, which creates the required format, to recreate MEF
  files that were split in order to perform some processing on the image
  extensions.
  </p>
  <p>
  The output list of MEF names may be left blank.  In that case the input
  rootname is used as the name of the output MEF file.  If the input images
  are not found or the output MEF files exist then a warning is printed and
  the task proceeds to the next input rootname.  The <i>delete</i> parameter
  may be used to delete the input images after joining.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Split an MEF file and delete it after splitting.  Then do some
  operations that modify the images.  Finally recreate the MEF file.
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
  <dl id="l_MSCJOIN">
  <dt><b>MSCJOIN - V3.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCJOIN' Line='MSCJOIN - V3.2' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mscsplit, fitsutil
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
