.. _listspec:

listspec: Print an ASCII list of a spectrum with  optional per pixel info
=========================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  listspec filelist
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Image file template.
  </dd>
  </dl>
  <dl id="l_specext">
  <dt><b>specext = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specext' Line='specext = 0' -->
  <dd>Spectrum extension number in multiextension FITS image
  </dd>
  </dl>
  <dl id="l_specnum">
  <dt><b>specnum 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specnum' Line='specnum 0' -->
  <dd>Spectrum number in multispec image
  </dd>
  </dl>
  <dl id="l_specband">
  <dt><b>specband 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specband' Line='specband 0' -->
  <dd>Spectrum band in multispec image
  </dd>
  </dl>
  <dl id="l_pix1">
  <dt><b>pix1 INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pix1' Line='pix1 INDEF' -->
  <dd>First pixel to list (INDEF starts with first pixel in this spectrum)
  </dd>
  </dl>
  <dl id="l_pix2">
  <dt><b>pix2 INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pix2' Line='pix2 INDEF' -->
  <dd>Last pixel to list (INDEF starts with last pixel in this spectrum)
  </dd>
  </dl>
  <dl id="l_lambda1">
  <dt><b>lambda1 INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lambda1' Line='lambda1 INDEF' -->
  <dd>Starting wavelength to list (INDEF starts with first defined wavelength in file)
  </dd>
  </dl>
  <dl id="l_lambda2">
  <dt><b>lambda2 INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lambda2' Line='lambda2 INDEF' -->
  <dd>Ending wavelength to list (INDEF starts with first defined wavelength in file)
  </dd>
  </dl>
  <dl id="l_logwav">
  <dt><b>logwav = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logwav' Line='logwav = no' -->
  <dd>Print log wavelength instead of wavelength
  </dd>
  </dl>
  <dl id="l_renormalize">
  <dt><b>renormalize = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='renormalize' Line='renormalize = 0.0' -->
  <dd>Renormalize data to this number (neg mean  pos max)
  </dd>
  </dl>
  <dl id="l_printlim">
  <dt><b>printlim = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='printlim' Line='printlim = no' -->
  <dd>Print values at only pix1 and pix2 if yes else pixels between
  </dd>
  </dl>
  <dl id="l_columns">
  <dt><b>columns = <span style="font-family: monospace;">"wf"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='columns' Line='columns = "wf"' -->
  <dd>Print n=ap p=pixel w=wavelength f=flux v=velocity d=deltawave
  </dd>
  </dl>
  <dl id="l_numform">
  <dt><b>numform = <span style="font-family: monospace;">"%3d"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='numform' Line='numform = "%3d"' -->
  <dd>IRAF format for spectrum number/aperture/order
  </dd>
  </dl>
  <dl id="l_pixform">
  <dt><b>pixform = <span style="font-family: monospace;">"%4d"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixform' Line='pixform = "%4d"' -->
  <dd>IRAF format for spectrum pixel number
  </dd>
  </dl>
  <dl id="l_fluxform">
  <dt><b>fluxform = <span style="font-family: monospace;">"%g"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxform' Line='fluxform = "%g"' -->
  <dd>IRAF format for flux output
  </dd>
  </dl>
  <dl id="l_waveform">
  <dt><b>waveform = <span style="font-family: monospace;">"%9.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='waveform' Line='waveform = "%9.3f"' -->
  <dd>IRAF format for wavelength/log wavelength output
  </dd>
  </dl>
  <dl id="l_outfile">
  <dt><b>outfile = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outfile' Line='outfile = no' -->
  <dd>Write list to output file x.wav (yes or no)
  </dd>
  </dl>
  <dl id="l_heading">
  <dt><b>heading = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='heading' Line='heading = no' -->
  <dd>Include one line description at start of each file (yes or no)
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of pixels to sum across dispersion
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose no' -->
  <dd>If yes, print the name of the spectrum before listing its values.
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>Print extra information for debugging (yes or no)
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Print wavelength/pixel value pairs for a spectrum image, computing the
  wavelength using the world coordinate system defined in the image header.
  If number is nonzero, print the pixel number in that column for each pixel.
  If lambda1 is set, start with the first pixel with a wavelength greater than
  or equal to lambda1 in angstroms.  If lambda2 is set, stop with the last
  pixel with a wavelength less than or equal to lambda2 in angstroms.  If pix1
  is set, start at that pixel number (overidden by lambda1).  If pix2 is set,
  end with that pixel number (overidden by lambda2).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1) Print a portion of a spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  rvsao&gt; listspec 2001.0530.0086.N5548.ms.fits pix1=1000 pix2=1010 columns=wf v+
  Spectrum N5548 1 - 2635
  5109.598 566.9747
  5111.069 535.2692
  5112.541 451.0975
  5114.012 507.8816
  5115.484 544.0441
  5116.955 518.6956
  5118.427 539.1362
  5119.898 530.2105
  5121.370 475.1248
  5122.841 489.9548
  5124.312 505.7442
  rvsao&gt;
  </pre></div>
  <p>
  2) Print a portion of a spectrum with pixel numbers:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  rvsao&gt; listspec 2001.0530.0086.N5548.ms.fits pix1=1000 pix2=1010 columns=pwf v+
  Spectrum N5548 1 - 2635
  1000  5109.598 566.9747
  1001  5111.069 535.2692
  1002  5112.541 451.0975
  1003  5114.012 507.8816
  1004  5115.484 544.0441
  1005  5116.955 518.6956
  1006  5118.427 539.1362
  1007  5119.898 530.2105
  1008  5121.370 475.1248
  1009  5122.841 489.9548
  1010  5124.312 505.7442
  rvsao&gt;
  </pre></div>
  <p>
  3) Print the first ten pixels of a spectrum with pixel numbers:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  rvsao&gt; listspec 2001.0530.0086.N5548.ms.fits pix2=10 columns=pwf
     1  3639.606 56.43489
     2  3641.077 29.7611
     3  3642.549 58.7378
     4  3644.020 101.496
     5  3645.492 108.704
     6  3646.963 69.95907
     7  3648.435 72.81136
     8  3649.906 71.15504
     9  3651.378 61.04418
    10  3652.849 77.30488
  rvsao&gt;
  </pre></div>
  <p>
  4) Print the width and velocity shift with pixel numbers:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; listspec 2001.0530.0086.N5548.ms.fits pix1=1000 pix2=1010 columns=pwdv v+
  Spectrum N5548 1 - 2635
  1000  5109.598     1.471    86.334
  1001  5111.069     1.471    86.309
  1002  5112.541     1.471    86.285
  1003  5114.012     1.471    86.260
  1004  5115.484     1.471    86.235
  1005  5116.955     1.471    86.210
  1006  5118.427     1.471    86.185
  1007  5119.898     1.471    86.161
  1008  5121.370     1.471    86.136
  1009  5122.841     1.471    86.111
  1010  5124.312     1.471    86.086
  rvsao&gt;
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  
