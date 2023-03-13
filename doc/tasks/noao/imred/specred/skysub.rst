.. _skysub:

skysub: Sky subtract extracted multispec spectra
================================================

**Package: specred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  skysub input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input multispec spectra to sky subtract.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output sky subtracted spectra.  If no output is specified then
  the output replaces the input spectra.
  </dd>
  </dl>
  <dl id="l_objaps">
  <dt><b>objaps = <span style="font-family: monospace;">""</span>, objbeams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objaps' Line='objaps = "", objbeams = ""' -->
  <dd>Object aperture and beam numbers.  An empty list selects all aperture
  or beam numbers.  Only the selected apertures are sky subtracted.
  Other apertures are left unmodified.  Note that it is valid to include
  the sky apertures in the object selection which results in residual
  sky spectra after subtraction by a mean sky.
  </dd>
  </dl>
  <dl id="l_skyaps">
  <dt><b>skyaps = <span style="font-family: monospace;">""</span>, skybeams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyaps' Line='skyaps = "", skybeams = ""' -->
  <dd>Sky aperture and beam numbers.  An empty list selects all aperture or
  beam numbers.
  </dd>
  </dl>
  <dl id="l_skyedit">
  <dt><b>skyedit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyedit' Line='skyedit = yes' -->
  <dd>Edit the sky spectra?  If yes the sky spectra are graphed using the
  task <b>specplot</b> and the user may delete contaminated sky spectra with
  the <span style="font-family: monospace;">'d'</span> key and exit with <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl id="l_combine">
  <dt><b>combine = <span style="font-family: monospace;">"average"</span> (average|median|sum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='combine' Line='combine = "average" (average|median|sum)' -->
  <dd>Option for combining pixels at the same dispersion coordinate after any
  rejection operation.  The options are to compute the  <span style="font-family: monospace;">"average"</span>, <span style="font-family: monospace;">"median"</span>,
  or <span style="font-family: monospace;">"sum"</span> of the pixels.  The median uses the average of the two central
  values when the number of pixels is even.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = <span style="font-family: monospace;">"none"</span> (none|minmax|avsigclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = "none" (none|minmax|avsigclip)' -->
  <dd>Type of rejection operation performed on the pixels which overlap at each
  dispersion coordinate.  The algorithms are discussed in the
  DESCRIPTION section.  The rejection choices are:
  <div class="highlight-default-notranslate"><pre>
       none - No rejection
     minmax - Reject the nlow and nhigh pixels
  avsigclip - Reject pixels using an averaged sigma clipping algorithm
  </pre></div>
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = no' -->
  <dd>Scale the sky spectra by the mode?
  </dd>
  </dl>
  <dl id="l_saveskys">
  <dt><b>saveskys = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='saveskys' Line='saveskys = yes' -->
  <dd>Save the sky spectra?  If no then the mean sky spectra will be deleted after
  sky subtraction is completed.  Otherwise a one dimensional image with
  the prefix <span style="font-family: monospace;">"sky"</span> and then the output name is created.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>Logfile for making a record of the sky subtraction operation.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task selects a subset of aperture spectra from a multispec
  format image, called sky spectra though they could be anything,
  and combines them into a master spectrum which is subtracted
  from another subset of spectra called the objects.  Options include
  saving the master sky spectrum and reviewing the selected sky spectra
  graphically and deleting some of them.
  </p>
  <p>
  The sky apertures are selected using the aperture and beam numbers
  defined during extraction (see the <b>apextract</b> package).  In
  some applications the beam numbers are used to code object and sky
  apertures and selection by beam number is quite easy.  Otherwise one
  must list the aperture numbers explicitly.
  </p>
  <p>
  The object apertures are also selected using an aperture and beam
  number list.  Spectra not selected to be objects are not modified
  by the sky subtraction.  Note that it is perfectly valid to include
  the sky spectra in the object list to produce residual sky spectra.
  </p>
  <p>
  When interactively editing the sky spectra the task <b>specplot</b>
  is used.  To delete a spectrum type <span style="font-family: monospace;">'d'</span>.  To undelete the last deleted
  spectrum type <span style="font-family: monospace;">'e'</span>.  When finished type <span style="font-family: monospace;">'e'</span>.
  </p>
  <p>
  The sky spectra are combined using one of combining and rejection options from
  the task <b>scombine</b> except for the option <span style="font-family: monospace;">"none"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To median and subtract apertures 1,10,15,20 from all apertures:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; skysub obj010.ms out=skysub010.ms skyaps="1,10,15,20"
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  specplot, scombine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
