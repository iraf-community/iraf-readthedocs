.. _aslist:

aslist: List the supported image surveys
========================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  aslist catalogs
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_imsurveys">
  <dt><b>imsurveys</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imsurveys' Line='imsurveys' -->
  <dd>The names of the image surveys to be listed. If surveys = <span style="font-family: monospace;">"*"</span> then
  all the image surveys in the image survey configuration file are listed.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>List the image survey wcs and keyword information  after the image survey
  name ?
  </dd>
  </dl>
  <dl id="l_imdb">
  <dt><b>imdb = <span style="font-family: monospace;">")_.imdb"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imdb' Line='imdb = ")_.imdb"' -->
  <dd>The image survey configuration file. The value of imdb defaults to the value
  of the package parameter of the same name. The default image survey
  configuration file is <span style="font-family: monospace;">"astcat$lib/imdb.dat"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Aslist lists the supported image surveys specified by the
  <i>imsurveys</i> parameter. If imsurveys = <span style="font-family: monospace;">"*"</span> then all the supported image
  surveys are listed, otherwise only the image survey names specified by the
  user are listed. Valid image survey names have the form imsurvey@site, e.g.
  <span style="font-family: monospace;">"dss1@cadc"</span>.  If <i>verbose</i> = <span style="font-family: monospace;">"yes"</span>, then the image survey wcs and
  keyword information is listed after the image survey name.
  </p>
  <p>
  The image survey names, addresses, query formats, output formats, wcs formats,
  and keyword formats, are specified in the image survey configuration file
  <i>imdb</i>. By default the image survey configuration file names defaults to
  the value of the imdb package parameters. The default image survey
  configuration file is <span style="font-family: monospace;">"astcat$lib/imdb.dat"</span>.  Users can add records
  to this file or create their own configuration file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List all the image surveys in the image survey configuration file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aslist *
  </pre></div>
  <p>
  2. List the wcs and keyword information for the dss1@cadc image survey.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aslist dss1@cadc verbose+
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  aclist
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
