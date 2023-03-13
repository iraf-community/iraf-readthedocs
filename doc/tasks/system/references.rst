.. _references:

references: Find all help database references for a given topic
===============================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  references topic
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_topic">
  <dt><b>topic</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='topic' Line='topic' -->
  <dd>The topic for which help is desired, i.e., a keyword, phrase, or pattern
  which the help database or quick-reference file is to be searched for.
  </dd>
  </dl>
  <dl id="l_quickref">
  <dt><b>quickref = <span style="font-family: monospace;">"uparm$quick.ref"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='quickref' Line='quickref = "uparm$quick.ref"' -->
  <dd>The name of the optional quick-reference file.
  </dd>
  </dl>
  <dl id="l_updquick">
  <dt><b>updquick = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='updquick' Line='updquick = no' -->
  <dd>Create or update the quick-reference file, e.g., because new packages
  have been added to the global help database.  Updating the quick-reference
  file automatically enables <i>usequick</i>, discussed below.
  </dd>
  </dl>
  <dl id="l_usequick">
  <dt><b>usequick = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='usequick' Line='usequick = no' -->
  <dd>Use the quick-reference file.  By default, a runtime search of all the package
  menus in the full help database is performed, which ensures that all packages
  are searched, but which is comparatively slow.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>references</i> task is used to search the help database for all tasks
  or other help modules pertaining to the given topic, where <i>topic</i> may be
  a keyword, phrase, or any general pattern as would be input to the <i>match</i>
  task.  By default the full help database will be searched.  If desired,
  the <span style="font-family: monospace;">"one-liner"</span> information used for topic searching may be extracted and
  used to prepare a quick-reference file to speed further searches.
  This is not done by default because the help database is too dynamic, e.g., 
  new external packages may be installed at any time, by any user, or new
  tasks may be added to existing packages at any time.
  </p>
  <p>
  References to tasks (or other objects) are printed in the form
  </p>
  <div class="highlight-default-notranslate"><pre>
  keyword1 - one line description
  keyword2 - one line description
  </pre></div>
  <p>
  and so on.  To determine the <i>package pathname</i> of each named task,
  get <i>help</i> on the named <i>keyword</i> and the pathname will be seen at
  the top of the help screen, followed by additional information about the
  referenced object.  If there are multiple objects with the same name,
  a <span style="font-family: monospace;">"help &lt;keyword&gt; all+"</span> may be required to locate a particular one.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Find all help on CCDs.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ref ccd
  </pre></div>
  <p>
  2. Create or update your private quick-reference file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ref upd+
  </pre></div>
  <p>
  3. Examine the quick-reference file to get a summary of all the tasks
  or other help modules in the help database.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page (ref.quickref)
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  If a quick-reference file is used searching takes seconds, otherwise it
  might take a minute or so for the typical large help database containing
  all help modules for the core system and several external, layered packages.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Only the one-liner (NAME) field describing each help module is used for
  the searches.  With a little work searching could be made much more
  comprehensive as well as faster.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  help, match
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
