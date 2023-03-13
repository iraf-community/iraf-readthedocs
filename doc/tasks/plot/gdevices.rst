.. _gdevices:

gdevices: List available imaging or other graphics devices
==========================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gdevices
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_devices">
  <dt><b>devices = <span style="font-family: monospace;">"^imt"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='devices' Line='devices = "^imt"' -->
  <dd>A list of patterns identifying the class of devices for which information
  is to be output.  If multiple patterns are given they should be separated
  by commas.  The default pattern matches all stdimage (e.g. IMTOOL) devices.
  </dd>
  </dl>
  <dl id="l_graphcap">
  <dt><b>graphcap = <span style="font-family: monospace;">"graphcap"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphcap' Line='graphcap = "graphcap"' -->
  <dd>The graphcap file to be scanned (any termcap format file will do).  By default
  the graphcap file specified by the graphcap environment variable, usually
  <span style="font-family: monospace;">"dev$graphcap"</span>, is scanned.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>gdevices</b> prints a table of the available devices in a given class of
  devices, giving for each device a list of the aliases by which the device
  is known, the imaging resolution in X and Y, and a short description of the
  device (if present in the graphcap file entry).
  </p>
  <p>
  By default <i>gdevices</i> lists the available stdimage devices as defined in
  the active graphcap file, however, by manipulating the <i>devices</i> and
  <i>graphcap</i> parameters any class of devices in any file can be listed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the available stdimage (e.g. IMTOOL or SAOIMAGE) devices.
  </p>
  <div class="highlight-default-notranslate"><pre>
      cl&gt; gdev
  #                     ALIASES    NX   NY  DESCRIPTION
                           imtx   512  512  Imtool display server
             imt1 imt512 imtool   512  512  Imtool display server
                    imt2 imt800   800  800
                   imt3 imt1024  1024 1024
                   imt4 imt1600  1600 1600
                   imt5 imt2048  2048 2048
                   imt6 imt4096  4096 4096
                                   (etc.)
  </pre></div>
  <p>
  2. List the available IMDKERN devices.
  </p>
  <div class="highlight-default-notranslate"><pre>
      cl&gt; gdev dev=imd
  #                     ALIASES    NX   NY  DESCRIPTION
     imdblack imdbla imdB imdbl  2048 2048
      imdwhite imdwhi imdW imdw  2048 2048
                                   (etc.)
  </pre></div>
  <p>
  3. List the VMS graphics devices.
  </p>
  <div class="highlight-default-notranslate"><pre>
      cl&gt; gdev dev=VMS
  #                     ALIASES    NX   NY  DESCRIPTION
                        iism70v   512  512  NOAO Vela hosted IIS model
                         iism75   512  512  IIS model 75 image display
                          ui300  3130 2370  UNIX interface to the NOAO
                           vver  2112 1636  VMS generic interface to th
                                   (etc.)
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The method used to extract device entries involves multiple scans of the
  graphcap file hence is not very efficient.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  system.devices, dev$graphcap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
