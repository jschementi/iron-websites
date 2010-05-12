===============================
IronPython.net and IronRuby.net
===============================

Quickstart
----------
- Open ``iron-websites.sln`` in Visual Studio 2010 as "Administrator"
  That will setup IIS to serve the website from ``http://localhost/iron-websites``.
  Building the solution generates the website for viewing; see ``generate.bat``
  for details.

**If you prefer the command-line:**

- Generate HTML files for both ruby and python in-place and stage for deployment::

      generate.bat

- Generate HTML files in-place for a specific site::

      python generate.py -[python|ruby]
      
- Visit the site::

      start (python|ruby)\index.html

- Stage for deployment and view it::

      ruby deploy.rb

      start deploy\Iron(Ruby|Python)Net\index.html

- See "Deploying" section below for instruction on how to get your change
  checked in and pushed to the live website.

Overview
--------
`IronRuby.net <http://ironruby.net>`_ and `IronPython.net <http://ironpython.net>`_
share the same infrastructure; basically the same CSS, HTML templates, images,
HTML generation and deployment scripts. The only difference are the content,
which are stored in the ``python`` and ``ruby`` directories.

Getting the source
------------------
If you intend to submit a change to the website, please "fork" this repository
and follow the instructions on how to get the source code locally. This will
make it really easy to check-in your changes to your own private copy,
and then submit a pull-request to get your changes back into the original repo.

Updating content
----------------
The content of each website is represented by `reStructuredText <http://docutils.sourceforge.net/rst.html>`_,
a plaintext markup syntax. Each file is processed first by `jinja <http://pypi.python.org/pypi/Jinja2/2.0>`_, and then
by RST to generate a HTML file to disk.

Generating HTML files
---------------------
The logic for generating the HTML files is in ``generate.py``, including
navigation, style, and template info.::

    Usage: python generate.py -[python|ruby]
    
View website
------------
After generating the website, you can view it by going to the language-specific
folders:
- IronRuby: http://localhost/iron-websites/ruby/index.html
- IronPython: http://localhost/iron-websites/python/index.html

Staging for deploy
------------------
To stage the sites for deployment, use ``deploy.rb``::

    ruby deploy.rb
    
The websites are copied to:
- http://localhost/iron-websites/deploy/IronRubyNet
- http://localhost/iron-websites/deploy/IronPythonNet

These directories are ready to go online, with all dependencies self-contained.

Checking in your changes
------------------------
Before you deploy these changes to the live websites, they must be in the main
repository. 
Check your changes back into your own fork, and push them back up to github. Then
send a "pull-request", which effectively is a code-review. When jschementi signs
off on the changes, they'll be pulled into the main repository. Then you're ready
to deploy.

Deploying
---------
Pass the ``-production`` flag to actually push the site online. This requires
the correct FTP password to be in the passwd file; jschementi will give you
this password when your code-review is okayed.



Please ask jschementi if you have any additional questions.