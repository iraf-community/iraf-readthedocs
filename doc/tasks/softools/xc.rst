.. _xc:

xc: Compile and/or link a program
=================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xc [flags] files
  </p>
  </section>
  <section id="s_flags">
  <h3>Flags</h3>
  <dl>
  <dt><b>-a</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-a' -->
  <dd>To support VMS link options file.  Next file is taken to be the VMS name
  of a link options file.  This is primarily for using long lists of files
  or libraries and not for actual VMS Linker options, since XC adds continuation
  characters where it believes it is appropriate.
  </dd>
  </dl>
  <dl>
  <dt><b>-C</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-C' -->
  <dd>Tells fortran to do array bound and other checking.
  By default no checking is done.  From DCL fortran usually
  does array and overflow checking which is not used here.
  </dd>
  </dl>
  <dl>
  <dt><b>-c</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-c' -->
  <dd>Tells <i>xc</i> not to link, i.e., not to create an executable.
  </dd>
  </dl>
  <dl>
  <dt><b>-d</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-d' -->
  <dd>Causes debug messages to be printed during execution.
  </dd>
  </dl>
  <dl>
  <dt><b>-F, -f</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-F, -f' -->
  <dd>Do not delete the Fortran translation of an SPP source file.
  </dd>
  </dl>
  <dl>
  <dt><b>-g</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-g' -->
  <dd>Generates debugging information and (for VMS), links in the debugger.
  </dd>
  </dl>
  <dl>
  <dt><b>-h</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-h' -->
  <dd>Causes the executable to be linked as a host program, i.e., without the
  IRAF main and without searching the IRAF libraries, unless explicitly
  referenced on the command line.  Used to compile and link host (e.g., Fortran)
  programs which may or may not reference the IRAF libraries.
  </dd>
  </dl>
  <dl>
  <dt><b>-i2</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-i2' -->
  <dd>Tells fortran to use I*2 by default.
  </dd>
  </dl>
  <dl>
  <dt><b>-i4</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-i4' -->
  <dd>Tells fortran to use I*4 by default.
  </dd>
  </dl>
  <dl>
  <dt><b>-l<i>lib</i></b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-l\fIlib\fR' -->
  <dd>This tells the linker which libraries besides the standard
  ones to include.  These must be either on the current
  directory, or in an IRAF system library (lib$ or hlib$).
  The library specification must be immediately after the option as in
  <span style="font-family: monospace;">"-lxtools"</span>.  No other option may follow the <span style="font-family: monospace;">'l'</span> option in the same
  argument as in -lxtoolsO.	
  </dd>
  </dl>
  <dl>
  <dt><b>-L</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-L' -->
  <dd>Creates a list file. VMS specific.
  </dd>
  </dl>
  <dl>
  <dt><b>-M, -m</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-M, -m' -->
  <dd>Tells the linker to create a link map.
  </dd>
  </dl>
  <dl>
  <dt><b>-n</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-n' -->
  <dd>Not really supported under VMS since <span style="font-family: monospace;">"normal"</span> users
  cannot install images.  In Unix this is just a link
  option to make a shareable image.
  </dd>
  </dl>
  <dl>
  <dt><b>-N</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-N' -->
  <dd>Same as -z for VMS.
  </dd>
  </dl>
  <dl>
  <dt><b>-Nh [filename]</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-Nh [filename]' -->
  <dd>This tells xpp that the foreign definitions in the
  file specified should be used in preference to
  standard include files.	
  </dd>
  </dl>
  <dl>
  <dt><b>-o</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-o' -->
  <dd>This flag redirects the output of the compile if used in
  conjunction with -c option or specifies where the executable
  or object is to be placed.  If not given the first file
  name is used to obtain the name for the executable or
  object.
  </dd>
  </dl>
  <dl>
  <dt><b>-O</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-O' -->
  <dd>Optimize object code produced; this is now the default, but this switch
  is still provided for backwards compatibility.
  </dd>
  </dl>
  <dl>
  <dt><b>-p pkgname</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-p pkgname' -->
  <dd>Load the package environment for the named external package, e.g.,
  <span style="font-family: monospace;">"xc -c -p noao file.x"</span>.  If the same package is always specified
  the environment variable or logical name PKGENV may be defined at the
  host level to accomplish the same thing.  The package name <i>must</i>
  be specified when doing software development in an external or layered
  package.
  </dd>
  </dl>
  <dl>
  <dt><b>-P</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-P' -->
  <dd>Check portability.  This should be used all of the time in IRAF,
  but the VMS C compiler forces the use of non-standard
  constructs in some cases.  Also &lt;stdio.h&gt; and &lt;ctype.h&gt; get
  complaints for the above reason.  This may be used and probably
  should when working with Fortran due to Dec non-standard
  extension.
  </dd>
  </dl>
  <dl>
  <dt><b>-q</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-q' -->
  <dd>Disable optimization.  Opposite of -O.  Object code will be optimized
  by default.
  </dd>
  </dl>
  <dl>
  <dt><b>-s</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-s' -->
  <dd>Strips all symbols and debugging information.
  </dd>
  </dl>
  <dl>
  <dt><b>-S</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-S' -->
  <dd>Same as -s for VMS.
  </dd>
  </dl>
  <dl>
  <dt><b>-v</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-v' -->
  <dd>Verbose mode.  Causes messages to be printed during execution telling
  what the <i>xc</i> program is doing.
  </dd>
  </dl>
  <dl>
  <dt><b>-w</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-w' -->
  <dd>Suppress warnings.				
  </dd>
  </dl>
  <dl>
  <dt><b>-X, -x</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-X, -x' -->
  <dd>Compile and link for debugging.  In VMS/IRAF, links in the VMS debugger
  and symbols.
  </dd>
  </dl>
  <dl>
  <dt><b>-z</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-z' -->
  <dd>Create a non-shareable image (default).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XC is a machine independent utility for compiling and linking IRAF
  tasks or files.  The XC utility may also be used to compile and/or link
  non-IRAF files and tasks.  The VMS version of XC supports all of the
  important flags except -D which VMS C doesn't support in any way.
  It can be used to generate fortran from xpp or ratfor code, to compile any
  number of files, and then link them if desired.  XC accepts and maps IRAF
  virtual filenames, but since it is a standalone bootstrap utility the
  environment is not passed, hence logical directories cannot be used.
  </p>
  <p>
  The following extensions are supported by the VMS version of xc:
  It is suggested that everyone stick with the iraf virtual file name extensions.
  These are : .x, .r, .f, .c, .s, .o, .a, .e. The mapping of these to their
  VMS counterparts is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  .x -&gt; .x    SPP code
  .r -&gt; .r    Ratfor code
  .f -&gt; .for  Fortran code
  .c -&gt; .c    C code
  .s -&gt; .mar  Macro assembler code
  .o -&gt; .obj  Object module
  .a -&gt; .olb  Library file
  .e -&gt; .exe  Executable Image
  </pre></div>
  <p>
  XC is available both in the CL, via the foreign task interface, and as
  a standalone DCL callable task.  Usage is equivalent in either case.  Upper
  case flags must be quoted to be recognized (the upper case flags will be
  done away with at some point).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Any upper case flags in the following examples must be doubly quoted in
  the CL, singly quoted in VMS, to make it to XC without VMS mapping
  everything to one case.  Omit the <span style="font-family: monospace;">"-x"</span> flag on a UNIX system.
  </p>
  <p>
  1. Compile and link the source file <span style="font-family: monospace;">"mytask.x"</span> to produce the executable
  <span style="font-family: monospace;">"mytask.e"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xc mytask.x
  </pre></div>
  <p>
  2. Translate the file <span style="font-family: monospace;">"file.x"</span> into Fortran.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xc -f file.x
  </pre></div>
  <p>
  3. Compile but do not link <span style="font-family: monospace;">"mytask.x"</span> and the support file <span style="font-family: monospace;">"util.x"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xc -c file.x util.x
  </pre></div>
  <p>
  4. Now link these for debugging.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xc -x file.o util.o
  </pre></div>
  <p>
  5. Link the same files without the VMS debug stuff, but link in the library
  -ldeboor (the DeBoor spline routines) as well.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xc file.o util.o -ldeboor
  </pre></div>
  <p>
  XC is often combined with <i>mkpkg</i> to automatically maintain large packages
  or libraries.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The -S flag should generate assembler
  output but does not presently do so in the VMS version.  All case sensitive
  switches should be done away with in both the UNIX and VMS versions of the
  utility.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkpkg, generic
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'FLAGS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
