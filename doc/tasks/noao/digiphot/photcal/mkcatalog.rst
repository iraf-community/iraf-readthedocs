.. _mkcatalog:

mkcatalog: Type in a standard star catalog or observations file
===============================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkcatalog catalog
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_catalog">
  <dt><b>catalog</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalog' Line='catalog' -->
  <dd>The name of the new output catalog to be created or a previously existing
  catalog to be edited.
  </dd>
  </dl>
  <dl id="l_review">
  <dt><b>review = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='review' Line='review = no' -->
  <dd>Review any pre-existing entries?
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Verify each new entry?
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = yes' -->
  <dd>Enter edit mode after entering all the values?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKCATALOG is a script task which permits the user to create or edit
  the catalog <i>catalog</i>, usually but not necessarily, a standard star
  catalog.  MKCATALOG has two modes of operation, entry mode and edit mode.
  In entry mode MKCATALOG prompts the user for input.
  In edit mode MKCATALOG calls up the default editor specified by
  the IRAF environment variable <i>editor</i>.
  </p>
  <p>
  If <i>catalog</i> is a new catalog, MKCATALOG prompts the user for 
  the name of the object id column, the names of the data columns,
  the names of the error columns (these are optional), and the widths
  of the columns. Typing the end-of-file character &lt;EOF&gt;,
  usually ^Z or ^D, terminates column definition
  and places the user in entry mode.
  In entry mode MKCATALOG prompts the user for the object ids and data values.
  Entering carriage return, &lt;CR&gt;, after MKCATALOG prompts for a new object id
  writes a blank line to the output catalog.
  Entering &lt;CR&gt; after MKCATALOG prompts for any other column
  value writes INDEF (the IRAF undefined value) in that column of the
  output catalog.
  Entry mode is terminated by typing &lt;EOF&gt; in response to a query for
  a new object id.  The user may verify each new
  entry by setting the parameter <i>verify</i> to <span style="font-family: monospace;">"yes"</span>.
  </p>
  <p>
  Each new catalog created by MKCATALOG has an associated format
  description file listing the column names and numbers associations defined by
  the user. This file, referenced by its parent catalog name, can be
  used as input to the MKCONFIG task.
  The actual name of the format description file on disk is constructed by
  prepending the catalog name <i>catalog</i> with the string <span style="font-family: monospace;">"f"</span> and
  appending the string <span style="font-family: monospace;">".dat"</span>. For example if a new catalog 
  called <span style="font-family: monospace;">"UBVcat"</span> is created by MKCATALOG, a format description
  file called <span style="font-family: monospace;">"fUBVcat.dat"</span> will also be created. Any pre-existing format
  description file of that name, which does not have an associated catalog
  file, will be deleted.
  </p>
  <p>
  If the catalog <i>catalog</i> exists and was created with MKCATALOG,
  MKCATALOG reads
  the number of columns, the column names, and column widths from the
  header of the catalog, and enters entry mode positioned at the end
  of the file. If the parameter <i>review</i> = <span style="font-family: monospace;">"yes"</span>, then the user can
  review and verify existing catalog entries before entering new ones.
  When entry mode is terminated MKCATALOG enters edit mode
  in the usual way. 
  </p>
  <p>
  If <i>catalog</i> exists but was not created with MKCATALOG, MKCATALOG
  enters edit mode immediately.
  </p>
  <p>
  If <i>catalog</i> is a standard star catalog, the user should be aware
  that the object ids he/she has typed in, are those against which the object
  ids in the standard star observations files will be matched by the
  fitting task FITPARAMS.
  Normally the user is expected to edit the object ids in the standard
  star observations
  files to match those in the standard star catalog.
  For example, the PHOTCAL APPHOT/DAOPHOT pre-processor tasks MKNOBSFILE
  and MKOBSFILE, produce observations files whose object ids
  are of the form <span style="font-family: monospace;">"field-#"</span>, where <span style="font-family: monospace;">"field"</span> is the name
  of the observed field and <span style="font-family: monospace;">"#"</span> is a sequence number, which is defined
  only if there is more than one observed star in the field.
  In this scheme the id of the  the fourth observed star in the field <span style="font-family: monospace;">"M92"</span>
  is <span style="font-family: monospace;">"M92-4"</span>. If this star is actually the standard star <span style="font-family: monospace;">"IX-10"</span> in
  <i>catalog</i>, the user must change the object id in the observations file
  to <span style="font-family: monospace;">"IX-10"</span>. Alternatively the user can set up the naming
  convention in <i>catalog</i> itself, to match  the naming
  convention of MKNOBSFILE
  or MKOBSFILE by assigning the standard stars names like <span style="font-family: monospace;">"field-#"</span> and
  subsequently measuring the standard stars in the same order as they
  appear in the catalog.  In this scheme star, <span style="font-family: monospace;">"M92-4"</span> in
  the observations file would also be <span style="font-family: monospace;">"M92-4"</span> in the standard star 
  catalog, and no editing would be required. This technique is most useful
  for standard sequences in clusters.
  </p>
  <p>
  THE MKCATALOG TASK AND THE ENTIRE PHOTCAL PACKAGE IMPOSE THE FOLLOWING
  RESTRICTIONS
  ON BOTH STAR ID NAMES AND THE COLUMN ID NAMES THAT MAY BE ASSIGNED, AND ON
  THE FORMAT OF EACH FIELD.
  </p>
  <p>
  Object id names must be composed of characters in the set [a-z,A-Z,0-9,+,-,_].
  Other characters may be included as part of the user id, but 
  will be ignored by the PHOTCAL id matching code. Object id names are
  case insensitive. To the id matching code the name <span style="font-family: monospace;">"BD+61_305"</span> is the
  same as <span style="font-family: monospace;">"bd+61_305"</span>.
  </p>
  <p>
  Column names must be composed of characters in the set [a-z,A-Z,0-9]
  and the first character of the column name must be a letter of the alphabet.
  This means for example, that an individual column cannot be assigned the
  name <span style="font-family: monospace;">"B-V"</span>, since <span style="font-family: monospace;">"B-V"</span> will be interpreted as an arithmetic expression not
  as a variable, by the PHOTCAL equation parsing routines.
  <span style="font-family: monospace;">"B-V"</span> may be replaced with something like <span style="font-family: monospace;">"BV"</span> or <span style="font-family: monospace;">"BMV"</span>.
  MKCATALOG will complain if the user tries to enter an illegal column name.
  Column names are case sensitive. Column <span style="font-family: monospace;">"BV"</span> is not the same as 
  column <span style="font-family: monospace;">"bv"</span>.
  </p>
  <p>
  Whitespace  is not permitted in either the object ids or in the column
  values. MKCATALOG will truncate any id or column value at the first
  whitespace encountered. The column widths entered by the user are used
  solely to determine
  the maximum width of each field (excess characters will be truncated)
  and to align the columns for ease of
  visual inspection by the user. The column widths are not used by the 
  PHOTCAL catalog reading code.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a new standard star catalog containing the 3 photometric indices
  V, B-V, and U-B and their respective errors. Note that MKCATALOG supplies
  default names of the form <span style="font-family: monospace;">"error(name)"</span> for the error columns where <span style="font-family: monospace;">"name"</span>
  is the name of the previous column. Users are strongly urged to use the
  default names since they simplify the use of the statistical weighting
  scheme in the FITPARAMS task. If no error information is available
  error column entry can be skipped by typing &lt;-&gt; in response to the query
  for an error column name.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkcatalog UBVcat
  
      and shown below, note that the end-of-file character &lt;EOF&gt; is
      actually ^Z in this case
  
  Enter the id column name (name, &lt;CR&gt;=ID, &lt;EOF&gt;=quit entry):
      Enter width of id column (width, &lt;CR&gt;=15):
  Enter a name for column 2 (name, &lt;CR&gt;=COL2, &lt;EOF&gt;=quit entry): V
      Enter width of column 2 (width, &lt;CR&gt;=10):
  Enter a name for error column 3 (name, &lt;CR&gt;=error(V), &lt;-&gt;=skip):
      Enter width of column 3 (width, &lt;CR&gt;=10):
  Enter a name for column 4 (name, &lt;CR&gt;=COL4, &lt;EOF&gt;=quit entry): BV
      Enter width of column 4 (width, &lt;CR&gt;=10):
  Enter a name for error column 5 (name, &lt;CR&gt;=error(BV), &lt;-&gt;=skip):
      Enter width of column 5 (width, &lt;CR&gt;=10):
  Enter a name for column 6 (name, &lt;CR&gt;=COL6, &lt;EOF&gt;=quit entry): UB
      Enter width of column 6 (width, &lt;CR&gt;=10):
  Enter a name for error column 7 (name, &lt;CR&gt;=error(UB), &lt;-&gt;=skip):
      Enter width of column 7 (width, &lt;CR&gt;=10):
  Enter a name for column 8 (name, &lt;CR&gt;=COL8, &lt;EOF&gt;=quit entry): ^Z
  
  Catalog UBVcat in file UBVcat has 7 columns
          Column 1:  ID
          Column 2:  V
          Column 3:  error(V)
          Column 4:  BV
          Column 5:  error(BV)
          Column 6:  UB
          Column 7:  error(UB)
  
  
  
  
  </pre></div>
  <p>
  2. Add new entries to the file created in example 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkcatalog UBVcat
  
  
  
  </pre></div>
  <p>
  3. Edit an existing catalog created with a foreign program.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkcatalog VRI.usr
  
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The longest line permitted by an editor varies from editor to
  editor. Users should be aware that it may not be possible to use
  edit mode on very long text lines.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  photcal$catalogs/README,mknobsfile,mkobsfile,mkconfig
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
