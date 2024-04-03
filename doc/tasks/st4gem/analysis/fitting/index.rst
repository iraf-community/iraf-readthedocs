fitting: Curve fitting tools.
=============================

.. toctree:: :maxdepth: 1

   gfit1d
   errorpars
   samplepars
.. raw:: html

  <p>
  This package contains tasks that perform function fitting operations on
  images, ST4GEM table columns, or lists.  Both linear and non-linear
  functions are supported.
  </p>
  <p>
  When fitting 1-dimensional functions with input data from 2- (or
  more) dimensional images, the data are projected over a 1-dimensional vector
  before fitting the function. 
  </p>
  <p>
  The fitting tasks write their results to ST4GEM tables.  A common table
  format is used by all tasks in the package, with the same column headers
  and formats. 
  </p>
  <p>
  The interative linear function fitting task is 'gfit1d' which fits
  Chebyshev or Legendre polynomials, linear or cubic splines, using
  Cholesky factorization to solve the standard least-squares normal
  equations. 
  </p>
  <p>
  Non-linear function fitting is split between several tasks.
  The first, 'nfit1d', interatively fits each of six different
  functional forms:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  * power law
  * Planck function
  * sum of two Planck functions
  * sum of a power law and a Planck function
  * galaxy brightness profile (bulge + disk)
  * user-defined function (implemented by a built-in FORTRAN interpreter)
  
  </pre></div>
  <p>
  The second task, 'ngaussfit', is meant to interatively fit multiple
  Gaussians to 1-dimensional data.  The third task, 'n2gaussfit', is a
  simple non-interactive tool for fitting a 2-dimensional Gaussian to image data. 
  Task 'i2gaussfit' is a script useful to run 'n2gaussfit' in noisy
  conditions. 
  </p>
  <p>
  The non-linear fitting can be performed by any of two algorithms, either
  one of
  which can be  used to minimize chi-squared: downhill simplex (amoeba) or
  Levenberg-Marquardt.
  </p>
  <p>
  There is one task to do the inverse operation, that is, to read the table
  with fitting results and build images, ST4GEM tables or lists.  Another
  task is available to list or print the fitting table contents in a
  human-readable format.
  </p>
  <!-- Contents:  -->
  
