.. _netstatus:

netstatus: Print the status of the local network
================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  netstatus
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  None.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Netstatus</i> prints the status of the local network as perceived by the
  system process x_system.e (the network status may differ for each subprocess).
  The status output identifies the local node, lists all nodes in the local
  network, and lists all the aliases (recognized names) for each node.
  A message will be printed if networking is disabled on the local machine.
  The local network is defined by the table files <span style="font-family: monospace;">"dev$hosts"</span>, <span style="font-family: monospace;">"dev$uhosts"</span>,
  and <span style="font-family: monospace;">"dev$hostlogin"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; netstatus
  Local node `draco' (5), default node `draco', 12 nodes in local network
  
      NODE SERVER NREFS STATUS  ALIASES
         1      0     0  00000  aquila vax1 a 1 class1 plot print
         2      0     0  00000  lyra vax2 b 2 class2
         3      0     0  00000  vela vax3 3 v class3
         4      0     0  00000  carina vax5 c 5 class5
         5      0     0  00000  draco vax6 6 d class6 0
         6      0     0  00000  tucana sun1 t
         7      0     0  00000  hydra sun2 h
         8      0     0  00000  mensa pc1 m
         9      0     0  00000  pictor pc2
        10      0     0  00000  octans sun3 o
        11      0     0  00000  pavo mvax1 p
        12      0     0  00000  volans lsi1
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
