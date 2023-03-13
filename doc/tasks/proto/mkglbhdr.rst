.. _mkglbhdr:

mkglbhdr: Make global header from keywords in images and reference
==================================================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkgblhdr input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output global dataless image.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference = ""' -->
  <dd>Optional reference image defining the allowed keywords, order, and
  blank cards.  If no reference image is specified the first image in
  the input list serves as the reference image.
  </dd>
  </dl>
  <dl id="l_exclude">
  <dt><b>exclude = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exclude' Line='exclude = ""' -->
  <dd>List of keywords to be excluded from the global header even if present
  in the reference header and with common values in all the input images.
  The case of the keywords in the list is ignored and the are matched to
  the headers in uppercase.  Typically the list would be specified as an
  @file; i.e. the contents of a file with keywords on separate lines.
  Note that one may use the output of a header listing without editing
  since only the first eight characters of each line are used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Mkgblhdr</b> makes a global (dataless) header with keywords common to a
  set of <i>input</i> images.  Common means present in all headers and
  with identical card records (value, formatting, and comments).  The
  purpose of this thask is to allow appending the images using the FITS
  <span style="font-family: monospace;">"inherit"</span> convention into a multi-extension file.
  </p>
  <p>
  The set of keywords which are allowed to appear in the global header are
  those in a reference image which are not in the <i>exclude</i> list and
  which have identical card records in all images.  The reference image is
  that specified by the <i>reference</i> parameter.  If the value of that
  parameter is a null string then the first image in the <i>input</i> list
  is used.  The <i>reference</i> image also determines the order of the cards
  including blank cards.
  </p>
  <p>
  The way the task works is that the header card records are read from
  the reference image.  Keywords in the excluded list are eliminated.
  Then reference card records which are not exactly matched in the input
  headers, independent of position, are eliminated.  Finally any leading
  blank cards are removed and consecutive blank cards are reduced to single
  blank lines.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  An initial multi-extension file with inherited global keywords is split
  into separate images.  The headers of the separate images are the union
  of the global and extension headers as is the convention for inheritance.
  After operating on the separate images it is desired to recreate a new
  MEF without having recourse to the original global header.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type images
  image1
  image2
  cl&gt; mkglbhdr @images newimage
  cl&gt; imcopy image1 newimage[im1,append,inherit]
  cl&gt; imcopy image2 newimage[im2,append,inherit]
  </pre></div>
  <p>
  To check the headers separately use the <span style="font-family: monospace;">"noinherit"</span> flag.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imhead newimage[0] l+
  cl&gt; imhead newimage[im1,noinherit] l+
  </pre></div>
  <p>
  Note that if the global header of the original MEF is available it is
  probably better to use that header instead of <b>mkglbhdr</b> as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcopy mefimage[0] newimage
  cl&gt; imcopy image1 newimage[im1,append,inherit]
  cl&gt; imcopy image2 newimage[im2,append,inherit]
  </pre></div>
  <p>
  It is important to understand how inheritance works when appending extensions.
  The IRAF FITS <span style="font-family: monospace;">"kernel"</span> eliminates keywords from the extension header when
  they have the same value as the global header.  If there are common
  keywords but with different values then they are both present and any
  task that read the union of the global and extension headers will see
  the value from the extension.
  </p>
  <p>
  2. The following example uses an exclusion list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type exclude.dat
  CTYPE1
  CTYPE2
  CRVAL1
  CRVAL2
  CRPIX1
  CRPIX2
  CD1_1
  CD1_2
  CD2_1
  CD2_2
  cl&gt; mkglbhdr @images newimage exclude="@exclude.dat"
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mscsplit, mscjoin
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
