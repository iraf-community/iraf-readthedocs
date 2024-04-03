dither: Dithered image combination.
===================================

.. toctree:: :maxdepth: 1

   dq
.. raw:: html

  <p>
  This package contains tasks which can be used to combine dithered images 
  using the <span style="font-family: monospace;">"drizzle"</span> algorithm. Some tasks are specialized for WFPC data 
  only, others, including the`drizzle' task, can be used to process 
  any image format supported by IRAF. 
  </p>
  <p>
  Two basic procedures are available, depending on the existence of only 
  linear shifts between the images to be combined, or linear shifts plus 
  a (small) rotation angle. Both procedures rely on cross-correlation to 
  derive the relative shifts and rotation angles. 
  </p>
  <p>
  The main combining task is `drizzle', which has to be supplied with the 
  linear shifts in X and Y and the rotation angle. It also supports 
  rescaling of the pixel grid and corrections for geometric distortions, 
  but only coefficients appropriate for WFPC-II data are currently available.
  </p>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec=None Level=0 Label='o' Line='o' -->
  <dd>NO ROTATION: this is the simplest case. One image is taken to be the 
  <span style="font-family: monospace;">"reference"</span> and the second image will be shifted to match it. The
  tasks to use are `offsets' and `shiftfind'. `offsets' builds
  4 cross-correlation <span style="font-family: monospace;">"images"</span>, one for each WFPC group, and `shiftfind' 
  measures the relative shift in each group by locating the correlation peak.
  For non-WFPC data, use task `crossdriz' instead of `offsets', with all
  rotation angles set to zero.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec=None Level=0 Label='o' Line='o' -->
  <dd>WITH ROTATION: the procedure for measuring the rotation between two images
  is to rotate the image against the reference by a set of angles and to
  compute the cross-correlation between each rotated image and the reference.
  A plot of the cross-correlation peak height as a function of rotation angle
  shows a peak at the <span style="font-family: monospace;">"correct"</span> (best fit) rotation angle. The task that
  executes these steps is `rotfind'. It relies on the `drizzle' task to perform
  the actual rotations, and on the `nfit1d' task to fit the cross-correlation
  maximum.
  </dd>
  </dl>
  <p>
  `avshift' uses the combined results from the 4 WFPC chips to asses the 
  quality of the final results.
  </p>
  <p>
  More information can be found in 
   A. S. Fruchter, R. N. Hook, I. C. Busko,  and M. Mutchler,
  1997, <span style="font-family: monospace;">"A  Package for the Reduction of Dithered Undersampled Images"</span>, in <span style="font-family: monospace;">"The
  1997 HST Calibration Workshop"</span>, S. Casertano et al.,
  ed. (Baltimore: Space Telescope Science Institute), in press.
  See http://www.stsci.edu/meetings/cal97.
  </p>
  <!-- Contents:  -->
  
