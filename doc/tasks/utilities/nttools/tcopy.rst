.. _tcopy:

tcopy: Copy tables.
===================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tcopy intable outtable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is used to copy tables.  The input may be a general filename
  template, including wildcard characters or the name of a file (preceded
  by an @ sign) containing table names.  The output may be either a directory
  specification or a list of table names.  If the output is a list of tables
  then there must be the same number of names in the input and output lists,
  and the names are taken in pairs, one from input and one from output.
  The input and output tables must not be the same.
  This task will convert the format of the table
  if the output filename extension indicates it.
  For example, if the output filename extension is <span style="font-family: monospace;">".fits"</span>,
  the output table will be a fits file.
  If the output is redirected or piped,
  it will be written to a text table.
  </p>
  <p>
  NOTE: Be careful when using a wildcard for the extension.
  If you have the files <span style="font-family: monospace;">"table.tab"</span> and <span style="font-family: monospace;">"table.lis"</span> in the current directory,
  for example, then the command <span style="font-family: monospace;">"tcopy tab* test/"</span> would copy both files
  to the subdirectory <span style="font-family: monospace;">"test"</span>.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>A list of one or more tables to be copied.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name template]' -->
  <dd>Either a directory name or a list of output table names.
  If 'outtable' is not a directory,
  the number of input tables and output tables must be the same.
  An exception to this rule is that if 'outtable' is a FITS file
  (i.e. an existing FITS file, or the name ends in <span style="font-family: monospace;">".fits"</span>)
  then multiple input tables can be copied to one output file.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Display names of input and output tables as they are copied?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To simply copy a table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcopy table.tab tablecopy.tab
  </pre></div>
  <p>
  2.  To copy one or more tables, possibly changing table type:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcopy table1.tab,table2.tab a.fits,b.tab
  tt&gt; tcopy a.fits,b.tab a.tab,b.fits
  tt&gt; tcopy a.fits &gt; a.txt
  </pre></div>
  <p>
  The number of input and output tables must be the same.
  In the third case,
  <span style="font-family: monospace;">"a.txt"</span> will be a text file because
  the output table name was <span style="font-family: monospace;">"STDOUT"</span>
  (the name was implicitly set, in this case,
  because the output was redirected.)
  </p>
  <p>
  3.  To copy a set of tables to a new directory:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcopy table*.tab directory
              or
  tt&gt; tcopy table*.tab directory$
              or
  tt&gt; tcopy table*.tab osdirectory
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"directory"</span> is an IRAF environment variable for a directory name,
  and <span style="font-family: monospace;">"osdirectory"</span> is an operating system directory name
  (e.g., <span style="font-family: monospace;">"/user/me/"</span> in UNIX).
  </p>
  <p>
  4.  To copy only specified extensions of a FITS file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcopy xyz.fits[3],xyz.fits[5] b.fits
  </pre></div>
  <p>
  If <span style="font-family: monospace;">"b.fits"</span> did not already exist,
  it would be created and would then contain two table extensions.
  If it did already exist,
  the two extensions would be appended.
  Note that the number of input and output files are not the same;
  this is OK because the output is a FITS file
  and can therefore contain multiple table extensions.
  </p>
  <p>
  5.  The input and/or output may be redirected:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; dir l+ | tproject columns=c7,c3 | tcopy dir.tab &gt; verbose.lis
  </pre></div>
  <p>
  <span style="font-family: monospace;">"verbose.lis"</span> contains just the one line <span style="font-family: monospace;">"# STDIN -&gt; dir.tab"</span>,
  and <span style="font-family: monospace;">"dir.tab"</span> has the output of 'tproject', the file names and sizes.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Phil Hodge.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tdelete
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
