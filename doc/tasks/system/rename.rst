.. _rename:

rename: Rename a file
=====================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rename file newname
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_file">
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file' Line='file' -->
  <dd>A template specifying the file or files to be renamed.
  </dd>
  </dl>
  <dl id="l_newname">
  <dt><b>newname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newname' Line='newname' -->
  <dd>If a single file is being renamed, the new filename, else the new name of
  the field being renamed in a set of filenames.  If <i>newname</i> is a
  directory the input files will be moved to this directory with the same
  name.
  </dd>
  </dl>
  <dl id="l_field">
  <dt><b>field = all</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='field' Line='field = all' -->
  <dd>If set to <span style="font-family: monospace;">"all"</span> the file name remains unchanged and the <i>newname</i> is
  assumed to be a destination directory in the case of multiple input files,
  or the new filename (which may contain a new directory path) in the case of
  a single input file.  If set to <i>ldir</i> the <i>newname</i> value is taken
  to be a destination directory and the file is moved to this directory.
  Setting to <i>root</i> will rename only the root portion of the filename,
  a value of <i>extn</i> will change or append the extension. <i>newname</i>
  cannot contain a directory path when changing the root or extn field.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Rename</i> renames either a single file to <span style="font-family: monospace;">"newname"</span>, or a set of files,
  changing either the ldir, root or the extension part of each name.  
  If <i>newname</i> is a directory or  <i>field</i> is <span style="font-family: monospace;">"ldir"</span> the input files
  are moved to this directory and the filenames remain the same.  When
  modifying the root or extension part of the filename <i>newname</i> is the
  new root or extension name for the input files, an extension will be added
  to the file name if it doesn't already exist and the extension field is being
  modified.  For multiple input files it is assumed
  that <i>newname</i> is a directory if the value of <i>field</i> is <span style="font-family: monospace;">"all"</span>, 
  otherwise an error is generated to prevent overwriting files.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Rename file <span style="font-family: monospace;">"fred"</span> to <span style="font-family: monospace;">"jay"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rename fred jay
  </pre></div>
  <p>
  2. Change the root name of a set of files from <span style="font-family: monospace;">"out"</span> to <span style="font-family: monospace;">"pkout"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rename out.x,out.o,out.par pkout field=root
  </pre></div>
  <p>
  3. Change the extension of all <span style="font-family: monospace;">".f77"</span> files from <span style="font-family: monospace;">".f77"</span> to <span style="font-family: monospace;">".f"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rename *.f77 f field=extn
  </pre></div>
  <p>
  4. Move all files with a <span style="font-family: monospace;">".dat"</span> extension to a new directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rename *.dat data$
  cl&gt; rename *.dat /data/user
  </pre></div>
  <p>
  5. Add a <span style="font-family: monospace;">".fits"</span> extension to all files in a directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rename im00* fits field=extn
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  movefiles, copy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
