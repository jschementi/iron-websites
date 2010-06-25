===================================
Ruby in the browser documentation
===================================

.. contents::

-----
Setup
-----
The only setup *absolutely* required is to reference ``dlr.js`` from any HTML 
file you wish write Ruby code in::

    <script src="http://gestalt.ironruby.net/dlr-latest.js"
            type="text/javascript"></script>

If you want to develop without a network connection, or deploy
IronRuby yourself, simply extract the re-distributable package and 
reference it::

    <script type="text/javascript">
        window.DLR = {path: 'path/to/gestalt.latest'}
    </script>
    <script src="path/to/gestalt.latest/dlr.js" type="text/javascript">
    </script>

.. note:: using the ``gestalt.ironruby.net`` version is preferred, especially in
   production. However, please pick a specific version (like ``dlr-20100305.js``,
   rather than ``dlr-latest.js``), as this will ensure your application keeps
   working between releases; ``dlr-latest.js`` will always point to the most
   recent version.

By default just doing this sets up your HTML page for executing Ruby code.
See the dlr.js API documentation for more advanced uses.


-------------------
Writing Ruby code
-------------------
Ruby code is executed by using HTML script-tags; either inline or as an
external file. This implementation aims to be compliant with the `HTML4
specification for scripting in HTML pages 
<http://www.w3.org/TR/html4/interact/scripts.html>`_.


Inline scripts
~~~~~~~~~~~~~~
The following attributes are used with a HTML script-tag to embed Ruby:

- ``type``: defines the mime-type the script code should map to; the following
  prefixes are allowed: ``application/``, ``text/``, and ``application/x-``.
  The actual language name will be passed to the DLR hosting API, so the above
  example could have used ``application/ironruby`` and it would still work::

      <script type="application/ruby">
        window.alert "Ruby inline script-tag" 
      </script>
      <script type="text/ruby">
        window.alert "Also a Ruby inline script-tag" 
      </script>

- (Optional) ``defer``: if this attribute is not present, its value is 
  ``false``. Otherwise, the value is ``true`` (even if it's explicitly set to 
  ``defer="false"``; this is how all modern browsers behave). If set to ``true``
  the code is not run; but it can be used to evaluate later::

      <script type="application/ruby" defer="true" id="for_later">
        puts 2 + 2
      </script>
      <script type="application/ruby">
        eval document.for_later.innerHTML
      </script>


External scripts
~~~~~~~~~~~~~~~~
The following attributes are used with a HTML script-tag to reference Ruby:

- ``src``: specify the path to a Ruby file. If it's a relative URI, it will
  be considered relative to the HTML file. The ``src`` URI is downloaded and
  cached in memory, building a virtual file-system of external script code.
  Then this file is executed in its own DLR ScriptScope, which properly
  isolates execution between scripts, and most closely matches what Ruby's
  ``import`` statement does.
  ::

      # foo.rb
      window.alert "Hello from a ruby file" 

      <!-- foo.html -->
      <script type="application/ruby" src="foo.rb"></script>

- ``type``: specifies the mime-type of the script-tag, which is used to figure
  out the language; see Inline Scripts ``type`` attribute.

  Technically this is not required, as the extension of the file will be used
  to detect the language if ``type`` is omitted, but most browsers will then
  attempt to run the code with it's built-in JavaScript engine, and most likely
  throw a JavaScript syntax exception. So, it's recommended to always using the
  ``type`` attribute.

- (Optional) ``defer``: See Inline Scripts ``defer`` attribute for symantics.
  If this is true, the ``src`` URI is just downloaded and cached, but is not
  run. This allows full control over when the script gets run, as another
  script can get the first shot at importing it::

      <script type="application/ruby" src="foo.rb" defer="true"></script> 
      <script type="application/ruby">import foo</script>


Execution order
~~~~~~~~~~~~~~~
Script-tags will be executed in the order they are defined, but before the
`start script <start-script>`_ is executed (if one is provided). All inline
code is to be executed in the same scope, basically as if they all one Ruby
file. This allow methods defined in one script-tag to be called from another::

    <script type="application/ruby">
      window.alert "in first script-tag" 
      def foo
        "In Foo"
      end
    </script>
    ...
    <script type="application/ruby">
      window.alert "in second script-tag"
      window.alert foo
    </script>


File-system operations
~~~~~~~~~~~~~~~~~~~~~~
Silverlight runs in a sand-box, not allowing programs access to the machine's
file system, as well as forbidding native user-code from being loaded. However,
IronRuby's implementation abstracts file-system operations, allowing it to
provide different behavior when running in Silverlight. External script tags
are used to define the file system entries.


