.. _cd:

cd: Change directory
====================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  chdir [newdir]  or  cd [newdir]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_newdir">
  <dt><b>newdir</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newdir' Line='newdir' -->
  <dd>The new working directory.
  The special name <span style="font-family: monospace;">"."</span> refers to the current directory; <span style="font-family: monospace;">".."</span> refers to the next
  higher directory.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Chdir</i> is used to change the current working directory.
  When called without any arguments, <i>chdir</i> sets the default directory
  to <span style="font-family: monospace;">"home$"</span>, the users home directory.
  The new directory can be specified as an IRAF logical name,
  as a sub-directory of the current directory,
  as a path from either a logical directory or the current directory,
  or as an operating system dependent name.
  </p>
  <p>
  The names <i>chdir</i> and <i>cd</i> are synonyms.  Note that the command
  <i>back</i> may be called after a <i>chdir</i> to return to the previous
  directory without typing its name.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Return to our home directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd
  </pre></div>
  <p>
  2. Go to the package logical directory <span style="font-family: monospace;">"pkg$"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; chdir pkg
  </pre></div>
  <p>
  3. Go down one level to the directory <span style="font-family: monospace;">"dataio"</span>, a subdirectory of <span style="font-family: monospace;">"pkg"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd dataio
  </pre></div>
  <p>
  4. From <span style="font-family: monospace;">"dataio"</span>, go back up to <span style="font-family: monospace;">"pkg"</span> and down into <span style="font-family: monospace;">"images"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd ../images
  </pre></div>
  <p>
  5. Go to the <span style="font-family: monospace;">"tv"</span> directory, a subdirectory of <span style="font-family: monospace;">"images"</span>, regardless of the
  current directory
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd pkg$images/tv
  </pre></div>
  <p>
  6. On a VMS system, define a new logical directory on a different disk device
  and go there.  Note that the character $ is not permitted in host file or
  directory names.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set dd = scr1:[data]
  cl&gt; cd dd
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  back, pathnames
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
