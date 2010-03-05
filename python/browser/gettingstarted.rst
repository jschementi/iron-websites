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

Note: depending on the ``gestalt.ironpython.net`` version is preferred.
``dlr-latest.js`` will always give you the latest version of IronPython.
You can also pick a specific version to ensure stability, like ``dlr-20100305.js``.
   
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

And that's it! Next see some `Examples`_, `Download`_ things to your local
machine, and learn more from the `Documentation`_.

.. _Examples: examples.html
.. _Download: download.html
.. _Documentation: docs.htma
