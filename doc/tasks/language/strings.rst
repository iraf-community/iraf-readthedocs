.. _strings:

strings: String manipulation routines
=====================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  str     (x)
  substr  (str, first, last)
  stridx  (test, str)
  strldx  (test, str)
  strlen  (str)
  strlwr  (str)
  strupr  (str)
  strstr  (str1, str2)
  strlstr (str1, str2)
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The following functions are available for the manipulation of strings
  within the CL.  All string positions are returned as 1-indexed values.
  </p>
  <dl id="l_str">
  <dt><b>str (x)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='str' Line='str (x)' -->
  <dd>Converts its argument into a string.  The argument may be
  boolean, integer or real.
  </dd>
  </dl>
  <dl id="l_substr">
  <dt><b>substr (str, first, last)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='substr' Line='substr (str, first, last)' -->
  <dd>Extracts a substring from string <i>str</i> from index <i>first</i> to 
  index <i>last</i>.  The <i>first</i> value may be larger than <i>last</i>, in 
  which case the returned string is reversed.  The first character in the 
  string is at index 1.
  </dd>
  </dl>
  <dl id="l_stridx">
  <dt><b>stridx (test, str)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='stridx' Line='stridx (test, str)' -->
  <dd>Finds the position of the first occurrence of any character found in <i>test</i>
  in the string <i>str</i>, returning 0 if the match fails.
  </dd>
  </dl>
  <dl id="l_strldx">
  <dt><b>strldx (test, str)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='strldx' Line='strldx (test, str)' -->
  <dd>Finds the position of the last occurrence of any character found in <i>test</i>
  in the string <i>str</i>, returning 0 if the match fails.
  </dd>
  </dl>
  <dl id="l_strlen">
  <dt><b>strlen (str)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='strlen' Line='strlen (str)' -->
  <dd>Returns the current length of a string.  Note that the maximum length may be
  obtained as the value of the expression `param.p_length'.
  </dd>
  </dl>
  <dl id="l_strlwr">
  <dt><b>strlwr (str)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='strlwr' Line='strlwr (str)' -->
  <dd>Converts <i>str</i> to all lower-case characters, returns a string value.
  </dd>
  </dl>
  <dl id="l_strupr">
  <dt><b>strupr (str)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='strupr' Line='strupr (str)' -->
  <dd>Converts <i>str</i> to all upper-case characters, returns a string value.
  </dd>
  </dl>
  <dl id="l_strstr">
  <dt><b>strstr (str1, str2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='strstr' Line='strstr (str1, str2)' -->
  <dd>Finds the position of the first occurrence of <i>str1</i> in <i>str2</i> (an
  exact match is required), or 0 if the match fails.
  </dd>
  </dl>
  <dl id="l_strlstr">
  <dt><b>strlstr (str1, str2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='strlstr' Line='strlstr (str1, str2)' -->
  <dd>Finds the position of the last occurrence of <i>str1</i> in <i>str2</i> (an
  exact match is required), or 0 if the match fails.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Simple function calls.
  </p>
  <div class="highlight-default-notranslate"><pre>
  s = str(y)                           # convert y to a string.
  s = substr  ("abcdefg", 2, 4)        # s = "bcd"
  s = substr  ("abcdefg", 4, 2)        # s = "dcb"
  i = stridx  ("abc", " eeboq")        # i = 4
  i = strldx  ("/", "/path/image.imh") # i = 6
  i = strlen  ("abc")                  # i = 3
  s = strlwr  ("ABC")                  # s = "abc"
  s = strupr  ("abc")                  # s = "ABC"
  i = strstr  ("imh","imhead.imh")     # i = 1
  i = strlstr ("imh","imhead.imh")     # i = 8
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  scan, radix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
