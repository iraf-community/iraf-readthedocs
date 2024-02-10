.. _improject:

improject: Project image along one axis decreasing the
======================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  improject infile outfile projaxis 
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This program projects an image along a chosen axis, producing an image
  with one fewer dimensions.
  The axis projected may be either summed or averaged.
  Processing a 1-dimensional image
  produces a 1-dimensional image with a single element.
  </p>
  <p>
  The task appends an image section to each input image name
  to serve as a template for the output image;
  this reduces the dimension and
  establishes appropriate coordinate parameters for the output.
  For this reason, the input image name must not include an image section.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name list]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name list]' -->
  <dd>List of input file names.
  An image section may not be used with the image names.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name list]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name list]' -->
  <dd>List of output file names, one for each input file.
  </dd>
  </dl>
  <dl id="l_projaxis">
  <dt><b>projaxis = 1 [integer, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='projaxis' Line='projaxis = 1 [integer, min=1]' -->
  <dd>Axis along which to project.
  If this value exceeds the number of dimensions in an input image,
  then no operation will be performed.
  </dd>
  </dl>
  <dl>
  <dt><b>(average = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(average = no) [boolean]' -->
  <dd>Average the image along the specified axis?  If 'average=no', the task 
  will produce a sum along the axis.
  </dd>
  </dl>
  <dl>
  <dt><b>(highcut = 0.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(highcut = 0.0) [real]' -->
  <dd>All values equal to or greater than, 'highcut' will be disregarded, 
  unless 'highcut=lowcut', in which case all points will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(lowcut = 0.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lowcut = 0.0) [real]' -->
  <dd>All values equal to or less than, 'lowcut' will be disregarded, unless 
  'highcut=lowcut', in which case all points will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(pixtype = real) [string, allowed values: real | long | int | </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pixtype = real) [string, allowed values: real | long | int | ' -->
  <dd>short | double]
  <br>
  Data type desired in the output image.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Print the file names of each image pair as they are processed?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Project an image along axis 2.
  If the input image is 2-dimensional, this example will
  produce a 1-dimensional
  image by summing the columns of the input image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; improject inim outim 2
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
  
