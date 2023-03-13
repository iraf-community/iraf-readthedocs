.. _files:

files: Expand a file template into a list of files
==================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  files template
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_template">
  <dt><b>template</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='template' Line='template' -->
  <dd>A file name template specifying the set of files to be listed.
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort = <span style="font-family: monospace;">"yes"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = "yes"' -->
  <dd>Sort the file list.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Files</i> lists all files matching the given template.  The existence of
  the listed files is checked only if pattern matching is used, hence <i>files</i>
  may also be used to parse a comma delimited list of strings which are not
  necessarily filenames.  <i>Files</i> performs the same function as <span style="font-family: monospace;">"dir l+"</span>
  but is simpler and more convenient to use when generating file lists.
  </p>
  <p>
  The <i>files</i> task and all other tasks which operate upon groups of files
  use the <b>file template</b> facility to specify the set of files to be
  operated upon.  This should not be confused with the <b>image template</b>
  facility, used by tasks which operate upon sets of images and which is
  documented in the manual page for the <i>sections</i> task.
  </p>
  <p>
  Pattern matching in a file template is provided by the usual pattern matching
  meta-characters <span style="font-family: monospace;">"*?[]"</span>, documented in the CL User's Guide.  Pattern matching 
  is used to select files from one or more directories.  In addition, the
  filename template notation provides two operators for generating new filenames
  from the matched filenames.  These are the <b>concatenation</b> operator <span style="font-family: monospace;">"//"</span>,
  and the <b>string substitution</b> operator <span style="font-family: monospace;">"%chars%newchars%"</span>.
  The concatenation operator concatenates either a prefix to a filename,
  or a suffix to the root of a filename.  The string substitution operator
  uses the <span style="font-family: monospace;">"chars"</span> to match filenames, and then replaces the <span style="font-family: monospace;">"chars"</span> by the
  <span style="font-family: monospace;">"newchars"</span> to generate the final output filename.  Either string may be null
  length to insert into or delete characters from a filename.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Generate a single column list of files in the current directory,
  sorted in ASCII collating sequence.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; files
  </pre></div>
  <p>
  2. Generate an unsorted single column list of files in logical directory
  <span style="font-family: monospace;">"lib$"</span>.  Each entry in the output list is of the form <span style="font-family: monospace;">"lib$..."</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; files lib$ sort-
  </pre></div>
  <p>
  3. Generate a file list to be used to make a set of new files.  The new file
  names will be the old file names with <span style="font-family: monospace;">"_1"</span> concatenated to the root, e.g.,
  <span style="font-family: monospace;">"root.x"</span> would map to <span style="font-family: monospace;">"root_1.x"</span> and so on.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; files root.*//_1
  </pre></div>
  <p>
  4. Generate a file list similar to that in [3], adding a directory prefix
  to each filename.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; files dir$//root.*
  </pre></div>
  <p>
  5. Use string substitution to change the filename extension of a set of files
  to <span style="font-family: monospace;">".y"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; files root.%*%y%
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  directory, pathnames, images.sections
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
