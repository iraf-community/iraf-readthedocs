.. _tbcalc:

tbcalc: Do arithmetic on a list of apphot/daophot tables databases
==================================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tbcalc textfiles column value
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_textfiles">
  <dt><b>textfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='textfiles' Line='textfiles' -->
  <dd>The APPHOT/DAOPHOT ST tables database(s) containing the column to be recomputed.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column' -->
  <dd>The column to be recomputed. Column must be an integer or real column
  in the input file(s).
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>The arithmetic expression used to recompute the specified column.
  Value may be an integer or real expression but must match the data
  type of column.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  TBCALC reads in the value of the <i>column</i> 
  from a set of  APPHOT/DAOPHOT ST tables databases, replaces it with a new
  value specified by the arithmetic expression <i>value</i>,
  and updates the ST tables databases(s).
  </p>
  <p>
  The expression <i>value</i> consists of variables which are column names
  in the APPHOT/DAOPHOT ST tables database.
  TBCALC uses the TABLES package task TCALC to actually perform the
  arithmetic operation.
  </p>
  <p>
  The supported
  arithmetic operators and functions are briefly described below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  addition                +               subtraction             -
  multiplication          *               division                /
  negation                -               exponentiation          **
  absolute value          abs(x)          cosine                  cos(x)
  sine                    sin(x)          tangent                 tan(x)
  arc cosine              acos(x)         arc sine                asin(x)
  arc tangent             atan(x)         arc tangent             atan2(x,y)
  exponential             exp(x)          square root             sqrt(x)
  natural log             log(x)          common log              log10(x)
  minimum                 min(x,y)        maximum                 max(x,y)
  convert to integer      int(x)          convert to real         real(x)
  nearest integer         nint(x)         modulo                  mod(x)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Change the XCENTER and YCENTER fields to XCENTER + 5.4 and YCENTER + 10.3
  respectively in a file produced by the daophot package allstar task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; tbcalc m92.als.1 xcenter "xcenter+5.4"
  pt&gt; tbcalc m92.als.1 ycenter "ycenter+10.3"
  </pre></div>
  <p>
  2.  Add a constant to the computed magnitudes produced by the daophot
  package nstar task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; tbcalc n4147.nst.2 mag "mag+3.457"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ptools.txcalc,tables.tcalc,ptools.pcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
