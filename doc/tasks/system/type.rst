.. _type:

type: Type a text file on the standard output
=============================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  type input_files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_files">
  <dt><b>input_files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_files' Line='input_files' -->
  <dd>A template specifying the file or files to be typed.
  </dd>
  </dl>
  <dl id="l_map_cc">
  <dt><b>map_cc = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='map_cc' Line='map_cc = yes' -->
  <dd>If set, output any non-printing control characters in the input text in
  a printable form, e.g., ctrl/c (ASCII 3) would be output as ^C.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"terminal"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "terminal"' -->
  <dd>The output device, defaulting to the user's terminal.  If the special device
  <span style="font-family: monospace;">"text"</span> is named, any standout mode control characters embedded in the text
  will cause the enclosed text to be output in upper case.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Type</i> copies the named files (or the files selected by
  the file template) to the standard output.
  If there is more than one file in the input list, a header naming the file
  to be printed will precede each output file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Type all files in the current directory with the extension <span style="font-family: monospace;">".x"</span> on the
  standard output.  Do not pause between files or pages (unlike <i>page</i>).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type *.x
  </pre></div>
  <p>
  2. Capture the manual page for task <i>hedit</i> in a text file, in a form
  suitable for printing on any device.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help hedit | type dev=text &gt; hedit.doc
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  page, head, tail, concatenate, lprint
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
