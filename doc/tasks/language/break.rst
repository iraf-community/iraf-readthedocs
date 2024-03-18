.. _break:

break: Break out of a loop
==========================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  break
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>break</i> statement is used to exit (break out of) the <i>for</i> or
  <i>while</i> loop in which it is found.  In the case of nested loop constructs
  only the innermost loop is terminated.
  Unlike C usage the <i>break</i> statement does not break out of a switch.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Scan a list (file), printing each list element until either the list is
  exhausted or a list element <span style="font-family: monospace;">"exit"</span> or <span style="font-family: monospace;">"quit"</span> is encountered.
  </p>
  <div class="highlight-default-notranslate"><pre>
  while (fscan (list, s1) != EOF) {
      if (s1 == "exit" || s1 == "quit")
          break
      print (s1)
  }
  </pre></div>
  <p>
  2. Sum the pixels in a two dimensional array, terminating the sum for each
  line if a negative pixel is encountered, and terminating the entire process
  when the total sum passes a predefined limit.
  </p>
  <div class="highlight-default-notranslate"><pre>
  total = 0
  for (i=1;  i &lt;= NCOLS;  i+=1) {
      for (j=1;  j &lt;= NLINES;  j+=1) {
          if (pixel[i,j] &lt; 0)
              break               # exit the J loop
          total += pixel[i,j]
      }
      if (total &gt; NPHOT)
          break                   # exit the I loop
  }
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  next, while, for
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
