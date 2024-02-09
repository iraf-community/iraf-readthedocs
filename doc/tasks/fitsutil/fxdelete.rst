.. _fxdelete:

fxdelete: Delete FITS extensions in place
=========================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxdelete input_list groups
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>Can be a list of FITS filenames with or without extension number.
  </dd>
  </dl>
  <dl id="l_groups">
  <dt><b>groups = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groups' Line='groups = "" [string]' -->
  <dd>Specify the list of extensions to delete from the those files without 
  explicit extension number. This list is applied to all input files.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print each operation as it takes place?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Fdelete  will delete one or more FITS units in place from a
  Multiple extension file or a list of files.
  </p>
  <p>
  FITS extensions are numbered from zero -as the primary unit, with one as
  the first extension two as the second extension and so on.
  </p>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <p>
  Notice that if you delete the PHU (group zero), fxdelete will not create
  a dummy PHU on the modified file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Delete group 3 from input.fits.
  
          im&gt; fxdelete input.fits[3]
  
  2. To delete extensions 1,3,5 from input file g10.fits.
  
          im&gt; fxdelete g10.fits groups="1,3,5"
  
  3. Delete extensions. Notice that for those files without an extension, the
     group extension list applies.
  
          im&gt; fxdelete fa.fits,fb.fits[5],fc.fits groups="1,3,4"
  
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Fdelete does not accept EXTNAME or EXTVER values yet. Cannot delete PHU
  (group 0). 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy, fxheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'NOTES' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
