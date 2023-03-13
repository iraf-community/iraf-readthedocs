.. _sections:

sections: Expand an image template on the standard output
=========================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sections images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Image template or list of images.  There is no check that the names are
  images and any name may be used.  The thing which distinguishes an image
  template from a file template is that the special characters <span style="font-family: monospace;">'['</span> and
  <span style="font-family: monospace;">']'</span> are interpreted as image sections rather than a character class
  wildcard unless preceded by the escape character <span style="font-family: monospace;">'!'</span>.  To explicitly
  limit a wildcard template to images one should use an appropriate
  extension such as <span style="font-family: monospace;">".imh"</span>.
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = <span style="font-family: monospace;">"fullname"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = "fullname"' -->
  <dd>The options are:
  <dl>
  <dt><b><span style="font-family: monospace;">"nolist"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"nolist"' -->
  <dd>Do not print list.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"fullname"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"fullname"' -->
  <dd>Print the full image name for each image in the template.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"root"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"root"' -->
  <dd>Print the root name for each image in the template.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"section"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"section"' -->
  <dd>Print the section for each image in the template.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_nimages">
  <dt><b>nimages</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimages' Line='nimages' -->
  <dd>The number of images in the image template.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The image template list <i>images</i> is expanded and the images are printed
  one per line on the standard output unless the <span style="font-family: monospace;">"nolist"</span> option is given.
  Other options allow selection of a portion of the image name.  The number
  of images in the list is determined and stored in the parameter <i>nimages</i>.
  </p>
  <p>
  This task is used for several purposes:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>To verify that an image template is expanded as the user desires.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>To create a file of image names which include image sections.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd>To create a file of new image names using the concatenation feature of the
  image templates.
  </dd>
  </dl>
  <dl>
  <dt><b>(4)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(4)' -->
  <dd>To determine the number of images specified by the user in a command language
  script.
  </dd>
  </dl>
  <p>
  There is no check that the names are images and any name may be used.
  The thing which distinguishes an <i>image template</i> from a <i>file
  template</i> is that the special characters <span style="font-family: monospace;">'['</span> and <span style="font-family: monospace;">']'</span> are interpreted
  as image sections rather than a character class wildcard unless
  preceded by the escape character <span style="font-family: monospace;">'!'</span>.  To explicitly limit a wildcard
  template to images one should use an appropriate extension such as <span style="font-family: monospace;">".imh"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate and print the number of images in a template:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sections fits*.imh opti=no
  cl&gt; = sections.nimages
  cl&gt; 7
  </pre></div>
  <p>
  2. Expand an image template:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sections fits*![3-9].imh[1:10,*]
  fits003.imh[1:10,*]
  fits004.imh[1:10,*]
  &lt;etc.&gt;
  </pre></div>
  <p>
  Note the use of the character class escape, image section appending,
  and explicit use of the .imh extension.
  </p>
  <p>
  3. Create a new list of image names by adding the suffix <span style="font-family: monospace;">"new"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sections jan18???//new
  jan18001new
  jan18002new
  &lt;etc.&gt;
  </pre></div>
  <p>
  Note the use of the append syntax.  Also there is no guarantee that the
  files are actually images.
  </p>
  <p>
  4. Subtract two sets of images:
  	
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sections objs*.imh[100:200,300:400] &gt; objslist
  cl&gt; sections skys*.imh[100:200,300:400] &gt; skyslist
  cl&gt; sections %objs%bck%* &gt; bcklist
  cl&gt; imarith @objslist - @skyslist @bcklist
  </pre></div>
  <p>
  Note the use of the substitution syntax.
  </p>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The  image list is not sorted.           
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  files
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
