.. _rd2xy:

rd2xy: Translate RA/Dec to the pixel coordinate.
================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  rd2xy infile[group] ra dec
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task uses the group parameters CRVAL, CRPIX, and the CD matrix 
  coefficients to translate RA/Dec to the pixel coordinate.
  Thus the epoch of RA and Dec must be the same as these group parameters.
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
  <dl id="l_ra">
  <dt><b>ra [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ra' Line='ra [real]' -->
  <dd>The right ascension.
  </dd>
  </dl>
  <dl id="l_dec">
  <dt><b>dec [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dec' Line='dec [real]' -->
  <dd>The declination.
  </dd>
  </dl>
  <dl>
  <dt><b>(hour) = yes [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(hour) = yes [boolean]' -->
  <dd>Is the input RA in hours or degrees?
  </dd>
  </dl>
  <dl>
  <dt><b>(x) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(x) [real]' -->
  <dd>The output X pixel coordinate.
  </dd>
  </dl>
  <dl>
  <dt><b>(y) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(y) [real]' -->
  <dd>The output Y pixel coordinate.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate (X,Y) in the first group of an image from RA/Dec:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  wf&gt; rd2xy w1234567t.d0h 11:11:53 03:28:53
  
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  xy2rd
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
