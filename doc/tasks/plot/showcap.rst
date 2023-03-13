.. _showcap:

showcap: Show and decode graphcap entries
=========================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  showcap
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  None
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Showcap</b> is an interactive, parameterless task that prints and interprets
  entries in the IRAF graphics device capability file dev$graphcap.  These
  entries contain device dimensions, character sizes etc. plus information for 
  encoding and decoding the ASCII control sequences sent to or returned by the
  device.  <b>Showcap</b> is thus mainly used by IRAF programmers for debugging
  new graphcap device entries.
  </p>
  <p>
  At startup <b>showcap</b> prints the following instructions to STDOUT, then
  prompts with an asterisk.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cmd :  `set' device
      |  <span style="font-family: monospace;">`*'</span> (to dump full graphcap entry)
      |  cc [arg1 [arg2 [arg3]]]
      ;
  
  cc  :   a two character capcode (e.g., 'cm')
      |   an encoder program (non alpha first char)
      ;
  *
  </pre></div>
  <p>
  The user must first use `set' to tell <b>showcap</b> which graphics device to
  read from graphcap.  After a `set' or <span style="font-family: monospace;">`*'</span>, the full graphcap entry for the
  named device will be printed.  To view an individual capability, type the
  two-character capability name.
  </p>
  <p>
  Some device capability entries take up to three arguments, which may be 
  listed on the same line after `cc', separated by whitespace.  <b>Showcap</b>
  is particularly useful for decoding the binary encoder entries used by the
  graphics kernels.  See the examples below.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Examine the graphcap entry for the Retrographics vt640.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; showcap
    * set vt640           (dumps vt640 entry)
  </pre></div>
  <p>
  2. Decode the sequence sent to the terminal for setting text height 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  * TH 2
            program:  ^[(1#47+.
            encoding: ^[1
  </pre></div>
  <p>
  3. Decode the sequence sent to the terminal to set line type 3.
  </p>
  <div class="highlight-default-notranslate"><pre>
  * LT 3
            program:  LT=\E/(1$0)1d\E`($1-5)0d\E(1_+.$D)0d\E`($$:\
            encoding: ^[/0d^[b
  </pre></div>
  <p>
  4. Set environment variable <span style="font-family: monospace;">"graphcap"</span> to your local test graphcap file, 
  set device to vt240 and examine the write-cursor (WC) command for
  x-coordinate 150, y-coordinate 350, and cursor 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set graphcap = "mytest.graphcap"
  cl&gt; showcap
    * set vt240           (dumps vt240 entry)
    * WC 150 350 1
              program:  P[(1)%d,(2)%d]
              encoding: P[150,350]
  </pre></div>
  <p>
  5. Examine the scan-cursor function returned when the user types key <span style="font-family: monospace;">`a'</span>
  from coordinate x=150, y=350 after a read-cursor request.
  </p>
  <div class="highlight-default-notranslate"><pre>
  * SC a[150,350]
            program:  (#0!1#0!2,!3,#0!8,#48-!99$0-91#10*9+!1#1!8
                      $$8#1=#-39;#0!8,#48-!99$0-92#10*9+!2#1!8
                      $$8#1=#-39;);
            X(R1)=150 Y(R2)=350, key = a
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Diagnostics are mostly limited to a numeric status return when debugging
  binary encoder entries that contain bugs.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  Graphics I/O Design Document.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
