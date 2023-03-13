.. _pcalc:

pcalc: Do arithmetic operations on a list of daophot databases
==============================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pcalc infiles field value
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infiles">
  <dt><b>infiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infiles' Line='infiles' -->
  <dd>The APPHOT/DAOPHOT database(s) containing the field to be recomputed.
  </dd>
  </dl>
  <dl id="l_field">
  <dt><b>field </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='field' Line='field ' -->
  <dd>The field to be recomputed. Field must be an integer or real field
  in the input file(s).
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>The arithmetic expression used to recompute the specified field.
  Value may be an integer or real expression but must match the data
  type of field. The functions real and int may be used to do type
  conversions.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PCALC reads in the values of the <i>field</i> keyword 
  from a set of  APPHOT/DAOPHOT databases, replaces the old values
  with new values equal to the value of the arithmetic expression <i>value</i>,
  and updates the databases(s).
  </p>
  <p>
  PCALC is script task which calls TXCALC is the input file is an
  APPHOT/DAOPHOT text database or TBCLAC if APPHOT/DAOPHOT is a tables
  database.
  If the input file is a text database, the expression <i>value</i> consists
  of variables which are the field names
  specified by the #N keywords or the parameters specified by the
  #K keywords in the APPHOT/DAOPHOT text databases.
  Only keywords beginning with #N can actually be replaced.
  If the input file is an ST tables database, the expression <i>value</i>
  consists of the table column names.
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
  respectively in a file produced by the apphot package center task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pcalc m92.ctr.1 xcenter "xcenter+5.4"
  pt&gt; pcalc m92.ctr.1 ycenter "ycenter+10.3"
  </pre></div>
  <p>
  2.  Add a constant to the computed magnitudes produced by nstar.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pcalc n4147.nst.2 mag "mag+3.457"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  TXCALC does not allow arrays in the expression field.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ptools.tbcalc,tables.tcalc,ptools.pcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
