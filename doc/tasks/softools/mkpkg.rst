.. _mkpkg:

mkpkg: Make or update an object library or package
==================================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkpkg [switches] [module ...] [name=value ...]
  </p>
  </section>
  <section id="s_arguments">
  <h3>Arguments</h3>
  <dl>
  <dt><b><b>-d[ddd]</b></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fB-d[ddd]\fR' -->
  <dd>Debug mode.  Print detailed messages describing what <i>mkpkg</i> is doing.
  There are four levels of debug messages, selected by repeating the <span style="font-family: monospace;">"d"</span>
  character in the switch, e.g., <span style="font-family: monospace;">"-d"</span> is level one, <span style="font-family: monospace;">"-dd"</span> is level two, and
  so on.  The debug messages get progressively more detailed as the debug level
  increases.  Debug mode automatically enables the verbose mode messages.
  </dd>
  </dl>
  <dl>
  <dt><b><b>-f </b><i>file</i></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fB-f \fIfile\fR' -->
  <dd>Set the name of the file to be interpreted (default: <span style="font-family: monospace;">"mkpkg"</span>).
  The special value <span style="font-family: monospace;">"stdin"</span> (lower case) allows commands to be entered
  interactively from the standard input, e.g., for debugging <i>mkpkg</i>.
  </dd>
  </dl>
  <dl>
  <dt><b><b>-i</b></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fB-i\fR' -->
  <dd>Ignore errors.  Execution continues even if an error occurs.
  </dd>
  </dl>
  <dl>
  <dt><b><b>-n</b></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fB-n\fR' -->
  <dd>No execute.  Go through the motions, but do not touch any files.
  No execute mode automatically enables verbose mode (flag <span style="font-family: monospace;">"-v"</span>).
  This switch should be used to verify new mkpkg files before execution.
  </dd>
  </dl>
  <dl>
  <dt><b><b>-p </b><i>pkgname</i></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fB-p \fIpkgname\fR' -->
  <dd>Load the package environment for the named external package, e.g.,
  <span style="font-family: monospace;">"mkpkg -p noao update"</span>.  If the same package is always specified
  the environment variable or logical name PKGENV may be defined at the
  host level to accomplish the same thing.  The package name <i>must</i>
  be specified when doing software development in an external or layered
  package.
  </dd>
  </dl>
  <dl>
  <dt><b><b>-v</b></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fB-v\fR' -->
  <dd>Verbose mode.  A message is printed whenever a file is touched.
  Recommended when running large mkpkg jobs in batch mode.
  </dd>
  </dl>
  <dl>
  <dt><b><b>-x</b>, <b>-g</b></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fB-x\fR, \fB-g\fR' -->
  <dd>Define the symbol <span style="font-family: monospace;">"DEBUG"</span> to build for debugging.
  </dd>
  </dl>
  <dl>
  <dt><b><b>module</b></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fBmodule\fR' -->
  <dd>The names of the module or modules (named entries in the <span style="font-family: monospace;">"mkpkg"</span> file) to be
  executed.  If no module is named the first module encountered is executed,
  unless a <i>mkpkg</i> macro preprocessor directive at the beginning of the file
  specifies a different default action.
  </dd>
  </dl>
  <dl>
  <dt><b><b>name=value [name=value...]</b></b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='\fBname=value [name=value...]\fR' -->
  <dd>Enter the named symbol/value pair into the symbol table of the <i>mkpkg</i>
  macro preprocessor.  The symbols <i>XFLAGS</i> (for the XC compiler) and
  <i>LFLAGS</i> (for the linker) are predefined but may be redefined on the
  command line.  Case is ignored in symbol names for portability reasons.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>mkpkg</i> utility is used to make or update IRAF packages or libraries.
  <i>Mkpkg</i> is used to bootstrap the IRAF system hence is implemented as
  a foreign task, callable either from within the IRAF environment or from the
  host system.  Usage is identical in either case (except that the details of
  when a particular argument may need to be quoted will vary depending on the
  command language used).  <i>Mkpkg</i> is upwards compatible with the old
  <i>mklib</i> utility.
  </p>
  <p>
  1. <b>Introduction</b>
  </p>
  <p>
      <i>Mkpkg</i> provides two major facilities: a library update capability and
  a macro preprocessor.  The macro preprocessor provides symbol definition and
  replacement, conditional execution, and a number of builtin commands.
  The usefulness of these facilities is enhanced by the ability of <i>mkpkg</i>
  to update entire directory trees, or to enter the hierarchy of <i>mkpkg</i>
  descriptors at any level.  For example, typing <span style="font-family: monospace;">"mkpkg"</span> in the root directory
  of IRAF will make or update the entire system, whereas in the <span style="font-family: monospace;">"iraf$sys"</span>
  directory <i>mkpkg</i> will update only the system libraries, and in the
  <span style="font-family: monospace;">"iraf$sys/fio"</span> directory <i>mkpkg</i> will update only the FIO portion of the
  system library <span style="font-family: monospace;">"libsys.a"</span>.
  </p>
  <p>
  The <i>mkpkg</i> utility is quite simple to use to maintain small packages
  or libraries, despite the complexity of the discussion which follows.
  The reader is encouraged to study several examples of working mkpkg-files
  before reading further; examples will be found throughout the IRAF system.
  The mkpkg files for applications packages tend to be very similar to one
  another, and it is quite possible to successfully copy and modify the
  mkpkg-file from another package without studying the reference information
  given here.
  </p>
  <p>
  2. <b>Lexical Conventions</b>
  </p>
  <p>
      The lexical conventions employed in <i>mkpkg</i> are those used throughout
  IRAF.  Comments may occur anywhere, begin with the character #, and extend
  to the end of the current line.  Blank lines are ignored virtually everywhere.
  Newline may be escaped with backslash to continue on the next line.
  All filenames are IRAF virtual filenames with the following extensions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  .a              object library
  .c              C source
  .e              executable (e.g., "x_package.e")
  .f              Fortran source
  .gc             generic C source
  .gx             generic SPP source
  .h              C or SPP header file
  .inc            include file
  .l              Lex source
  .o              object file
  .r              Ratfor source
  .s              assembler source
  .y              Yacc source
  </pre></div>
  <p>
  Since <i>mkpkg</i> is an IRAF utility it recognizes the major IRAF logical
  directories; these are summarized in the list below.  The IRAF (or UNIX)
  pathname convention is used to specify pathnames rooted in the current
  directory or a logical directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  bin$            installed executables           iraf$bin/
  dev$            device tables                   iraf$dev/
  hlib$           machdep header files            host$hlib/
  host$           host system interface           [MACHDEP]
  iraf$           the root directory of IRAF      [MACHDEP]
  lib$            system library                  iraf$lib/
  math$           math sources                    iraf$math/
  pkg$            applications packages           iraf$pkg/
  sys$            the VOS, system libraries       iraf$sys/
  tmp$            where temporary files go        [MACHDEP]
  </pre></div>
  <p>
  All other directories should be referenced by giving the path from either the
  current directory or from one of the system logical directories shown above.
  For example, <span style="font-family: monospace;">"pkg$system/"</span> is the root directory of the SYSTEM package,
  and <span style="font-family: monospace;">".."</span> is the directory one level up from the current directory.
  </p>
  <p>
  3. <b>Maintaining Libraries with MKPKG</b>
  </p>
  <p>
      Libraries are described by a <b>member list</b> module in the <span style="font-family: monospace;">"mkpkg"</span> file.
  The syntax of a library member list module is shown below.  Note that the
  <b>mkpkg</b> module name for a library member list module is the same as the
  name of the actual library, hence must end with the extension <span style="font-family: monospace;">".a"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  libname.a:
          member1         dep1 dep2 ... depN
          member2         dep1 dep2 ... depN
            ...
          memberN         dep1 dep2 ... depN
          ;
  </pre></div>
  <p>
  Here, <span style="font-family: monospace;">"libname.a"</span> is the IRAF virtual filename of the library (regardless of
  what directory it resides in), <span style="font-family: monospace;">"memberN"</span> is the name of a source file which
  may contain any number of actual library object modules, and <span style="font-family: monospace;">"depN"</span> is the
  name of a file upon which the named member depends.  If any of the named
  dependency files is newer than the corresponding member source file, or if
  the member source file is newer than the compiled library object module,
  the source file is recompiled and replaced in the library.  Both source
  files and dependency files may reside in remote directories.  The names of
  dependency files in system libraries should be enclosed in &lt;&gt; delimiters,
  e.g., <span style="font-family: monospace;">"&lt;fset.h&gt;"</span>.  Each member must be described on a separate line.
  </p>
  <p>
  If the library being updated does not reside in the current directory
  (directory from which the <span style="font-family: monospace;">"mkpkg"</span> command was entered) then the library must
  be <span style="font-family: monospace;">"checked out"</span> of the remote directory before it can be updated, and checked
  back in when updating is complete.  These operations are performed by macro
  preprocessor directives, e.g.:
  </p>
  <div class="highlight-default-notranslate"><pre>
  $checkout libsys.a lib$
  $update   libsys.a
  $checkin  libsys.a lib$
  $exit
  
  libsys.a:
          @symtab         # update libsys.a in ./symtab
          brktime.x       &lt;time.h&gt;
          environ.x       environ.com environ.h &lt;ctype.h&gt;\
                          &lt;fset.h&gt; &lt;knet.h&gt;
          main.x          &lt;clset.h&gt; &lt;config.h&gt; &lt;ctype.h&gt;\
                          &lt;error.h&gt; &lt;fset.h&gt; &lt;knet.h&gt;\
                          &lt;printf.h&gt; &lt;xwhen.h&gt;
          onentry.x       &lt;clset.h&gt; &lt;fset.h&gt; &lt;knet.h&gt;
          spline.x        &lt;math.h&gt; &lt;math/interp.h&gt;
          ;
  </pre></div>
  <p>
  Note that the checkout operation is required only in the directory from which
  the <span style="font-family: monospace;">"mkpkg"</span> command was entered, since the library has already been checked
  out when the mkpkg-file in a subdirectory is called to update its portion
  of the library (as in the <span style="font-family: monospace;">"@symtab"</span> in the example above).  The checkout
  commands should however be included in each mkpkg-file in a hierarchy in such
  a way that the library will be automatically checked out and back in if
  <i>mkpkg</i> is run from that directory.  The checkout commands are ignored
  if the mkpkg-file is entered when updating the library from a higher level,
  because in that case <i>mkpkg</i> will search for the named entry for the
  library being updated, ignoring the remainder of the mkpkg-file.
  </p>
  <p>
  Sometimes it is necessary or desirable to break the library member list up
  into separate modules within the same mkpkg-file, e.g., to temporarily
  change the value of the symbol XFLAGS when compiling certain modules.
  To do this use the <span style="font-family: monospace;">"@"</span> indirection operator in the primary module list to
  reference a named sublist, as in the example below.  Normal indirection
  cannot be used unless the sublist resides in a subdirectory or in a different
  file in the current directory, e.g., <span style="font-family: monospace;">"@./mki2"</span>, since a single mkpkg-file
  cannot contain two modules with the same name.  The same restrictions apply
  to the <i>$update</i> operator.
  </p>
  <div class="highlight-default-notranslate"><pre>
  libpkg.a:
          @(i2)
          alpha.x
          beta.x
          zeta.f
          ;
  i2:
          $set    XFLAGS = "-cO -i2"
          gamma.f
          delta.f
          ;
  </pre></div>
  <p>
  In the example above five object modules are to be updated in the library
  <span style="font-family: monospace;">"libpkg.a"</span>.  The files listed in module <span style="font-family: monospace;">"i2"</span>, if out of date, will be compiled
  with the nonstandard XFLAGS (compiler flags) specified by the <i>$set</i>
  statement shown.
  </p>
  <p>
  4. <b>The MKPKG Macro Preprocessor</b>
  </p>
  <p>
      The <i>mkpkg</i> macro preprocessor provides a simple recursive symbol
  definition and replacement facility, an include file facility, conditional
  execution facilities, an OS escape facility, and a number of builtin directives.
  The names of the preprocessor directives always begin with a dollar sign;
  whitespace is not permitted between the dollar sign and the remainder of the
  name.  Several preprocessor directives may be given on one line if desired.
  Preprocessor directives are executed as they are encountered, and may appear
  anywhere, even in the member list for a library.
  </p>
  <p>
  4.1 Symbol Replacement
  </p>
  <p>
      Symbol substitution in the <i>mkpkg</i> macro preprocessor is carried out
  at the character level rather than at the token level, allowing macro expansion
  within tokens, quoted strings, or OS escape commands.  Macros are recursively
  expanded but may not have arguments.
  </p>
  <p>
  Macros may be defined on the <b>mkpkg</b> command line, in the argument list
  to a <b>$call</b> or <b>$update</b> directive (see below), in an include file
  referenced with the <b>$include</b> directive, or in a <b>$set</b> directive.
  All symbols are global and hence available to all lower level modules,
  but symbols are automatically discarded whenever a module exits, hence cannot
  affect higher level modules.  A local symbol may redefine a previously
  defined symbol.  The IRAF and host system environment is treated as an
  extension of the <b>mkpkg</b> symbol table, i.e., a logical directory such
  as <span style="font-family: monospace;">"iraf"</span> may be referenced like a locally defined symbol.
  </p>
  <p>
  Macro replacement occurs only when explicitly indicated in the input text,
  as in the following example, which prints the pathname of the
  <b>dev$graphcap</b> file on the <b>mkpkg</b> standard output.  The sequence
  <span style="font-family: monospace;">"$("</span> triggers macro substitution.  The value of a symbol may be obtained
  interactively from the standard input by adding a question mark after the
  left parenthesis, i.e., <span style="font-family: monospace;">"$(?terminal)"</span> (this does not work with the -f stdin
  flag).  The contents of a file may be included using the notation
  <span style="font-family: monospace;">"$(@file)"</span>.   Note that case is ignored in macro names; by convention,
  logical directories are normally given in lower case, and locally defined
  symbols in upper case.
  </p>
  <div class="highlight-default-notranslate"><pre>
  $echo $(dev)graphcap
  !xc $(XFLAGS) filea.x fileb.x
  </pre></div>
  <p>
  Symbols are most commonly defined locally with the <b>$set</b> directive.
  The <b>$include</b> directive is useful for sharing symbols amongst different
  modules, or for isolating any machine dependent definitions in a separate
  file.  The IRAF <b>mkpkg</b> system include file <b>hlib$mkpkg.inc</b> is
  automatically included whenever <i>mkpkg</i> is run.
  </p>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='' -->
  <dd><dl>
  <dt><b><b>$set</b> symbol = value</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$set\fR symbol = value' -->
  <dd>Enter the named symbol into the symbol table with the given string value.
  Any existing symbol will be silently redefined.  Symbols defined within a
  module are discarded when the module exits.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$include</b> filename</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$include\fR filename' -->
  <dd>Read commands (e.g., <b>$set</b> directives) from the named include file.
  The include filename may be any legal virtual filename, but only the
  major logical directories are recognized, e.g., <span style="font-family: monospace;">"iraf$"</span>, <span style="font-family: monospace;">"host$"</span>, <span style="font-family: monospace;">"hlib$"</span>,
  <span style="font-family: monospace;">"lib$"</span>, <span style="font-family: monospace;">"pkg$"</span>, and so on.
  </dd>
  </dl>
  </dd>
  </dl>
  <p>
  The use of the <b>$set</b> directive is illustrated in the example below.
  Note the doubling of the preprocessor meta-character to avoid macro expansion
  when entering the value of the GEN macro into the symbol table.  The sequence
  <span style="font-family: monospace;">"$$"</span> is replaced by a single <span style="font-family: monospace;">"$"</span> whenever it is encountered in the input
  stream.
  </p>
  <div class="highlight-default-notranslate"><pre>
  $set GFLAGS = "-k -t silrdx -p ak/"
  $set GEN    = "$generic $$(GFLAGS)"
  
  ifolder (amulr.x, amul.x) $(GEN) amul.x $endif
  </pre></div>
  <p>
  4.2 Conditional Execution
  </p>
  <p>
      Conditional control flow is implemented by the <b>$if</b> directives
  introduced in the last example and described below.  The character <span style="font-family: monospace;">"n"</span> may
  be inserted after the <span style="font-family: monospace;">"$if"</span> prefix of any directive to negate the sense of
  the test, e.g., <span style="font-family: monospace;">"$ifndef"</span> tests whether the named symbol does not exist.
  Nesting is permitted.
  </p>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='' -->
  <dd><dl>
  <dt><b><b>$ifdef</b> (symbol [, symbol, ...])</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$ifdef\fR (symbol [, symbol, ...])' -->
  <dd><br>
  Test for the existence of one of the named symbols.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$ifeq</b> (symbol, value [, value,...])</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$ifeq\fR (symbol, value [, value,...])' -->
  <dd><br>
  Test if the value of the named symbol matches one of the listed value strings.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$iferr</b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$iferr\fR' -->
  <dd><br>
  Test for an error return from the last directive executed which touched
  a file. This has only effect if mkpkg is invoked with the <b>-i</b> option
  so that it doesn't exit on the first error.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$iffile</b> (file [, file,...])</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$iffile\fR (file [, file,...])' -->
  <dd><br>
  Test for the existence of any of the named files.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$ifnewer</b> (file, filea)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$ifnewer\fR (file, filea)' -->
  <dd><b>$ifnewer</b> (file: filea [, fileb, ...])
  <br>
  Test if the named file is newer (has been modified more recently) than
  any of the named files to the right.  The colon syntax may be used for
  clarity when comparing one file to many, but a comma will do.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$ifolder</b> (file, filea)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$ifolder\fR (file, filea)' -->
  <dd><b>$ifolder</b> (file: filea [, fileb, ...])
  <br>
  Test if the named file is older than any of the named files.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$else</b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$else\fR' -->
  <dd><br>
  Marks the <i>else</i> clause of an <i>if</i> statement.  The <i>else-if</i>
  construct is implemented as <span style="font-family: monospace;">"$else $if"</span>, i.e., as a combination of the two
  more primitive constructs.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$endif</b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$endif\fR' -->
  <dd><br>
  Terminates a $if or $if-$else statement.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$end</b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$end\fR' -->
  <dd><br>
  Terminates an arbitrary number of $if or $if-$else statements.  This is most
  useful for terminating a long list of $if-$else clauses, where the alternative
  would be a long string of $endif directives.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$exit</b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$exit\fR' -->
  <dd>Terminate the current program; equivalent to a semicolon, but the latter
  is normally used only at the end of the program to match the colon at the
  beginning, whereas <b>$exit</b> is used in conditionals.
  </dd>
  </dl>
  </dd>
  </dl>
  <p>
  4.3 Calling Modules
  </p>
  <p>
      The following preprocessor directives are available for calling <i>mkpkg</i>
  modules or altering the normal flow of control.
  </p>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd><dl>
  <dt><b><b>$call</b> module[@subdir[/file]] [name=value] [name=value...]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$call\fR module[@subdir[/file]] [name=value] [name=value...]' -->
  <dd><br>
  Call the named mkpkg-file module as a subroutine.  In most cases the called
  module will be in the current mkpkg-file, but the full module name syntax
  permits the module to be in any file of any subdirectory (<span style="font-family: monospace;">"./file"</span> references
  a different file in the current directory).  Arguments may be passed to
  the called module using the symbol definition facility; any symbols
  defined in this fashion are available to any modules called in turn by
  the called module, but the symbols are discarded when the called module returns.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$update</b> module[@subdir[/file]] [name=value] [name=value...]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$update\fR module[@subdir[/file]] [name=value] [name=value...]' -->
  <dd><br>
  Identical to <b>$call</b> except that the named module is understood to
  be a library member list.  The current value of the symbol XFLAGS is used
  if XC is called to compile any files.  If the named library does not exist
  one will be created (a warning message is issued).
  </dd>
  </dl>
  <dl>
  <dt><b><b>$goto</b> label</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$goto\fR label' -->
  <dd><br>
  Causes execution to resume at the line following the indicated label.
  The syntax of a goto label is identical to that of a mkpkg-file module name,
  i.e., a line starting with the given name followed by a colon.
  The <i>$goto</i> statement automatically cancels any <i>$if</i> nesting.
  </dd>
  </dl>
  </dd>
  </dl>
  <p>
  4.4 Preprocessor Directives
  </p>
  <p>
      The remaining preprocessor directives are described below in alphabetical
  order.  Additional capability is available via OS escapes, provided the
  resultant machine dependence is acceptable.
  </p>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd><dl>
  <dt><b><b>$echo</b> message</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$echo\fR message' -->
  <dd><br>
  Print the given message string on the standard output.  The string must be
  quoted if it contains any spaces.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$checkout</b> file directory</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$checkout\fR file directory' -->
  <dd><br>
  Check the named file out of the indicated directory.  The checkout operation
  makes the file accessible as if it were in the current directory; checkout
  is implemented either as a symbolic link or as a physical file copy depending
  upon the host system.  The referenced directory may be a logical directory,
  e.g., <span style="font-family: monospace;">"lib$"</span>, or a path, e.g, <span style="font-family: monospace;">"pkg$images/"</span>.  Checkout is not disabled by
  the <span style="font-family: monospace;">"-n"</span> flag.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$checkin</b> file directory</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$checkin\fR file directory' -->
  <dd><br>
  Check the named file back into the indicated directory.  The checkin operation
  is implemented either as a remove link or copy and delete depending upon the
  host system.  Checkin is not disabled by the <span style="font-family: monospace;">"-n"</span> flag.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$copy</b> filea fileb</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$copy\fR filea fileb' -->
  <dd><br>
  Make a copy <i>fileb</i> of the existing file <i>filea</i>.  On a UNIX host
  the copy operation will preserve the file modify date if the file is a library
  (to avoid the <span style="font-family: monospace;">"symbol table out of date"</span> syndrome).
  </dd>
  </dl>
  <dl>
  <dt><b><b>$delete</b> file [file ...]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$delete\fR file [file ...]' -->
  <dd><br>
  Delete the named file or files.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$generic</b> [-k] [-p prefix] [-t types] [-o root] files</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$generic\fR [-k] [-p prefix] [-t types] [-o root] files' -->
  <dd><br>
  Run the generic preprocessor on the named files.  The generic preprocessor
  is an IRAF bootstrap utility.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$xyacc</b> [options] file</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$xyacc\fR [options] file' -->
  <dd><br>
  Run the xyacc parser generator on the named files.  The yacc parser
  generator is an IRAF bootstrap utility.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$link</b> [switches] file1 file2 ... fileN [-o file.e]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$link\fR [switches] file1 file2 ... fileN [-o file.e]' -->
  <dd><br>
  Call XC with the given argument list to link the indicated files and libraries.
  The value of the symbol LFLAGS (default value the null string) is automatically
  inserted at the beginning of the command line.  This is equivalent to
  <span style="font-family: monospace;">"!xc $(LFLAGS) ..."</span>.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$move</b> file destination</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$move\fR file destination' -->
  <dd><br>
  Move the named file to the indicated directory, or rename the file in the
  current directory.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$omake</b> file [dep1] [dep2 ...]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$omake\fR file [dep1] [dep2 ...]' -->
  <dd><br>
  Compile the named source file if it does not have a corresponding object file
  in the current directory, if the object file is older, or if any of the
  listed dependency files are newer (or not found).  The current value of the
  symbol XFLAGS is used if XC is called to compile the file.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$purge</b> directory</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$purge\fR directory' -->
  <dd><br>
  Delete all old versions of all files in the named directory.  Nothing is done
  if the system does not support multiple file versions.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$special</b> directory : filelist ;</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$special\fR directory : filelist ;' -->
  <dd><br>
  Add one or more files to the special file list for the host system.  This is
  a system facility, not intended for use in applications <i>mkpkg</i> files.
  The special file list is a list of all source files needing special processing
  for the local host system.  Examples of special files are files which are
  optimized in assembler (or some other nonstandard language), or files which
  must be compiled in a special way to get around bugs in a host compiler.
  The special file list makes it possible to flag arbitrary files for special
  processing, without having to modify the standard software distribution.
  In the IRAF system, the special file list is defined in the file
  <span style="font-family: monospace;">"hlib$mkpkg.sf"</span> which is included automatically by <span style="font-family: monospace;">"hlib$mkpkg.inc"</span> whenever
  <i>mkpkg</i> is run.
  The syntax of a <i>filelist</i> entry is as follows:
  	modname source_file mkobj_command
  where <i>modname</i> is the filename of a library module as it appears in a
  library module list for the named directory, <i>source_file</i> is the virtual
  pathname of the source file to be used in lieu of the standard portable
  source file <i>modname</i>, and <i>mkobj_command</i> is the <i>mkpkg</i> command
  (e.g., $xc or an OS escape) to be executed to compile the named module.
  The character <span style="font-family: monospace;">"&amp;"</span> appearing in either the source file name or mkobj command
  is replaced by <i>modname</i>.  If the <i>mkobj_command</i> is omitted the
  specified source file will be compiled with $XC using the current value of
  XFLAGS.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$xc</b> [switches] file1 file2 ... fileN</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$xc\fR [switches] file1 file2 ... fileN' -->
  <dd><br>
  Call the XC compiler to compile the named files.  Note that the value of
  the symbol XFLAGS is <i>not</i> used when XC is explicitly called in this
  fashion (XFLAGS is used by <b>$update</b> and <b>$omake</b>).
  </dd>
  </dl>
  <dl>
  <dt><b><b>$debug</b> [on|off]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$debug\fR [on|off]' -->
  <dd><br>
  Turn debug mode on or off.  If no argument is supplied debug mode is turned
  on.  Turning on debug mode automatically enables verbose mode.
  </dd>
  </dl>
  <dl>
  <dt><b><b>$verbose</b> [on|off]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='\fB$verbose\fR [on|off]' -->
  <dd><br>
  Turn verbose mode on or off.  If no argument is supplied verbose mode is turned
  on.
  </dd>
  </dl>
  </dd>
  </dl>
  <p>
  5. Error Recovery
  </p>
  <p>
      <b>Mkpkg</b> is implemented in such a way that it is restartable.  If a mkpkg
  operation terminates prematurely for some reason, e.g., because of a compile
  error, execution error (such as cannot find the mkpkgfile in a subdirectory),
  interrupt, etc., then the mkpkg command can be repeated after correcting
  the error, without repeating the operations already completed.  If <b>mkpkg</b>
  is interrupted it may leave checked out files, objects compiled but not yet
  updated in a library, etc. lying about, but this is harmless and the
  intermediate files will be cleaned up when the errors have been corrected
  and the run successfully completes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Update the current package.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkpkg
  </pre></div>
  <p>
  Update the package library but do not relink.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkpkg libpkg.a
  </pre></div>
  <p>
  Make a listing of the package.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkpkg listing
  </pre></div>
  <p>
  Sample mkpkg-file for the above commands:
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Make my package.
  
  $call relink
  $exit
  
  relink:
          $update libpkg.a
          $omake  x_mypkg.x
          $link   x_mypkg.o -lxtools
          ;
  
  libpkg.a:
          task1.x         pkg.h
          task2.x
          filea.x         pkg.com pkg.h &lt;fset.h&gt;
          fileb.x         pkg.com
          ;
  
  listing:
          !pr task1.x task2.x file[ab].x | vpr -Pvup
          ;
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  xc, generic, softools package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'ARGUMENTS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  
