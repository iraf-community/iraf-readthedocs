.. _wcardimage:

wcardimage: Convert text files to cardimage files
=================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  wcardimage infiles outfiles
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_textfile">
  <dt><b>textfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='textfile' Line='textfile' -->
  <dd>A character string identifying the file (s) on disk to be processed.
  The string acts as a <span style="font-family: monospace;">"template"</span> so that multiple files can be pro-
  cessed.
  </dd>
  </dl>
  <dl id="l_cardfile">
  <dt><b>cardfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cardfile' Line='cardfile' -->
  <dd>Name of the output tape device of the form <span style="font-family: monospace;">"mta800"</span> or <span style="font-family: monospace;">"mta800[#]"</span>
  or name of disk file (s). EOT and BOT are acceptable tape file numbers.
  The file number will be appended to
  the output file name in the case of multiple file disk output.
  </dd>
  </dl>
  <dl id="l_new_tape">
  <dt><b>new_tape</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_tape' Line='new_tape' -->
  <dd>Specifies whether the output tape is blank or contains data.
  </dd>
  </dl>
  <dl id="l_contn_string">
  <dt><b>contn_string = <span style="font-family: monospace;">"&gt;&gt;"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='contn_string' Line='contn_string = "&gt;&gt;"' -->
  <dd>Character string which will be inserted at the beginning of
  card image lines which have been split from a single text line.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages of actions performed?
  </dd>
  </dl>
  <dl id="l_detab">
  <dt><b>detab = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='detab' Line='detab = yes' -->
  <dd>Remove tabs?
  </dd>
  </dl>
  <dl id="l_card_length">
  <dt><b>card_length = 80</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='card_length' Line='card_length = 80' -->
  <dd>Number of columns per card.
  </dd>
  </dl>
  <dl id="l_cards_per_blk">
  <dt><b>cards_per_blk = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cards_per_blk' Line='cards_per_blk = 50' -->
  <dd>Number of card images per physical record.
  </dd>
  </dl>
  <dl id="l_ebcdic">
  <dt><b>ebcdic = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ebcdic' Line='ebcdic = no' -->
  <dd>Translate ascii characters to ebcdic?
  </dd>
  </dl>
  <dl id="l_ibm">
  <dt><b>ibm = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ibm' Line='ibm = no' -->
  <dd>Translate ascii characters to ibm ebcdic?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  If multiple file disk output is requested, <span style="font-family: monospace;">".crd"</span> is appended to the input
  file name. Oversize lines are split and prefixed by the string <span style="font-family: monospace;">"&gt;&gt;"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a set of IRAF text files to a set of blocked ASCII cardimage files
  on tape, replacing tabs with blanks and prefixing the leftover portions
  of oversize lines with <span style="font-family: monospace;">"&gt;&gt;"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcardimage files* mtb1600[1]
  </pre></div>
  <p>
  2. Convert a set of IRAF text files to a set of blocked EBCDIC cardimage files
  on tape, replacing tabs with blanks and prefixing the leftover portions
  of oversize lines with <span style="font-family: monospace;">"&gt;&gt;"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcardimage files* mtb1600[1] eb+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The card_length in bytes must be an integral number of chars.
  At present WCARDIMAGE can only handle lines with less than or equal to
  161 characters.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rcardimage
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
