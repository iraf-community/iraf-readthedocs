.. _ecreidentify:

ecreidentify: Automatically identify features in spectra
========================================================

**Package: echelle**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ecreidentify images reference
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Echelle images in which the features in the reference image are to be
  reidentified and a new dispersion function fit.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>Echelle image with previously identified features and dispersion
  function.
  </dd>
  </dl>
  <dl id="l_shift">
  <dt><b>shift = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shift' Line='shift = 0.' -->
  <dd>Shift in user coordinates to be added to the reference features before
  centering.  If INDEF then a shift is determined by correlating the
  reference features to features automatically identified in the image to
  be reidentified.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 5.' -->
  <dd>Centering radius in pixels.  If a reidentified feature falls further
  than this distance from the reference position (after shifting) it is
  not reidentified.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10.' -->
  <dd>In order for a feature center to be determined the range of pixel
  intensities around the feature must exceed this threshold.
  </dd>
  </dl>
  <dl id="l_refit">
  <dt><b>refit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refit' Line='refit = yes' -->
  <dd>Refit the dispersion function?  If yes and there are more than 4
  features in more than one order and a dispersion function was defined
  in the reference image then a new dispersion function of the same type
  and order offset
  as in the reference image is fit using the new pixel positions.
  Otherwise only a zero point shift is determined from the revised fitted
  coordinates without changing the form of the dispersion function.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database containing the feature data for the reference image and in
  which the features for the reidentified images are recorded.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT,logfile"' -->
  <dd>List of file in which to keep a processing log.  If a null file, <span style="font-family: monospace;">""</span>, is
  given then no log is kept.  If the log file is <span style="font-family: monospace;">"STDOUT"</span> then the log is
  written to the terminal.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Emission or absorption features in a reference echelle spectrum are
  reidentified in other echelle spectra.  The features for the reference
  image and those determined for reidentified images are recorded in the
  specified database.
  </p>
  <p>
  The first step in transferring identifications from the reference
  spectrum to another spectrum is to add a shift (in wavelength) to each
  feature in the reference image.  The shift is specified by the
  parameter <i>shift</i>.  This shift is for the fundamental order (order
  number 1) which is then applied to each order by dividing by the order
  number.  If the shift is specified as INDEF then a shift is determined
  by finding the peaks in the input spectrum and correlating these peaks
  against the feature in the reference spectrum.  This is the <span style="font-family: monospace;">'x'</span>
  algorithm described in <b>ecidentify</b>.
  </p>
  <p>
  After the shift has been added to move the reference features to near
  the input spectrum features these positions are adjusted by centering
  on the features using the <b>center1d</b> algorithm.  The parameters
  <i>cradius</i> and <i>threshold</i> are used in this operation.  If the
  centering fails to find the feature within the centering radius
  (<i>cradius</i>) that feature is eliminated from the feature list.
  </p>
  <p>
  If the parameter <i>refit</i> has the value <span style="font-family: monospace;">"no"</span> then the average shift
  in the feature positions is recorded as a zero point wavelength offset
  for the fundamental order without changing the shape of the dispersion
  function.  If the parameter has the value <span style="font-family: monospace;">"yes"</span> then the new feature
  positions are used to refit the dispersion function (of the same function
  type and orders).  The order offset is also maintained.
  </p>
  <p>
  Log information is written to the specified log files.  To log this to
  the terminal, called the standard output, use STDOUT.  The log
  information includes reference spectrum, the spectrum being reidentified,
  the number of initial features and the number actually reidentified,
  the average shift in pixels, the average shift in wavelength (in terms
  of the fundamental order), the average fractional shift in wavelength
  (which can be scaled to a radial velocity), and the RMS of the features
  wavelengths given by the dispersion function to the user specified true
  wavelengths.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The features in the spectrum f033.ec were identified previously
  with the task <b>ecidentify</b>.  The features positions in f043.ec are
  are reidentified with and without refitting the dispersion function as
  follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ec&gt; ecreidentify f043.ec f033.ec
  
  ECREIDENTIFY: NOAO/IRAF V2.7 seaman@puppis Mon 09:03:51 27-Jun-88
    Reference image = f033.ec, Refit = yes
                 Image    Found  Pix Shift  User Shift  Z Shift      RMS
               f043.ec  561/561       0.11       -1.07  -1.9E-6   0.0117
  
  ec&gt; ecreidentify f043.ec f033.ec refit=no
  
  ECREIDENTIFY: NOAO/IRAF V2.7 seaman@puppis Mon 09:15:21 27-Jun-88
    Reference image = f033.ec, Refit = no
                 Image    Found  Pix Shift  User Shift  Z Shift      RMS
               f043.ec  561/561       0.11       -1.07  -1.9E-6   0.0131
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  center1d, ecidentify
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
