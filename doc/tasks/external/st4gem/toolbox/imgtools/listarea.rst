.. _listarea:

listarea: Print an area of an image.
====================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  listarea input
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task will print image values with pixels labelled by their
  image coordinates.  If an image section is given, the pixel coordinates
  refer to the original image.  If the image has keywords 'SAMPBEG' and 
  'LINEBEG' then these integers are also added to the printed coordinates.
  </p>
  <p>
  Note that the 'images.listpix' task produces a list of values, whereas 
  this task prints a 2-dimensional section of an image which may, for 
  example, be examined to look for image features.
  </p>
  <p>
  If the output is redirected,
  the page width is obtained from the 'pagewidth' parameter; otherwise,
  the page width is set to the value of the environment variable 'ttyncols'.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name template]' -->
  <dd>List of images to be printed.
  Frequently only a portion of the image is to be printed,
  in which case the portion is specified by giving an image section.
  If you specify the range of line numbers with the larger number first,
  values will be printed with the origin toward the bottom of the screen.
  </dd>
  </dl>
  <dl>
  <dt><b>(pformat = <span style="font-family: monospace;">"g9.3"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pformat = "g9.3") [string]' -->
  <dd>Format to use for printing each pixel value.
  Both Fortran and SPP formats are acceptable.
  Note that the format does not have to match the image data type,
  e.g., a format of <span style="font-family: monospace;">"i5"</span> can be used with real data.
  The format does have to be reasonable for the numbers to be printed, however.
  SPP formats include octal (e.g., %4o) and hexadecimal (%4x) for integer values.
  When printing floating point values with an integer format,
  the values will be rounded to the nearest integer.
  One additional space will be printed as a column separator.
  </dd>
  </dl>
  <dl>
  <dt><b>(pagewidth = 132) [int, min=9, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pagewidth = 132) [int, min=9, max=INDEF]' -->
  <dd>If the output is written to the terminal, this parameter is ignored,
  and the page width is gotten from 'ttyncols'.
  If the output has been redirected to a file, however,
  the page width is set to the value of this parameter.
  The page width is relevant when there are more columns to be printed
  than will fit on a page,
  in which case the task prints as many columns as will fit
  (printing all rows), and then prints the next set of columns,
  until all have been printed.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Print an area of the image 'focim'.
  Note that the range of line numbers has been specified as 330:325 rather
  than as 325:330.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
    im&gt; listarea focim.hhh[415:425,330:325]
  
  Here is some sample output:
  
  Listing of image:
  focim.hhh[415:425,330:325]
  
   Sample   415   416   417   418   419   420   421   422   423   424   425
  Line
      330     0     3    94    95    95    95    95    95    95    95    95
      329     0     0    80    95    95    95    95    95    95    95    95
      328     0     0    65    95    95    95    95    88    71    55    39
      327     0     0    40    59    43    27    11    -5   -21   -37   -53
      326     0     0    -6   -33   -49   -66   -82     0     0     0     0
      325     0     0     0     0     0     0     0     0     0     0     0
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
