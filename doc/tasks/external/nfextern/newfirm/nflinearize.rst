.. _nflinearize:

nflinearize: Linearize NEWFIRM exposures
========================================

**Package: newfirm**

.. raw:: html

  <section id="s_usage___">
  <h3>Usage   </h3>
  <p>
  nflinearize input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input			</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input			' -->
  <dd>List of input NEWFIRM MEF files.  Files which have already been linearized
  are silently skipped.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output			</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output			' -->
  <dd>List, pattern, or expression defining output filenames for each input
  file. See <b>proctool.output</b> for a description of the various
  options.
  </dd>
  </dl>
  <dl id="l_coeffs">
  <dt><b>coeffs = <span style="font-family: monospace;">"parameter"</span> (parameter|exprdb|keyword|image)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coeffs' Line='coeffs = "parameter" (parameter|exprdb|keyword|image)' -->
  <dd>Coefficients
  </dd>
  </dl>
  <dl id="l_lin1">
  <dt><b>lin1, lin2, lin3, lin4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lin1' Line='lin1, lin2, lin3, lin4' -->
  <dd>Linearity coefficients for each NEWFIRM extension.  These parameters
  are only used when the <i>coeffs</i> parameter is <span style="font-family: monospace;">"parameter"</span>.  This
  allows easy user control.  The default values are
  <div class="highlight-default-notranslate"><pre>
  lin1 = -5.404E-6
  lin2 = -5.952E-6
  lin3 = -6.123E-6
  lin4 = -7.037E-6
  </pre></div>
  which were recommended in Nov. 2008.
  </dd>
  </dl>
  <dl id="l_linimage">
  <dt><b>linimage = <span style="font-family: monospace;">""</span>		</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linimage' Line='linimage = ""		' -->
  <dd>List of linearity coefficient images.  The images must be the same
  size as the NEWFIRM arrays and pixels are matched by pixel
  coordinates. The pixel values are the coefficient values for the
  linearization expression.  The list need not match the
  input list and the last coefficient image is used for longer input lists
  while extra coefficient images in the list are not used.  The typical
  usage would be a single MEF or one image for each extension.  The
  images are matched to the input by the IMAGEID keyword.  This
  parameter is only used with <i>coeffs</i> is <span style="font-family: monospace;">"image"</span>.
  </dd>
  </dl>
  <dl id="l_exprdb">
  <dt><b>exprdb = <span style="font-family: monospace;">"newfirm$exprdb.dat"</span> </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exprdb' Line='exprdb = "newfirm$exprdb.dat" ' -->
  <dd>Expression database.  This file is critical to the linearization
  operation because it defines the linearization expression used by
  this task.  It also contains many of the instrument parameters and
  recommended coefficients for NEWFIRM.  This file may be updated
  independently of this task if new linearization expressions and
  coefficients are recommended.  Users may copy the default file to
  their own directory, make modifications and reset this parameter.
  </dd>
  </dl>
  <dl id="l_list">
  <dt><b>list = no		</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='list' Line='list = no		' -->
  <dd>Verbose list output only?  This maps to the <span style="font-family: monospace;">"vlist"</span> output type
  described in <b>proctool.output</b>.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT"</span>	</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT"	' -->
  <dd>List of log files for log output.  The special value <span style="font-family: monospace;">"STDOUT"</span> may be
  used to write to the terminal.  The output is appending to any
  existing output.  This is described further in <b>proctool.output</b>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task applies a linearization expression to each input pixel to
  correct from measured counts to linear counts.  This task is based on
  the more general, and hence complex, task <b>nfproc</b>.  It simplifies
  the parameters and generates the recommended linearization
  expressions.
  </p>
  </section>
  <section id="s_expressions">
  <h3>Expressions</h3>
  <dl id="l_coeffs">
  <dt><b>coeffs = <span style="font-family: monospace;">"parameter"</span></b></dt>
  <!-- Sec='EXPRESSIONS' Level=0 Label='coeffs' Line='coeffs = "parameter"' -->
  <dd>%(lin(nflinearize.lin\I))
  </dd>
  </dl>
  <dl id="l_coeffs">
  <dt><b>coeffs = <span style="font-family: monospace;">"exprdb"</span></b></dt>
  <!-- Sec='EXPRESSIONS' Level=0 Label='coeffs' Line='coeffs = "exprdb"' -->
  <dd>%(lin(L\I))
  </dd>
  </dl>
  <dl id="l_coeffs">
  <dt><b>coeffs = <span style="font-family: monospace;">"keyword"</span></b></dt>
  <!-- Sec='EXPRESSIONS' Level=0 Label='coeffs' Line='coeffs = "keyword"' -->
  <dd>%(lin(lincoeff))
  </dd>
  </dl>
  <dl id="l_coeffs">
  <dt><b>coeffs = <span style="font-family: monospace;">"image"</span></b></dt>
  <!-- Sec='EXPRESSIONS' Level=0 Label='coeffs' Line='coeffs = "image"' -->
  <dd>%(lin($L))
  </dd>
  </dl>
  <p>
  The <span style="font-family: monospace;">"lin"</span> macro is defined in the expression database.  That macro is
  further expanded by other macros.  The example below shows the final
  expression that is actually executed.
  </p>
  </section>
  <section id="s_nfproc">
  <h3>Nfproc</h3>
  <p>
  This task simply formats the linearity expression and hides and fixes
  most of the parameters for <b>nfproc</b>.  The command that is executed
  is
  </p>
  <div class="highlight-default-notranslate"><pre>
  nfproc (input, output, outtype=outtype, logfiles=logfiles,
      trim=no, fixpix=no, biascor=no, lincor=yes, permask=no,
      darkcor=no, flatcor=no, skysub=no, replace=no, normalize=no,
      dorder="TXBD", forder="TXBDLR,N", order="TXBDLFR,S",
      bpm="(bpm)", obm="(objmask)", trimsec="(trimsec)",
      biassec="(biassec)", linexpr=expr, linimage=linimage,
      persist="", perwindow="5", darks="", flats="", flatexpr="",
      skies="", skymatch="", skymode="median 10", repexpr="",
      repimage="", btype="fit", bfunction="legendre",
      bsample="*", border="1", bnaverage="1", bniterate="1",
      bhreject="3.", blreject="3.", bgrow="0.", intype="",
      dtype="(obstype='dark')", ftype="(obstype='flat')",
      gtype="", stype="", imageid="(str(imageid))",
      filter="(filter)", sortval="(@'mjd-obs')", exptime="(exptime)",
      opdb="newfirm$opdb.dat", exprdb=exprdb, override=no, copy=no,
      erraction="warn", gdevice="stdgraph", gcursor="", gplotfile="")
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"expr"</span> is the expression created by this task.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Dickinson, M. 2008, NEWFIRM Linearity Calibration,
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nfproc, proctool.output
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE   ' 'PARAMETERS' 'DESCRIPTION' 'EXPRESSIONS' 'NFPROC' 'REFERENCES' 'SEE ALSO'  -->
  
