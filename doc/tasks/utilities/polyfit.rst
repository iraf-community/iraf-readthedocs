.. _polyfit:

polyfit: Fit polynomial to list of X,Y data
===========================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  polyfit filelist order
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b><b>filelist</b></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='\fBfilelist\fR' -->
  <dd>File containing X,Y, SIGMAY triples to be fit. May be STDIN, or a list
  of file names. Note that the third list quantity is only required if
  <i>weighting</i> = instrumental.
  </dd>
  </dl>
  <dl>
  <dt><b><b>order</b></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='\fBorder\fR' -->
  <dd>The order of the polynomial fit. (e.g. a parabolic fit has order 2)
  </dd>
  </dl>
  <dl id="l_weighting">
  <dt><b>weighting = uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = uniform' -->
  <dd>The type of weighting for the fit. The choices are:
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>No weighting.
  </dd>
  </dl>
  <dl>
  <dt><b>instrumental</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='instrumental' Line='instrumental' -->
  <dd>The weight of each point is equal to 1. / SIGMAY ** 2.
  </dd>
  </dl>
  <dl>
  <dt><b>statistical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='statistical' Line='statistical' -->
  <dd>The weight of each point is equal to 1. / Y.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b><b>verbose</b> = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='\fBverbose\fR = no' -->
  <dd>If <b>verbose</b> = yes, additional information about the fit is printed on
  the standard output.
  </dd>
  </dl>
  <dl>
  <dt><b><b>listdata</b> = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='\fBlistdata\fR = no' -->
  <dd>If <b>listdata</b> = yes, the only output will be the calculated values for the
  X,Y pairs. This is useful as input to <i>graph</i>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A polynomial weighted fit of specified order is fit to the X,Y, SIGMAY data
  triples
  read from the input file, files, or STDIN. The resulting coefficients
  of the polynomial are printed on the first line of the standard output.
  The uncertainty in each coefficient is printed on the next line.
  These are listed as:
  </p>
  <br>
  <p>
  a0 a1 a2 a3 ...
  <br>
  s0 s1 s2 s3 ...
  </p>
  <br>
  <p>
  where the polynomial has the form:
  </p>
  <br>
  <p>
  y = a0 + a1*x + a2*x**2 + a3*x**3 + ...
  </p>
  <br>
  <p>
  and the coefficients have uncertainties (<span style="font-family: monospace;">"sigmas"</span>) s0 - sN.
  </p>
  <p>
  If verbose is set to yes, the following additional information is
  listed: the resulting reduced chi-square, f-test, correlation coefficient,
  standard deviation of residuals, and number of items in the list.
  Also a tabular listing of each data element, X,Y, SIGMAY and the independent
  variable, Yc, as calculated according to the fit, is printed.
  </p>
  <p>
  If listdata is set to yes, the only output which will appear will
  be the listing of X,Yc,Y, SIGMAY. This provides a list suitable as input to
  GRAPH or any other list oriented utility. Setting listdata to yes
  overrides the verbose option.
  </p>
  <p>
  The routine REGRES from the library of routines written by Bevington is used 
  for the fit; see <b>Data Reduction and Error Analysis</b>, by Bevington.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; polyfit STDIN 2
  cl&gt; polyfit datafile 4 verbose+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The maximum number of data elements is currently limited to 1000
  X,Y,SIGMAY triples.  Also the system must be overdetermined.  That is, the
  number of data elements must exceed the order by at least 2.
  </p>
  <p>
  Beware of data elements having large dynamic range.  The limitation
  of the machine exponent range can produce overflow and underflow
  arithmetic exceptions.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  curfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
