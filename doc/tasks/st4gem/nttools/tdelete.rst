.. _tdelete:

tdelete: Delete tables.
=======================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tdelete table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task deletes tables.
  The input may be a general filename template,
  including wildcard characters, or the name of a list file
  (preceded by the <span style="font-family: monospace;">"@"</span> character) containing table names.
  </p>
  <p>
  The task checks that the file to be deleted really is a table
  before deleting it.
  In order to protect against accidental deletion of files other than tables,
  text tables may be deleted using 'tdelete' only if 'verify = yes'.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>A list of one or more tables to be deleted.
  </dd>
  </dl>
  <dl>
  <dt><b>(verify = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verify = no) [boolean]' -->
  <dd>Prompt for confirmation before deleting?  It is possible to delete
  text tables using 'tdelete' if 'verify' is set to <span style="font-family: monospace;">"yes"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(default_action = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(default_action = yes) [boolean]' -->
  <dd>Default action for the verify query.  If 'default_action = yes', then the
  prompt will come back with <span style="font-family: monospace;">"yes?"</span> and striking return will proceed with
  the delete.
  </dd>
  </dl>
  <dl id="l_go_ahead">
  <dt><b>go_ahead = yes [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='go_ahead' Line='go_ahead = yes [boolean]' -->
  <dd>This is a copy of 'default_action' used for prompting if 'verify = yes'.
  This parameter is set by the task, it copies the value of 'default_action',
  but cannot be directly set by the user.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Delete a single table.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tdelete table
  </pre></div>
  <p>
  2. Delete several tables.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tdelete table1,table2,tab67
  cl&gt; tdelete *.tab,a,b,c
  </pre></div>
  <p>
  In the latter case, the extension is given explicitly because there may be
  other files beginning with <span style="font-family: monospace;">"tab"</span> that are not tables.
  </p>
  <p>
  3. Delete a list of tables using verify.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tdelete fits*.tab ver+
  cl&gt; delete table `fits1.tab' ? (yes): yes
  cl&gt; delete table `fits2.tab' ? (yes): yes
  cl&gt; delete table `fits3.tab' ? (yes): yes
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Text tables cannot be deleted by 'tdelete' unless 'verify' is set to yes.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Phil Hodge.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  delete, tcopy, trename
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
