.. _mscblkavg:

mscblkavg: Block average mosaic exposures with header keyword updating
======================================================================

**Package: msctools**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  This task block averages mosaic exposures by specified block factors.
  It updates the RDNOISE, GAIN, CCDSUM, DATASEC, BIASSEC, TRIMSEC, and
  CCDSEC parameters.  The output pixel type is the same as the input
  pixel type.  For this reason block averaging of raw unsigned short
  data may lead to undersampling the noise.  The output name maybe the
  same as the input name to replace the input by the block average output.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mscblkavg input output nc nl
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Block average a set exposures.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscblkavg obj*fits bav//obj*fits 2 2
  </pre></div>
  <p>
  2. Block average in place a set of exposures.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscblkavg obj*fits obj*fits 2 2
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCBLKAVG">
  <dt><b>MSCBLKAVG</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCBLKAVG' Line='MSCBLKAVG' -->
  <dd>First release in MSCRED V2.0.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  msccmd, blkavg
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
