.. _filtpars:

filtpars: Edit the filter function parameters
=============================================

**Package: xrv**

.. raw:: html

  <section id="s_name_">
  <h3>Name </h3>
  <p>
  filtpars -- edit the filter function parameters
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage </h3>
  <p>
  filtpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_f_type">
  <dt><b>f_type = <span style="font-family: monospace;">"ramp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f_type' Line='f_type = "ramp"' -->
  <dd>Type of filter to be used.  Possible choices are
  <dl>
  <dt><b>ramp</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ramp' Line='ramp' -->
  <dd>A ramp function which begins to rise at the <i>cuton</i> wavenumber and
  reaches full value (i.e. passes the full value of the component) at the
  <i>fullon</i> wavenumber.  It begin to decline at the <i>cutoff</i> wavenumber
  and returns to zero at the <i>fulloff</i> wavenumber.
  </dd>
  </dl>
  <dl>
  <dt><b>Hanning</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='Hanning' Line='Hanning' -->
  <dd>A Hanning function is used to attenuate the fourier components over the
  range specified by the <i>cuton</i> and <i>cutoff</i> parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>Welch</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='Welch' Line='Welch' -->
  <dd>A Welch function is used to attenuate the fourier components over the range
  specified by the <i>cuton</i> and <i>cutoff</i> parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>Square</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='Square' Line='Square' -->
  <dd>A standard step function which is zero outside the <i>cuton</i> and
  <i>cutoff</i> component numbers and one within those numbers.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_cuton">
  <dt><b>cuton = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cuton' Line='cuton = 0' -->
  <dd>The fourier wavenumber at which the filter begins to pass the filtered fft
  component.
  </dd>
  </dl>
  <dl id="l_cutoff">
  <dt><b>cutoff = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cutoff' Line='cutoff = 0' -->
  <dd>The fourier wavenumber at which the filter ceases to pass fft components.
  </dd>
  </dl>
  <dl id="l_fullon">
  <dt><b>fullon = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fullon' Line='fullon = 0' -->
  <dd>Used only for a 'ramp' filter.  The fourier wavenumber at which the filter
  reaches full value and passes all of the data.
  </dd>
  </dl>
  <dl id="l_fulloff">
  <dt><b>fulloff = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fulloff' Line='fulloff = 0' -->
  <dd>Used only for a 'ramp' filter.  The fourier wavenumber at which the filter
  reaches zero value and passes none of the data.
  </dd>
  </dl>
  </section>
  <section id="s_description_">
  <h3>Description </h3>
  <p>
  The filtering parameters control the type of filter to be used
  on the Fourier transformed data as well as the range in wavenumbers over
  which it will operate.  Filtering of the data may be necessary to remove
  high frequency noise or low-frequency tends not removed by continuum
  subtraction.  If the filtering is enabled, then once the data have been 
  transformed, a bandpass filter of the type chosen by the
  <i>f_type</i> parameter is applied to the Fourier components of the
  spectra.  Wavenumbers lower than that specified by the <i>cuton</i> parameter
  are set to zero and wavenumbers up to that specified by the <i>cutoff</i>
  parameter (or the <i>fulloff</i> parameter in the case of a 'ramp' filter)
  are attenuated or passed in full according to the filter chosen.   
  Since the data are assumed to be linearized in log-wavelength space, applying 
  a filter to the data in Fourier space introduces no phase shift and has 
  the same effect as smoothing the data in real space.  The data are centered 
  and zero padded in an array of length 2**N such that the number of elements 
  is greater than or equal to the number of actual data points.  This array in
  then Fourier transformed, and the resulting fft is then filtered prior
  to correlation.
  </p>
  <p>
  Filtering is enabled by turning on the <i>fxcor.filter</i> parameter and setting
  it to something other than <span style="font-family: monospace;">"none"</span>.  Filtering may be done on only one of the
  two spectra or both prior to correlation.
  </p>
  <p>
  The filter choices behave as follows:
  </p>
  <dl id="l_Square">
  <dt><b>Square Filter</b></dt>
  <!-- Sec='DESCRIPTION ' Level=0 Label='Square' Line='Square Filter' -->
  <dd>The fourier components at wavenumbers between the <i>cuton</i> and <i>cutoff</i>
  wavenumbers are passed without change.  Those wavenumbers outside this region
  are set to zero.
  </dd>
  </dl>
  <dl id="l_Ramp">
  <dt><b>Ramp Filter</b></dt>
  <!-- Sec='DESCRIPTION ' Level=0 Label='Ramp' Line='Ramp Filter' -->
  <dd>Fourier components below the <i>cuton</i> and above the <i>fulloff</i> 
  wavenumbers are set to zero. 
  At the <i>cuton</i> wavenumber the filter function
  begins to rise until the <i>fullon</i> wavenumber is reached.  Data in this 
  region is weighted by the slope of the filter until at the <i>fullon</i>
  wavenumber data are passed through without change.  Similarly, the filter
  begins to fall at the <i>cutoff</i> wavenumber until it completely blocks
  (i.e. zeros) the fourier components at the <i>fulloff</i> wavenumber.
  </dd>
  </dl>
  <dl id="l_Welch">
  <dt><b>Welch Filter</b></dt>
  <!-- Sec='DESCRIPTION ' Level=0 Label='Welch' Line='Welch Filter' -->
  <dd>Fourier components below the <i>cuton</i> and above the <i>cutoff</i> 
  wavenumbers are set to zero.  Components between these regions are weighted
  according to the equation for a Welch window.  Namely,
  <div class="highlight-default-notranslate"><pre>
  
                                               2
  w(j)  = 1. - [ (j - 1/2(N-1)) / (1/2(N+1)) ]
  
          where j =  (wavenumber - cuton_wavenumber)
                N =  (cutoff - cuton) + 1
  </pre></div>
  </dd>
  </dl>
  <dl id="l_Hanning">
  <dt><b>Hanning Filter</b></dt>
  <!-- Sec='DESCRIPTION ' Level=0 Label='Hanning' Line='Hanning Filter' -->
  <dd>Fourier components below the <i>cuton</i> and above the <i>cutoff</i> 
  wavenumbers are set to zero. Components between these regions are weighted
  according to the equation for a Hanning window.  Namely,
  <div class="highlight-default-notranslate"><pre>
  
  w(j)  =  1/2 [ 1. - cos( (TWOPI*j) / (N-1) ) ]
  
          where j =  (wavenumber - cuton_wavenumber)
                N =  (cutoff - cuton) + 1
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_task_colon_commands">
  <h3>Task colon commands</h3>
  <p>
  The values of the <i>filtpars</i> pset may be changed, displayed, or updated
  from within the Fourier mode of the <i>fxcor</i> task.  Simply 
  typing the parameter name will have the default action of printing the current
  value of that parameter. An optional value may be added to change the named
  parameter.
  </p>
  <dl>
  <dt><b>:update  filtpars</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':update  filtpars' -->
  <dd>Update the pset with the current values of the filter parameters.
  The argument <span style="font-family: monospace;">"filtpars"</span> must be present or else the command will default
  to the task parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>:unlearn  filtpars</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':unlearn  filtpars' -->
  <dd>Reset the parameter values to their defaults.
  The argument <span style="font-family: monospace;">"filtpars"</span> must be present or else the command will default
  to the task parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>:show  filtpars</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':show  filtpars' -->
  <dd>Clear the screen and display all values in the filtpars pset.
  The argument <span style="font-family: monospace;">"filtpars"</span> must be present or else the command will default
  to the task default.
  </dd>
  </dl>
  <dl>
  <dt><b>:filttype	[ramp|welch|hanning|square|none]</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':filttype	[ramp|welch|hanning|square|none]' -->
  <dd>Set or show the current value of the filter type to use
  </dd>
  </dl>
  <dl>
  <dt><b>:cuton	[int_value]</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':cuton	[int_value]' -->
  <dd>Set or show the current value of the cuton fourier component
  </dd>
  </dl>
  <dl>
  <dt><b>:cutoff	[int_value]</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':cutoff	[int_value]' -->
  <dd>Set or show the current value of the cutoff fourier component
  </dd>
  </dl>
  <dl>
  <dt><b>:fullon	[int_value]</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':fullon	[int_value]' -->
  <dd>Set or show the current value of the fullon fourier component
  </dd>
  </dl>
  <dl>
  <dt><b>:fulloff	[int_value]</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':fulloff	[int_value]' -->
  <dd>Set or show the current value of the fulloff fourier component
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the filtering parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  rv&gt; lpar filtpars
  </pre></div>
  <p>
  2. Edit the filtering parameters
  </p>
  <div class="highlight-default-notranslate"><pre>
  rv&gt; filtpars
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fxcor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME ' 'USAGE ' 'PARAMETERS' 'DESCRIPTION ' 'TASK COLON COMMANDS' 'EXAMPLES' 'SEE ALSO'  -->
  
