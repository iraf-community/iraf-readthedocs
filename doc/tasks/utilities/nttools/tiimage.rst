.. _tiimage:

tiimage: Insert images into rows of a 3-D table.
================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tiimage input outtable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task performs the inverse operation of task tximage: it inserts one or 
  more images into rows of a 3-D table  The input may be a filename template, 
  including wildcard characters, or the name of a file (preceded by an @ sign) 
  containing image names.  The output is a single 3-D table name.
  Each image in the input list is inserted as an array into a single cell at 
  the specified row in the output table. Any dimensionality information existent
  in the input image is lost in the process, that is, the image will be always
  inserted as a 1-D array, regardless of its number of axis.
  </p>
  <p>
  If the output table exists, insertion will be done in place. Alternatively, 
  the task can create a 3-D table from information taken either from a template 
  3-D table, or, if this table is not supplied, from the input images themselves. 
  This task supports a column selector in table names. This selector may be 
  used to select a single column in the table. If no selector is used, all 
  columns will be processed. Type 'help selectors' to see a description of 
  the selector syntax. 
  </p>
  <p>
  If the output table exists, insertion may take place in two ways. If the
  output table name contains a column selector that selects a single column
  in the table, all input images will be inserted in that column, starting
  at the row pointed by task parameter <span style="font-family: monospace;">"row"</span>. 
  If <span style="font-family: monospace;">"row"</span> is negative or INDEF the task will look for the ORIG_ROW
  keyword in the image header and use that keyword value for row number.
  The second mode of insertion in an existing table is used if no matching
  column selector is found in the output table name. In this case the task
  will look for the columnar information written in the input image header by 
  task tximage, and use that information to place the image in the proper 
  column. If no columnar information exists in the header, or if the column 
  name in there does not match any column in the output table, the image is 
  skipped and the user warned. The <span style="font-family: monospace;">"row"</span> parameter processing works the same 
  way in this second mode.
  </p>
  <p>
  If the output table does not exist, the task will look for a template table
  where to take column information from. If the template exists, the insertion
  operation will be performed in an analogous way as above. Notice that the
  result may be a single-column table if the template has a valid (matching)
  column selector in its name, or a sparse table if not, because only the 
  actual input images will be stored in an otherwise empty table (the template 
  data is not copied into the output, only the column descriptors).
  </p>
  <p>
  If the template is missing, the task will attempt to retrieve columnar
  information from the input image headers and build the output table with
  enough columns and rows to fit all images in the list. Only images that
  have columnar information in their headers can be processed, though. If
  no images are found with the proper header keywords, no output takes place.
  </p>
  <p>
  NOTE: Both the output and template table names must always be supplied 
  complete, including their extension. Otherwise the task may get confused 
  on the existence of an already existing table.
  </p>
  <p>
  The column matching criterion is based on the column name. An error results 
  when data types in input image and output column do not agree.
  </p>
  <p>
  If the maximum array size in a target column in the output 3-D table is
  larger than the number of pixels in the input image, the array will be filled 
  up starting from its first element, and the empty elements at the end will 
  be set to INDEF. If the maximum array size is smaller than the number of 
  pixels, insertion begins by the first pixel up to the maximum allowable size, 
  the remaining pixels being ignored.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [image name list/template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [image name list/template]' -->
  <dd>A list of one or more images to be inserted.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [table name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [table name]' -->
  <dd>Name of 3-D output table, including extension. No support exists for 
  <span style="font-family: monospace;">"STDOUT"</span> (ASCII output).
  </dd>
  </dl>
  <dl>
  <dt><b>(template = <span style="font-family: monospace;">""</span>) [table name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(template = "") [table name]' -->
  <dd>Name of 3-D table to be used as template when creating a new output table.
  </dd>
  </dl>
  <dl>
  <dt><b>(row = INDEF) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(row = INDEF) [int]' -->
  <dd>Row where insertion begins. If set to INDEF or a negative value, the row
  number will be looked for in the input image header.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Display names as files are processed ?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Insert images into a 3-D table at column named FLUX:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tiimage flux*.hhh "otable.tab[c:FLUX]"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The output and template table names must be supplied in full, including 
  the extension (e.g. <span style="font-family: monospace;">".tab"</span>). If the output table name is not typed in full, 
  the task will create a new table in place of the existing one, with only 
  the rows actually inserted. This behavior relates to the way the underlying 
  <span style="font-family: monospace;">"access"</span> routine in IRAF's fio library works.
  </p>
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
  tximage, selectors
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
