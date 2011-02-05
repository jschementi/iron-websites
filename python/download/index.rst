==============
Get IronPython
==============


---------------
Stable versions
---------------
IronPython maintains compatible versions with `Python 2.5`_ and `Python 2.6`_;
`IronPython 2.0.3`_ and `IronPython 2.6.2`_, respectively. If you're not sure
which version to use, use `IronPython 2.6.2`_.

`All major Iron{{language}} releases`_


--------------
Latest version
--------------
The latest version of IronPython is `IronPython 2.7 Beta 1`_, which is
tracking compatibility with `Python 2.7`_.

.. container:: download col
   
   `Download IronPython 2.7 Beta 1`_


-----------
Source code
-----------
IronPython is an `open source project`_ freely available under the `Apache License (Version 2)`_.

.. container:: download col
   
   `Download IronPython 2.7 Beta 1 Source Code`_
   
   `Download IronPython 2.6.2 Source Code`_

`Download latest (zip)`_ | `Browse Online`_ | `Recent Check-ins`_

`Instructions for accessing with GIT`_

.. container:: divider

   _

-------------
Prerequisites
-------------
Iron{{language}} is a cross-platform and cross-browser programming language,
so prerequisites will vary based on usage.

Here are the recommended runtimes are for each platform:


Windows desktop & server apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. container:: strip

   On Windows for desktop and server usage, the .NET framework is the
   recommended runtime.
 
   .. container:: download
 
     `Latest .NET version (4.0)`_

   .. note::
 
      | Iron{{language}} also runs on .NET: `3.5 SP1`_, but must be compiled from
      | source.

Windows & Mac OS browser apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. container:: strip
   
   On Windows & Mac OS for browser usage, Silverlight is the recommended
   runtime.

   .. container:: download

      `Latest Silverlight version (4.0)`_

   Silverlight enables you to use {{language}} to script HTML pages just as
   you would with JavaScript, and also enables advanced vector graphics
   for rich user-interfaces and video.
    
   |
   | `Learn more about {{language}} in the browser`_


Mac OS & Linux desktop & server apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. container:: strip
      
   IronPython runs on
   Mono_, a cross platform, open source .NET framework,
   enables IronPython to be used on Linux, Mac OS, and BSD systems.

   .. container:: download

      `Latest Mono version (2.6.4)`_

Linux browser apps
~~~~~~~~~~~~~~~~~~
.. container:: strip

   IronPython also runs on Moonlight_, a open source 
   implementation of Microsoft Silverlight for Unix systems.

   .. container:: download

      `Latest Moonlight version (2.0)`_


   .. note::

      | Moonlight 2 targets the Silverlight 2 API, so if you want to
      | run the same application on all platforms make sure to only use
      | Silverlight 2 APIs, or provide a fallback implementation for
      | Moonlight.



.. _Python 2.5:       http://www.python.org/download/releases/2.5/
.. _Python 2.6:       http://www.python.org/download/releases/2.6/
.. _Python 2.7:       http://www.python.org/download/releases/2.7/
.. _IronPython 2.0.3: http://ironpython.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=30416
.. _IronPython 2.6.2:   http://ironpython.codeplex.com/releases/view/41236
.. _IronPython 2.7 Beta 1:   http://ironpython.codeplex.com/releases/view/48818
.. _Download IronPython 2.7 Beta 1: http://ironpython.codeplex.com/releases/view/48818#DownloadId=159517
.. _All major Iron{{language}} releases: http://iron{{language_lower}}.codeplex.com/wikipage?title=SupportedReleaseList
.. _open source project: http://iron{{language_lower}}.codeplex.com
.. _Apache License (Version 2): http://ironpython.codeplex.com/license
.. _Download IronPython 2.6.2 Source Code: http://ironpython.codeplex.com/releases/view/41236#DownloadId=159516
.. _Download IronPython 2.7 Beta 1 Source Code: http://ironpython.codeplex.com/releases/view/48818
.. _Download latest (zip): http://github.com/iron-languages/main
.. _Browse Online: http://github.com/iron-languages/main
.. _Recent Check-ins: http://github.com/iron-languages/main
.. _Instructions for accessing with GIT: http://github.com/iron-languages/main
.. _Latest .NET version (4.0): http://bit.ly/iron-dotnet40
.. _4.0: http://bit.ly/iron-dotnet40
.. _3.5 SP1: http://bit.ly/iron-dotnet35sp1
.. _3.5: http://bit.ly/iron-dotnet35
.. _3.0: http://bit.ly/iron-dotnet3
.. _2.0 SP1: http://bit.ly/iron-dotnet20sp1
.. _Latest Silverlight version (4.0): http://go.microsoft.com/fwlink/?linkid=150228
.. _Learn more about {{language}} in the browser: ../browser/
.. _Mono: http://www.mono-project.com
.. _Latest Mono version (2.6.4): http://www.go-mono.com/mono-downloads/download.html
.. _Moonlight: http://www.mono-project.com/Moonlight
.. _Latest Moonlight version (2.0): http://go-mono.com/moonlight-beta
