.. _taperedge:

taperedge: Apply a cosine bell or linear taper to image edges.
==============================================================

**Package: fourier**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  taperedge input output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task applies a taper function to the edges of a list of 1-D or 2-D images.
  The image values will be tapered down from their original values
  toward zero at the edges.
  This task is intended to prepare images for cross correlation.
  The 'crosscor' task extends the input images
  with zeros to reduce the effect of aliasing,
  but if the images have non-zero values around the edges,
  the discontinuities will bias the cross correlation.
  </p>
  <p>
  If 'input' and 'output' image names are identical,
  the image will be modified in-place.
  This is done by writing the output to a temporary image,
  then deleting the input image and renaming the temporary image.
  </p>
  <p>
  This task includes an option to subtract a value from the input image
  before applying the taper.
  The default is to subtract the mean of the values near the edges.
  </p>
  <p>
  The specific function used for the taper may be selected to be
  either the cosine bell or a linear function, as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  i is the pixel number, starting at one at the edge.
  
  function = "cosbell":
  
      taper(i) = (1 - cos(x)) / 2,
      where x = i * pi / (width + 1)
  
  function = "linear":
  
      taper(i) = i / (width + 1)
  </pre></div>
  <p>
  Near the corners of a 2-D image,
  the taper function is the product of the taper in each dimension.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input = <span style="font-family: monospace;">""</span> [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input = "" [file name template]' -->
  <dd>Names of the input images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span> [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "" [file name template]' -->
  <dd>Names of the output images created by this task.
  If the output list is null, all the input images will be modified in-place;
  otherwise, the number of input and output names must be the same.
  If an output name is identical to the corresponding input name,
  the input image will be modified in-place.
  </dd>
  </dl>
  <dl>
  <dt><b>(width = <span style="font-family: monospace;">"10 %"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(width = "10 %") [string]' -->
  <dd>Width of taper zone at each edge.
  If 'width' is set to zero,
  this task may be used to subtract the mean from each input image.
  The taper effects pixels to and including 'width' pixels from each edge,
  and the taper is such that the result does not actually reach zero
  at the pixels at the edge.
  The result would reach zero one pixel beyond the edges of the image.
  For example, for a 1-D input image filled with a value of one,
  using parameters 'width=<span style="font-family: monospace;">"5"</span>', 'subtract=<span style="font-family: monospace;">"none"</span>', 'function=<span style="font-family: monospace;">"cosbell"</span>',
  the first six output values would be  0.067, 0.25, 0.5, 0.75, 0.933, 1;
  the last six would be the same in reverse order.
  If 'width' contains a <span style="font-family: monospace;">"%"</span> sign or the word <span style="font-family: monospace;">"percent"</span>,
  the numerical value is interpreted to be a percent of the image size.
  In this case, for 2-D images the width of the taper region
  may be different for the two axes.
  For each axis, the width in pixels will be the nearest integer to
  the product of 'width' and the axis length divided by 100.
  If 'width' does not contain <span style="font-family: monospace;">"%"</span> or <span style="font-family: monospace;">"percent"</span>,
  only a single numerical value may be given,
  and that value is taken to be the width in pixels.
  For 2-D images the width will be the same for both axes.
  </dd>
  </dl>
  <dl>
  <dt><b>(subtract = <span style="font-family: monospace;">"edge"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(subtract = "edge") [string]' -->
  <dd>Value to be subtracted from each input image before applying taper.
  The value to be subtracted may be specified as
  <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"mean"</span>, <span style="font-family: monospace;">"edge"</span>, or a specific numerical value.
  (This is case insensitive, and only the first letter is examined.)
  If subtract = <span style="font-family: monospace;">"none"</span> or <span style="font-family: monospace;">"0"</span>, then nothing will be subtracted.
  For subtract = <span style="font-family: monospace;">"mean"</span>, the value is the average of the entire input image.
  For subtract = <span style="font-family: monospace;">"edge"</span>, the value is the average within
  the band of 'width' pixels around the edge,
  or for 1-D the average of 'width' pixels at the left end
  and 'width' pixels at the right end.
  You can also specify a specific numerical value for 'subtract'.
  </dd>
  </dl>
  <dl>
  <dt><b>(function = <span style="font-family: monospace;">"cosbell"</span>) [string, Allowed values:  cosbell | linear ]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(function = "cosbell") [string, Allowed values:  cosbell | linear ]' -->
  <dd>This is the function to use for the taper.
  The default is to use the cosine bell function,
  but a linear taper is also available.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Print names of input and output images along with width in pixels as
  each image is processed?
  If 'subtract' is something other than <span style="font-family: monospace;">"none"</span>,
  the value that was subtracted will also be printed.
  The image names and width are printed before processing begins,
  and the value subtracted is printed after processing is completed.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Taper the edges of <span style="font-family: monospace;">"x4"</span>, writing the output to <span style="font-family: monospace;">"x4t"</span>.
  The average of the edge values are subtracted from <span style="font-family: monospace;">"x4"</span>
  before tapering toward zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fo&gt; taperedge x4 x4t subtract="edge"
  </pre></div>
  <p>
  2.  Add 27.3 to <span style="font-family: monospace;">"x4"</span> and use a linear taper.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fo&gt; taperedge x4 x4t subtract="-27.3" function="linear"
  </pre></div>
  <p>
  If 'verbose=yes', you could get the following output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  x4 --&gt; x4t
      xwidth = 5, ywidth = 7 pixels;  subtract = -27.3
  </pre></div>
  <p>
  3.  Apply a taper to the edges of <span style="font-family: monospace;">"x4"</span>, <span style="font-family: monospace;">"x5"</span>, and <span style="font-family: monospace;">"x6"</span>,
  writing the output back into the input images.
  No value is subtracted from the input before tapering.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fo&gt; taperedge "x4,x5,x6" "" subtract="none"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  Type <span style="font-family: monospace;">"help fourier option=sys"</span> for a higher-level description of
  the 'fourier' package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
