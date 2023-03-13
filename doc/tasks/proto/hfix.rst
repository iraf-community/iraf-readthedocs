.. _hfix:

hfix: Fix image headers with a user specified command
=====================================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hfix images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images whose headers are to be fixed.  If <i>update</i> is yes then
  the user must have write permission on the image headers.
  </dd>
  </dl>
  <dl id="l_command">
  <dt><b>command = <span style="font-family: monospace;">"edit $fname"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='command' Line='command = "edit $fname"' -->
  <dd>Command to be applied to a file containing the image header.  The command
  may be any CL command which includes escapes to host commands.  The file
  containing the header in text form is specified by the special string
  <span style="font-family: monospace;">"$fname"</span>.  The command should modify this file to the desired form.  The
  default is to invoke a text editor but there are many other possibilities.
  The image name may also be specified with <span style="font-family: monospace;">"$image"</span>.  See the EXAMPLES
  section for some ideas.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update the image header with the modified header.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task allows you to extract the image headers into a text file,
  modify this file with a specified command, and update the image header
  with the modified file.  The command to be applied is specified with
  the <i>command</i> parameter.  In this command the text file containing
  the header to be acted upon is referenced with the string <span style="font-family: monospace;">"$fname"</span>.
  If it is desired to update the image header with the modified file
  the <i>update</i> switch must be set.  You must have write permission
  to update the image headers.
  </p>
  <p>
  A common command, which is the default, is to use a text editor.
  Other possibilities are to save the file, use a non-interactive host
  command such as <b>sed</b> in UNIX, or write your own program or
  script.
  </p>
  <p>
  This task does very little processing on the header after you are finished
  editing.  It checks for legal FITS characters in the first 8 columns and if
  there is an <span style="font-family: monospace;">'='</span> in column 9 then there must be a <span style="font-family: monospace;">' '</span> (blank) in column 10.
  Lines violating these checks are skipped.  It also sets each line in the
  header to the correct length.  Because you have total freedom to change the
  header parameters while in the text editor, you must make sure that the
  header has a legal format after you are through editing it. In particular,
  be sure each field in the header parameters that you add or change begin in
  the proper columns.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Edit the header of the image test.imh:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hfix test.imh
  &lt;Edit the header text&gt;
  </pre></div>
  <p>
  2. Get the header of a single image and save the file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hfix myim command="copy $fname save" update-
  </pre></div>
  <p>
  3. A image header was created with an incorrect format such that the
  equal sign is in column 10 instead of 9:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hfix *.imh \
  &gt;&gt;&gt; command="!sed 's/ =/=/' $fname &gt;temp;mv temp $fname"
  </pre></div>
  <p>
  Note that this example should not be tried on a valid header where the
  equal sign is in column 9.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  images.hedit noao.artdata.mkheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
