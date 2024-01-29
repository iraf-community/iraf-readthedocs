.. _msczero:

msczero: Display, measure coordinates, set WCS zeropoint offsets
================================================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  If the specified Mosaic exposure is not in the display it is displayed.
  The cursor is used to report WCS coordinates (space bar).  Pointing at a
  star and typing <span style="font-family: monospace;">'z'</span> applys a centering to the star data, reports the
  coordinate based on the current WCS, and queries for a corrected
  coordinate.  The difference between the current and corrected coordinate is
  used to compute an offset to the current WCS.  When <span style="font-family: monospace;">'q'</span> is typed the last
  offset may be recorded in the parameters for <b>mscwcs</b> for adjusting
  other exposures and it can be used to update the WCS of the image.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  msczero images
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
  <dl id="l_MSCZERO">
  <dt><b>MSCZERO - V2.11 external package</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCZERO' Line='MSCZERO - V2.11 external package' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mscdisplay mscexamine mscwcs
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
