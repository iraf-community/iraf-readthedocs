.. _thselect:

thselect: Select tables satisfying an expression; print keywords.
=================================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  thselect table keywords expr
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task was based on 'hselect',
  and it behaves in a very similar manner,
  except that it works on tables rather than images.
  </p>
  <p>
  Keyword values will be printed to the standard output,
  one line per input table,
  with the values separated by tabs.
  String values that contain whitespace will be enclosed in quotes.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>A list of tables for which keywords are to be printed.
  These will be opened read-only and will not be modified.
  </dd>
  </dl>
  <dl id="l_keywords">
  <dt><b>keywords [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keywords' Line='keywords [string]' -->
  <dd>One or more keywords, separated by commas and/or blanks.
  The special keywords such as <span style="font-family: monospace;">"i_table"</span>
  that are supported by 'thedit' can also be used with 'thselect'.
  For each input table,
  the values of these keywords in the current input table will be printed,
  if 'expr' is a true expression for the current table.
  Any keyword that is not found will be silently ignored.
  Wildcards are supported; however,
  the <span style="font-family: monospace;">"@filename"</span> syntax is not supported.
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr = <span style="font-family: monospace;">"yes"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr = "yes" [string]' -->
  <dd>This is a boolean expression
  to be evaluated for each table in the list.
  The default value may be used to unconditionally print keyword values.
  The expression may include constants and/or keyword names.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Compare 'thselect' with 'thedit' for displaying a single keyword value.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thselect timetag.fits[events,7] rootname yes
  
  O57P03030
  
  tt&gt; thedit timetag.fits[events,7] rootname .
  
  timetag.fits[events,7],ROOTNAME = O57P03030 / rootname of the obser
  vation set
  </pre></div>
  <p>
  2.  Compare i_file with i_table for a FITS table
  ($I and i_table are equivalent).
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thselect timetag.fits[events,7] i_file,i_table yes
  
  timetag.fits      timetag.fits[EVENTS,7]
  </pre></div>
  <p>
  3.  Find all FITS files with DETECTOR = 'CCD' in the primary header.
  Since the primary header of a FITS file can be opened
  either as an image or as a table,
  either 'hselect' or 'thselect' could be used for this example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thselect *.fits[0] $I "detector == 'CCD'"
  
  h1v11148o_1dx.fits[0]
  h4s13500o_1dx.fits[0]
  i1c1615po_1dx.fits[0]
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Phil Hodge,
  based on 'hselect'.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  hselect, thedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
