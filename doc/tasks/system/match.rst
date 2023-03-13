.. _match:

match: Print all lines in a file that match a pattern
=====================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  match pattern files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_pattern">
  <dt><b>pattern</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pattern' Line='pattern' -->
  <dd>The pattern to be matched.  A pattern may contain any of the
  pattern matching <i>meta-characters</i> described below.
  </dd>
  </dl>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A template specifying the file or files to be searched.  Omitted if the
  standard input is redirected.
  </dd>
  </dl>
  <dl id="l_meta">
  <dt><b>meta-characters = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='meta' Line='meta-characters = yes' -->
  <dd>Set to <span style="font-family: monospace;">"no"</span> to disable the pattern matching meta-characters, e.g., when
  you want to explicitly match one of the meta-characters as a regular character.
  </dd>
  </dl>
  <dl id="l_stop">
  <dt><b>stop = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='stop' Line='stop = no' -->
  <dd>If <i>stop</i> is enabled, lines with match the pattern are <span style="font-family: monospace;">"stopped"</span> (not
  passed to the output), otherwise only those lines with match the pattern
  are output.
  </dd>
  </dl>
  <dl id="l_print_file_names">
  <dt><b>print_file_names = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='print_file_names' Line='print_file_names = yes' -->
  <dd>If more than one file is being searched, preface each printed line
  with the <span style="font-family: monospace;">"file_name: "</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The listed files are searched for the given pattern, copying each line that
  matches to the standard output.  If <span style="font-family: monospace;">"stop"</span> is set the action is reversed,
  i.e., all lines are passed on to the output except those which match the
  pattern.  If no files are named text is read from the standard input.
  The pattern matching meta-characters are described in the table below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ^               matches the beginning of a line
  $               matches the end of a line
  ?               matches any single character
  *               matches zero or more of whatever is at the left
  [12345]         matches any single character in the given set
  [1-5]           matches any single character in a range
  [^a-z]          matches any character NOT in the range/set
  #               matches whitespace
  {chars}         turns off case sensitivity inside the braces
  \               used to include a meta-character in the pattern
  </pre></div>
  <p>
  If more than one file is being searched, each output line is prefixed
  with its file name.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. From all the lines displayed by <span style="font-family: monospace;">"set"</span>, print only those that have
  the string <span style="font-family: monospace;">"tty"</span> somewhere in them.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set | match tty
  </pre></div>
  <p>
  2. Find all tasks that delete something.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help * | match delete
  </pre></div>
  <p>
  3. Delete all the <span style="font-family: monospace;">"red"</span> objects from the list file <span style="font-family: monospace;">"catalog"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; match red catalog stop+ &gt; newcatalog
  </pre></div>
  <p>
  4. Type out the file <span style="font-family: monospace;">"spool"</span>, omitting all lines that end in a colon,
  and paginating the output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; match ":$" spool stop+ | page
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  lcase, ucase, translit, sort, unique
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
