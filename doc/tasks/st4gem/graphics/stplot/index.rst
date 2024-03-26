stplot: General plotting utilities.
===================================

.. toctree:: :maxdepth: 1

   igi
   psikern
.. raw:: html

  <p>
  The 'stplot' package includes general purpose plotting tasks
  tailored toward STSDAS data formats; that is, tables and group format
  image files. These tasks include:
  </p>
  <dl id="l_sgraph">
  <dt><b>sgraph</b></dt>
  <!-- Sec=None Level=0 Label='sgraph' Line='sgraph' -->
  <dd>The 'sgraph' task 
  includes all of the functions of the IRAF 'plot.graph' task, but adds
  the ability to plot from STSDAS tables (images and text files were supported
  by 'graph'). In 'sgraph', you can plot a single column against a row, or
  a column against another column.
  </dd>
  </dl>
  <dl id="l_depind">
  <dt><b>depind</b></dt>
  <!-- Sec=None Level=0 Label='depind' Line='depind' -->
  <dd>The 'depind' task prints pairs of dependent and independent pixel
  values from two one-dimensional images to STDOUT.  This may be piped to
  'sgraph' or 'plot.graph' to plot one image line (spectrum) against another.
  </dd>
  </dl>
  <dl id="l_skymap">
  <dt><b>skymap</b></dt>
  <!-- Sec=None Level=0 Label='skymap' Line='skymap' -->
  <dd>The 'skymap' task interprets an STSDAS table as a catalog of
  coordinates and brightnesses to produce a star chart.  That is, it
  plots symbols whose size depends on brightness and whose position
  on the plot is a projection of the celestial coordinates.  There is an
  interactive interface that allows a user to roam among different
  parts of the catalog, change the chart scale, and perform other actions.
  </dd>
  </dl>
  <dl id="l_Group">
  <dt><b>Group Format</b></dt>
  <!-- Sec=None Level=0 Label='Group' Line='Group Format' -->
  <dd>Three tasks support group format STSDAS images and plot more
  than one group member on a single graph.
  <dl>
  <dt><b>grlist</b></dt>
  <!-- Sec=None Level=1 Label='grlist' Line='grlist' -->
  <dd>A generic task to permit converting a range of groups to a list of image names.  The output list may be used by any task that accepts alist of images as input.
  </dd>
  </dl>
  <dl>
  <dt><b>grplot</b></dt>
  <!-- Sec=None Level=1 Label='grplot' Line='grplot' -->
  <dd>Overplots
  selected members on a single plot
  </dd>
  </dl>
  <dl>
  <dt><b>grspec</b></dt>
  <!-- Sec=None Level=1 Label='grspec' Line='grspec' -->
  <dd>Uses the
  'noao.onedspec.specplot' task to allow interaction with a plot of several
  group members.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_fieldplot">
  <dt><b>fieldplot</b></dt>
  <!-- Sec=None Level=0 Label='fieldplot' Line='fieldplot' -->
  <dd>The 'fieldplot' task is a general purpose task to draw arrows
  representing a vector field, that is, directions and magnitudes.  Data
  are read from STDIN to represent the coordinates of a point and the
  field vector.  The vector may be either a pair of projected magnitudes
  or the absolute magnitude and direction.  The magnitude may be scaled
  arbitrarily.
  </dd>
  </dl>
  <dl id="l_igi">
  <dt><b>igi</b></dt>
  <!-- Sec=None Level=0 Label='igi' Line='igi' -->
  <dd>The 'igi' task is an interactive interpreter for producing
  arbitrary plots.  The syntax of the commands is based on Mongo, but 'igi'
  operates within IRAF and is device independent. (A complete reference
  manual for 'igi' is available on request from the STSDAS group.)
  </dd>
  </dl>
  <dl id="l_newcont">
  <dt><b>newcont</b></dt>
  <!-- Sec=None Level=0 Label='newcont' Line='newcont' -->
  <dd>The 'newcont' task is an improved version of 'plot.contour'.  The
  algorithm used produces smoother contours that will not cross.  
  It also provides more options for determining contour level and specifying
  contour line types.
  </dd>
  </dl>
  <dl id="l_rdsiaf">
  <dt><b>rdsiaf</b></dt>
  <!-- Sec=None Level=0 Label='rdsiaf' Line='rdsiaf' -->
  <dd>The 'rdsiaf' task reads in the aperture descriptions from the Project
  Data Base (PDB) Science Instrument Aperture File (SIAF) and writes
  them into an SDAS table. This table is used by siaper, which plots
  the telescope apertures.
  </dd>
  </dl>
  <dl id="l_siaper">
  <dt><b>siaper</b></dt>
  <!-- Sec=None Level=0 Label='siaper' Line='siaper' -->
  <dd>The 'siaper' task uses any graphics device to draw the science 
  instrument apertures of the HST.
  It requires an input image containing WCS information. The drawn aperture
  can then be laid over an image.
  </dd>
  </dl>
  <dl id="l_psikern">
  <dt><b>psikern</b></dt>
  <!-- Sec=None Level=0 Label='psikern' Line='psikern' -->
  <dd>The 'psikern' task is a GIO kernel that translates from IRAF's graphics
  to PostScript.
  </dd>
  </dl>
  <!-- Contents:  -->
  
