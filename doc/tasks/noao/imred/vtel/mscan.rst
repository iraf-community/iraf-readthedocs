.. _mscan:

mscan: Read all sector scans on a tape and put them into images.
================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mscan input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>File template or device, e.g. <span style="font-family: monospace;">"junk"</span> or <span style="font-family: monospace;">"s*"</span> or <span style="font-family: monospace;">"mta1600[1]"</span> or <span style="font-family: monospace;">"mtb800"</span>
  </dd>
  </dl>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>List of tape file numbers or ranges delimited by commas, e.g. <span style="font-family: monospace;">"1-3,5-8"</span>.
  `Files' is requested only if no file number is given in `input' and the
  input is tape.
  Files will be read in ascending order, regardless of the order of the list.
  Reading will terminate if EOT is reached, thus a list such as <span style="font-family: monospace;">"1-999"</span>
  may be used to read all the files on the tape.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Flag to signal program that it should produce verbose output.  This means
  header information.
  </dd>
  </dl>
  <dl id="l_makeimage">
  <dt><b>makeimage = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='makeimage' Line='makeimage = yes' -->
  <dd>Flag to signal the program that it should make images.  If this parameter
  is set to no, the header will be read and decoded but no data will be read
  and no image will be produced on disk.
  </dd>
  </dl>
  <dl id="l_brief">
  <dt><b>brief = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='brief' Line='brief = yes' -->
  <dd>Flag to make mscan produce brief filenames for the output images.  These
  filenames have the form [svb]nnn e.g. s034 or b122.  The b is for a brightness
  image, the v is for a velocity image, and the s is for a select image.  The
  'nnn' is the tape sequence number or the filenumber in a template expansion.
  If this flag is set to false the long filenames described below in the 
  <span style="font-family: monospace;">"Description"</span> section will be produced.
  </dd>
  </dl>
  <dl id="l_select">
  <dt><b>select = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='select' Line='select = yes' -->
  <dd>Flag to tell the program to make a select image.
  </dd>
  </dl>
  <dl id="l_bright">
  <dt><b>bright = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bright' Line='bright = yes' -->
  <dd>Flag to tell the program to make a brightness image.
  </dd>
  </dl>
  <dl id="l_velocity">
  <dt><b>velocity = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='velocity' Line='velocity = yes' -->
  <dd>Flag to tell the program to make a velocity image.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Mscan reads all or selected area scans from a vacuum telescope tape
  and formats the data into multiple IRAF images.  Type 1, 2, and 3 area
  scans can produce 3 output images and type 4 produces one output image.
  The long image names are assembled in the following way:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  The first letter is one of [bsv] for brightness, select, or velocity.
  The next two digits are the day of the month.
  Underbar.
  The next 4 digits are the hour and minute.
  Underbar.
  Finally there is a three digit tape sequence number.
  ie.
  
              b13_1709_002
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To read files 5-7 from mta at 1600 bpi, the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; mscan mta1600 5-7
  </pre></div>
  <p>
  2. To see the header information only for file 6, one could use the command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; mscan mta1600[6] make-
  </pre></div>
  <p>
  3. To read file 4 from mta and only produce a velocity image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; mscan mta[4] bri- sel-
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  
