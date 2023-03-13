.. _setimpars:

setimpars: Save/restore parameter sets for a particular image
=============================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  setimpars image restore update
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The image for which the daophot parameters are to be saved or restored.
  </dd>
  </dl>
  <dl id="l_restore">
  <dt><b>restore</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='restore' Line='restore' -->
  <dd>If restore = yes, parfile is <span style="font-family: monospace;">""</span>, and the file <span style="font-family: monospace;">"image.pars"</span> exists, SETIMPARS
  sets the current algorithm parameters by reading in the file <span style="font-family: monospace;">"image.pars"</span>. If
  parfile is not <span style="font-family: monospace;">""</span>, then restore is automatically assumed to be yes.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update' -->
  <dd>If update = yes, SETIMPARS saves the new current values of the DAOPHOT algorithm
  parameters in the file <i>image.pars</i> and any previously existing file of the same name is overwritten.
  </dd>
  </dl>
  <dl id="l_review">
  <dt><b>review = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='review' Line='review = no' -->
  <dd>Review and/or edit the values of the parameters in the parameter sets DATAPARS,
  FINDPARS, CENTERPARS, FITSKYPARS, PHOTPARS, and DAOPARS by calling up the EPAR
  task for each of the named parameter sets in turn?
  </dd>
  </dl>
  <dl id="l_parfile">
  <dt><b>parfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parfile' Line='parfile' -->
  <dd>The name of the input file containing the values of the DAOPHOT algorithm
  parameters to be restored. If defined <i>parfile</i> must have been written
  by SETIMPARS.  If parfile is null (<span style="font-family: monospace;">""</span>), SETIMPARS searches for a file named
  <i>image.pars</i> in the user's current directory. If no file is found, the
  DAOPHOT algorithm parameters are restored from the files <i>datapars</i>,
  <i>findpars</i>, <i>centerpars</i>, <i>fitskypars</i>, <i>photpars</i>, and
  <i>daopars</i>.
  </dd>
  </dl>
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the DATAPARS parameter values. Datapars must be
  a named DATAPARS parameter set file written by the EPAR task, or <span style="font-family: monospace;">""</span> in which
  case the default DATAPARS parameter set in the user's uparm directory is used.
  If the parameter <i>unlearn</i> is <span style="font-family: monospace;">"yes"</span> and datapars is <span style="font-family: monospace;">""</span>, DATAPARS is
  unlearned.
  </dd>
  </dl>
  <dl id="l_findpars">
  <dt><b>findpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='findpars' Line='findpars = ""' -->
  <dd>The name of the file containing the FINDPARS parameter values. Findpars
  must be a named FINDPARS parameter set file written by the EPAR task, or <span style="font-family: monospace;">""</span>
  in which case the default FINDPARS parameter set in the user's uparm
  directory is used. If the parameter <i>unlearn</i> is <span style="font-family: monospace;">"yes"</span> and findpars
  is <span style="font-family: monospace;">""</span>, FINDPARS is unlearned.
  </dd>
  </dl>
  <dl id="l_centerpars">
  <dt><b>centerpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='centerpars' Line='centerpars = ""' -->
  <dd>The name of the file containing the CENTERPARS parameter values.  Centerpars
  must be a named CENTERPARS parameter set file written by the EPAR task, or <span style="font-family: monospace;">""</span>
  in which case the default CENTERPARS parameter set in the user's uparm
  directory is used. If the parameter <i>unlearn</i> is <span style="font-family: monospace;">"yes"</span> and centerpars
  is <span style="font-family: monospace;">""</span>, CENTERPARS is unlearned.
  </dd>
  </dl>
  <dl id="l_fitskypars">
  <dt><b>fitskypars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitskypars' Line='fitskypars = ""' -->
  <dd>The name of the file containing the FITSKYPARS parameter values. Fitskypars
  must be a named FITSKYPARS parameter set file written by the EPAR task, or <span style="font-family: monospace;">""</span>
  in which case the default FITSKYPARS parameter set in the user's uparm
  directory is used. If the parameter <i>unlearn</i> is <span style="font-family: monospace;">"yes"</span> and fitskypars
  is <span style="font-family: monospace;">""</span>, FITSKYPARS is unlearned.
  </dd>
  </dl>
  <dl id="l_photpars">
  <dt><b>photpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photpars' Line='photpars = ""' -->
  <dd>The name of the file containing the PHOTPARS parameter values. Photpars must be
  a named PHOTPARS parameter set file written by the EPAR task, or <span style="font-family: monospace;">""</span> in which
  case the default PHOTPARS parameter set in the user's uparm directory is used.
  If the parameter <i>unlearn</i> is <span style="font-family: monospace;">"yes"</span> and photpars is <span style="font-family: monospace;">""</span>, PHOTPARS is
  unlearned.
  </dd>
  </dl>
  <dl id="l_daopars">
  <dt><b>daopars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='daopars' Line='daopars = ""' -->
  <dd>The name of the file containing the DAOPARS parameter values. Daopars must be a
  named DAOPARS parameter set file written by the EPAR task, or <span style="font-family: monospace;">""</span> in which case
  the default DAOPARS parameter set in the user's uparm directory is used. If the
  parameter <i>unlearn</i> is <span style="font-family: monospace;">"yes"</span> and daopars is <span style="font-family: monospace;">""</span>, DAOPARS is unlearned.
  </dd>
  </dl>
  <dl id="l_unlearn">
  <dt><b>unlearn = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='unlearn' Line='unlearn = no' -->
  <dd>Return the values of the parameters in the parameter sets DATAPARS, FINDPARS,
  CENTERPARS, FITSKYPARS, PHOTPARS, and DAOPARS to their default values?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SETIMPARS saves and restores the DAOPHOT task and algorithm parameters for the
  image <i>image</i>. On startup SETIMPARS initializes all the DAOPHOT package
  input and output coordinates and photometry file names, input and output images,
  and input and output plot files to their default values or <i>image</i> whichever
  is appropriate. Next SETIMPARS reads in the values of the algorithm parameters
  from <i>parfile</i> if it is defined, or from the file <i>image.pars</i> if it
  exists and <i>restore</i> is <span style="font-family: monospace;">"yes"</span>, or from the named parameter set files
  <i>datapars</i>, <i>findpars</i>, <i>centerpars</i>, <i>fitskypars</i>,
  <i>photpars</i>, and <i>daopars</i> if they exist, or from the default parameters
  sets in the user's uparm directory. If <i>unlearn</i> is <span style="font-family: monospace;">"yes"</span>, these default
  parameter sets are unlearned.
  </p>
  <p>
  If <i>review</i> is <span style="font-family: monospace;">"yes"</span>, the user can review and or edit the newly set
  algorithm parameters in DATAPARS, FINDPARS, CENTERPARS, FITSKYPARS, PHOTPARS,
  and DAOPARS using the IRAF EPAR task.
  </p>
  <p>
  If <i>update</i> is <span style="font-family: monospace;">"yes"</span>, SETIMPARS saves the new current values of the DAOPHOT
  algorithm parameters DATAPARS, FINDPARS, CENTERPARS, FITSKYPARS, PHOTPARS, and
  DAOPARS in the file <i>image.pars</i>. Any previously existing file of the same
  name is overwritten.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Save the current values of the daophot task and algorithm parameters for
  the image m92v.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; setimpars m92v no yes
  
      ... m92v parameters are saved in m92v.pars
  </pre></div>
  <p>
  2. Make some minor alterations in the current values of the m92v algorithm
  parameters and save the new parameters set.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; setimpars m92v no yes
  
      ... m92v parameters are saved in new version of m92v.pars
  </pre></div>
  <p>
  3. Begin work on the image m92b. Initialize the values of the daophot task
  and algorithm parameters for m92b using those stored for m92v. After doing
  some preliminary editing and reductions for m92b, save the parameters,
  and return to work on m92v.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; setimpars m92b yes no parfile=m92v.pars
  
      ... current parameters for m92v are set using saved
          m92v parameters
  
  da&gt; daoedit m92b
  
      ... edit the parameters as necessary for the new image
  
  da&gt; daofind m92b
  
      ... find the stars in m92b
  
  da&gt; phot m92b
  
      ... do the initial photometry for stars in m92b
  
  da&gt; setimpars m92b no yes
  
      ... current m92b parameters are saved in m92b.pars
  
  da&gt; setimpars m92v yes no
  
      ... m92v parameters are restored from m92v.pars
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  daoedit,datapars,findpars,centerpars,fitskypars,photpars,daopars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
