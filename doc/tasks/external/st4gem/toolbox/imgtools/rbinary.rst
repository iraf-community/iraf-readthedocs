.. _rbinary:

rbinary: Create an image from a binary file.
============================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rbinary input output naxis dimen[7] datatype offset
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates an image from the contents of a binary file.
  The input file may be four-byte real, four-byte integer, or
  two-byte integer; the output image will have the same data type as the 
  input image.
  The user may specify a number of bytes (an even number) that is to be 
  skipped at the beginning of the file before reading the data.
  </p>
  <p>
  We suggest that you either use the 'eparam' task to fill in parameter values
  or let the cl prompt you.
  The problem is that the 'dimen' parameter is an array,
  and it's rather clumsy to give array values on the command line.
  It can be done, though.  See the examples.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>The input binary file, including extension.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>The name of the output image to be created.
  </dd>
  </dl>
  <dl id="l_naxis">
  <dt><b>naxis = 1 [integer, min=1, max=7]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naxis' Line='naxis = 1 [integer, min=1, max=7]' -->
  <dd>The number of axes.
  </dd>
  </dl>
  <dl id="l_dimen">
  <dt><b>dimen[7] = [1,1,1,1,1,1,1] [integer array, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dimen' Line='dimen[7] = [1,1,1,1,1,1,1] [integer array, min=1, max=INDEF]' -->
  <dd>The length of each axis.
  </dd>
  </dl>
  <dl id="l_datatype">
  <dt><b>datatype = <span style="font-family: monospace;">"real"</span> [string, allowed values: real | integer | short]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datatype' Line='datatype = "real" [string, allowed values: real | integer | short]' -->
  <dd>Type of data in the input file.
  The data types currently supported are 
  single-precision real (4-byte), integer (4-byte), and short integer (2-byte).
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0 [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0 [integer, min=0, max=INDEF]' -->
  <dd>The number of bytes to be skipped at the beginning of the input file.
  The value passed to 'offset' must be divisible by two.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Suppose you have an STSDAS table containing a single column of real data
  starting 112 bytes after the beginning of the file.
  You can convert the table to an image using 'naxis = 1',
  setting 'dimen' to the number of rows, and setting 'offset = 112'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  to&gt; rbinary spec.tab spec.imh 1
  </pre></div>
  <p>
  2.  Suppose <span style="font-family: monospace;">"f.dat"</span> contains single-precision floating-point data
  in a 45 x 80 pixel array.
  You can create an image <span style="font-family: monospace;">"f.hhh"</span> from that file with the following command.
  Note how we're giving the values of the array parameter 'dimen'.
  It does appear to be necessary to use compute mode rather than command mode
  in order to give the dimensions on the command line.
  </p>
  <div class="highlight-default-notranslate"><pre>
  to&gt; rbinary "f.dat" "f.hhh" 2 dimen[1]=45 dimen[2]=80 \
  &gt;&gt;&gt;   datatype="real" offset=0
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  None known.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
