.. _xy2rd:

xy2rd: Translate a 2-D image pixel coordinate to right ascension
================================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  xy2rd infile[group] x y
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task uses the group parameters CRVAL, CRPIX, and the CD matrix 
  coefficients to translate a pixel coordinate to RA and DEC.
  Thus the epoch of RA and Dec is the same as these group parameters.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infile">
  <dt><b>infile [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infile' Line='infile [string]' -->
  <dd>Input image name.  Images are calculated one at a time and wildcards are 
  not supported.  
  If no group number is specified, it assumes the default group of 1.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x' Line='x [real]' -->
  <dd>X pixel coordinate.
  </dd>
  </dl>
  <dl id="l_y">
  <dt><b>y [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y' Line='y [real]' -->
  <dd>Y pixel coordinate.
  </dd>
  </dl>
  <dl>
  <dt><b>(hms) = yes [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(hms) = yes [boolean]' -->
  <dd>Print the output RA in hour-minute-second and DEC in 
  degree-minute-second?
  If 'hms=no', output will be in decimal degrees. 
  </dd>
  </dl>
  <dl>
  <dt><b>(ra) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ra) [string]' -->
  <dd>The output right ascension.
  </dd>
  </dl>
  <dl>
  <dt><b>(dec) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(dec) [string]' -->
  <dd>The output declination.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate RA and DEC of a pixel in the first group:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  wf&gt; xy2rd w1234567t.d0h 19 53
  
  </pre></div>
  <p>
  2. Calculate RA and DEC of a point in group 2, and produce output in 
  decimal degrees:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  wf&gt; xy2rd w1234567t.d0h[2] 12.34 56.78 h-
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rd2xy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
