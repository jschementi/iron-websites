---------------
Getting Started
---------------
Give HTML the ability to be scripted with Python by simply referencing 
a JavaScript file::

    <script src="http://gestalt.ironpython.net/dlr-latest.js"
            type="text/javascript"></script>
 
Or, if you want to develop without a network connection, or deploy
IronPython yourself, simply extract the re-distributable package and 
reference it::

    <script type="text/javascript">
        window.DLR = {path: 'path/to/gestalt.latest'}
    </script>
    <script src="path/to/gestalt.latest/dlr.js" type="text/javascript">
    </script>

Note: depending on the ``gestalt.ironpython.net`` version is preferred (`see why <faq.html>`_).
However, rather than depending on ``dlr-latest.js``, you should pick a version
to ensure stability, like ``dlr-20091120.js``.
   
And that's it! Now you can place Python script tags on the HTML page to script
the HTML page. For example, here's handling a button click::

    <input id="button" type="button" value="Say, Hello!" />
    <script type="text/python">
      def button_onclick(s, e):
          window.Alert("Hello from Python!")
      document.button.onclick += button_onclick
    </script>

Vector-graphics can also be used; here's an example which loads a 
vector-graphics markup file in the 
`XAML <http://en.wikipedia.org/wiki/Extensible_Application_Markup_Language>`_
format and uses Python to start animations defined in the XAML file::

    <script id="blinking_mushroom" type="application/xml+xaml" width="200" height="230"
            src="xaml/blinking_mushroom.xaml"></script>

    <script class="blinking_mushroom" type="text/python">
      bm = xaml.blinking_mushroom
      bm.left_eye_blink.Begin()
      bm.right_eye_blink.Begin()
    </script>

Download
--------
No downloads are required to develop and deploy Python applications for the
browser, though you can always download the pieces hosted online.

- `Silverlight (developer version) <http://microsoft.com/silverlight>`_

  Though any Python-based web-applications will prompt the user to install
  Silverlight if it is not already, there is a specific version of Silverlight
  for developers, which contains full strings for error messages.

- `IronPython in Silverlight re-distributable package <gestalt-20091120.zip>`_
  
  Zip-compressed file containing all the pieces needed to develop and deploy
  Python applications for the browser. You can also download the contents 
  separately:
  
  - `dlr.js <http://gestalt.ironpython.net/dlr-latest.js>`_
  
    Handles enabling the HTML page to run Python code with IronPython in
    Silverlight.
    
  - `dlr.xap <http://gestalt.ironpython.net/dlr-latest/dlr.xap>`_
  - `Microsoft.Scripting.slvx <http://gestalt.ironpython.net/dlr-latest/Microsoft.Scripting.slvx>`_
  - `IronPython.slvx <http://gestalt.ironpython.net/dlr-latest/IronPython.slvx>`_

Examples
--------
- `Gestalt Widget Pack <http://www.visitmix.com/labs/gestalt/widgets/>`_

Documentation
-------------
- `Full Documentation <docs.html>`_
- Specs

  - `Back to "Just Text" <spec.v2.html>`_ (last updated: 2010-02-23)
  - `Dynamic Silverlight <spec.v1.html>`_ (last updated: 2008-03-14)

Public APIs
~~~~~~~~~~~
- dlr.js
- Microsoft.Scripting.Silverlight.dll
- DLR Hosting API

