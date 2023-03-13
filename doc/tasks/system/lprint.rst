.. _lprint:

lprint: Print a file on the line printer device
===============================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  lprint files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A filename template specifying the files to be printed.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"printer"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "printer"' -->
  <dd>The output device.  If the value of <i>device</i> is the reserved string
  <span style="font-family: monospace;">"printer"</span>, the name of the actual printer device is taken from the value
  of the environment variable <span style="font-family: monospace;">"printer"</span>.
  </dd>
  </dl>
  <dl id="l_map_cc">
  <dt><b>map_cc = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='map_cc' Line='map_cc = yes' -->
  <dd>If set to <span style="font-family: monospace;">"yes"</span>, any unprintable characters embedded in the text are printed
  in the form <span style="font-family: monospace;">"^X"</span>, where ^A is &lt;ctrl/A&gt; (ASCII 1), and so on.
  </dd>
  </dl>
  <dl id="l_paginate">
  <dt><b>paginate = <span style="font-family: monospace;">"auto"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='paginate' Line='paginate = "auto"' -->
  <dd>If <i>paginate</i> is set to <span style="font-family: monospace;">"auto"</span> and the standard input is not redirected,
  pages are broken and a header is printed at the top of each page.
  If <i>paginate</i> is set to <span style="font-family: monospace;">"auto"</span> and the standard input <i>is</i> redirected,
  the input text is not paginated, allowing proper operation when <i>lprint</i>
  is used in a pipe, e.g., taking input from <i>help</i>.
  If <span style="font-family: monospace;">"paginate"</span> is set to <span style="font-family: monospace;">"yes"</span>, pages are broken even if the input text
  is being read from STDIN.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label = <span style="font-family: monospace;">"STDIN"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='label' Line='label = "STDIN"' -->
  <dd>If displaying a header with input from the standard input, use the
  <span style="font-family: monospace;">"label"</span> string where the filename would appear in a normal header.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The named files, or the standard input, are printed on the standard
  line printer device.  Each file is printed starting at the top of a new
  page, with a header giving the page number and the date of last modification
  for the file.  Pagination and headers are normally suppressed when reading
  input from the standard input, but may be enabled if desired.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print all files with an extension of either <span style="font-family: monospace;">".x"</span> or <span style="font-family: monospace;">".h"</span>, followed by
  all files with the extension <span style="font-family: monospace;">".com"</span>.  Note that filename sorting occurs only
  within a comma delimited field of the filename template, hence the <span style="font-family: monospace;">"*.[xh]"</span>
  files are printed in sort order, followed by the <span style="font-family: monospace;">".com"</span> files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lprint *.[xh],*.com
  </pre></div>
  <p>
  2. Print the output of the <i>imstat</i> task on the versatec printer,
  paginating the output with the given label on each page.  Note that the
  command may be broken after the <span style="font-family: monospace;">"pipe"</span> character without need for
  explicit backslash continuation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imstat nite1.* |
  &gt;&gt;&gt; lprint pag+ label="Image Statistics" device=versatec
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  type
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
