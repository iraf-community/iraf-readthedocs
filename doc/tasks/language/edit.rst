.. _edit:

edit: Edit a text file
======================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  edit files [files...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The file or files to be edited.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>edit</i> task invokes a host system editor to edit the named file or
  files.  The editor to be used is determined by the value of the CL environment
  variable <i>editor</i>.  Filename mapping is applied to the <i>files</i>
  argument strings to convert virtual filenames into host system filenames.
  File templates are not supported, unless the host system editor supports them.
  </p>
  <p>
  The EDT, EMACS, and VI editors are currently supported.  Each editor interface
  is controlled by an <i>edcap</i> table file in the logical directory <span style="font-family: monospace;">"dev$"</span>;
  these files are also used by the <i>ehistory</i> and <i>eparam</i> screen
  editors.  For example, the file <span style="font-family: monospace;">"dev$edt.ed"</span> is required to run the EDT
  editor.  The EDITOR_CMD field of the <i>edcap</i> file defines the command
  to be send to the host system to run the editor; this is not necessarily the
  same as the name of the editor.  Support for additional editors is easily added
  by adding new <i>edcap</i> files.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Edit the login.cl file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; edit home$login.cl
  </pre></div>
  <p>
  2. Edit the file <span style="font-family: monospace;">"temp"</span> in the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; edit temp
  </pre></div>
  <p>
  3. On a UNIX system, edit all the <span style="font-family: monospace;">".x"</span> files in the current directory.
  Filename templates cannot be used with the editor unless the editor itself,
  or the host system, expands the filename template.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; edit *.x
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The EOF control character is set in the edcap file for the editor language in
  use, e.g., <span style="font-family: monospace;">"dev$vi.ed"</span> for the VI editor.  The value in this file may differ
  from that used on the local system; if this is the case, the system installer
  should edit the file and change the value of the parameter EXIT_UPDATE.
  </p>
  <p>
  The control sequences for the keyboard arrow keys are also defined in the
  <span style="font-family: monospace;">".ed"</span> edcap file; TERMCAP should be used instead.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ehistory, eparam
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