Ruby script files
+++++++++++++++++++
Each time an external script-tag is downloaded, it is also cached in-memory so
the same file isn't re-downloaded. This download cache is actually presented to
Ruby as a read-only file system, which is how things like ``require`` still
work; they are actually asking if the file exists, except all file-system
operations in Silverlight are redirected to the download cache.


Zip files
+++++++++
The external script tag's ``src`` attribute can be a ``*.zip`` file; this is
useful for larger libraries where it may be cumbersome to list all the script
files out as script-tags.

The following attributes are used with a HTML script-tag to reference zip files:

- ``src``: URI to a ``*.zip`` file.

  The value of the src attribute will be placed on the language's path, and
  basically treated as a folder. When a script file is requested from any other
  script, the language will try to find it by using its path and checking for
  the existence of the file. If the path contains a known zip file name, then
  it will continue to look inside the zip file::

      <script type="application/x-zip-compressed" src="lib.zip"></script>
      <script type="application/ruby">
        $LOAD_PATH << 'lib'
        require 'erb'
      </script>

- ``type``: must be set to ``application/x-zip-compressed``
- *Not implemented yet* (Optional) ``defer``: toggles whether the zip file is placed on the path. 
  Defaults to false which adds it to the path, while true will not add it to the
  path. When ``defer="true"`` you can always programmatically add it to the path
  using Ruby's sys module::

      <script type="application/x-zip-compressed" src="ruby-stdlib.zip" defer="true"> 
      </script> 
      <script type="application/x-ruby"> 
        $LOAD_PATH << "ruby-stdlib"
      </script>

Note: "added the zip file to the path" is not implemented at the moment, so
it will always behave as ``defer="true"``.

Since zip files are treated just like a folder, you can put anything inside
the ZIP file; DLLs, XAML files, text files, images, etc, and use them just
like you would if they were part of the file-system::

    <script type="application/x-zip-compressed" src="my-archive.zip"></script>
    <script type="application/ruby">
      require "my-archive.zip/Foo.dll"
      txt = File.read "my-archive/foo.txt"
    </script>

When accessing files inside a zip file, just use the zip filename as if it were
a folder name.

Note: Today only the zip file's filename (without the .zip extension) is
required to access it (example: ``open('my-archive/foo.txt')``), though that's
a bug in the implementation, not the spec.


---------------
Vector-graphics
---------------
Silverlight not only provides an execution model for Ruby scripts, but it also
allows for rendering vector graphics in the browser, for animations or rich 
user-interfaces. This can be accomplished by using `eXtensible Application
Markup Language (XAML) <http://msdn.microsoft.com/en-us/library/ms752059.aspx>`_,
or directly from Ruby.


XAML
~~~~
XAML markup can be embedded into a script-tag, either inline or as an external
file::

    <!-- inline XAML file -->
    <script type="application/xaml+xml" id="inlineXAML" width="200" height="75">
      <Canvas Background="Wheat">
        <TextBlock Canvas.Left="20" FontSize="24" />
      </Canvas>
    </script>

    <!-- external XAML file -->
    <script type="application/xaml+xml" id="externalXAML" src="foo.xaml">
    </script>

The following attributes are used with a HTML script-tag to embed XAML content:

- ``width``: the width of Silverlight control surface.

- ``height``: the height of Silverlight control surface.

- ``type``: should be set to ``application/xaml+xml``, though
  ``application/xml+xaml`` also works.

- ``src``: URI to a XAML file. It behaves like external scripts ``src``
  attribute with regard to downloading and caching. If it is not set, the XAML
  content is expected to be provided in the script-tag's innerText.

- ``id``: DOM ID the generated Silverlight control will have; this is needed
  to tell Ruby code to run against a specific Silverlight control.

- (Optional) ``defer``: By default either the external or inline XAML
  causes ``dlr.js`` to inject a Silverlight control, and set the RootVisual of
  that Silverlight instance to the XAML provided by the script-tag. However, if
  this is ``true``, the Silverlight control is still injected into the DOM, but
  the XAML content is not set as the RootVisual of that control. If the XAML
  content was provided by the ``src`` attribute, then the file is still
  downloaded and cached. Setting the RootVisual can be done manually, however::

      <script type="application/xaml+xml" id="xamlContent" defer="true">
        <Canvas Background="Wheat">
          <TextBlock Canvas.Left="20" FontSize="24" />
        </Canvas>
      </script>

      <script type="application/ruby" class="xamlContent">
        include System::Windows
        Application.current.load_root_visual_from_string document.xamlContent.innerHTML
      </script>
  
  If you do not want to even have the control added, then you'll have to
  disable dlr.js's auto-adding::

      <script type="text/javascript">
        window.DLR = {autoAdd: false}
      </script>
      <script type="text/javascript" src="dlr.js"></script>
      
      <script type="application/xaml+xml" id="xamlContent" defer="true">
        <Canvas Background="Wheat">
          <TextBlock Canvas.Left="20" FontSize="24" />
        </Canvas>
      </script>

  Then you can add a control at any time::

      <script type="text/javascript">
        DLR.createObject({width: 200, height: 200});
      </script>


