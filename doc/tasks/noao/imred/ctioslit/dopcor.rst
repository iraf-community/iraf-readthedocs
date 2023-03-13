.. _dopcor:

dopcor: Doppler correct spectra
===============================

**Package: ctioslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dopcor input output redshift
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input spectra to be doppler corrected.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of doppler corrected spectra.  If no output list is specified then
  the input spectra are modified.  Also the output name may be
  the same as the input name to replace the input spectra by the
  calibrated spectra.
  </dd>
  </dl>
  <dl id="l_redshift">
  <dt><b>redshift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='redshift' Line='redshift' -->
  <dd>Redshift or radial velocity (km/s) to be removed?  The spectra are corrected so
  that the specified redshift is removed; i.e. spectra with a positive
  velocity are shifted to shorter wavelengths and vice-versa.  This parameter
  may be either a number or an image header keyword with the desired redshift
  or velocity value.  An image header keyword may also have an initial minus
  sign, <span style="font-family: monospace;">'-'</span>, to specify the negative of a velocity or the redshift complement
  (1/(1+z)-1) of a redshift.  The choice between a redshift and a velocity is
  made with the <i>isvelocity</i> parameter.
  </dd>
  </dl>
  <dl id="l_isvelocity">
  <dt><b>isvelocity = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='isvelocity' Line='isvelocity = no' -->
  <dd>Is the value specified by the <i>redshift</i> parameter a velocity?  If
  no then the value is interpreted as a redshift and if it is yes then
  it is interpreted as a physical  velocity in kilometers per second.  Note that
  this is a relativistic velocity and not c*z!  For nearby cosmological
  velocities users should specify a redshift (z = v_cosmological / c).
  </dd>
  </dl>
  <dl id="l_add">
  <dt><b>add = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='add' Line='add = no' -->
  <dd>Add doppler correction to existing correction in <span style="font-family: monospace;">"multispec"</span> spectra?
  </dd>
  </dl>
  <dl id="l_dispersion">
  <dt><b>dispersion = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispersion' Line='dispersion = yes' -->
  <dd>Apply a correction to the dispersion function?
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = no' -->
  <dd>Apply a flux correction?
  </dd>
  </dl>
  <dl id="l_factor">
  <dt><b>factor = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='factor' Line='factor = 3' -->
  <dd>Flux correction factor as a power of 1+z when applying a flux correction.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be corrected.  If none are specified then all apertures
  are corrected.  An aperture list consists of comma separated aperture
  number or aperture number ranges.  A range is hypen separated and may
  include an interval step following the character <span style="font-family: monospace;">'x'</span>.  See <b>ranges</b>
  for further information.  For N-dimensional spatial spectra such as
  long slit and Fabry-Perot spectra this parameter is ignored.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print corrections performed?  The information includes the output image
  name, the apertures, the redshift, and the flux correction factor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input spectra (as specified by the input image list and apertures) are
  corrected by removing a specified doppler shift and written to the
  specified output images.  The correction is such that if the actual
  shift of the observed object is specified then the corrected spectra
  will be the rest spectra.  The opposite sign for a velocity or the
  redshift complement (1/(1+z)-1) may be used to add a doppler shift
  to a spectrum.
  </p>
  <p>
  There are two common usages.  One is to take spectra with high doppler
  velocities, such as cosmological sources, and correct them to rest with
  respect to the earth.  In this case the measured redshift or velocity is
  specified to <span style="font-family: monospace;">"remove"</span> this component.  The other usage is to correct
  spectra to heliocentric or local standard of rest.  The heliocentric or LSR
  velocities can be computed and entered in the image header with the task
  <b>rvcorrect</b>.  In this case it is tempting to again think you are
  <span style="font-family: monospace;">"removing"</span> the velocity so that you specify the velocity as given in the
  header.  But actually what is needed is to <span style="font-family: monospace;">"add"</span> the computed standard of
  rest velocity to the observed spectrum taken with respect to the telescope
  to place the dispersion in the desired center of rest.  Thus, in this case
  you specify the opposite of the computed heliocentric or LSR velocity; i.e.
  use a negative.
  </p>
  <p>
  The redshift or space velocity in km/s is specified either as a number or
  as an image header keyword containing the velocity or redshift.  If a
  number is given it applies to all the input spectra while an image header
  keyword may differ for each image.  The latter method of specifying a
  velocity is useful if velocity corrections are recorded in the image
  header.  See <b>rvcorrect</b> for example.
  </p>
  <p>
  The choice between a redshift and a space velocity for the <i>redshift</i>
  parameter is made using the <i>isvelocity</i> parameter. If isvelocity=yes
  then the header dispersion solution is modified according to the
  relativistic Doppler correction:
  </p>
  <p>
  	lambda_new = lamda_old * sqrt((1 + v/c)/(1 - v/c))
  </p>
  <p>
  where v is the value of <span style="font-family: monospace;">"redshift"</span>.  If isvelocity=no, <i>redshift</i> is
  interpreted as a cosmological redshift and the header dispersion solution
  is modified to give:
  </p>
  <p>
  	lambda_new = lamda_old * z
  </p>
  <p>
  where z is the value of <span style="font-family: monospace;">"redshift"</span>
  </p>
  <p>
  If the <i>add</i> parameter is used and the image uses a <span style="font-family: monospace;">"multispec"</span>
  format where the previous doppler factor is stored separately
  then the new doppler factor is:
  </p>
  <p>
  	znew = (1 + z) * (1 + zold) - 1 = z + zold + z * zold
  </p>
  <p>
  where z is the specified doppler factor, zold is the previous one,
  and znew is the final doppler factor.  If the <i>add</i> parameter
  is no then the previous correction is replaced by the new correction.
  Note that for images using a linear or equispec coordinate system
  the corrections are always additive since a record is not kept of
  the previous correction.  Also any flux correction is made based
  on the specified doppler correction rather than znew.
  </p>
  <p>
  There are two corrections which may be made and the user selects one
  or both of these.  A correction to the dispersion function is selected
  with the <i>dispersion</i> parameter.  This correction is a term to be
  applied to the dispersion coordinates defined for the image.  <i>The spectrum
  is not resampled, only the dispersion coordinate function is affected</i>.
  A correction to the flux, pixel values, is selected with the <i>flux</i>
  parameter.  This correction is only significant for cosmological redshifts.
  As such the correction is dependent on a cosmological model as well as
  whether a total flux or surface brightness is measured.  To provide the
  range of possible corrections the flux correction factor is defined by
  the <i>factor</i> parameter as the power of 1+z (where z is the
  redshift) to be multiplied into the observed pixel values.
  </p>
  <p>
  A keyword DOPCORnn is added to the image header.  The index starts from
  01 and increments if multiple corrections are applied.  The value of
  the keywords gives the redshift applied, the flux factor if used, and
  the apertures which were corrected.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To dispersion and flux correct a quasar spectrum with redshift of
  3.2 to a rest frame:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dopcor qso001.ms qso001rest.ms 3.2 flux+
  </pre></div>
  <p>
  2.  To correct a set of spectra (in place) to heliocentric rest the task
  <b>rvcorrect</b> is used to set the VHELIO keyword using an observed
  velocity of 0.  Then:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dopcor *.imh "" -vhelio isvel+
  </pre></div>
  <p>
  3.  To artificially add a redshift of 3.2 to a spectrum the complementary
  redshift is computed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; = 1/(1+3.2)-1
  -0.76190476190476
  cl&gt; dopcor artspec "" -0.762 flux+
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DOPCOR">
  <dt><b>DOPCOR V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOPCOR' Line='DOPCOR V2.10.3' -->
  <dd>This task was extended to work on two and three dimensional spatial spectra
  such as long slit and Fabry-Perot spectra.
  The <i>add</i> parameter was added.
  </dd>
  </dl>
  <dl id="l_DOPCOR">
  <dt><b>DOPCOR V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOPCOR' Line='DOPCOR V2.10.3' -->
  <dd>A keyword is added to log the correction applied.
  </dd>
  </dl>
  <dl id="l_DOPCOR">
  <dt><b>DOPCOR V2.10.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOPCOR' Line='DOPCOR V2.10.2' -->
  <dd>A sign error in converting velocity to redshift was fixed.  A validity
  check on the velocities and redshifts was added.  The documentation
  was corrected and improved.
  </dd>
  </dl>
  <dl id="l_DOPCOR">
  <dt><b>DOPCOR V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOPCOR' Line='DOPCOR V2.10' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ranges, rvcorrect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
