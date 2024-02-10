.. _acefilter:

acefilter: filter catalogs and object masks
===========================================

**Package: ace**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  acefilter images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images with catalogs or object masks to be filtered.  The images
  may be single images or multi-extension format (MEF) files.
  </dd>
  </dl>
  <dl id="l_icatalogs">
  <dt><b>icatalogs = <span style="font-family: monospace;">"!catalog"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icatalogs' Line='icatalogs = "!catalog"' -->
  <dd>Input list of catalogs to be filtered.  The list must match the list of
  input images.  Keyword pointers and substitution patterns may be used in
  addtion to any other IRAF list format.  The catalog need not have been
  produced by ACE and may be any format supported by the <b>tables</b> package.
  However, if a filtered object mask is to be produced the catalog must
  contain a field, specified by the <i>catomid</i> parameter, with the object
  mask identification numbers.
  </dd>
  </dl>
  <dl id="l_ocatalogs">
  <dt><b>ocatalogs = <span style="font-family: monospace;">"+new_cat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ocatalogs' Line='ocatalogs = "+new_cat"' -->
  <dd>Output list of filtered catalogs.  The list must either be empty to
  select no catalog output or match the list of input images.  Keyword
  pointers and substitution patterns may be used in addition to any other
  IRAF list format.  Extensions will be supplied if needed.  MEF input
  images and catalogs will produce MEF binary table catalogs with matching
  extension names.
  </dd>
  </dl>
  <dl id="l_objmasks">
  <dt><b>objmasks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objmasks' Line='objmasks = ""' -->
  <dd>Output list of filtered object masks.  The list must either be empty to
  select no object mask output or match the list of input images.  Keyword
  pointers and substitution patterns may be used in addition to any other
  IRAF list format.  Extensions will be supplied if needed.  MEF input
  images will produced MEF binary table mask files with matching extension
  names.  To produce an output mask an input mask must exist and be
  specified by the <span style="font-family: monospace;">"OBJMASK"</span> keyword in the catalog header or the image
  header (in that order).
  </dd>
  </dl>
  <dl id="l_catfilter">
  <dt><b>catfilter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catfilter' Line='catfilter = ""' -->
  <dd>Catalog filter expression.  If no expression is given then all input
  catalog records are selected.  An expression must evaluate to a boolean
  value.  Operands are case sensitive catalog field names.  Field names
  are those defined by the <b>tables</b> package.  In particular, simple
  text fields may be used as input catalogs and the field names are
  <span style="font-family: monospace;">"c1"</span>, <span style="font-family: monospace;">"c2"</span>, etc.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT"' -->
  <dd>List of output log files.  The list may be empty.  Output is appended to
  existing files.  The special name <span style="font-family: monospace;">"STDOUT"</span> may be used for output to the
  standard output (terminal or redirection output).
  </dd>
  </dl>
  <dl id="l_extnames">
  <dt><b>extnames = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extnames' Line='extnames = ""' -->
  <dd>List of extension name patterns for MEF files.  Note the patterns must
  match the entire name.
  </dd>
  </dl>
  <dl id="l_omtype">
  <dt><b>omtype = <span style="font-family: monospace;">"all"</span> (all|numbers|boolean|bnumbers|bboolean)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omtype' Line='omtype = "all" (all|numbers|boolean|bnumbers|bboolean)' -->
  <dd>Type of output object mask numbers.  All types use a value of zero for
  background pixels.  In all masks except the boolean masks, values up
  to 10 are used for bad and flagged pixels and above 10 are used for
  objects. A <span style="font-family: monospace;">"boolean"</span> mask uses values of 1 for all non-background pixels.
  A <span style="font-family: monospace;">"numbers"</span> mask uses the detection number for each object.  The
  <span style="font-family: monospace;">"all"</span> type adds bit flags to the detection number for boundary, grown,
  and split pixels.  The <span style="font-family: monospace;">"bnumbers"</span> and <span style="font-family: monospace;">"bboolean"</span> only mark boundary
  pixels and set interior detection pixels to zero.  Note that for
  later evaluations using the object segmentations the type must be
  <span style="font-family: monospace;">"all"</span>.
  </dd>
  </dl>
  <dl id="l_catomid">
  <dt><b>catomid = <span style="font-family: monospace;">"NUM"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catomid' Line='catomid = "NUM"' -->
  <dd>Catalog field containing the object mask identification number for
  filtering object masks.  This is only used when outputing a filtered
  object mask.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Write output catalog and object mask names to the image header under
  the keywords <span style="font-family: monospace;">"CATALOG"</span> and <span style="font-family: monospace;">"OBJMASK"</span>?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task filters catalogs and object masks by selecting records and
  object mask identification numbers for catalog records satisfying a
  filter expression.  Input images and catalogs are required.  The input
  image is used for extension names, keyword references, and object mask
  matching.
  </p>
  <p>
  The input catalog is normally produced by an <b>ace</b> package but this
  task may be used with any catalog supported by the <b>tables</b> package.
  The only requirement on a catalog is that in order to filter object masks
  it must contain a field with the object mask identification numbers.  Since
  the <b>ace</b> cataloging tasks allow renaming and fields created using
  functions and expressions, the user must use field names as they appear
  in the catalog.  The task <b>tlcol</b> may be used to check the field
  names.  The field names used in the filter expression and catalog
  object identification selection are case sensitive even though
  <b>tables</b> package tasks may not be.
  </p>
  <p>
  The heart of this task is the filter expression specified by the
  <i>catfilter</i> expression.  Normally an expression is specified though a
  null string, which selects all records, may be useful for some purposes.
  For general information on expressions see the help topic <i>expressions</i>.
  The operands in the expression are catalog field names.  The functions
  provided for output catalog fields in <i>ace</i> may be used in filter
  expressions.  The filter expresion, if one is given, must evaluate to a
  boolean value.
  </p>
  <p>
  An output filtered object mask is produced when an output object mask file
  name is specified, possibly through a keyword reference, and an existing
  object mask is defined by the <span style="font-family: monospace;">"OBJMASK"</span> keyword in the input catalog or
  input image (in that order).  A filtered object mask means a mask with only
  the object mask numbers, as given by the catalog field with name specified
  by the <i>catomid</i> parameter, for the catalog records matching the filter.
  Input object mask numbers for bad pixels and flagged pixels with values up
  to 10 are also included in the output object mask.
  </p>
  <p>
  An output mask type is specified by the <i>omtype</i> parameter.
  The typ allows using this task might to convert an object mask to
  a different with or without filtering.
  </p>
  <p>
  The <i>update</i> parameter is provided to allow filtering catalogs and
  object masks without resetting the image header keywords used by
  default in other tasks; e.g. <b>acedisplay</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  acecatalog, acetvmark, tables, expressions
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
