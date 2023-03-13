.. _logout:

logout: Log out of the CL
=========================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  logout
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Logout</i> causes the CL to shut itself down, regardless of how many
  packages may currently be active.  The only way to shut the CL down without
  killing it is to use <i>logout</i>; <i>bye</i> is not allowed to shut the
  CL down, since it would be too easy to enter it by accident (and it takes
  a while to log back in).
  </p>
  <p>
  An error message will be printed if one attempts to log out of the CL while
  a device is still allocated.  The device should be deallocated and the
  <i>logout</i> repeated, else type <i>logout</i> several times and you will
  be permitted to logout with the device still allocated.
  </p>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  1. Logout of the CL.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; logo
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  deallocate, bye
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLE' 'SEE ALSO'  -->
  
