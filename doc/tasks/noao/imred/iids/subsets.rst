.. _subsets:

subsets: Subtract pairs in strings of spectra
=============================================

**Package: iids**

.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <b>ccdred</b> package groups observation into subsets.
  The image header parameter used to identify the subsets is defined
  in the instrument translation file (see help for <b>instruments</b>).
  For example to select subsets by the header parameter <span style="font-family: monospace;">"filters"</span> the
  instrument translation file would contain the line:
  </p>
  <p>
  	subset	filters
  </p>
  <p>
  Observations are generally grouped into subsets based on a common
  instrument configuration such as a filter, aperture mask,
  grating setting, etc.  This allows combining images from several
  different subsets automatically and applying the appropriate
  flat field image when processing the observations.  For example
  if the subsets are by filter then <b>flatcombine</b> will search
  through all the images, find the flat field images (based on the
  CCD type parameter), and combine the flat field images from
  each filter separately.  Then when processing the images the
  flat field with the same filter as the observation is used.
  </p>
  <p>
  Each subset is assigned a short identifier.  This is listed when
  using <b>ccdlist</b> and is appended to a root name when combining
  images.  Because the subset parameter in the image header may be
  any string there must be a mapping applied to generate unique
  identifiers.  This mapping is defined in the file given by
  the package parameter <i>ccdred.ssfile</i>.  The file consists of
  lines with two fields (except that comment lines may be included
  as a line by itself or following the second field):
  </p>
  <p>
  	'subset string'	subset_id
  </p>
  <p>
  where the subset string is the image header string and the subset_id is
  the identifier.  A field must be quoted if it contains blanks.  The
  user may create this file but generally it is created by the tasks.  The
  tasks use the first word of the subset string as the default identifier
  and a number is appended if the first word is not unique.  The
  following steps define the subset identifier:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>Search the subset file, if present, for a matching subset string and
  use the defined subset identifier.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>If there is no matching subset string use the first word of the
  image header subset string and, if it is not unique,
  add successive integers until it is unique.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd>If the identifier is not in the subset file create the file and add an
  entry if necessary.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The subset file is <span style="font-family: monospace;">"subsets"</span> (the default).  The subset parameter is
  translated to <span style="font-family: monospace;">"f1pos"</span> in the image header (the old NOAO CCD parameter)
  which is an integer filter position.  After running a task, say
  <span style="font-family: monospace;">"ccdlist *.imh"</span> to cause all filters to be checked, the subset file contains:
  </p>
  <div class="highlight-default-notranslate"><pre>
  <span style="font-family: monospace;">'2'</span>        2
  <span style="font-family: monospace;">'5'</span>        5
  <span style="font-family: monospace;">'3'</span>        3
  </pre></div>
  <p>
  The order reflects the order in which the filters were encountered.
  Suppose the user wants to have more descriptive names then the subset
  file can be created or edited to the form:
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Sample translation file.
  <span style="font-family: monospace;">'2'</span>        U
  <span style="font-family: monospace;">'3'</span>        B
  <span style="font-family: monospace;">'4'</span>        V
  </pre></div>
  <p>
  (This is only an example and does not mean these are standard filters.)
  </p>
  <p>
  2. As another example suppose the image header parameter is <span style="font-family: monospace;">"filter"</span> and
  contains more descriptive strings.  The subset file might become:
  </p>
  <div class="highlight-default-notranslate"><pre>
  'GG 385 Filter' GG
  'GG 495 Filter' GG1
  'RG 610 Filter' RG
  'H-ALPHA'       H_ALPHA
  </pre></div>
  <p>
  In this case use of the first word was not very good but it is unique.
  It is better if the filters are encoded with the thought that the first
  word will be used by <b>ccdred</b>; it should be short and unique.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  instruments
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
