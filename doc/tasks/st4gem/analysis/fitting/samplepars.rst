.. _samplepars:

samplepars: Pset with data sampling parameters.
===============================================

**Package: fitting**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  samplepars
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The points to be fit are determined by selecting a sample of data
  specified by the parameter 'sample' and taking either the average or
  median of the number of points specified by the parameter 'naverage'. 
  The type of averaging is selected by the sign of the parameter and the
  number of points is selected by the absolute value of the parameter. 
  </p>
  <p>
  If 'niterate' is greater than zero the sigma of the residuals between the
  fitted points and the fitted function is computed and those points whose
  residuals are less than LOW_REJECT * sigma or HIGH_REJECT * sigma value
  are excluded from the fit.  Points within a distance of 'grow' pixels of a
  rejected pixel are also excluded from the fit.  The function is then
  refit without the rejected points.  The rejection can be iterated the
  number of times specified by the parameter 'niterate'.  Note a rejection
  value of zero is the same as no rejection. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(axis = 1) [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(axis = 1) [integer, min=1, max=INDEF]' -->
  <dd>Axis onto which to project  if fitting an image section of more than one 
  dimension. It is relative to the full image, and not to the particular
  section being fitted. For instance, when fitting the section
  data[100:*:*], 'axis' can have either a value of 2 or 3. Notice that
  redundant section constructs such as dev$pix[256:256,*] will not work.
  </dd>
  </dl>
  <dl>
  <dt><b>(sample = *) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(sample = *) [string]' -->
  <dd>Sample points to use in fit. The default (*) is to set the sample to the 
  full data range. Sub-ranges may be specified by two real numbers 
  separated by a colon. Any number of sub-ranges are allowed, separated by 
  commas or spaces. The numbers must be in the same units as the X-axis.
  </dd>
  </dl>
  <dl>
  <dt><b>(naverage = 1) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(naverage = 1) [integer]' -->
  <dd>Number of points to be used in sample averaging.
  </dd>
  </dl>
  <dl>
  <dt><b>(low_reject = 0.) [real, min=0., max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(low_reject = 0.) [real, min=0., max=INDEF]' -->
  <dd>Lower threshold (in sigma) of the fit.  Values below this level will be 
  rejected. 
  </dd>
  </dl>
  <dl>
  <dt><b>(high_reject = 0.) [real, min=0., max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(high_reject = 0.) [real, min=0., max=INDEF]' -->
  <dd>Upper threshold (in sigma) of the fit.  Values above this level will be 
  rejected. 
  </dd>
  </dl>
  <dl>
  <dt><b>(niterate = 1) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(niterate = 1) [integer, min=0, max=INDEF]' -->
  <dd>Number of rejection iterations.
  </dd>
  </dl>
  <dl>
  <dt><b>(grow = 0.) [real, min=0., max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(grow = 0.) [real, min=0., max=INDEF]' -->
  <dd>Rejection growing radius (in pixels).
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gfit1d, nfit1d, ngaussfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'SEE ALSO'  -->
  
