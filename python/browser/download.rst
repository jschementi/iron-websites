--------
Download
--------
**No** downloads are required to develop and deploy Python applications for the
browser, though you can always download the pieces hosted online (for working
without a network connection).

- `Silverlight (developer version) <http://microsoft.com/silverlight>`_

  Though any Python-based web-applications will prompt the user to install
  Silverlight if it is not already, there is a specific version of Silverlight
  for developers, which contains full strings for error messages.

- `IronPython in Silverlight re-distributable package <gestalt-20091120.zip>`_
  
  Zip-compressed file containing all the pieces needed to develop and deploy
  Python applications for the browser. Here are its contents:
  
  - `dlr.js <http://gestalt.ironpython.net/dlr-20091120.js>`_
  
    Handles enabling the HTML page to run Python code with IronPython in
    Silverlight.
    
  - `dlr.xap <http://gestalt.ironpython.net/dlr-20091120/dlr.xap>`_

    Actual static Silverlight application, which has logic for executing
    Python.

  - `Microsoft.Scripting.slvx <http://gestalt.ironpython.net/dlr-20091120/Microsoft.Scripting.slvx>`_
    and `IronPython.slvx <http://gestalt.ironpython.net/dlr-20091120/IronPython.slvx>`_
 
    IronPython binaries, including the Dynamic Language Runtime.
