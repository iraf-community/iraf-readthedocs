graphics: Graphics and image display packages.
==============================================

.. toctree:: :maxdepth: 1

   stplot/index
.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  The `stsdas.graphics' package contains two subpackages of tasks for
  viewing one- and two-dimensional data.  These tasks are not necessarily
  specific to HST data.  They tasks are designed to make use of IRAF
  image formats (OIF, STF and QPOE), and STSDAS binary tables.  A summary
  of the available packages is given in Table 1 below; a more detailed
  summary can be found in the following sections and the help for each
  package.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
              Table 1.  Graphics Packages
  +--------------------------------------------------------+
  | Package    | Description                               |
  +--------------------------------------------------------+
  | stplot     | General data plotting                     |
  +--------------------------------------------------------+
  
  </pre></div>
  <p>
  There currently remains some separation between the capabilities of
  displaying one-dimensional data (spectra) and two-dimensional data
  (bit-mapped raster images).  In the past, hardware and software
  limitations enforced a rather strict distinction between vector
  graphics and image display.  This distinction is, however,  becoming fuzzier.
  It is possible to draw any vector graphics to the image
  display (using an <span style="font-family: monospace;">"imd"</span> device and SAOimage).  It is also becoming
  possible to draw gray-scale and color images to some vector graphics
  <span style="font-family: monospace;">"devices"</span> (with the PostScript kernel, for example).  Some tasks
  in the 'stplot' package take advantage of this.
  </p>
  </section>
  <section id="s_general_data_plotting">
  <h3>General data plotting</h3>
  <p>
  Tasks in the 'stplot' package support drawing graphs from IRAF data.
  Several tasks also recognize STSDAS binary tables in addition to the
  various IRAF image formats.
  </p>
  <p>
  The two generic tasks 'igi' and 'sgraph' draw graphs from any recognized
  IRAF data format. (A detailed <span style="font-family: monospace;">"IGI Reference Manual"</span> is available from
  the STSDAS group by sending e-mail requests to: hotseat@stsci.edu).
  </p>
  <p>
  Other tasks provide more specific capabilities such as contour plots,
  labeling of 2-D images with linear or celestial coordinates, drawing
  vector fields and histograms.  The one task specific to HST is 'siaper',
  which draws the science apertures at the telescope's focal plane at
  arbitrary scale and rotation.
  </p>
  <p>
  The 'psikern' GIO kernel allows any IRAF task that produces graphics to
  fully exploit PostScript capabilities, whether printed directly
  to a PostScript printer, saved as encapsulated PostScript (EPS) and
  imported into a document, or rendered on a workstation using a
  PostScript viewer.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sdisplay, stplot, vdisplay, tv, tv.display
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'GENERAL DATA PLOTTING' 'SEE ALSO'  -->
  
