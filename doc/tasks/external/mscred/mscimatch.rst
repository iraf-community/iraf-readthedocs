.. _mscimatch:

mscimatch: Match intensity scales in reconstructed mosaic images
================================================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  A list of celestial coordinates is used to select square regions in images
  to measure.  The mean values in the box and in a larger square region
  around the box are determined.  A linear fit between the values for
  a reference image and a target image is computed.  The zero point
  offset and multiplicative scale factor which match the target image
  intensities to the reference image intensities is recorded in the
  image header for later use by <b>mscstack</b>.  The task can be
  used in various levels interactivity or non-interactively.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mscimatch input coords
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
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCIMATCH">
  <dt><b>MSCIMATCH - V2.11 external package</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCIMATCH' Line='MSCIMATCH - V2.11 external package' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  msczero, mscstack
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