This is similar to the way that `Silverlight 1.0 allowed XAML to be embedded
<http://msdn.microsoft.com/en-us/library/cc189016(VS.95).aspx>`_.


From Ruby
~~~~~~~~~~~
XAML is simply a markup language for creating objects, so the same thing can
be done directly from Ruby. Given this XAML::
      
    <script type="application/xaml+xml" id="xamlContent">
      <Canvas Background="Wheat">
        <TextBlock Canvas.Left="20" FontSize="24" />
      </Canvas>
    </script>

The equivalent in Ruby would be::

    import System::Windows
    import System::Windows::Media
    import System::Windows::Controls
    c = Canvas.new
    c.background = SolidColorBrush.new Colors.wheat
    t = TextBlock.new
    t.font_size = 24
    c.children.add t
    Canvas.set_left t, 20
    Application.current.root_visual = c


--------------------------
Unclassified documentation
--------------------------
This is just random documentation, which has yet to be incorporated into a place
that makes sense.


Multiple controls
~~~~~~~~~~~~~~~~~
Browsers allow for multiple object-controls to be on a single page, so you
could have multiple Silverlight controls on the same page. This introduces an
unexpected side-effect to having Silverlight run code inside script-tags;
every Silverlight would run run every script-tag. Consider the following::

    <div id="message"></div>
    <script src="dlr.js"></script>
    <script type="text/javascript">
      DLR.createObject({width: '100', height: '100'})
    </script>
    <script type="application/ruby">
      include System::Windows
      Application.current.root_visual = UserControl.new
    </script>

Both Silverlight controls will get their `root_visual` set, since the Ruby
script-tag is executed twice, once for each Silverlight control. To avoid
this, script-tags must be scoped to a specific Silverlight control. ``dlr.js``
instructs ``dlr.xap`` to only run "un-scoped" script-tags on the first control
added to a page, and only run "scoped" script-tags with subsequent added
controls. To "scope" a script-tag, the class attribute contains the same value
as its corresponding Silverlight control's ``xamlid`` initParam::

    <script type="text/javascript">
      DLR.createObject({xamlid: 'control1'})
    </script>
    <script type="application/ruby" class="control1">
      # will only run in the "control1" object
    </script>

An un-scoped script-tag is simply a script-tag without a class attribute.
These will run in a Silverlight control that does not have the "xamlid"
initParam set; dlr.js does this for only the first control it injects.

If you intend to not use Silverlight graphics through script-tags, or only use
them in one control, then you don't need to worry about scoping; scoping only
comes into play when you have multiple controls. If you want to use
Silverlight graphics, you can use this same strategy on script-tags containing
XAML to make sure the proper RootVisual is set.

A script-tag having a "*" class attribute will cause it to run in every
script-tag, so the first-example's behavior is still possible.


Changes to existing behavior 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Though there are no major breaking changes to any existing behavior of
existing applications, there needs to be some changes to existing features to
make this new activation-model work properly.

Previously, the "start" initParam (entry-point/start-script to the DLR
Silverlight app) is required if there is no ``app.*`` file in the XAP file. If
the "start" initParam is omitted in this condition, an error would have been
raised, complaining about not finding an ``app.*`` file.

This requirement is now completely relaxed; neither an app.* file or a "start"
initParam is required. If no "start" script or defer=false script-tags exist
on the page; then nothing runs and no error is raised. This is relaxed because
a Silverlight application can be only inline XAML.
::

    <script type="application/ruby"> 
      ... 
    </script> 
    <object ...> 
      <params name="source" value="app.xap" /> 
      <params name="initParams" value="" /> <!-- no initParams value needed --> 
    </object> 
 
Though these changes are being introduced to remove the need for Chiron, it is
still a useful tool for generating XAP files on the fly. Chiron now serves
files out of the "externalUrlPrefix" path if it is a relative path, so
extensions can be developed locally and Chiron instantly picks them up. Also,
Chiron's XAP building features will build an appropriate XAP file depending on
whether you're using slvx files or not.


Interacting with markup
~~~~~~~~~~~~~~~~~~~~~~~
To make accessing the HTML and XAML easier and more like how JavaScript works,
variables pointing to them are added to the scope in which script-tags are
executed in.

