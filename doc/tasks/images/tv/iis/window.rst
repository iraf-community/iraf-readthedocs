.. _window:

window: Adjust the contrast and dc offset of the current frame
==============================================================

**Package: iis**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  window
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The lookup table between the display frame values and the values sent
  to the display monitor is adjusted interactively to enhance the display.
  The mapping is linear with two adjustable parameters; the intercept
  and the slope.  The two values are set with the image display cursor
  in the two dimensional plane of the display.  The horizontal position
  of the cursor sets the intercept or zero point of the transformation.
  Moving the cursor to the left lowers the zero point while moving the cursor to
  the right increases the zero point.  The vertical position of the cursor
  sets the slope of the transformation.  The middle of the display is zero
  slope (all frame values map into the same output value) while points above
  the middle have negative slope and points below the middle have positive
  slope.  Positions near the middle have low contrast while positions near
  the top and bottom have very high contrast.  By changing the slope from
  positive to negative the image may be displayed as positive or negative.
  </p>
  <p>
  The interactive loop is exited by pressing any button on the cursor control.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; window
  Window the display and push any button to exit:
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  It may be necessary to execute FRAME before windowing.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cv
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
