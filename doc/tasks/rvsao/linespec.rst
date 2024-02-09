.. _linespec:

linespec: Make a spectrum from a list of emission and/or absorption lines
=========================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  linespec linefile specfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_linefile">
  <dt><b>linefile <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linefile' Line='linefile ""' -->
  <dd>Filename with list of emission or absorption lines in the format
  <br>
  	Center wavelength of line in Angstroms
  <br>
  	Half-width of line:  in Angstroms if positive,
  <br>
  			     in km/sec if negative
  <br>
  	Height of line in counts (this is arbitrary)
  <br>
  	Name of line
  </dd>
  </dl>
  <dl id="l_linedir">
  <dt><b>linedir <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linedir' Line='linedir ""' -->
  <dd>Directory for line list (null string means current directory)
  </dd>
  </dl>
  <dl id="l_linewidth">
  <dt><b>linewidth 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linewidth' Line='linewidth 2.0' -->
  <dd>Half-width at half-max of Gaussian emission lines in Angstroms
  This instrumental function is convolved with the spectrum from linefile.
  </dd>
  </dl>
  <dl id="l_maxwidth">
  <dt><b>maxwidth no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxwidth' Line='maxwidth no' -->
  <dd>Use maximum of line or instrument width (yes) or convolve instrument with
  spectrum (no).
  </dd>
  </dl>
  <dl id="l_zspec">
  <dt><b>zspec 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zspec' Line='zspec 0' -->
  <dd>Delta lambda / lambda to which to shift individual spectral lines. This
  is useful for making spectra for very distant objects and supercedes
  velspec if it is not zero. 
  <dl>
  <dt><b>velspec 0</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='velspec' Line='velspec 0' -->
  <dd>If this is not zero, shift the wavelengths of all specified lines to this
  velocity.
  </dd>
  </dl>
  <dl>
  <dt><b>continuum 0 </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='continuum' Line='continuum 0 ' -->
  <dd>Continuum level for output spectrum. This is useful if software to be
  used on the created spectrum has problems with a continuum of zero or
  absorption lines with negative nadirs. 
  </dd>
  </dl>
  <dl>
  <dt><b>specobj = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='specobj' Line='specobj = ""' -->
  <dd>Title for output spectrum
  </dd>
  </dl>
  <dl>
  <dt><b>specfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='specfile' Line='specfile = ""' -->
  <dd>File name for output spectrum
  </dd>
  </dl>
  <dl>
  <dt><b>specdir = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='specdir' Line='specdir = ""' -->
  <dd>Directory for output spectrum (null string means current directory)
  </dd>
  </dl>
  <dl>
  <dt><b>st_lambda = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='st_lambda' Line='st_lambda = INDEF' -->
  <dd>Starting wavelength in angstroms for output file
  </dd>
  </dl>
  <dl>
  <dt><b>end_lambda = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='end_lambda' Line='end_lambda = INDEF' -->
  <dd>Ending wavelength in angstroms for output file
  </dd>
  </dl>
  <dl>
  <dt><b>pix_lambda 0.25,</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='pix_lambda' Line='pix_lambda 0.25,' -->
  <dd>Wavelength per pixel in Angstroms
  </dd>
  </dl>
  <dl>
  <dt><b>spec_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spec_plot' Line='spec_plot = yes' -->
  <dd>If yes, a plot of the output spectrum is displayed.
  Cursor commands are activated for zooming in on a portion of the
  spectrum and hard copies may be made to stdplot using the <i>@</i> command.
  If maxwidth is no, the spectrum is displayed both before and after it is
  convolved with the instrumental Gaussian.
  </dd>
  </dl>
  <dl>
  <dt><b>spec_int no</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spec_int' Line='spec_int no' -->
  <dd>If yes, interact with the graph of the output spectrum
  </dd>
  </dl>
  <dl>
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='device' Line='device = "stdgraph"' -->
  <dd>Interactive device on which to display a graphic summary of XCSAO's results.
  </dd>
  </dl>
  <dl>
  <dt><b>plotter = <span style="font-family: monospace;">"stdplot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='plotter' Line='plotter = "stdplot"' -->
  <dd>Second, non-interactive device on which to plot the graphic summary of results.
  </dd>
  </dl>
  <dl>
  <dt><b>verbose yes </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='verbose' Line='verbose yes ' -->
  <dd>     Print summary to log file (yes or not).
  </dd>
  </dl>
  <dl>
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,linespec.log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logfiles' Line='logfiles = "STDOUT,linespec.log"' -->
  <dd>All results from LINTEMP are recorded in these files.
  </dd>
  </dl>
  <dl>
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='debug' Line='debug = no' -->
  <dd>If yes, values of the parameters fit to the selected peak
  are recorded in the log files.  This is most useful for debugging.
  </dd>
  </dl>
  <dl>
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  When null the standard cursor is used otherwise
  the specified file is used.
  </dd>
  </dl>
   
  </section>
  <section id="s_description">
  <h3>Description</h3>
  LINESPEC reads a list of positions of emission and/or absorptions lines
  and creates a spectrum with Gaussian lines of the the indicated
  half-widths at the indicated positions, writing a one-dimensional IRAF
  file with the appropriate keywords in the header.  If velspec is nonzero,
  the emission lines are shifted to that redshift velocity.
   
  </section>
  <section id="s_cursor">
  <h3>Cursor</h3>
  The following keystrokes are active for spectrum template plots in addition
  to the normal IRAF cursor facilities (a list of those is available with
  the command <span style="font-family: monospace;">":.help"</span>):
  <dl>
  <dt><b>@</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='' Line='@' -->
  <dd>Make a hard copy on the device designated by <i>plotter</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>c</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='c' Line='c' -->
  <dd>Prints cursor position in x and y.  This is the default.  All other
  undefined keys perform this same function.
  </dd>
  </dl>
  <dl>
  <dt><b>d</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='d' Line='d' -->
  <dd>Replaces a region between the marked vertical cursors with interpolated
  values from the edges of the marked region.  This is can be used to eliminate
  lines from a template without changing the line list, though the line will
  still appear in the image header.
  </dd>
  </dl>
  <dl>
  <dt><b>n</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='n' Line='n' -->
  <dd>Smooth spectrum n times before plotting.  This affects the actual spectrum,
  so it is usually not a good idea to exit from a plot with this set to any
  value other than 0.
  </dd>
  </dl>
  <dl>
  <dt><b>q</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='q' Line='q' -->
  <dd>Quit and exit.
  </dd>
  </dl>
  <dl>
  <dt><b>r</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='r' Line='r' -->
  <dd>Forces a replot of the current spectrum at the original scale.
  </dd>
  </dl>
  <dl>
  <dt><b>u</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='u' Line='u' -->
  <dd>Redisplay the entire plot after zooming.
  </dd>
  </dl>
  <dl>
  <dt><b>z</b></dt>
  <!-- Sec='CURSOR' Level=1 Label='z' Line='z' -->
  <dd>Zoom in on the region marked by two successive &lt;z&gt;'s
  </dd>
  </dl>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  To make a emission line template from a list of commonly observed
  emission lines:
          cl&gt; linespec emtemp.dat emtemp
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  On-line help is available over the World Wide Web at
  http://tdc-www.harvard.edu/iraf/rvsao/linespec
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR' 'EXAMPLE' 'SEE ALSO'  -->
  
