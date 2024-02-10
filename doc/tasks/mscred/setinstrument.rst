.. _setinstrument:

setinstrument: Set instrument parameters
========================================

**Package: mscred**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  setinstrument instrument
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_instrument">
  <dt><b>instrument</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='instrument' Line='instrument' -->
  <dd>Instrument identification for instrument parameters to be set.  If <span style="font-family: monospace;">'?'</span>
  then a list of the instrument identifiers is printed.
  </dd>
  </dl>
  <dl id="l_site">
  <dt><b>site = <span style="font-family: monospace;">"kpno"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='site' Line='site = "kpno"' -->
  <dd>Site ID.
  </dd>
  </dl>
  <dl id="l_directory">
  <dt><b>directory = <span style="font-family: monospace;">"ccddb$"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='directory' Line='directory = "ccddb$"' -->
  <dd>Instrument directory containing instrument files.  The instrument files
  are found in the subdirectory given by the site ID. 
  </dd>
  </dl>
  <dl id="l_review">
  <dt><b>review = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='review' Line='review = yes' -->
  <dd>Review the instrument parameters?  If yes then <b>eparam</b> is run for
  the parameters of <b>ccdred</b> and <b>ccdproc</b>.
  </dd>
  </dl>
  <dl id="l_query">
  <dt><b>query</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='query' Line='query' -->
  <dd>Parameter query if initial instrument is not found.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The purpose of the task is to allow the user to easily set default
  parameters for a new instrument.  The default parameters are generally
  defined by support personal in an instrument directory for a particular
  site.  The instrument directory is the concatenation of the specified
  directory and the site.  For example if the directory is <span style="font-family: monospace;">"ccddb$"</span> and
  the site is <span style="font-family: monospace;">"kpno"</span> then the instrument directory is <span style="font-family: monospace;">"ccddb$kpno/"</span>.
  The user may have his own set of instrument files in a local directory.
  The current directory is used by setting the directory and site to the
  null string (<span style="font-family: monospace;">""</span>).
  </p>
  <p>
  The user specifies an instrument identifier.  This instrument may
  be specific to a particular observatory, telescope, instrument, and
  detector.  If the character <span style="font-family: monospace;">'?'</span> is specified or the instrument file is
  not found then a list of instruments
  in the instrument directory is produced by paging the file <span style="font-family: monospace;">"instruments.men"</span>.
  The task then performs the following operations:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>If an instrument translation file with the name given by the instrument
  ID and the extension <span style="font-family: monospace;">".dat"</span> is found then the instrument translation
  file parameter, <i>ccdred.instrument</i>, is set to this file.
  If it does not exist then the user is queried again.  Note that a
  null instrument, <span style="font-family: monospace;">""</span>, is allowed to set no translation file.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>If an instrument setup script with the name given by the instrument ID
  and the extension <span style="font-family: monospace;">".cl"</span> is found then the commands in the file are
  executed (using the command <i>cl &lt; script</i>.  This script generally
  sets default parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd>If the review flag is set the task <b>eparam</b> is run to allow the user
  to examine and modify the parameters for the package <b>ccdred</b> and task
  <b>ccdproc</b>.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To get a list of the instruments;
  </p>
  <div class="highlight-default-notranslate"><pre>
          cl&gt; setinstrument ?
          [List of instruments]
  
  2. To set the instrument and edit the processing parameters:
  
          cl&gt; setinstrument ccdlink
          [Edit CCDRED parameters]
          [Edit CCDPROC parameters]
  
  3. To use your own instrument translation file and/or setup script in
  your working directory.
  
          cl&gt; setinst.site=""
          cl&gt; setinst.dir=""
          cl&gt; setinst myinstrument
  
  To make these files see help under <b>instruments</b>.  Copying and modifying
  system files is also straightforward.
  
          cl&gt; copy ccddb$kpno/fits.dat .
          cl&gt; edit fits.dat
          cl&gt; setinst.site=""
          cl&gt; setinst.dir=""
          cl&gt; setinst fits
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  instruments, ccdred, ccdproc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
