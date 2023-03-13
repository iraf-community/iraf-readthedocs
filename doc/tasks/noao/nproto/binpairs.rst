.. _binpairs:

binpairs: Bin pairs of (x,y) points in log separation
=====================================================

**Package: nproto**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  binpairs file1 file2 rmin rmax nbins
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_file1">
  <dt><b>file1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file1' Line='file1' -->
  <dd>File containing (x,y) points to be paired.
  </dd>
  </dl>
  <dl id="l_file2">
  <dt><b>file2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file2' Line='file2' -->
  <dd>File containing (x,y) points to be paired.  This file may be the same
  as file1.
  </dd>
  </dl>
  <dl id="l_rmin">
  <dt><b>rmin</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmin' Line='rmin' -->
  <dd>The minimum separation to be binned.
  </dd>
  </dl>
  <dl id="l_rmax">
  <dt><b>rmax</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmax' Line='rmax' -->
  <dd>The maximum separation to be binned.
  </dd>
  </dl>
  <dl id="l_nbins">
  <dt><b>nbins</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbins' Line='nbins' -->
  <dd>The number of log separation bins to be computed.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print progress information?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The (x,y) points in the specified files are paired and the number of pairs
  in each bin of log separation is computed and output.  The two files may
  be the same.  There are
  <i>nbins</i> separation bins between the separations <i>rmin</i> and <i>rmax</i>.
  If the verbose parameter is yes then progress information is printed on the
  standard error output at intervals of 5% of the time.
  The output consists of the lower limit of the separation bin, the number of
  pairs in the bin, the number of pairs divided by the total number of pairs,
  and the annular area of the bin.
  </p>
  <p>
  This task is useful for computing two point correlation functions.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; binpairs data1 data2 .01 1 20 &gt;&gt; result
  
          or
  
  cl&gt; binpairs data data .01 1 20 &gt;&gt; result
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
