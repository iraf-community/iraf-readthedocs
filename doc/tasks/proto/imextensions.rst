.. _imextensions:

imextensions: Make a list of image extensions
=============================================

**Package: proto**

.. raw:: html

  <section id="s_usage___">
  <h3>Usage   </h3>
  <div class="highlight-default-notranslate"><pre>
  imextensions input
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input files containing image extensions to be listed.  This list
  may not contain any image kernel but it can contain an image section.  The
  image filename extension, such as <span style="font-family: monospace;">".fits"</span>, is optional in the same way as
  with other IRAF image tasks.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"file"</span> (none|list|file)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "file" (none|list|file)' -->
  <dd>Output type for the list of image extensions.  The choices are:
  <div class="highlight-default-notranslate"><pre>
  none - no output
  list - a list as a single line
  file - a list of one image extension per line
  </pre></div>
  The <span style="font-family: monospace;">"none"</span> output is used to just set the number of image extensions in the
  <i>nimages</i> parameter.  The <span style="font-family: monospace;">"list"</span> output is used for a short list that
  can be scanned into a CL variable.  The <span style="font-family: monospace;">"file"</span> output is used for a long
  list and to be redirected to a file for use as an <span style="font-family: monospace;">"@file"</span>.  If <span style="font-family: monospace;">"list"</span>
  output is selected and the list length exceeds 255 characters (the
  size of a CL string) the task will abort with an error.
  </dd>
  </dl>
  <dl id="l_index">
  <dt><b>index = <span style="font-family: monospace;">"1-"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='index' Line='index = "1-"' -->
  <dd>Extension index range list.  The range list syntax is specified under the
  help topic <b>ranges</b>.  Note that the range list may be specified that
  includes 0 to select the primary image header in FITS files.
  </dd>
  </dl>
  <dl id="l_extname">
  <dt><b>extname = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extname' Line='extname = ""' -->
  <dd>Extension name pattern.  If a null string is specified then there is
  no check on the extension name.  If a pattern is specified then only
  image extensions with an extension name matching the pattern will be
  selected.  The pattern syntax is described under the help topic <i>match</i>.
  </dd>
  </dl>
  <dl id="l_extver">
  <dt><b>extver = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extver' Line='extver = ""' -->
  <dd>Extension version range list.  If a null list is specified then there is
  no check on the extension version.  If a list is given then only image
  extensions with extension versions in the list will be selected.
  The range list syntax is described under the help topic <b>ranges</b>.
  </dd>
  </dl>
  <dl id="l_lindex">
  <dt><b>lindex = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lindex' Line='lindex = yes' -->
  <dd>List the image extensions with the extension index?  If the value is
  <span style="font-family: monospace;">"no"</span> then the extension index will not be listed if the extension
  name and/or the extension version is listed.  If there is no
  extension name or extension version then the extension index is
  always listed regardless of the value of this parameter.
  </dd>
  </dl>
  <dl id="l_lname">
  <dt><b>lname = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lname' Line='lname = no' -->
  <dd>List the image extensions with the extension name if there is one?
  </dd>
  </dl>
  <dl id="l_lver">
  <dt><b>lver = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lver' Line='lver = no' -->
  <dd>List the image extensions with the extension version if there is one?
  </dd>
  </dl>
  <dl id="l_ikparams">
  <dt><b>ikparams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ikparams' Line='ikparams = ""' -->
  <dd>Include the specified image kernel parameters in the image extension
  names.  The image kernel parameters are specific to the various
  IRAF image formats.
  </dd>
  </dl>
  <dl id="l_nimages">
  <dt><b>nimages</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimages' Line='nimages' -->
  <dd>This is an output parameter which is set to the number of image extensions
  selected in the last execution of the task.  Note that if the task
  is run as a background job this parameter will not be set in the
  disk parameter file though it can be made available in a background
  script using this task by caching the parameter set; i.e. 
  include the command <span style="font-family: monospace;">"cache imextensions"</span> at the beginning of the script.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Imextensions</b> selects and lists image extensions in files.  Image
  extensions currently occur in multi-extension FITS files and multi-group
  Geiss (STF format) files.  The image extension names are given in proper
  syntax for IRAF image names for use in tasks expecting image names.
  The output format type may be a one line list, a list of one image
  extension name per line, or no output.  These options allow capturing
  the expanded list in a CL string variable, in a file for use as
  an <span style="font-family: monospace;">"@file"</span>, or to simply count the number of image extensions matching
  the selection criteria.  Note that if the <span style="font-family: monospace;">"list"</span> output type is selected
  and the list of image extensions exceeds 255 characters (the limit
  for a CL string) then the task aborts with an error.
  </p>
  <p>
  Image extensions may be selected by index value (the position in the file),
  by extension name (keyword EXTNAME used in FITS image extensions), and by
  extension version number (keyword EXTVER).  The numeric selection uses
  range lists and the extension name selection uses pattern matching.  The
  primary image in a multi-extension FITS file may also be selected by
  including an index value of 0 in the index range list.
  </p>
  <p>
  The output image extension names may be given with the index value and/or
  the image kernel specification.  The image kernel specification, which is
  image type dependent, may include the extension name, extension version,
  and other kernel parameters.  Note that if the image does not have an
  extension name or version then the index value is always given whether or
  not the <i>lindex</i> parameter is set to insure that a proper image name is
  generated.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Get a list of image extensions in a CL string and use it to select
  header keywords.  This illustrates the use of the <span style="font-family: monospace;">"list"</span> output and
  a CL variable.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imext obj001 output=list | scan (s1)
  cl&gt; = s1
  obj001[1],obj001[2],obj001[3]
  cl&gt; if (imext.nimages &gt; 0)
  &gt;&gt;&gt; hselect (s1, "$I,title", yes)
  obj001[1]   Alpha Leo
  obj001[2]   Beta Leo
  obj001[3]   Gamma Leo
  </pre></div>
  <p>
  2.  Do the same thing as in the first example using an <span style="font-family: monospace;">"@file"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imext obj001 output=file &gt; list.dat
  cl&gt; type list.dat
  obj001[1]
  obj001[2]
  obj001[3]
  cl&gt; if (imext.nimages &gt; 0)
  &gt;&gt;&gt; hselect @list.dat $I,title yes
  obj001[1]   Alpha Leo
  obj001[2]   Beta Leo
  obj001[3]   Gamma Leo
  </pre></div>
  <p>
  3.  Create a list selecting only the first and third extension and using the
  image extension name, version, and an image kernel section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imext obj*[1:100,1:100] index=1,3 lindex- lname+ lver+ ikparams=expand
  obj001.fits[aleo,1,expand][1:100,1:100]
  obj003.fits[gleo,1,expand][1:100,1:100]
  obj002.fits[im1,1,expand][1:100,1:100]
  obj002.fits[im3,1,expand][1:100,1:100]
  cl&gt; = imext.nimages
  4
  </pre></div>
  <p>
  4.  List only the primary images in a set of multi-extension FITS files.
  A primary image need not contain image data; i.e. this will select
  global headers with NDIM=0 as well as headers with image data.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imext *.fits index=0
  abc.fits[0]
  def.fits[0]
  ghi.fits[0]
  </pre></div>
  <p>
  5.  Use this task in a script to test on the existence of extension name
  <span style="font-family: monospace;">"joy"</span>.  This example shows the use of the pattern matching and of the
  <b>cache</b> command to insure the script works as a background task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  procedure example (image)
  
  file    image   {prompt="Image"}
  
  begin
          file    im
  
          cache imextensions
          im = image
  
          imextensions (im, output="none", extname="joy")
          if (imextensions.nimages == 0)
              call printf ("No joy found with %s\n", im)
  end
  </pre></div>
  <p>
  Note that proper script programming would make all the hidden parameters
  explicit.
  </p>
  <p>
  6.  Example of the extension name pattern matching.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imext obj.fits extname=joy lindex- lname+
  obj.fits[joy]
  obj.fits[nojoy]
  obj.fits[joyfull]
  cl&gt; imext obj.fits extname="^joy$" lindex- lname+
  obj.fits[joy]
  cl&gt; imext obj.fits extname="{joy}$" lindex- lname+
  obj.fits[joy]
  obj.fits[Joy]
  obj.fits[nojoy]
  </pre></div>
  <p>
  The first example matches <span style="font-family: monospace;">"joy"</span> anywhere in the extension name, the
  second requires an exact match with the begin and end string characters,
  and the last example ignores the case and requires the name end with
  joy.
  </p>
  <p>
  7.  An example with a Geiss file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imext y00vk102r.d0h index="x5"
  y00vk102r.d0h[1]
  y00vk102r.d0h[6]
  y00vk102r.d0h[11]
  y00vk102r.d0h[16]
  y00vk102r.d0h[21]
  y00vk102r.d0h[26]
  y00vk102r.d0h[31]
  y00vk102r.d0h[36]
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_IMEXTENSIONS">
  <dt><b>IMEXTENSIONS V2.11.?</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEXTENSIONS' Line='IMEXTENSIONS V2.11.?' -->
  <dd>Image sections are now allowed in the input names.
  </dd>
  </dl>
  <dl id="l_IMEXTENSIONS">
  <dt><b>IMEXTENSIONS V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEXTENSIONS' Line='IMEXTENSIONS V2.11' -->
  <dd>This task is new in this release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <div class="highlight-default-notranslate"><pre>
  files, sections, ranges, match
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE   ' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
