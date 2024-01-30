.. _velset:

velset: Set velocity by modifying starting wavelength
=====================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  velset input output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task changes the wavelength scale of spectra, moving them from one 
  given redshift to another one.  The input spectra are specified by an 
  image template list.  The output is either a matching list of spectra or 
  a directory.  The task works by copying the input spectra to the output 
  destination, and then modifying the header keywords that describe the 
  wavelength axis, on the output spectra only.  A spectrum may not be 
  copied onto itself; this prevents original wavelength information from 
  being accidently overwritten.  Image sections are ignored both on input 
  and output, because it is assumed that the user wants a copy of the 
  input  with the wavelength scale modified. 
  </p>
  <p>
  *** WARNING ***
  Use this task on log-wavelength spectra ONLY.  SUMSPEC will rebin and
  shift linear wavelength spectra.
  </p>
  <p>
  This task looks in the header for keywords describing the wavelength 
  axis; keywords are sought in the following order: first, IRAF keywords 
  'W0' and 'WPC'; next, CD keywords 'CRVALn' and 'CDn_1'; and finally, 
  FITS keywords 'CRVALn' and 'CDELTn' (n is the value of task parameter 
  'axis', unless the IRAF header keyword 'DISPAXIS' is found, in which 
  case it takes precedence over the parameter).  Logarithmic wavelength 
  scale is treated correctly if either the 'log' task parameter is set to 
  <span style="font-family: monospace;">"yes"</span> or if the IRAF header keyword 'DC-FLAG' is found in the header 
  with value 1.  'HISTORY' records are appended to the header. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name template]' -->
  <dd>Name(s) of the input files containing spectra.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name or directory name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name or directory name]' -->
  <dd>The output file, or directory, to which the transformed spectra will be 
  written.
  </dd>
  </dl>
  <dl id="l_velz">
  <dt><b>velz=yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='velz' Line='velz=yes' -->
  <dd>Is the new redshift in Z (yes) or km/sec (no)
  </dd>
  </dl>
  <dl id="l_newz">
  <dt><b>newz = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newz' Line='newz = 0.0' -->
  <dd>The redshift of the output spectra.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Print operations? 
  If set to <span style="font-family: monospace;">"yes"</span>, the wavelength origin and step for 
  both the input and output spectra are listed as the task progresses.
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  1. Transform a set of spectra with root name 'cluster*'
  to redshift 0.0. The result will be stored in subdirectory 
  'local/'. The input spectra are in STSDAS format (extension 
  '.hhh').
  <div class="highlight-default-notranslate"><pre>
  to&gt; setvel cluster*.hhh local/ newz=0.0
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
