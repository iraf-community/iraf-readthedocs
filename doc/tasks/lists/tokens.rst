.. _tokens:

tokens: Break a file up into a stream of tokens
===============================================

**Package: lists**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tokens files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The list of files to be converted into a stream of tokens.
  </dd>
  </dl>
  <dl id="l_ignore_comments">
  <dt><b>ignore_comments = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ignore_comments' Line='ignore_comments = yes' -->
  <dd>Ignore comments in the input string?
  </dd>
  </dl>
  <dl id="l_begin_comment">
  <dt><b>begin_comment = <span style="font-family: monospace;">"#"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='begin_comment' Line='begin_comment = "#"' -->
  <dd>The string marking the start of a comment
  </dd>
  </dl>
  <dl id="l_end_comment">
  <dt><b>end_comment = <span style="font-family: monospace;">"eol"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='end_comment' Line='end_comment = "eol"' -->
  <dd>The string marking the end of a comment.  The value <b>end_comment</b> = <span style="font-family: monospace;">"eol"</span>
  means the end of a line terminates a comment.
  </dd>
  </dl>
  <dl id="l_newlines">
  <dt><b>newlines = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newlines' Line='newlines = yes' -->
  <dd>Is newline a legal token?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>tokens</i> breaks the input up into a series of tokens.
  The makeup of the
  various tokens is defined by the FMTIO primitive ctotok, which is not very 
  sophisticated, and does not claim to recognize the tokens for any particular
  language (though it does reasonably well for most modern languages).  Comments
  can be deleted if desired, and newlines may be passed on to the output as
  tokens.
  </p>
  <p>
  Comments are delimited by user specified strings.  Only strings which are also
  recognized by ctotok() as legal tokens may be used as comment delimiters.
  If newline marks the end of a comment, the end_comment string should be given
  as <span style="font-family: monospace;">"eol"</span>.  Examples of acceptable comment conventions are (<span style="font-family: monospace;">"#"</span>, eol),
  (<span style="font-family: monospace;">"/*"</span>, <span style="font-family: monospace;">"*/"</span>), (<span style="font-family: monospace;">"{"</span>, <span style="font-family: monospace;">"}"</span>), and (<span style="font-family: monospace;">"!"</span>, eol).  Fortran style comments (<span style="font-family: monospace;">"^{c}"</span>,eol)
  can be stripped by filtering with match beforehand.
  </p>
  <p>
  Each token is passed to the output on a separate line.  Multiple newline
  tokens are compressed to a single token (a blank line).  If newline is not
  desired as an output token, it is considered whitespace and serves only to
  delimit tokens.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Break up the source file for this task into tokens:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tokens tokens.x
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  words
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
