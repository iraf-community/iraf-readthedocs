.. _fxdummyh:

fxdummyh: Create a dataless single FITS file
============================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxdummyh filename
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_filename">
  <dt><b>filename [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filename' Line='filename [string]' -->
  <dd>The name of your new dataless (NAXIS=0) FITS file.
  </dd>
  </dl>
  <dl id="l_hdr_file">
  <dt><b>hdr_file [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hdr_file' Line='hdr_file [string]' -->
  <dd>The name of your input ascii file containing a FITS like set of keywords and
  values. Each line needs to be standard FITS header keyword of up to 80
  character long per card. The task will take care of padding each card to 80
  characters.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Fxdummyh will create a dataless Primary FITS file with an optional
  user header information.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Create a new dataless FITS file with user FITS header file.
  
          im&gt; fxdummyh file3.fits hdr_file=myhdr.txt
  
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fxcopy,imcopy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
