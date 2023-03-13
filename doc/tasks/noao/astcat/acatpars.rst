.. _acatpars:

acatpars: Default astrometry file format parameter set
======================================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  acatpars 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_ftype">
  <dt><b>ftype = <span style="font-family: monospace;">"stext"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ftype' Line='ftype = "stext"' -->
  <dd>The astrometry file format. The current options are:
  <dl>
  <dt><b>stext</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='stext' Line='stext' -->
  <dd>Simple text. Records are newline delimited and fields are whitespace delimited.
  </dd>
  </dl>
  <dl>
  <dt><b>btext</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='btext' Line='btext' -->
  <dd>Blocked text. Records are newline delimited and fields are offset and
  size delimited.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_ccsystem">
  <dt><b>ccsystem = <span style="font-family: monospace;">"j2000"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccsystem' Line='ccsystem = "j2000"' -->
  <dd>The default celestial coordinate system. The coordinate systems of most
  interest to users are <span style="font-family: monospace;">"icrs"</span>, <span style="font-family: monospace;">"j2000"</span>, and <span style="font-family: monospace;">"b1950"</span>. For more detailed
  information on all the celestial coordinate system options type
  <span style="font-family: monospace;">"help ccsystems"</span>.
  </dd>
  </dl>
  <dl id="l_standard">
  <dt><b>standard astrometry file fields</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='standard' Line='standard astrometry file fields' -->
  <dd>The following parameters define the standard astrometry file fields. The
  parameter names are the same as the standard field names. The parameter
  values are the standard field descriptions.
  <br>
  Every astrometry file returned by
  a catalog query or created by the user must contain the standard fields ra and
  dec. The remaining fields are optional and may or may not be present
  in either the original catalog or the astrometry file produced by a
  catalog query.
  <br>
  The format of the standard fields is <span style="font-family: monospace;">"fieldno [units [format]]"</span> for simple
  text files and <span style="font-family: monospace;">"foffset fsize [units [format]]"</span> for blocked text files
  where the quantities in <span style="font-family: monospace;">"[]"</span> are optional. Standard fields with <span style="font-family: monospace;">""</span> valued
  field descriptions are assumed to be undefined.
  <br>
  <dl>
  <dt><b>id = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='id' Line='id = ""' -->
  <dd>The standard id field. The data type is character. The default units and
  format values are <span style="font-family: monospace;">"INDEF"</span> and <span style="font-family: monospace;">"%20s"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> ra = <span style="font-family: monospace;">"1 hours"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' ra = "1 hours"' -->
  <dd>The standard right ascension / longitude field. The data type is double. The
  default units and format values are <span style="font-family: monospace;">"hours"</span>and <span style="font-family: monospace;">"%11.2h"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> dec = <span style="font-family: monospace;">"2 degrees"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' dec = "2 degrees"' -->
  <dd>The standard declination / latitude field. The data type is double. The default
  units and format values are <span style="font-family: monospace;">"degrees"</span>and <span style="font-family: monospace;">"%11.1h"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> era = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' era = ""' -->
  <dd>The standard right ascension / longitude error field. The data type is double.
  The default units and format values are <span style="font-family: monospace;">"asecs"</span> and <span style="font-family: monospace;">"%6.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> edec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' edec = ""' -->
  <dd>The standard declination / latitude error field. The data type is double.
  The default units and format values are <span style="font-family: monospace;">"asecs"</span> and <span style="font-family: monospace;">"%6.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> pmra = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' pmra = ""' -->
  <dd>The standard right ascension / longitude proper motion field. The data type
  is double. The default units and format values are <span style="font-family: monospace;">"masecs/yr"</span> and <span style="font-family: monospace;">"%7.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> pmdec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' pmdec = ""' -->
  <dd>The standard declination / latitude proper motion field. The data type
  is double. The default units and format values are <span style="font-family: monospace;">"masecs/yr"</span> and <span style="font-family: monospace;">"%7.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> epmra = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' epmra = ""' -->
  <dd>The standard right ascension / longitude proper motion error field. The data
  type is double. The default units and format values are <span style="font-family: monospace;">"masecs/yr"</span> and <span style="font-family: monospace;">"%7.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b> epmdec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' epmdec = ""' -->
  <dd>The standard declination / latitude proper motion error field. The data
  type is double. The default units and format values are <span style="font-family: monospace;">"masecs/yr"</span> and <span style="font-family: monospace;">"%7.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>catsystem = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='catsystem' Line='catsystem = ""' -->
  <dd>The standard celestial coordinate system field. The data type is character.
  The default units and format field values are <span style="font-family: monospace;">"INDEF"</span> and <span style="font-family: monospace;">"%15s"</span>. If defined
  the value of this field overrides the coordinate system defined by the
  <i>csystem</i> parameter. Supported values of catsystem are <span style="font-family: monospace;">"icrs"</span>, <span style="font-family: monospace;">"fk5"</span>,
  <span style="font-family: monospace;">"fk4"</span>, <span style="font-family: monospace;">"fk4-noe"</span>, <span style="font-family: monospace;">"ecliptic"</span>, <span style="font-family: monospace;">"galactic"</span>, and <span style="font-family: monospace;">"supergalactic"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>equinox = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='equinox' Line='equinox = ""' -->
  <dd>The standard celestial coordinate system equinox field. The data type is
  character. The default units and format field values are <span style="font-family: monospace;">"INDEF"</span> and
  <span style="font-family: monospace;">"%15s"</span>. Equinoxes are typical expressed as Julian epochs e.g. <span style="font-family: monospace;">"J2000.0"</span>,
  Besselian epochs e.g. <span style="font-family: monospace;">"B1950.0"</span>, or years <span style="font-family: monospace;">"2000.0"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>epoch = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='epoch' Line='epoch = ""' -->
  <dd>The standard celestial coordinate system epoch field. The data type is
  character. The default units and format field values are <span style="font-family: monospace;">"INDEF"</span> and
  <span style="font-family: monospace;">"%15s"</span>. Epochs are typical expressed as Julian epochs e.g. <span style="font-family: monospace;">"J2000.0"</span>,
  Besselian epochs e.g. <span style="font-family: monospace;">"B1950.0"</span>, years <span style="font-family: monospace;">"2000.0"</span>, or Julian date if the
  epoch value &gt; 3000.0.
  </dd>
  </dl>
  <dl>
  <dt><b>px = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='px' Line='px = ""' -->
  <dd>The standard parallax field. The data type is double. The default units
  and format values are <span style="font-family: monospace;">"msecs"</span> and <span style="font-family: monospace;">"%6.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>rv = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rv' Line='rv = ""' -->
  <dd>The standard radial velocity field. The data type is double. The default units
  and format values are <span style="font-family: monospace;">"km/sec"</span> and <span style="font-family: monospace;">"%6.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>epx = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='epx' Line='epx = ""' -->
  <dd>The standard parallax error field. The data type is double. The default units
  and format values are <span style="font-family: monospace;">"msecs"</span> and <span style="font-family: monospace;">"%6.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>erv = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='erv' Line='erv = ""' -->
  <dd>The standard radial velocity error field. The data type is double. The default
  units and format values are <span style="font-family: monospace;">"km/sec"</span> and <span style="font-family: monospace;">"%6.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>mag = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='mag' Line='mag = ""' -->
  <dd>The standard magnitude field. The  data type is real. The default units
  and format field values are <span style="font-family: monospace;">"mags"</span> and <span style="font-family: monospace;">"%8.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>color = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='color' Line='color = ""' -->
  <dd>The standard color field. The  data type is real. The default units
  and format field values are <span style="font-family: monospace;">"mags"</span> and <span style="font-family: monospace;">"%8.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>emag = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='emag' Line='emag = ""' -->
  <dd>The standard magnitude error field. The  data type is real. The default units
  and format field values are <span style="font-family: monospace;">"mags"</span> and <span style="font-family: monospace;">"%8.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>ecolor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ecolor' Line='ecolor = ""' -->
  <dd>The standard color error field. The  data type is real. The default units
  and format field values are <span style="font-family: monospace;">"mags"</span> and <span style="font-family: monospace;">"%8.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>xp = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xp' Line='xp = ""' -->
  <dd>The predicted x coordinate field. The data type is double. The default units
  and format field values are <span style="font-family: monospace;">"pixels"</span> and <span style="font-family: monospace;">"%9.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>yp = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='yp' Line='yp = ""' -->
  <dd>The predicted y coordinate field. The data type is double. The default units
  and format field values are <span style="font-family: monospace;">"pixels"</span> and <span style="font-family: monospace;">"%9.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>xc = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xc' Line='xc = ""' -->
  <dd>The centered x coordinate field. The data type is double. The default units
  and format field values are <span style="font-family: monospace;">"pixels"</span> and <span style="font-family: monospace;">"%9.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>yc = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='yc' Line='yc = ""' -->
  <dd>The centered y coordinate field. The data type is double. The default units
  and format field values are <span style="font-family: monospace;">"pixels"</span> and <span style="font-family: monospace;">"%9.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>exc = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='exc' Line='exc = ""' -->
  <dd>The centered x coordinate error field. The data type is double. The default
  units and format field values are <span style="font-family: monospace;">"pixels"</span> and <span style="font-family: monospace;">"%9.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>eyc = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='eyc' Line='eyc = ""' -->
  <dd>The centered y coordinate error field. The data type is double. The default
  units and format field values are <span style="font-family: monospace;">"pixels"</span> and <span style="font-family: monospace;">"%9.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>imag = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='imag' Line='imag = ""' -->
  <dd>The standard instrumental magnitude field. The data type is real. The default
  units and format values are <span style="font-family: monospace;">"mags"</span> and <span style="font-family: monospace;">"8.3f"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>eimag = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='eimag' Line='eimag = ""' -->
  <dd>The standard instrumental magnitude error field. The data type is real. The
  default units and format values are <span style="font-family: monospace;">"mags"</span> and <span style="font-family: monospace;">"8.3f"</span>.
  </dd>
  </dl>
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The acatpars parameters define the default astrometry file format. These
  parameters are used if the input astrometry file does not contain a standard
  header describing the file format. By default standard headers are written
  by all astcat package tasks which create astrometry files. If the
  astrometry file does not have a header the acatpars parameters
  are used to define one.
  </p>
  <p>
  By default acatpars assumes that the input astrometry file is a
  simple text file, <i>ftype</i> = <span style="font-family: monospace;">"stext"</span>, with newline delimited records
  and whitespace delimited fields. In this case users can define
  the fields by setting the appropriate standard file parameters
  to a string with the following format, e.g.
  </p>
  <div class="highlight-default-notranslate"><pre>
  parname = "fieldno [units [format]]"
  
       ra = "1 hours"
      dec = "2 degrees"
  </pre></div>
  <p>
  where fieldno is the field or column number in the record. The
  units and format strings are optional and reasonable defaults are
  supplied if they are missing. Currently the units information is
  only used for decoding coordinate fields. For other fields the
  units should be left at their default values. The format information
  is used when an application has to decode a field into a numeric value
  modify it in some way and rewrite it.
  </p>
  <p>
  If <i>ftype</i> is set to <span style="font-family: monospace;">"btext"</span> for blocked text the input astrometry file
  is assumed to be a text file with newline delimited records and fixed size
  fields. This format can be used to describe astrometry files with
  fields containing embedded blanks such as id fields. In this case users
  define the fields by setting the appropriate standard file parameters to
  a string with the following format, e.g.
  </p>
  <div class="highlight-default-notranslate"><pre>
  parname = "foffset fsize [units [format]]"
       ra = "1 15 hours"
      dec = "16 15 degrees"
  </pre></div>
  <p>
  where foffset and fsize are the field offset and size in characters.
  Formats and units are treated in the same way as they for simple text files.
  </p>
  <p>
  The fundamental coordinate system of the astrometry file is set by
  the <i>csystem</i> parameter. This is a global parameter applying to the
  entire astrometry file . Its value is overwritten if the <span style="font-family: monospace;">"catsystem"</span> standard
  field is defined, in which case the astrometry file may contain entries in
  many different fundamental coordinate systems.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the astrometry file format parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lpar acatpars
  </pre></div>
  <p>
  2. Edit the astrometry file format parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; acatpars
  </pre></div>
  <p>
  3. Edit the astrometry file format parameters from the afiltcat task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar afiltcat
  </pre></div>
  <p>
  4. Save the current acatpars parameter values in a text file called
  acat1.par.  Use the saved parameter set in the next call to the afiltcat
  task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar acatpars
  cl&gt; afiltcat ... acatpars=afilt1.par ...
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  afiltcat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  
