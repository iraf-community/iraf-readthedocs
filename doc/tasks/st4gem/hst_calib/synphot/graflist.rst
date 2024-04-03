.. _graflist:

graflist: List the components downstream from a given component.
================================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  graflist grftable compname
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task prints the names of all components downstream from a specified
  component.  The specified component is called the <span style="font-family: monospace;">"root"</span>.  A component is
  downstream from the root if a path passes through both the component and
  the root and the root occurs first in the path.  A root is always considered
  to be downstream from itself, so at least one component name will be 
  printed whenever this task is run.
  </p>
  <p>
  The list of component names is printed in the order they occur along the
  path.  When component names are printed, each component name is indented
  to show the distance between it and the root.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_grftable">
  <dt><b>grftable = <span style="font-family: monospace;">"mtab$*.tmg"</span> [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grftable' Line='grftable = "mtab$*.tmg" [file name]' -->
  <dd>The name of the graph table to be listed. If a filename template is
  specified, the task will list from the most recent graph table
  matching the template. 
  </dd>
  </dl>
  <dl id="l_compname">
  <dt><b>compname [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='compname' Line='compname [string]' -->
  <dd>The name of the root component. All components downstream from the root
  component are listed. The component name is not case sensitive and leading
  or trailing white space will not affect the match. If more than one component
  in the graph matches 'compname', the component with the smallest value in
  the 'INNODE' column will be used. (The 'INNODE' and 'OUTNODE' columns are
  used to navigate through the graph table).  The user can make the component
  name unique by optionally specifying an 'INNODE' number as part of the 
  value passed to 'compname'.  The desired 'INNODE' number follows the component
  name, separated by a white space.  If no value is passed to 'compname', the
  entire graph will be listed.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List all components that are downstream from <span style="font-family: monospace;">"hrs_echa"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; graflist hstgraph.tab hrs_echa
  </pre></div>
  <p>
  2. List all components that are downstream from clear, where 'INNODE=1000':
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; graflist hstgraph.tab "clear 1000"
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  grafpath, grafplot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  
