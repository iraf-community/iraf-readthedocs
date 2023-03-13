.. _evalfit:

evalfit: Compute the standard indices by evaluating the fit
===========================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  evalfit observations config parameters calib
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_observations">
  <dt><b>observations</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observations' Line='observations' -->
  <dd>The list of files containing the observations.
  <i>Observations</i> are multi-column text files, whose columns are delimited
  by whitespace, and whose first column is reserved for an object id.
  All observations files in the list must have the same format.
  </dd>
  </dl>
  <dl id="l_config">
  <dt><b>config</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='config' Line='config' -->
  <dd>The configuration file. <i>Config</i> is a text file which
  specifies the format of the <i>observations</i> and <i>catalog</i> files, and
  defines the form of the transformation equations to be evaluated.
  More information can be obtained about this file by typing
  <span style="font-family: monospace;">"help mkconfig"</span> and <span style="font-family: monospace;">"help config"</span>.
  </dd>
  </dl>
  <dl id="l_parameters">
  <dt><b>parameters</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameters' Line='parameters' -->
  <dd>The name of the file produced by the FITPARAMS task.
  <i>Parameters</i> is a text file 
  containing the fitted parameter values for each
  equation and other information about the quality of the
  fit. Records in <i>parameters</i> are assigned a name equal to the label
  of fitted equation. If more than one record in <i>parameters</i> has
  the same name then the last record of that name is used by EVALFIT to 
  evaluate the fit.
  </dd>
  </dl>
  <dl id="l_calib">
  <dt><b>calib</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calib' Line='calib' -->
  <dd>The name of the output file. <i>Calib</i> is a text file
  containing the name of the fitted object in the first column,
  followed by the <i>print</i>
  variables if any, followed by the fitted value, error of the fit (if
  <i>errors</i> is not <span style="font-family: monospace;">"undefined"</span>), and residual of the
  fit (if catalog matching is enabled) for each equation.
  </dd>
  </dl>
  <dl id="l_catalogs">
  <dt><b>catalogs</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalogs' Line='catalogs' -->
  <dd>The list of files containing the catalog data.
  <i>Catalogs</i> are multi-column text files, whose columns are delimited
  by whitespace, and whose first column is reserved for an object id.
  All catalog files in the list must have the same format.
  If <i>catalogs</i> = <span style="font-family: monospace;">""</span>, then no id matching with the observations
  files is done.
  </dd>
  </dl>
  <dl id="l_errors">
  <dt><b>errors = <span style="font-family: monospace;">"undefined"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='errors' Line='errors = "undefined"' -->
  <dd>The algorithm used to compute formal errors for each object fit. The choices
  are:
  <dl>
  <dt><b>undefined</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='undefined' Line='undefined' -->
  <dd>No errors are computed and no error values are output.
  </dd>
  </dl>
  <dl>
  <dt><b>obserrors</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='obserrors' Line='obserrors' -->
  <dd>The error in each fitted value is computed by summing in quadrature
  the contribution to the total error made by each individual error in the
  observations file variables. If no error columns are defined for the
  observations files the error is assumed to be INDEF.
  </dd>
  </dl>
  <dl>
  <dt><b>equations</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='equations' Line='equations' -->
  <dd>The error in each fitted value is computed by evaluating the error
  equations associated with each transformation equation. If no error equation
  is defined then the error is assumed to be INDEF.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_objects">
  <dt><b>objects = <span style="font-family: monospace;">"all"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objects' Line='objects = "all"' -->
  <dd>The type of objects to output to <i>calib</i>. The choices are:
  <dl>
  <dt><b>all</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='all' Line='all' -->
  <dd>Both program and standard stars are output.
  </dd>
  </dl>
  <dl>
  <dt><b>program = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='program' Line='program = yes' -->
  <dd>Only program stars are output.
  </dd>
  </dl>
  <dl>
  <dt><b>standard = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='standard' Line='standard = yes' -->
  <dd>Only standard stars are output.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_print">
  <dt><b>print = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='print' Line='print = ""' -->
  <dd>Additional variables to be printed in the output file. These variables are
  printed immediately after the id, and may be any of the
  catalog variables, observations variables, or the set equation variables
  defined in <i>config</i>.
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format = ""' -->
  <dd>An SPP style format string to apply to the output data, in place of the
  default format.  SPP format strings
  are described in detail in the formats section.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append the output to <i>calib</i> instead of creating a new file. If the
  file already exists and <i>append</i> is <span style="font-family: monospace;">"no"</span> EVALFIT will abort.
  </dd>
  </dl>
  <dl id="l_catdir">
  <dt><b>catdir = <span style="font-family: monospace;">")_.catdir"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catdir' Line='catdir = ")_.catdir"' -->
  <dd>The directory containing the supported standard star catalogs.
  The default parameter value  redirects <i>catdir</i>
  to a package parameter of the same name. A list of standard
  catalogs may be obtained by printing the file <span style="font-family: monospace;">"photcal$catalogs/README"</span>.
  Alternatively the user may create their own standard star catalogs 
  and standard star catalog directory.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  EVALFIT evaluates the transformation  equations
  for the program and/or standard objects in <i>observations</i>, using
  the transformation equations defined in <i>config</i>,
  the fitted parameter values in the file <i>parameters</i> produced by the
  FITPARAMS
  task, and writes the output to the file <i>calib</i>. If <i>append</i> is <span style="font-family: monospace;">"yes"</span>
  output may be appended to an existing file.
  </p>
  <p>
  EVALFIT computes the values of the catalog variables for the program
  stars by inserting the observations variables directly into the
  transformation equations. EVALFIT can evaluate any number of transformation
  equations, but if there are any standard catalog variables in the right-hand
  side of the transformation equation, EVALFIT will assign INDEF to the fitted
  for that equation.
  </p>
  <p>
  Below are two sets of transformation equations. The first set can be evaluated
  with EVALFIT, the second set cannot and must be inverted with INVERTFIT.
  In both cases the catalog variables to be fit are V and BV, and
  the observed quantities are mv, mb, Xv, and Xb.
  </p>
  <div class="highlight-default-notranslate"><pre>
  System 1:    V = v0 + mv + v1 * (Xv + Xb) / 2. + v2 * (mb - mv)
               BV = b0 + b1 * (Xv + Xb) / 2. + b2 * (mb - mv)
  
  System 2:    mv = v0 + V + v1 * Xv + v2 * BV
               mb = b0 + V + BV + b1 * Xb + b2 * BV
  </pre></div>
  <p>
  Formal errors for each fit may
  be computed by,  1) setting <i>errors</i> to <span style="font-family: monospace;">"obserrors"</span> and using the
  error columns defined in the observations section of <i>config</i>
  to estimate the errors or 2) evaluating the error equations defined in
  <i>config</i>.
  </p>
  <p>
  If the user wishes to match the objects in <i>observations</i> with those
  in <i>catalogs</i> in order for example, to compute the residuals of the fit,
  <i>catalogs</i> must be defined. Similarly if <i>objects</i> is <span style="font-family: monospace;">"program"</span>
  or <span style="font-family: monospace;">"standard"</span>, <i>catalogs</i> must be defined in order to enable
  id matching.
  </p>
  <p>
  Legal <i>catalog</i> and <i>observations</i> files are multi-column text
  files whose columns are delimited by whitespace.
  The first column of a catalog file is <i>always</i> reserved for an object id.
  The first column of an observations file is reserved for an
  object id which can be
  used to match the observational data with the corresponding catalog data.
  All other columns may contain any quantity which can be
  expressed as an integer or real number.  Sexagesimal format numbers
  (hh:mm:ss) are interpreted internally as real numbers. The constant
  INDEF can be used to represent data that is missing or undefined.
  Double precision and complex data are
  not supported. Lines beginning with <span style="font-family: monospace;">"#"</span> are treated as comment lines.
  </p>
  <p>
  By default EVALFIT prints out the object id,
  followed by the variables listed in the <i>print</i>
  parameter, followed by the fit value, estimated
  error (if <i>errors</i> is not <span style="font-family: monospace;">"undefined"</span>), and residual of the fit
  (for any standard star observations that can be matched with the
  catalog values) for each fitted equation. The user can format the output
  by setting the <i>format</i> parameter to an SPP style string. 
  SPP format strings are described in detail below.
  </p>
  </section>
  <section id="s_formats">
  <h3>Formats</h3>
  <p>
  A format specification has the form <span style="font-family: monospace;">"%w.dCn"</span>, where w is the field width,
  d is the number of decimal places or the number of digits of precision,
  C is the format code, and n is radix character for format code <span style="font-family: monospace;">"r"</span> only.
  The w and d fields are optional.  The format codes C are as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  b       boolean (YES or NO)
  c       single character (c or '\c' or '\0nnn')
  d       decimal integer
  e       exponential format (D specifies the precision)
  f       fixed format (D specifies the number of decimal places)
  g       general format (D specifies the precision)
  h       hms format (hh:mm:ss.ss, D = no. decimal places)
  m       minutes, seconds (or hours, minutes) (mm:ss.ss)
  o       octal integer
  rN      convert integer in any radix N
  s       string (D field specifies max chars to print)
  t       advance To column given as field W
  u       unsigned decimal integer
  w       output the number of spaces given by field W
  x       hexadecimal integer
  z       complex format (r,r) (D = precision)
  
  Conventions for w (field width) specification:
  
      W =  n      right justify in field of N characters, blank fill
          -n      left justify in field of N characters, blank fill
          0n      zero fill at left (only if right justified)
  absent, 0       use as much space as needed (D field sets precision)
  
  Escape sequences (e.g. "\n" for newline):
  
  \b      backspace   (<b>not implemented</b>)
  formfeed
  \n      newline (crlf)
  \r      carriage return
  \t      tab
  \"      string delimiter character
  \'      character constant delimiter character
  \\      backslash character
  \nnn    octal value of character
  
  Examples
  
  %s          format a string using as much space as required
  %-10s       left justify a string in a field of 10 characters
  %-10.10s    left justify and truncate a string in a field of 10 characters
  %10s        right justify a string in a field of 10 characters
  %10.10s     right justify and truncate a string in a field of 10 characters
  
  %7.3f       print a real number right justified in floating point format
  %-7.3f      same as above but left justified
  %15.7e      print a real number right justified in exponential format
  %-15.7e     same as above but left justified
  %12.5g      print a real number right justified in general format
  %-12.5g     same as above but left justified
  
  \n          insert a newline
  </pre></div>
  <p>
  Note that deferred value fields are <b>not implemented</b> in EVALFIT.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Evaluate the fit for a list of program stars in m92. Use the errors
  in the observed quantities to estimate the errors.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; evalfit m92.obs m92.cfg m92.fit m92.cal
  </pre></div>
  <p>
  2. Repeat the fit computed above but include the variables xu and yu which
  are the positions of the objects in the u frame in the output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; evalfit m92.obs m92.cfg m92.fit m92.cal print="xu,yu"
  </pre></div>
  <p>
  3. Repeat the fit computed above but format the output. The user has
  determined that the output will have 5 columns containing the object id,
  xu, yu, fit value and fit error respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; evalfit m92.obs m92.cfg m92.fit m92.cal print="xu,yu"\
      format="%-10.10s  %-7.2f  %-7.2f  %-7.3f  %-6.3f\n"
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkconfig,chkconfig,fitparams,invertfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FORMATS' 'EXAMPLES' 'SEE ALSO'  -->
  
