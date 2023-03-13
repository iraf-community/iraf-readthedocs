.. _zoom:

zoom: Zoom in on the image (change magnification)
=================================================

**Package: iis**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  zoom
  </p>
  <dl id="l_zoom_factor">
  <dt><b>zoom_factor</b></dt>
  <!-- Sec='USAGE' Level=0 Label='zoom_factor' Line='zoom_factor' -->
  <dd>Zoom factor by the display is to be expanded.  The factors are powers
  of 2; 1 = no zoom, 2 = factor of 2, 3 = factor of 4, and 4 = factor of 8.
  </dd>
  </dl>
  <dl id="l_window">
  <dt><b>window = no</b></dt>
  <!-- Sec='USAGE' Level=0 Label='window' Line='window = no' -->
  <dd>Window the enlarged image?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The display is zoomed by the specified factor.  A zoom factor of 1 is no
  magnification and higher factors correspond to factors of 2.  The zoom
  replicates pixels on the monitor and only a part of the display frame
  centered on the display cursor is visible.  The window option allows
  the user to adjust interactively with the cursor the part of the zoomed
  frame.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To magnify the displayed frame by a factor of 2:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; zoom 2
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cv
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