HTML accessors
++++++++++++++

`document` maps to `System.Windows.Browser.HtmlPage.Document`, which is of type
`HtmlDocument`, and `window` maps to `System.Windows.Browser.HtmlPage.Window`, which
is of type `HtmlWindow`.
 
When a method is called on an `HtmlDocument` that does not exist, it calls
`GetElementById(methodName)`. The following examples are in Ruby::

    document.a_div_id 
    # same as ... 
    document.GetElementById("a_div_id") 

    document.doesnotexist # None 
 
When a method is called on an `HtmlElement` that does not exist, it should call
`GetProperty(methodName)`. When calling the non-existent method as a setter,
call `SetProperty(methodName, value)`::

    document.a_div_id.innerHTML 
    # same as ... 
    document.a_div_id.GetProperty("innerHTML") 

    document.a_div_id.innerHTML = "Hi" 
    # same as ... 
    document.a_div_id.SetProperty("innerHTML", "Hi") 
 
When an indexer is used on an `HtmlElement`, it should call
``GetAttribute(methodName)``. When setting the indexer, call
``SetAttribute(methodName, value)``::

    document.link_id['href'] 
    # same as ... 
    document.link_id.GetAttribute('href') 
 
    document.link_id['href'] = 'http://foo.com' 
    # same as ... 
    document.a_div_id.SetAttribute('href', 'http://foo.com') 

XAML accessors
++++++++++++++

``me`` and ``xaml`` both map to ``System.Windows.Application.Current.RootVisual``, having a
base-type of ``FrameworkElement``. When a method is called that does not exist on
``me`` or ``xaml``, then ``FindName(methodName)`` is called. This allows access to any
XAML elements with an ``x:Name`` value to be accessed by the ``x:Name`` value as a
method call::

    xaml.Message.Text = "New Message"
 

To load a XAML file into the root visual, use the ``LoadRootVisual`` methods::

    xaml.LoadRootVisual(UserControl.new, File.open("foo.xaml"))
    xaml.LoadRootVisualFromString(document.xamlContent.innerHTML)


Event handling from code
++++++++++++++++++++++++

From code, events on both HTML and XAML elements can be hooked via the
language's specific .NET event hookup syntax. Given the following HTML::

    <a id="cm">Click Me</a>

You can hook the ``onclick`` event from Ruby::

    <script type="application/ruby"> 
      document.cm.onclick do |s, e|
        s.innerHTML = "Clicked!"
      end
    </script> 
 
Hooking XAML events also works::

    <script type="application/xml+xaml"> 
      ... 
      <TextBox x:Name="xcm" Text="Click Me" /> 
      ... 
    </script>

    <script type="application/ruby">
      include System::Windows
      root_visual = Application.current.root_visual
      root_visual.xcm.MouseLeftButtonDown do |s, e|
        s.text = "Clicked!"
      end
    </script> 

Event handling from HTML or XAML markup is not supported!


Debugging
~~~~~~~~~

Visual Studio Debugger
++++++++++++++++++++++

When you have debug mode turned on, it will just work as it used to. Attach
the debugger to the browser, open the script file in Visual Studio, place a
breakpoint, etc. Having the script files in the XAP does not make a difference
for debugging; it's all about the debug-able code being generated and having
the file open in VS.


----------------------
Implementation details
----------------------

Silverlight XAP file structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
With both user scripts and larger libraries outside the main XAP file, the
main XAP only serves as a container for the AppManifest.xaml and any dynamic
language assemblies required by the application. Silverlight 3 introduced
"Transparent Silverlight Extensions", a way to package your own libraries into
a .slvx (Silverlight versioned extension) file (really just zip file) which
applications can depend on by referencing it from their AppManifest.xaml.
Using this feature all the assemblies can be removed from the XAP file, put in
a slvx file, and hosted on an internet location so other applications can
depend on it. Instead of IronRuby and IronRuby releases containing the
assemblies built for Silverlight, they will just contain a dlr.xap file. This
xap file will be shared between all applications; only advanced scenarios will
need to modify the xap file. It will only containing just two files:

AppManifest.xaml
++++++++++++++++
The AppManifest.xaml file just references the Microsoft.Scripting.slvx file,
and points the Silverlight application at the static entry point in
Microsoft.Scripting.Silverlight.dll (included in Microsoft.Scripting.slvx)::

    <Deployment 
     xmlns="http://schemas.microsoft.com/client/2007/deployment" 
     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
     RuntimeVersion="3.0.40624.0" 
     EntryPointAssembly="Microsoft.Scripting.Silverlight" 
     EntryPointType="Microsoft.Scripting.Silverlight.DynamicApplication"> 
     <Deployment.ExternalParts> 
       <ExtensionPart Source="http://gestalt.ironruby.net/dlr-20100305/Microsoft.Scripting.slvx"/> 
     </Deployment.ExternalParts> 
    </Deployment> 

