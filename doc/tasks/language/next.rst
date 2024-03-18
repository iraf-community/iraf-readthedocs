.. _next:

next: Start next iteration of a loop
====================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  next
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>next</i> statement begins the next iteration of the loop construct
  in which it is enclosed, without executing any of the statements remaining
  before the end of the loop.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sum the pixels in a two dimensional array.  Skip any negative valued pixels.
  </p>
  <div class="highlight-default-notranslate"><pre>
  for (i=1;  i &lt;= NCOLS;  i+=1) {
      for (j=1;  j &lt;= NLINES;  j+=1) {
          if (pixel[i,j] &lt; 0)
              next
          total += pixel[i,j]
      }
  }
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  break, while, for
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
