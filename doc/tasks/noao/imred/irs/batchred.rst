.. _batchred:

batchred: Batch processing of IIDS/IRS spectra
==============================================

**Package: irs**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  batchred
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  This script task has many parameters, but most are used as
  variables internal to the task and are not user parameters.
  There are 5 parameters having similar purposes: standard,
  sensfunc, bswitch, calibrate, and addsets. Each corresponds
  to the ONEDSPEC task of the same name and BATCHRED will generate
  the commands necessary to invoke those tasks if the associated
  parameter is set to yes (the default in all cases).
  </p>
  <dl id="l_standard">
  <dt><b>standard = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='standard' Line='standard = yes' -->
  <dd></dd>
  </dl>
  <dl id="l_sensfunc">
  <dt><b>sensfunc = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sensfunc' Line='sensfunc = yes' -->
  <dd></dd>
  </dl>
  <dl id="l_bswitch">
  <dt><b>bswitch = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bswitch' Line='bswitch = yes' -->
  <dd></dd>
  </dl>
  <dl id="l_calibrate">
  <dt><b>calibrate = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calibrate' Line='calibrate = yes' -->
  <dd></dd>
  </dl>
  <dl id="l_addsets">
  <dt><b>addsets = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='addsets' Line='addsets = yes' -->
  <dd></dd>
  </dl>
  <dl id="l_fnu">
  <dt><b>fnu = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnu' Line='fnu = no' -->
  <dd>This parameter is identical to the fnu parameter for CALIBRATE.
  </dd>
  </dl>
  <dl id="l_wave1">
  <dt><b>wave1 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wave1' Line='wave1 = 0.0' -->
  <dd>This parameter is identical to the wave1 parameter for BSWITCH.
  </dd>
  </dl>
  <dl id="l_wave2">
  <dt><b>wave2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wave2' Line='wave2 = 0.0' -->
  <dd>This parameter is identical to the wave2 parameter for BSWITCH.
  </dd>
  </dl>
  <dl id="l_subset">
  <dt><b>subset = 32767</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subset' Line='subset = 32767' -->
  <dd>This parameter is identical to the subset parameter for BSWITCH.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Through a question and answer session, a series of commands to
  ONEDSPEC is generated which are then processed as a batch job
  to reduce <span style="font-family: monospace;">"typical"</span> spectra from the IIDS and IRS spectrographs.
  </p>
  <p>
  By setting the appropriate hidden parameters, the user may
  <span style="font-family: monospace;">"turn off"</span> command generation for any of the possible tasks.
  </p>
  <p>
  A script task is generated having the name <span style="font-family: monospace;">"process.cl"</span> which is
  submitted to the CL as the final command of BATCHRED.
  All terminal output which would normally appear during the course
  of running each of the individual tasks is redirected to a log file
  (default=ttylog).
  </p>
  <p>
  After the script has been generated, the user may suppress running
  the processing task. The script file remains on disk so that subsequent
  cases may be appended, such as when
  several independent runs of data are to be processed in one
  stream (e.g. several nights of data, each to be reduced separately).
  </p>
  <p>
  The questions which are asked are described below:
  </p>
  <p>
  <span style="font-family: monospace;">"Root name for spectra file names:"</span> This is the input root file name
  for all spectra which will be run through STANDARD and BSWITCH.
  </p>
  <p>
  <span style="font-family: monospace;">"Root name for spectra to be created:"</span> This is the output root file
  name which all newly created spectra will use. It is also the
  input file name for tasks CALIBRATE and ADDSETS since these tasks
  operate on spectra created by BSWITCH.
  </p>
  <p>
  <span style="font-family: monospace;">"Starting record number for spectra to be created:"</span> All created spectra
  will have a suffix number starting with this value and incremented
  by one for each new spectrum created.
  </p>
  <p>
  <span style="font-family: monospace;">"File name to contain statistics information:"</span> This file will contain
  informative output from SENSFUNC and BSWITCH. (default=stats)
  </p>
  <p>
  <span style="font-family: monospace;">"File name to contain a log of terminal output:"</span> All tasks talk back
  to let you know how things are proceding. The backtalk is saved
  in this file. (default=ttylog)
  </p>
  <p>
  <span style="font-family: monospace;">"File name for output from STANDARD and input to SENSFUNC:"</span> Just
  what it says. (default=std)
  </p>
  <p>
  <span style="font-family: monospace;">"Record string to process:"</span> The spectra are assumed to be representable
  by strings (try <span style="font-family: monospace;">"help ranges"</span> for details on the formats allowed).
  Both STANDARD and BSWITCH expect ranges of spectral record numbers
  which are appended to the root given in answer to the first question
  above. This question is asked repeatedly so that you can enter as
  many strings of spectra as you like and is ended by hitting return
  without entering a value. There is a short delay after entering
  each string of records while a check is made to verify that all
  your spectra actually exist.
  </p>
  <p>
  <span style="font-family: monospace;">"Standard star name:"</span> For each record string STANDARD expects
  the name of the standard star observed, but it must be given in
  a manner acceptable to STANDARD. (see STANDARD and LCALIB for
  more details).
  </p>
  <p>
  <span style="font-family: monospace;">"Use weighted averages:"</span> If answered yes, then SENSFUNC and BSWITCH
  will use their weighted averaging schemes.
  </p>
  <p>
  <span style="font-family: monospace;">"Apply magnitude fudging:"</span> If answered yes, then SENSFUNC will 
  use its <span style="font-family: monospace;">"fudge"</span> option. (see SENSFUNC)
  </p>
  <p>
  <span style="font-family: monospace;">"Solve for grey additive extinction constant:"</span> If answered yes, then
  SENSFUNC will solve for this value.
  </p>
  <p>
  <span style="font-family: monospace;">"File name for sensitivity image file:"</span> This will be the root name
  for the output sensitivity spectra from SENSFUNC.
  </p>
  <p>
  At anytime during the processing phase, you can inquire about the
  progress by listing the latest contents of the file <span style="font-family: monospace;">"ttylog"</span>
  either by <span style="font-family: monospace;">"type ttylog"</span> or by <span style="font-family: monospace;">"tail ttylog"</span>. The latter command
  lists the last 12 lines of the file.
  </p>
  <p>
  Be sure to have all your record strings, standard star names,
  and options well planned and written down so that you can enter
  the answers correctly. The batch reductions are not overly
  tolerant of incorrect entries although some preliminary checks
  are performed during the entry process.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following invokes the batch reductions using all task options;
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; batchred
  </pre></div>
  <p>
  The following inhibits the STANDARD and SENSFUNC tasks which must have
  been run previously. This is equivalent to the IPPS <span style="font-family: monospace;">"autoreduce"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; batchred standard- sensfunc-
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If you make an error while entering the requested information, there
  is no way to effect repairs other than to (1) start all over, or (2) edit
  the generated script file <span style="font-family: monospace;">"process.cl"</span> using the system editor.
  </p>
  <p>
  If a task encounters an irrecoverable error, the background job
  hangs until you kill it using <span style="font-family: monospace;">"kill N"</span> where N is the job number.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkscript, standard, sensfunc, bswitch, calibrate, addsets
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
