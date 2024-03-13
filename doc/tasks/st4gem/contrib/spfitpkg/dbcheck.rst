.. _dbcheck:

dbcheck: Check format of specfit database files
===============================================

**Package: spfitpkg**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dbcheck database
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>This is the name of the database file to be checked.  The file is assumed to
  have a leading <span style="font-family: monospace;">"sf"</span> prefix and to reside in the current directory.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Dbcheck will check a database 
  file to make sure that it is in a format readable by specfit.  It will also
  check for any minor inconsistencies in the data such as a lower 
  limit with a higher value than the actual parameter.  Please note 
  that the <span style="font-family: monospace;">"sf"</span> extension at the beginning of every specfit database file 
  will be added by the program.  It will also take file name expanders 
  like asterisks.  For example, typing <span style="font-family: monospace;">"h*"</span> for the database name will 
  check all files in the current directory starting with <span style="font-family: monospace;">"sfh"</span>.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION'  -->
  
