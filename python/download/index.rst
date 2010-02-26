==============
Get IronPython
==============


--------
Versions
--------
IronPython maintains compatible versions with `Python 2.5`_ and `Python 2.6`_;
`IronPython 2.0.3`_ and `IronPython 2.6`_, respectively. If you're not sure
which version to use, use `IronPython 2.6`_.

`All major IronPython releases`_


-----------
Source code
-----------
IronPython is an `open source project`_ freely available under the `Microsoft
Public License`_.

.. container:: download col
   
   `Download IronPython 2.6 Source Code`_

`Download latest (zip)`_ | `Browse Online`_ | `Recent Check-ins`_

`Instructions for accessing with SVN or TFS`_

.. container:: divider

   _

-------------
Prerequisites
-------------
IronPython is a cross-platform and cross-browser programming language,
so prerequisites will vary based on usage.

Here are the recommended runtimes are for each platform:


Windows desktop & server apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. container:: strip

   On Windows for desktop and server usage, the .NET framework is the
   recommended runtime. Keep in mind the latest version is already installed
   on all Windows Vista and Windows 7 machines.
 
   .. container:: download
 
     `Latest .NET version (3.5 SP1)`_

   .. note::
 
      | IronPython also runs on the pre-released `.NET 4.0 RC`_, 
      | as well as previous versions of .NET: `3.5`_, `3.0`_, and `2.0 SP1`_. 

Windows & Mac OS browser apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. container:: strip
   
   On Windows & Mac OS for browser usage, Silverlight is the recommended
   runtime.

   .. container:: download

      `Latest Silverlight version (3.0)`_

   Silverlight enables you to use Python to script HTML pages just as
   you would with JavaScript, and also enables advanced vector graphics
   for rich user-interfaces and video.
    
   |
   | `Learn more about Python in the browser`_


Mac OS & Linux desktop & server apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. container:: strip
      
   IronPython runs on
   Mono_, a cross platform, open source .NET framework,
   enables IronPython to be used on Linux, Mac OS, and BSD systems.

   .. container:: download

      `Latest Mono version (2.4)`_

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
.. _IronPython 2.0.3: http://ironpython.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=30416
.. _IronPython 2.6:   http://ironpython.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=12482
.. _All major IronPython releases: http://ironpython.codeplex.com/wikipage?title=SupportedReleaseList
.. _open source project: http://ironpython.codeplex.com
.. _Microsoft Public License: http://www.opensource.org/licenses/ms-pl.html
.. _Download IronPython 2.6 Source Code: http://ironpython.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=12482#DownloadId=96608
.. _Download latest (zip): http://ironpython.codeplex.com/SourceControl/ListDownloadableCommits.aspx#DownloadLatest
.. _Browse Online: http://ironpython.codeplex.com/SourceControl/BrowseLatest
.. _Recent Check-ins: http://ironpython.codeplex.com/SourceControl/ListDownloadableCommits.aspx
.. _Instructions for accessing with SVN or TFS: http://ironpython.codeplex.com/SourceControl/ListDownloadableCommits.aspx
.. _Latest .NET version (3.5 SP1): http://bit.ly/iron-dotnet35sp1
.. _.NET 4.0 RC: http://www.microsoft.com/downloads/details.aspx?FamilyID=a9ef9a95-58d2-4e51-a4b7-bea3cc6962cb
.. _3.5: http://bit.ly/iron-dotnet35
.. _3.0: http://bit.ly/iron-dotnet3
.. _2.0 SP1: http://bit.ly/iron-dotnet20sp1
.. _Latest Silverlight version (3.0): http://go.microsoft.com/fwlink/?linkid=150228
.. _Learn more about Python in the browser: ../browser/
.. _Mono: http://www.mono-project.com
.. _Latest Mono version (2.4): http://www.go-mono.com/mono-downloads/download.html
.. _Moonlight: http://www.mono-project.com/Moonlight
.. _Latest Moonlight version (2.0): http://go-mono.com/moonlight-beta
