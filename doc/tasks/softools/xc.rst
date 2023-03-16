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
  <dd>Generates debugging information.
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
  <dt><b>-H</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-H' -->
  <dd>Link a host program as with <span style="font-family: monospace;">"-h"</span>, but include the VOS libraries.
  </dd>
  </dl>
  <dl>
  <dt><b>-A</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-A' -->
  <dd>Force architecture specific include files.
  </dd>
  </dl>
  <dl>
  <dt><b>-C</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-C' -->
  <dd>Link a host program which has a C main.  We may need to tweak the
  command line as a special case here since we normally assume Fortran
  sources.
  </dd>
  </dl>
  <dl>
  <dt><b>-/<i>flag</i>, -//<i>foo</i></b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-/\fIflag\fR, -//\fIfoo\fR' -->
  <dd>Pass <i>flag</i> to host compiler without further
  interpretation. <span style="font-family: monospace;">"-/<i>flag</i><span style="font-family: monospace;">" becomes "</span>-<i>foo</i><span style="font-family: monospace;">", "</span>-//<i>foo</i><span style="font-family: monospace;">"
  becomes "</span><i>foo</i><span style="font-family: monospace;">".
  </dd>
  </dl>
  <dl>
  <dt><b>-D<i>define</i></b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-D\fIdefine\fR' -->
  <dd>Pass a -D<i>define</i> flag on to the host compiler.
  </dd>
  </dl>
  <dl>
  <dt><b>-I<i>dir</i></b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-I\fIdir\fR' -->
  <dd>Pass a -I<i>dir</i> flag on to the host compiler.  A special case is
  <span style="font-family: monospace;">"-Inolibc"</span> which disables automatic inclusion of the IRAF LIBC
  includes (hlib$libc).
  </dd>
  </dl>
  <dl>
  <dt><b>-l<i>lib</i>, -L<i>dir</i></b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-l\fIlib\fR, -L\fIdir\fR' -->
  <dd>This tells the linker which library files or library directories
  besides the standard ones to include.  These must be either on the current
  directory, or in an IRAF system library (lib$ or hlib$).
  The library specification must be immediately after the option as in
  <span style="font-family: monospace;">"-lxtools"</span>.  No other option may follow the <span style="font-family: monospace;">'l'</span> option in the same
  argument as in -lxtoolsO.
  </dd>
  </dl>
  <dl>
  <dt><b>-N</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-N' -->
  <dd>Generates the output temp file in /tmp during the link, then moves it
  to the output directory in one operation when done.  For cases such as
  linking in an NFS-mounted directory, where all the NFS i/o may slow
  the link down excessively.
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
  <dt><b>-x</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-x' -->
  <dd>Compile and link for debugging.
  </dd>
  </dl>
  <dl>
  <dt><b>-z</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-z' -->
  <dd>Create a non-shareable image (default).
  </dd>
  </dl>
  <dl>
  <dt><b>-V</b></dt>
  <!-- Sec='FLAGS' Level=0 Label='' Line='-V' -->
  <dd>Print XC version identification.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XC is a machine independent utility for compiling and linking IRAF
  tasks or files.  The XC utility may also be used to compile and/or
  link non-IRAF files and tasks. It can be used to generate fortran from
  xpp or ratfor code, to compile any number of files, and then link them
  if desired.  XC accepts and maps IRAF virtual filenames, but since it
  is a standalone bootstrap utility the environment is not passed, hence
  logical directories cannot be used.
  </p>
  <p>
  It is suggested that everyone stick with the iraf virtual file name extensions.
  These are : .x, .r, .f, .c, .s, .o, .a, .e.
  The meaning of these is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  .x  SPP code
  .r  Ratfor code
  .f  Fortran code
  .c  C code
  .s  Macro assembler code
  .o  Object module
  .a  Library file
  .e  Executable Image
  </pre></div>
  <p>
  XC is available both in the CL and as a standalone task.
  Usage is equivalent in either case.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
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
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkpkg, generic
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'FLAGS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
