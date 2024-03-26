.. _scan:

scan: Scan the standard input
=============================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  scan  (p1, p2, p3 ... pn)
  fscan (param, p1, p2, p3, ... pn)
  scanf  (format, p1, p2, p3 ... pn)
  fscanf (param, format, p1, p2, p3, ... pn)
  
  n = nscan()
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_pN">
  <dt><b>pN</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pN' Line='pN' -->
  <dd>The name of an output parameter, to receive a scanned value.
  </dd>
  </dl>
  <dl id="l_param">
  <dt><b>param</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='param' Line='param' -->
  <dd>The name of the input parameter whose <i>value</i> is to be scanned to
  produce the output values.
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format' -->
  <dd>A C-like format specification string containing plain characters, which 
  which must match exactly what's on the input stream, and conversion 
  specifications,
  each of which causes conversion and scanning of zero or more <i>args</i>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Scan</i>, <i>scanf</i>, <i>fscan</i>,
  and <i>fscanf</i> permit the user to read in values from the
  standard input, a file, or a parameter and assign them to the listed parameters.
  <i>Fscan</i> or <i>fscanf</i> may also be used to read a string already in core.
  It is useful to consider these functions as performing two disjoint actions:
  acquiring a string, where <i>scan/scanf</i> and <i>fscan/fscanf</i> differ; 
  and parsing the string, where they are identical.
  </p>
  <p>
  <i>Scan/scanf</i> acquires its string by reading exactly one 
  line from the standard
  input.  The action of <i>fscan/fscanf</i> depends on <i>param</i>.  
  If <i>param</i> is
  a string, or a struct, then the string is simply the value of <i>param</i>.
  If, however, <i>param</i> is a list-directed struct, a call to <i>fscanfscanf</i>
  will get the next line from the file pointed to by <i>param</i>.
  The file can be rewound by assigning a file name to <i>param</i>.
  If either scan or fscan reach an EOF, they return with the value EOF and
  do not change any parameters.
  </p>
  <p>
  Once the string has been acquired it is parsed into segments delimited by
  spaces or tabs in the case of <i>scan</i> or <i>fscan</i>, or when using
  <i>scanf</i> and <i>fscanf</i> with no field width specification for the
  field formats.
  <i>Scan</i> and <i>fscan</i> do not recognize quoted strings, nor do they
  view <span style="font-family: monospace;">','</span> as a delimiter.  The formatted scan functions scanf and fscanf
  recognize <span style="font-family: monospace;">','</span> as a delimiter in the case of numeric conversion only.
  Each token is then assigned in turn to p1 through
  pn.  If there are too many tokens they are discarded, if there are too
  few, the corresponding parameters are not affected by the call.
  Any conversion error terminates the scan, but parameters already scanned
  retain their new values.  An assignment to a struct terminates the scan
  because the entire unscanned portion of the string is assigned to the
  struct.  Thus any struct should be the last parameter in a scan or
  fscan call.
  </p>
  <p>
  Scan/scanf and fscan/fscanf are intrinsic functions returning either EOF 
  if end of 
  file on the input list is sensed, or the number of parameters successfully
  scanned.  The function <i>nscan</i> also returns the number of parameters
  successfully scanned in the last call to scan or fscan.
  </p>
  <p>
  A field format specification has the form <span style="font-family: monospace;">"%[*][W][lh]C"</span>, where <span style="font-family: monospace;">'*'</span> indicates
  the field should be skipped, W is  the  field width,
  <span style="font-family: monospace;">'l'</span> indicates longword output, <span style="font-family: monospace;">'h'</span> indicates halfword output, and
  C is the format code.  The format codes C are as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  c    single character (c or '\c' or '\0nnn')
  d    decimal integer
  e    exponential format
  f    fixed format
  g    general format
  o    octal integer
  s    string
  x    hexadecimal integer
  </pre></div>
  <p>
  The W (field width) specification indicates the exact number of characters
  to assign to the given argument, e.g. <span style="font-family: monospace;">"%2s"</span> would assign two characters of
  an input string to a string variable even though the actual string might
  contain more before a delimiting whitespace.  For numeric input, only W
  digits, decimal points, or exponentiation characters are assigned, e.g.
  <span style="font-family: monospace;">"%3f"</span> used on the string <span style="font-family: monospace;">"1.23456"</span> would result in a value of <span style="font-family: monospace;">"1.2"</span>,
  <span style="font-family: monospace;">"%2d"</span> used on the string <span style="font-family: monospace;">"12345"</span> would result in a value of <span style="font-family: monospace;">"12"</span>, and so
  on.  If no field width is specified all characters up to a delimiting
  whitespace are used in the conversion, in the case of numeric data and a
  numeric format characters up to a whitespace or non-numeric (including
  decimal points and an <span style="font-family: monospace;">'e'</span> or <span style="font-family: monospace;">'d'</span> exponentiation character) are used.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print a list of radii, given a list of coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  list = coords
  while (fscan (list, x, y) != EOF)
      print (sqrt (x**2 + y**2))
  </pre></div>
  <p>
  2. Use a formatted scan of the standard input.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; print ("1.234 5 7.34abc") | scanf ("%g %d %f %s", x, i, y, s1)
  cl&gt; =x
  1.234
  cl&gt; =i
  5
  cl&gt; =y
  7.34
  cl&gt; =s1
  abc
  </pre></div>
  <p>
  3. Use a formatted scan from a <span style="font-family: monospace;">"list"</span> parameter.
  </p>
  <p>
          fscanf (list, <span style="font-family: monospace;">"%g %d %f %s"</span>, x, i, y, s1)
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The syntax of scan and fscan is peculiar, in that they are the only
  functions where parameters are effectively passed by reference rather than by
  value.  Thus p1, ... pn must be parameters whereas in similar contexts an
  arbitrary expression can be used wherever a parameter can.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  string, print, fprint, printf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
