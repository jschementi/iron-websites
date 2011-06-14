============
Get IronRuby
============


---------------
Stable versions
---------------
IronRuby maintains compatible versions with `Ruby 1.8.6`_ and `Ruby 1.9`_;
`IronRuby 1.0`_ and `IronRuby 1.1.3`_, respectively. If you're not sure
which version to use, use `IronRuby 1.1.3`_, but only if you do not need
`Ruby 1.8.6`_ compatibility.

.. container:: download col
   
   `Download IronRuby 1.0`_

`All major IronRuby releases`_


--------------
Latest version
--------------
The latest version of IronRuby is `IronRuby 1.1.3`_, which is
tracking compatibility with `Ruby 1.9.2`_.

.. container:: download col
   
   `Download IronRuby 1.1.3`_

-----------
Source code
-----------
Iron{{language}} is an `open source project`_ freely available under the `Apache License (Version 2)`_.

.. container:: download col
   
   `Download IronRuby 1.1.3 Source Code`_

   `Download IronRuby 1.0 Source Code`_

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



.. _Ruby 1.8.6:       http://ruby-lang.org/en/downloads/
.. _Ruby 1.9:       http://ruby-lang.org/en/downloads/
.. _Ruby 1.9.2:       http://ruby-lang.org/en/downloads/
.. _IronRuby 1.0:     http://ironruby.codeplex.com/releases/view/25901
.. _IronRuby 1.1.3:     http://ironruby.codeplex.com/releases/view/60511
.. _Download IronRuby 1.0:     http://ironruby.codeplex.com/releases/view/25901#DownloadId=116524
.. _Download IronRuby 1.1.3:     http://ironruby.codeplex.com/releases/view/60511#DownloadId=217152
.. _All major IronRuby releases: http://ironruby.codeplex.com/releases
.. _open source project: http://ironruby.codeplex.com
.. _Apache License (Version 2): http://ironruby.codeplex.com/license
.. _Download IronRuby 1.0 Source Code: https://github.com/IronLanguages/main/zipball/v1.0-rtm
.. _Download IronRuby 1.1.3 Source Code: https://github.com/IronLanguages/main/zipball/v1.1.3
.. _Download latest (zip): https://github.com/IronLanguages/main/zipball/master
.. _Browse Online: https://github.com/IronLanguages/main/tree/master/Languages/Ruby
.. _Recent Check-ins: https://github.com/IronLanguages/main/commits/master
.. _Instructions for accessing with GIT: https://github.com/IronLanguages/main/wiki/Getting-the-sources
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
