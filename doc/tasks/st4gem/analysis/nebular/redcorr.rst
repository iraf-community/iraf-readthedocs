.. _redcorr:

redcorr: Correct line flux for interstellar reddening
=====================================================

**Package: nebular**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  redcorr wave flux
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task corrects the input flux for the effects of interstellar 
  reddening.  The reddening corrected line flux <span style="font-family: monospace;">"I"</span> is derived from 
  the input line flux <span style="font-family: monospace;">"F"</span> by: 
  </p>
  <div class="highlight-default-notranslate"><pre>
                        {-c * f(lambda)}
  I(line) = F(line) * 10
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"c"</span> is the extinction constant (i.e. the logarithmic 
  extinction at H-beta, 4861 Ang), and <span style="font-family: monospace;">"f(lambda)"</span> is derived from 
  one of a few possible extinction functions.  The choices for 
  Galactic extinction are: Savage &amp; Mathis (1979), Cardelli, Clayton, 
  &amp; Mathis (1989), and the function of Kaler (1976) which is based 
  on Whitford (1958).  The choices for extra-Galactic extinction laws 
  are Howarth (1983) for the LMC, and Prevot et al. (1984) for the 
  SMC.  
  </p>
  <p>
  The task output gives the selected reddening function and the 
  corrected flux.  The dereddened flux is also stored in the task 
  parameter <span style="font-family: monospace;">"result"</span> for ease of use in CL scripts.  
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_wave">
  <dt><b>wave = 4861.3 [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wave' Line='wave = 4861.3 [real]' -->
  <dd>Wavelength of emission line, in Angstroms.  
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = 0. [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = 0. [real]' -->
  <dd>Oberved flux of the emission line.  
  </dd>
  </dl>
  <dl>
  <dt><b>(red_func = <span style="font-family: monospace;">"gal"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(red_func = "gal") [string]' -->
  <dd>Choice of interstellar redding function, which is one of: <span style="font-family: monospace;">"gal"</span>, 
  <span style="font-family: monospace;">"ccm"</span>, <span style="font-family: monospace;">"jbk"</span>, <span style="font-family: monospace;">"lmc"</span>, or <span style="font-family: monospace;">"smc"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(c_ext = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(c_ext = 0.) [real]' -->
  <dd>Value to assume for the extinction constant--i.e., the logarithmic 
  extinction at H(beta) 4861.3 Ang.  Note that this value may be 
  negative to <span style="font-family: monospace;">"un-correct"</span> the flux.  
  </dd>
  </dl>
  <dl>
  <dt><b>(result = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(result = INDEF) [real]' -->
  <dd>Result of the calculation--i.e, the redding-corrected flux.  
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = no) [boolean]' -->
  <dd>Print verbose output for each iteration?  
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The observed flux of the [O ii] 3727 Ang doublet, relative to 
  I(H-beta) = 100, is 12.4.  Find the unreddened flux if the 
  extinction constant is 0.24, using the reddening function of 
  Seaton (1979). 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; redcorr 3727 12.4 c_ext=0.24 red_func=seaton
  # Redding correction using SEATON function:
    Flux: 14.62217
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This auxilliary task was written by R.A. Shaw (STScI).  Type <span style="font-family: monospace;">"help 
  nlevel"</span> for additional information about how the reddening correction 
  is used throughout the `nebular' package, and for literature 
  references for the reddening functions.  
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nlevel 
  </p>
  <p>
  For general information about this package, type <span style="font-family: monospace;">"help nebular 
  opt=sysdoc"</span>.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
