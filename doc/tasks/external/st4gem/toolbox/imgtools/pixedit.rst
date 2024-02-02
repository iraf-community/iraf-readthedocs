.. _pixedit:

pixedit: Screen editor for image pixels
=======================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pixedit image
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is a screen editor for images. The screen is divided into two
  windows, the image window and the command window.  You edit a image by
  moving the cursor in the image window with the cursor keys and typing
  in the new value of the image pixel. The screen scrolls both sideways
  and up and down as you move the cursor, so all pixels of the image can
  be reached. Other editing commands are entered in the command window.
  To switch from the image window to the command window, you press the
  EXIT key. The default binding for the EXIT key is Control-Z, however, you can
  change this default, as described later. 
  </p>
  <p>
  After performing a command,
  the editor returns to the image window, unless the
  command exits the editor. The most important commands in command mode
  are `help', `exit', and `quit'. The `help' command displays all the
  commands and editing key bindings. The `exit' command will get you out
  of the editor and automatically save the edited image. The `quit'
  command will get you out of the editor after asking you whether you
  want to save the image. By default, the editor modifies a copy instead
  of the original image, so if you quit without saving the image, the
  original image is still there without any modifications.
  </p>
  <p>
  Some editing commands are entered from the command window.  To get to
  the command window, press the EXIT key. This key is bound to Control-Z by
  default. If you enter a blank line, the editor will return to the
  image window. Some commands take arguments. They can be included when
  the command is entered, or if they are omitted, the editor will prompt
  you for their values.  When the editor interactively prompts you for a
  command argument it sometimes displays a default value for the
  argument.  You may edit the default value or use it unchanged.
  Command names can be abbreviated, as long as the abbreviation is
  unique. All commands have unique single letter abbreviations.
  </p>
  <p>
  The following is a list of commands:
  </p>
  <dl id="l_exit">
  <dt><b>exit</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='exit' Line='exit' -->
  <dd>Exit the image editor, saving any changes made to the image.
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format &lt;fmt_string&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='format' Line='format &lt;fmt_string&gt;' -->
  <dd>Change the display format of image pixels. The format string may be
  either a Fortran SPP format string. SPP format strings should start
  with a <span style="font-family: monospace;">"%"</span>. Example format strings would be f10.3 for real images or
  i7 for integer images.
  </dd>
  </dl>
  <dl id="l_goto">
  <dt><b>goto &lt;row&gt; &lt;column&gt; &lt;plane&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='goto' Line='goto &lt;row&gt; &lt;column&gt; &lt;plane&gt;' -->
  <dd>Move the cursor to the indicated pixel. The number of arguments for
  this command is equal to the dimesionality of the image. This command
  is the only way to move between planes in a three dimensional image.
  </dd>
  </dl>
  <dl id="l_help">
  <dt><b>help</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='help' Line='help' -->
  <dd>Display online help information for the image editor. The help includes 
  a brief description of each command line command and the key bindings 
  for image editing commands.
  </dd>
  </dl>
  <dl id="l_quit">
  <dt><b>quit</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='quit' Line='quit' -->
  <dd>Exit the image editor. If the image has been changed, the image editor 
  will ask you whether to save it before exiting.
  </dd>
  </dl>
  <p>
  The bindings to the image editing keys are read from the edcap file.
  This is the same file which is used to define the key bindings for the
  parameter editor and history editor. The edcap file defines key
  bindings which resemble those of commonly used text editors. Three
  edcap files are distributed with IRAF. They define key bindings which
  resemble edt, emacs, and vi. These edcap files are located in the dev$
  directory and have the extension <span style="font-family: monospace;">".ed"</span>. The appropriate file is chosen
  according to the value of the environment variable 'editor'. If you
  want to customize the key bindings of the image editor, copy the
  appropriate edcap file from the dev$ directory to your home$ directory
  and edit the second column of the file. The image editor searches your
  home directory first for the edcap file and if it does not find it,
  then it searches the dev$ directory.
  </p>
  <p>
  The image editor also uses the termcap file to determine the screen
  size and the escape sequences used to modify the screen. There are
  entries in the termcap file for almost all terminal types. The proper
  entry is selected according to the environment variable terminal. To
  change your terminal type or the screen size, use the iraf stty
  command. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image [string]' -->
  <dd>The name of the image to be edited. 
  The editor checks for the
  existence of the image and its access mode before editing. If you do
  not have write access to a image you can display it using this
  task by setting 'readonly'
  to <span style="font-family: monospace;">"yes"</span>, but you will be unable to overwrite the original image.
  </dd>
  </dl>
  <dl>
  <dt><b>(silent = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(silent = no) [boolean]' -->
  <dd>Disable the bell?
  Setting this to <span style="font-family: monospace;">"yes"</span> will ring a bell whenever a warning
  message is displayed.
  </dd>
  </dl>
  <dl>
  <dt><b>(readonly = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(readonly = no) [boolean]' -->
  <dd>Use the editor to display the image only?
  Set this parameter to <span style="font-family: monospace;">"yes"</span> if you want to use the editor to view a
  image but not to modify it. This parameter prevents you from executing
  any command that would modify the file.
  </dd>
  </dl>
  <dl>
  <dt><b>(inplace = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inplace = no) [boolean]' -->
  <dd>Overwrite the original image?
  Set this to <span style="font-family: monospace;">"yes"</span> if you want to edit the image in place. This speeds
  the editor startup time when editing large images. If 'readonly' is
  set to <span style="font-family: monospace;">"yes"</span> the image is always edited in place.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Interactively edit an image called 'omegcen.hhh'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; pixedit omegcen.hhh
  </pre></div>
  <p>
  2. Edit the image in readonly mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; pixedit omegcen.hhh read+
  </pre></div>
  </section>
  <section id="s_see_also_">
  <h3>See also </h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'SEE ALSO '  -->
  