languages.config
++++++++++++++++
The languages.config file lists the configuration information for DLR
languages that can be used in Silverlight. This file can be present in a
DLR-based xap today for defining configuration information for languages other
than Ruby and Ruby, but now this file must be present if an application
depends on the Microsoft.Scripting.slvx file. Included in this information is
the URL for each language's slvx file::

    <Languages> 
        <Language names="IronRuby;Ruby;rb" 
                  extensions=".rb" 
                  languageContext="IronRuby.Runtime.RubyContext" 
                  assemblies="IronRuby.dll;IronRuby.Libraries.dll" 
                  external="http://gestalt.ironruby.net/dlr-20100305/IronRuby.slvx" /> 
    </Languages> 
  
The language node can have the following attributes: 

- ``names``: ``;``-separated list of names the language can use 
- ``extensions``: ``;``-separated list of file extensions the language can use 
- ``languageContext``: language's type that inherits from ``LanguageContext``
- ``assemblies``: URIs to assemblies which make up the language

  - Optional: but if external is missing, then this list of assemblies is
    assumed to be in the XAP

- ``external``: SLVX file for all language assemblies

Microsoft.Scripting.slvx
++++++++++++++++++++++++
Microsoft.Scripting.slvx will contain the following DLLs:
- Microsoft.Scripting.dll 
- Microsoft.Dynamic.dll 
- Microsoft.Scripting.Core.dll 
- Microsoft.Scripting.ExtensionAttribute.dll 
- Microsoft.Scripting.Silverlight.dll

When an application starts up, Silverlight downloads the
Microsoft.Scripting.slvx file, loads all the assemblies inside it, and then
kicks off the static entry point,
Microsoft.Scripting.Silverlight.DynamicApplication. During its startup logic,
it tries to load language configuration from the languages.config file; if
that fails it looks to already loaded assemblies referenced in the
AppManifest.xaml and loads the configuration info off the assemblies directly.
Because of this, XAP files must have a languages.config to download languages
on-demand. After the language configuration is loaded, the script-tags on the
HTML page are processed; for each language used, the existence of all the
language's assemblies in the XAP file is checked, and if they are not all
found the language's external-package is downloaded, assemblies inside loaded,
and a ScriptEngine created for the language. Both the list of assemblies and
external-package URI are provided by languages.config.

If an application cannot depend on the slvx files hosted on the internet, they
can be hosted on any machine. Just change the AppManifest.xaml and
languages.config to point to the new location. If Chiron is still being used
to generate the XAP file, then the externalUrlPrefix in Chiron.exe.config is
the only setting that needs to be changed.


---------
Non-goals
---------
These are clearly non-goals for IronRuby, though some persuasion might move
them up into ideas.

jQuery-influenced selectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Though the idea of having a jQuery-like selector API for DLR languages is
attractive, it is less feasible since each language will want a different way
to specify the syntax. Also, libraries in those languages may exist (eg.
Ruby's Hpricot), so it'd be best to use those directly. This might be
addressed in a future change, or another library, but is out of scope for this
change.


---
FAQ
---

The "start" script referenced in the Inline Scripts section ... what is it?
 
    The "start" script is another term for the entry-point script. By default it's
    ``app.*``, and ``*`` is used to figure out the correct language to instantiate.
    However, the user can specify the specific start-script in the initParams::
 
        <param name="initParams" value="start=myapp.rb" />
 
    See the original dynamic languages in Silverlight specification for more
    information TODO add link.

Can I write offline Silverlight applications with this? 
 
    Not with Silverlight 3. Offline Silverlight applications do not allow using
    the browser DOM APIs, since they just run the Silverlight control outside the
    browser. Therefore, offline Silverlight applications cannot use <script> tag
    code. If you'd like to write a Silverlight application that runs both in the
    browser and on the desktop, you'll need to keep everything in the XAP file and
    use the "start" script as the application's entry-point. Silverlight 4
    supports HTML hosted in an OOB app, so it's possible to directly support this
    in the future.

-----
Specs
-----
- `Back to "Just Text" <spec.v2.html>`_ (last updated: 2010-02-23)
- `Dynamic Silverlight <spec.v1.html>`_ (last updated: 2008-03-14)

-----------
Public APIs
-----------
- dlr.js
- Microsoft.Scripting.Silverlight.dll
- DLR Hosting API

