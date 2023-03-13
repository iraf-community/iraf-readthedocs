.. _astradius:

astradius: Find images within a circle on the sky
=================================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  astradius images racenter deccenter epcenter radius
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images for which the radius to a point on the sky is to be
  determined.
  </dd>
  </dl>
  <dl id="l_racenter">
  <dt><b>racenter, deccenter, epcenter</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='racenter' Line='racenter, deccenter, epcenter' -->
  <dd>Right ascension in hours, declination in degrees, and epoch of a position
  on the sky to use as the center of a circle.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius' -->
  <dd>Search radius in arc seconds about the center position.
  </dd>
  </dl>
  <dl id="l_keywpars">
  <dt><b>keywpars = <span style="font-family: monospace;">""</span> (pset)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keywpars' Line='keywpars = "" (pset)' -->
  <dd>Parameter set defining the image header keywords.  This task requires
  keywords for the right ascension, declination, and epoch.  If
  there is no epoch in the image header keywords for the date of observation
  and the universal time are used for the epoch.  The default parameter
  set (specified by the empty string) is <b>keywpars</b>.
  </dd>
  </dl>
  <dl id="l_commands">
  <dt><b>commands = <span style="font-family: monospace;">"astutil$astradius.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='commands' Line='commands = "astutil$astradius.dat"' -->
  <dd>Command file used to compute the distance from the coordinate center
  and print a result if the distance is less than the specified radius.
  The command file uses the syntax described for <b>astcalc</b>.
  Users may copy and modify this file if desired.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Astradius</b> computes the spherical distance from a specified point on
  the sky for each image in a list of images (<i>images</i>).  The point on
  the sky is specified by the parameters <i>racenter</i>, <i>deccenter</i>, and
  <i>epcenter</i> which give a right ascension in hours, a declination in
  degrees, and an epoch.  Each image is required to have keywords for the
  right ascension (hours), declination (degrees), and epoch.  However, if no
  epoch is defined in the image header then an epoch is computed from the
  observation date and universal time.  The spherical distance is compared to
  a specified radius (<i>radius</i>) in arc seconds.  If the distance is less
  than the radius the image name and title are printed.
  </p>
  <p>
  The image header keywords giving the observation coordinates are defined
  by the parameter set selected with the <i>keywpars</i> parameter.
  If no value is given then the parameters from the <b>keywpars</b>
  parameter set task are used.  The keywords required are those
  select by the <i>keywpars.ra</i>, <i>keywpars.dec</i>, and
  <i>keywpars.epoch</i>.  If the epoch is absent or zero then the
  keywords selected by <i>keywpars.date_obs</i> and <i>keywpars.ut</i>
  are used to compute an epoch.
  </p>
  <p>
  <b>Astradius</b> is a simple script which calls <b>astcalc</b>.  The
  command file is specified by the parameter <i>commands</i>.  The
  default file precesses the observation coordinates to the epoch
  of the search center coordinates and then computes the spherical
  distance between the search center and the observation.  Finally
  it tests the distance against the specified radius and prints
  the image name and title if the observation is within the radius.
  Users may copy the default command file and modify it.  The
  command syntax is described in the help for <b>astcalc</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Page the script task and the command file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page astutil$astradius.cl,astutil$astradius.dat
  # ASTRADIUS -- Find images within a radius.
  
  procedure astradius (images, racenter, deccenter, epcenter, radius)
  
  string  images = ""             {prompt="List of images"}
  string  racenter = ""           {prompt="RA center (hours)"}
  string  deccenter = ""          {prompt="DEC center (degrees)"}
  real    epcenter = 2000.        {prompt="Epoch of center"}
  real    radius = 60.            {prompt="Radius in arc seconds"}
  pset    keywpars = ""           {prompt="Keywords for RA, DEC, EPOCH\n"}
  
  file    commands = "astutil$astradius.dat"      {prompt="ASTCALC file"}
  
  begin
          astcalc (commands=commands, images=images, table="", verbose=no)
  end
  
   Print images which are within a given radius in the sky.
  
  # Get parameters.
  racenter = clget ("astradius.racenter")
  deccenter = clget ("astradius.deccenter")
  epcenter = clget ("astradius.epcenter")
  radius = clget ("astradius.radius")
  ra = imget(clget("keywpars.ra"))
  dec = imget(clget("keywpars.dec"))
  
  epoch = imget(clget("keywpars.epoch"))
  if (str(epoch) == "" || real(epoch) == 0.)
      date = imget(clget("keywpars.date_obs"))
      ut = imget(clget("keywpars.ut"))
      epoch = epoch (date, ut)
  endif
  
  # Precess image coordinates to center epoch and compute separation.
  radec = precess (ra, dec, epoch, epcenter)
  ra1 = ra_precess (ra, dec, epoch, epcenter)
  dec1 = dec_precess (ra, dec, epoch, epcenter)
  sep = arcsep (racenter, deccenter, ra1, dec1)
  
  # Print result if within radius.
  if (sep &lt; real (radius))
      printf ("%-15s %s\n", $I, imget ("title"))
  endif
  </pre></div>
  <p>
  2. Find images within an arc minute of a particular position.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; astradius
  List of images: *.imh
  RA center (hours): 13:31
  DEC center (degrees): 47:00
  Epoch of center (2000.):
  Radius in arc seconds (60.):
  obj0020.imh         m51 B 600s
  obj0021.imh         m51 V 600s
  obj0022.imh         m51 R 600s
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_ASTRADIUS">
  <dt><b>ASTRADIUS V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='ASTRADIUS' Line='ASTRADIUS V2.11' -->
  <dd>This task is new in this release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  astcalc, hselect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  
