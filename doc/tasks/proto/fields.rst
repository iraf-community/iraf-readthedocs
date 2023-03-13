.. _fields:

fields: Extract specified fields from a list
============================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fields files fields
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>File or files from which the fields are to be extracted.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields' -->
  <dd>The fields to be extracted.  
  </dd>
  </dl>
  <dl id="l_lines">
  <dt><b>lines = <span style="font-family: monospace;">"1-"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lines' Line='lines = "1-"' -->
  <dd>The lines from which the fields are to be extracted.  If multiple files are 
  being extracted, the same lines apply to each file.
  </dd>
  </dl>
  <dl id="l_quit_if_missing">
  <dt><b>quit_if_missing = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='quit_if_missing' Line='quit_if_missing = no' -->
  <dd>This flag determines the task behavior when a field is missing from the
  specified line.  If <b>quit_if_missing</b> = yes, the task exits and an error 
  is reported.
  </dd>
  </dl>
  <dl id="l_print_file_names">
  <dt><b>print_file_names = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='print_file_names' Line='print_file_names = no' -->
  <dd>If <b>print_file_name</b> = yes, the first string of each output line of
  extracted fields is the file name.  
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The list processing tool <i>fields</i> is used to extract whitespace
  separated fields from the specified files and lines.
  The input to this task can be either the standard input or a list of
  files; output is a new list of the extracted fields.
  </p>
  <p>
  The fields of a line are numbered from 1 up to a newline character; those
  fields to be extracted are specified as a range of numbers.
  If a specified field is missing from a selected
  line the action taken is determined by the <b>quit_if_missing</b> flag;
  <i>fields</i> will either continue processing after printing a warning
  message, or call an error and exit.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Reverse the order of the 5 columns in list file <span style="font-family: monospace;">"list"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fields list 5-1 &gt; newlist
  </pre></div>
  <p>
  2. Extract columns 1 and 3 from file <span style="font-family: monospace;">"newlist"</span> and pipe them to task
  <i>graph</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fields newlist 1,3 | graph
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_FIELDS">
  <dt><b>FIELDS V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='FIELDS' Line='FIELDS V2.11' -->
  <dd>The default value for the <i>lines</i> parameter was changed to an open
  upper limit.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  joinlines, xtools.ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
