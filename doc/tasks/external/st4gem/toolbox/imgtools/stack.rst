.. _stack:

stack: Stack images to form a new image with one more dimension.
================================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  stack input output 
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The program stacks a list of images, producing an image
  with one greater dimension. Pixel [i,j,k] of the output image will be 
  equal to pixel [i,j] of image <span style="font-family: monospace;">'k'</span>.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file list]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file list]' -->
  <dd>Names of the input files that are to be stacked. All images must be of 
  the same size and have the same number of dimensions.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>Name of the output file produced by this task.
  </dd>
  </dl>
  <dl>
  <dt><b>(pixtype = real) [string, allowed values: real | long | int |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pixtype = real) [string, allowed values: real | long | int |' -->
  <dd> short | double]
  <br>
  Data type of pixels in the output image.
  </dd>
  </dl>
  <dl>
  <dt><b>(ctype = <span style="font-family: monospace;">"PIXEL"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ctype = "PIXEL") [string]' -->
  <dd>Value for the ctype keyword for the new axis.
  </dd>
  </dl>
  <dl>
  <dt><b>(crval = 0.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(crval = 0.0) [real]' -->
  <dd>Value for the crval keyword for the new axis.
  </dd>
  </dl>
  <dl>
  <dt><b>(crpix = 0.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(crpix = 0.0) [real]' -->
  <dd>Value for the crpix keyword for the new axis.
  </dd>
  </dl>
  <dl>
  <dt><b>(cdelt = 1.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cdelt = 1.0) [real]' -->
  <dd>Value for the CD matrix keyword for the new axis.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Stack all images matching the template <span style="font-family: monospace;">"inim*.imh"</span>.
  If there are 20 files with a size of 512 x 512,
  then <span style="font-family: monospace;">"outim"</span> will have dimension 512 x 512 x 20.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; stack inim*.imh outim
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by David Giaretta.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
