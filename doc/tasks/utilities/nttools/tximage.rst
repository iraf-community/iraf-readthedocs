.. _tximage:

tximage: Extract images from rows of 3-D tables.
================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tximage intable output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task extracts one or more 1-D images from cells of a 3-D table.
  The input may be a filename template, including wildcard characters, 
  or the name of a file (preceded by an @ sign) containing table names. 
  The output may be either a directory specification or a list of image names. 
  If the output is a list of images then there must be the same number of names 
  in the input and output lists, and the names are taken in pairs, one from 
  input and one from output.
  </p>
  <p>
  Images can be extracted only from a single column in the input table.
  That column must be designated by an appropriate column selector appended to 
  the table name. Type 'help selectors' to get more information on row/column 
  selector syntax.
  </p>
  <p>
  Row selectors may be used to select subsets of rows from the input table.
  If no row selector is used, all rows will be extracted, and the number
  of output images will be the number of rows in the input table.
  </p>
  <p>
  Since one input table may generate several output images, the task adopts
  the following naming scheme for these output images: their names are
  built by appending a suffix to the name given in parameter <span style="font-family: monospace;">"output"</span>.
  The suffix has the form <span style="font-family: monospace;">"_rXXXX"</span>, where XXXX stands for the row number 
  in the input table. The suffix is appended before the file name extension.
  The task recognizes as valid image name extensions the values <span style="font-family: monospace;">".??h"</span>,
  <span style="font-family: monospace;">".fits"</span> and <span style="font-family: monospace;">".fit"</span>. Any other extension is assumed to be part of the root
  file name. If only one row is extracted, no suffixing takes place.
  </p>
  <p>
  NOTE: Be careful when using a wildcard for the extension.
  If you have the files <span style="font-family: monospace;">"table.tab"</span> and <span style="font-family: monospace;">"table.lis"</span> in the current directory,
  for example, then the command <span style="font-family: monospace;">"tximage tab* test/"</span> would expand both files 
  to the subdirectory <span style="font-family: monospace;">"test"</span>.
  </p>
  <p>
  Basic column information describing the column where the image came from
  is written into the image header in the <span style="font-family: monospace;">"COLDATA"</span> keyword. This information
  can be used later by task 'tiimage' to re-insert the image into a cell of 
  a 3-D table.
  </p>
  <p>
  The task does not propagate array dimensionality when extracting arrays
  into images. If dimensionality information exists in the 3-D table, that 
  information is lost, that is, the table cell from the input table is written 
  as a structureless, plain 1-D image.
  </p>
  <p>
  The input row number is written to the header of the output image in
  keyword ORIG_ROW. This allows 'tiimage' to put the data back where 
  'tximage' got them from.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name list/template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name list/template]' -->
  <dd>A list of one or more tables to be expanded. A column selector selecting
  a single column is mandatory. Row selectors are supported as well.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name template]' -->
  <dd>Either a directory name or a list of output image names.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Display names of input and output files ?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Extract 1-D images from a column named FLUX from rows 11 to 13 of a 3-D 
  table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tximage "table.tab[c:FLUX][r:row=(11:13)]" image
  </pre></div>
  <p>
  This will generate three images named <span style="font-family: monospace;">"image_r0011"</span>, <span style="font-family: monospace;">"image_r0012"</span>
  and <span style="font-family: monospace;">"image_r0013"</span>.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by I. Busko.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tiimage, selectors
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
