.. _tscopy:

tscopy: Copy row/column subsets of tables using selectors.
==========================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tscopy intable outtable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is used to copy tables.  The input may be a filename
  template, including wildcard characters or the name of a file (preceded
  by an @ sign) containing table names.  The output may be either a directory
  specification or a list of table names.  If the output is a list of tables
  then there must be the same number of names in the input and output lists,
  and the names are taken in pairs, one from input and one from output.
  The input and output tables must not be the same.
  </p>
  <p>
  This task supports row/column selectors in the input table name. These
  may be used to select subsets of both rows and columns from the input table.
  Type 'help selectors' to see a description of the selector syntax. 
  </p>
  <p>
  NOTE: Be careful when using a wildcard for the extension.
  If you have the files 'table.tab' and 'table.lis' in the current directory,
  for example, then the command <span style="font-family: monospace;">"tscopy tab* test/"</span> would copy both files to the subdirectory
  'test'.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>A list of one or more tables to be copied. Row/column selectors are supported.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name template]' -->
  <dd>Either a directory name or a list of output table names. The standard
  value <span style="font-family: monospace;">"STDOUT"</span> generates ASCII output that can be redirected to a file.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Display names of input and output tables as files are copied?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To simply copy a table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tscopy table tablecopy
  </pre></div>
  <p>
  2. To copy a table into an ASCII table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tscopy table STDOUT &gt; table.txt
  </pre></div>
  <p>
  3. To copy several tables:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tscopy table1,table2,tab67 a,b,c
  cl&gt; tscopy tab*.tab a,b,c
  </pre></div>
  <p>
  In the latter case the extension is given explicitly in case there
  are other files beginning with <span style="font-family: monospace;">"tab"</span> that are not tables; there must
  be exactly three tables beginning with <span style="font-family: monospace;">"tab"</span> because the output list
  has three names.
  </p>
  <p>
  4. To copy a set of tables to a new directory:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tscopy table*.tab directory
                    or
  cl&gt; tscopy table*.tab directory$
                    or
  cl&gt; tscopy table*.tab osdirectory
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"directory"</span> is an IRAF environment variable for a directory name,
  and <span style="font-family: monospace;">"osdirectory"</span> is an operating system directory name
  (e.g., <span style="font-family: monospace;">"/user/me/"</span> in UNIX).
  </p>
  <p>
  5. To copy a subset of rows and columns:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tscopy "table.tab[c:wave,flux][r:wave=(4000:5000)]" tableout
  </pre></div>
  <p>
  This command will copy only columns named <span style="font-family: monospace;">"wave"</span> and <span style="font-family: monospace;">"flux"</span> from the input
  table to the output. It will also select and copy only the rows in which
  the <span style="font-family: monospace;">"wave"</span> value lies between 4000 and 5000.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  selectors
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
