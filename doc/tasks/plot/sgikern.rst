.. _sgikern:

sgikern: Simple graphics interface (SGI) graphics kernel
========================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sgikern input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input metacode files.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"sgimc"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "sgimc"' -->
  <dd>The name of the logical or physical graphics device for which SGI metacode
  is to be generated.
  </dd>
  </dl>
  <dl id="l_generic">
  <dt><b>generic = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='generic' Line='generic = no' -->
  <dd>The remaining parameters are ignored when <b>generic</b> = yes.
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>If <b>debug</b> = yes, the graphics instructions are decoded and printed
  during processing.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If <b>verbose</b> = yes, the elements of polylines, cell arrays, etc. will
  be printed in debug mode.
  </dd>
  </dl>
  <dl id="l_gkiunits">
  <dt><b>gkiunits = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gkiunits' Line='gkiunits = no' -->
  <dd>By default, coordinates are printed in NDC rather than GKI units.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>sgikern</i> translates GKI metacode into a much simpler format and
  then calls up a host system task to dispose of the intermediate file to a
  plotter device.  The SGI kernel can generate as output either an SGI metacode
  file, used to drive laser plotters and pen plotters, or a bitmap file, used
  to drive raster graphics devices.  Both types of files have a very simple
  format, making it straightforward to implement interfaces for new devices.
  </p>
  <p>
  The SGI/SGK <b>metacode format</b> is a sequence of 16 bit integer values encoded
  in the machine independent MII format (twos complement, most significant byte
  first).  The SGI kernel reduces all IRAF plotting instructions to only four
  SGK metacode instructions, i.e.:
  </p>
  <div class="highlight-default-notranslate"><pre>
  opcode  arguments                description
  
     1      0    0                start a new frame
     2      X    Y                move to (x,y)
     3      X    Y                draw to (x,y)
     4      W    0                set line width (&gt;= 1)
  </pre></div>
  <p>
  All coordinates are specified in GKI NDC units in the range 0-32767.  Note that
  all metacode instructions are the same length.  All text generation, line type
  emulation, mark drawing, etc., is done in the higher level IRAF software.
  The metacode file is a standard IRAF random access (non record structured)
  binary file.
  </p>
  <p>
  The <b>bitmap format</b> written by the SGK is even simpler than the metacode
  format.  Output consists either of a single binary raster file containing one
  or more bitmaps with no embedded header information, or a set of binary files
  with the same root name and the extensions .1, .2, etc., each of which contains
  a single bitmap.  All bitmaps the same size.  The size is specified in the
  graphcap entry for the device and may be passed to the host dispose task on
  the foreign task command line if desired.  Page offsets may also be passed on
  the command line, e.g., to position the plot on the plotter page.
  </p>
  <p>
  The following graphcap fields apply to both metacode and bitmap devices.
  </p>
  <div class="highlight-default-notranslate"><pre>
  DD      host command to dispose of metacode file ($F)
  DB      have the kernel print debug messages during execution
  RM      boolean; if present, SGK will delete metacode file
  MF      multiframe count (max frames per job)
  NF      store each frame in a new file (one frame/file)
  RO      rotate plot (swap x and y)
  YF      y-flip plot (flip y axis) (done after rotate)
  </pre></div>
  <p>
  The following additional fields are defined for bitmap devices.
  </p>
  <div class="highlight-default-notranslate"><pre>
  BI      boolean; presence indicates a bitmapped or raster device
  LO      width in device pixels of a line of size 1.0
  LS      difference in device pixels between line sizes
  PX      physical x size of bitmap as stored in memory, bits
  PY      physical y size of bitmap, i.e., number of lines in bitmap
  XO,YO   origin of plotting window in device pixels
  XW,YW   width of plotting window in device pixels
  NB      number of bits to be set in each 8 bit byte output
  BF      bit-flip each byte in bitmap (easier here than later)
  BS      byte swap the bitmap when output (swap every two bytes)
  WS      word swap the bitmap when output (swap every four bytes)
  </pre></div>
  <p>
  The multiframe count (MF) limits the number of frames per job, where a job
  refers to the dispose command submitted to the host to process the frames.
  If the new file flag (NF) is absent, all frames will be stored in the same
  physical file (this holds for both metacode and bitmap frames).  If the new
  file flag (NF) is set, each frame will be stored in a separate file, with
  the N files having the names $F.1, $F.2, ... $F.N, where $F is the unique
  (root) filename generated from the template given in the DD string.  The $F
  is replaced by the root filename, rather than by a list of all the filenames,
  to keep the OS command to a reasonable length and to permit the use of host
  file templates to perform operate upon the full set of files (and to avoid
  having to choose between spaces and commas to delimit the filenames).
  For example, if MF=8 and NF=yes, then <span style="font-family: monospace;">"$F.[1-8]"</span> will match the file set
  on a UNIX host.  The template <span style="font-family: monospace;">"$F.*"</span> is less precise but would also work.
  </p>
  <p>
  The values of graphcap device capability fields may also be substituted
  symbolically when building up the dispose command.  If the sequence
  $(<i>CC</i>) is encountered in the dispose command template, the string
  value of the capability <i>CC</i> will be substituted.  For example, given
  the sequence <span style="font-family: monospace;">"-w $(xr)"</span> and the graphcap capability entry <span style="font-family: monospace;">":xr#1024:"</span>,
  the output sequence would be <span style="font-family: monospace;">"-w 1024"</span>.  This feature is particularly
  useful when several high level device entries include (via <span style="font-family: monospace;">"tc=device"</span>)
  a generic device entry.  The DD string in the generic entry may substitute
  the values of device parameters defined differently in the high level
  entries; this avoids the need to duplicate an almost identical DD string
  in several device entries.
  </p>
  <p>
  The output raster will consist of PY lines each of length PX bits.  If PX is
  chosen to be a multiple of 8, there will be PX/8 bytes per line of the output
  raster.  Note that the values of PX and PY are arbitrary and should be chosen
  to simplify the code of the translator and maximize efficiency.  In particular,
  PX and PY do not in general define the maximum physical resolution of the
  device, although if NB=8 the value of PX will typically approximate the
  physical resolution in X.  If there are multiple bitmap frames per file,
  each frame will occupy an integral number of SPP char units of storage in the
  output file, with the values of any extra bits at the end of the bitmap being
  undefined (a char is 16 bits on most IRAF host machines).
  </p>
  <p>
  The plot will be rasterized in a logical window XW one-bit pixels wide and YW
  pixels high.  The first YO lines of the output raster will be zero, with the
  plotting window beginning at line YO+1.  The first XO bits of each output line
  will be zeroed, with the plotting window beginning at bit XO+1.  The bytes in
  each output line may be bit-flipped if desired, and all of the bits in each
  output byte need not be used for pixel data.  If the bit packing factor NB is
  set to 8 the plotting window will map into XW bits of storage of each output
  line.  If fewer than 8 bits are used in each output byte more than XW physical
  bits of storage will be used, e.g., if NB=4, XW*2 bits of storage are required
  for a line of the plotting window.  The unused bits are set to zero.  The
  translator can later <span style="font-family: monospace;">"or"</span> a mask into the zeroed bits, flip the data bits,
  or perform any other bytewise operation using simple lookup table mapping
  techniques.
  </p>
  <p>
  The DD entry consists of three fields delimited by commas, i.e., the device
  name, including node name (not used at present for this kernel), the VOS
  root filename to be used to make a temporary file to contain the output (note
  that this is NOT a host filename), and lastly the command to be sent to the
  host system to dispose of the output metacode file or bitmap file to the
  plotter device.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert the GIO/GKI metacode file <span style="font-family: monospace;">"dev$mc"</span> into an SGI format metacode file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgikern dev$mc device=sgimc
  </pre></div>
  <p>
  2. The same GIO/GKI metacode file read in the previous example (<span style="font-family: monospace;">"dev$mc"</span>) can
  be plotted on the SGI device <span style="font-family: monospace;">"qms_sgi"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgikern dev$mc device=qms_sgi
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  <span style="font-family: monospace;">"The IRAF Simple Graphics Interface (SGI)"</span>, August 1986
  <br>
  sgidecode, stdgraph, stdplot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
