.. _syndico:

syndico: Make dicomed print of daily grams 18 cm across.
========================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  syndico image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Image to plot on the dicomed.
  </dd>
  </dl>
  <dl id="l_logofile">
  <dt><b>logofile = iraf$noao/imred/vtel/nsolcrypt.dat</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logofile' Line='logofile = iraf$noao/imred/vtel/nsolcrypt.dat' -->
  <dd>File containing the text encoded NSO logo image.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = dicomed</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = dicomed' -->
  <dd>Device on which to plot the image.
  </dd>
  </dl>
  <dl id="l_sbthresh">
  <dt><b>sbthresh = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sbthresh' Line='sbthresh = 2' -->
  <dd>Squibby brightness threshold used to determine the limb for trimming.
  </dd>
  </dl>
  <dl id="l_plotlogo">
  <dt><b>plotlogo = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotlogo' Line='plotlogo = yes' -->
  <dd>Flag indicating whether or not to plot the logo.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Flag indicating to the program that it should give progress reports.
  </dd>
  </dl>
  <dl id="l_forcetype">
  <dt><b>forcetype = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcetype' Line='forcetype = no' -->
  <dd>Flag to override the wavelength designation from the image header.
  </dd>
  </dl>
  <dl id="l_magnetic">
  <dt><b>magnetic = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magnetic' Line='magnetic = yes' -->
  <dd>If 'forcetype' = 'yes' then this flag designates that we should force
  to magnetic (8688).  If set to 'no' the type is forced to 10830.
  The effect of forcing the type is to choose which lookup table to
  use when scaling the image.
  </dd>
  </dl>
  <dl id="l_month">
  <dt><b>month</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='month' Line='month' -->
  <dd>Month the observation was taken (January = 1,,,December = 12).
  </dd>
  </dl>
  <dl id="l_day">
  <dt><b>day</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='day' Line='day' -->
  <dd>Day of the month the observation was taken.
  </dd>
  </dl>
  <dl id="l_year">
  <dt><b>year</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='year' Line='year' -->
  <dd>Year the observation was taken (two digits only, ie. 89 for 1989).
  </dd>
  </dl>
  <dl id="l_hour">
  <dt><b>hour</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hour' Line='hour' -->
  <dd>Hour of the day the observation was taken (universal time, 1-24).
  </dd>
  </dl>
  <dl id="l_minute">
  <dt><b>minute</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minute' Line='minute' -->
  <dd>Minute the observation was taken (0-59).
  </dd>
  </dl>
  <dl id="l_second">
  <dt><b>second</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='second' Line='second' -->
  <dd>Second the observation was taken (0-59).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Syndico produces full disk plots on the Dicomed.  The ephemeris data
  is used to estimate the radius of the image and the center of the
  disk is gotten from the image header.  Using this data, an image is
  made that is as close to 18 centimeters in diameter as possible.
  There are two greyscale lookup tables corresponding to the two types
  of image normally used, the magnetogram and the spectroheliogram.
  If the wavelength is something other than 8688 or 10830, a linear
  greyscale is used.
  </p>
  <p>
  The National Solar Observatory (tentative) logo is read from an encoded
  text file and put on the plot if requested (default).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; syndico image1
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
