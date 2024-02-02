.. _fparse:

fparse: Parse file specifications and leave results in parameters.
==================================================================

**Package: tools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fparse input
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  'fparse' takes as input a pathname specification and parses the
  specification into the various components: directory, root, extension,
  group, and section.  The parameters of 'fparse' are set to these
  different components.  Optionally, through the use of the 'verbose'
  parameter, 'fparse' can write to standard output with the components
  separated by spaces.  The order in which the components are written
  out is in the same order as the parameters.  If any component is missing,
  two double-quotes, <span style="font-family: monospace;">""</span>, are used as a place holder.
  </p>
  <p>
  Note that any numbers used in the specification, such as group number
  or image section, are limited to a maximum of about 2 billion.  Any
  larger number will give invalid results.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>The pathname specification to parse into the individual components.
  The maximum length of this string is 160 characters.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = no) [boolean]' -->
  <dd>Write components to standard output?
  If set to <span style="font-family: monospace;">"yes"</span>, the components are written to standard output on one line
  separated by spaces.  The components are written in the following
  order: directory root extension group section
  </dd>
  </dl>
  <dl>
  <dt><b>(directory) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(directory) [string]' -->
  <dd>This output parameter will contain the directory part of the pathname
  specification after 'fparse' is executed.  The directory specification
  will end with the appropriate directory indication character, for
  example, <span style="font-family: monospace;">"$"</span> or <span style="font-family: monospace;">"/"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(root) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(root) [string]' -->
  <dd>This output parameter will contain the root name part of the pathname
  specification after 'fparse' is executed.
  </dd>
  </dl>
  <dl>
  <dt><b>(extension) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(extension) [string]' -->
  <dd>This output parameter will contain the extension part of the pathname
  specification after 'fparse' is executed.  This will also contain the
  <span style="font-family: monospace;">"."</span> extension indicator.
  </dd>
  </dl>
  <dl>
  <dt><b>(cl_index) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cl_index) [integer]' -->
  <dd>This will contain the group number, or -1 if no group was specified.
  </dd>
  </dl>
  <dl>
  <dt><b>(cl_size) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cl_size) [integer]' -->
  <dd>This will contain the number of groups, or -1 if no group was specified.
  </dd>
  </dl>
  <dl>
  <dt><b>(section) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(section) [string]' -->
  <dd>This output parameter will contain the section specification part of the pathname
  specification after 'fparse' is executed.  This includes the brackets
  <span style="font-family: monospace;">"["</span> and <span style="font-family: monospace;">"]"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Parse the pathname 'dev$pix.imh'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fparse dev$pix.imh
  </pre></div>
  <p>
  2. Parse the pathname 'dev$pix.imh' and write the result to standard
  output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl &gt;fparse dev$pix.imh verbose+
  dev$ pix imh -1 -1 ""
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  This routine will break if any more syntax is added to pathname
  specifications. This routine uses the <span style="font-family: monospace;">"illegal"</span> call to 'imparse'.
  </p>
  <p>
  This routine ignores what is called a <span style="font-family: monospace;">"ksection"</span>.  Not clear what this is.
  </p>
  <p>
  Though the IRAF system parsing routines don't handle wildcards, the capability
  is here.  The assumption is that directory specifications can never have
  wildcards and anything after the last <span style="font-family: monospace;">'.'</span> is an extension, wildcards included.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
