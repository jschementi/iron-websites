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
navigation, style, and template info. The simplest way to generate the HTML
files is to just use::

    generate.bat
    
This will generate HTML for both sites and stage it for deployment. If for some
reason you only want to generate HTML for a specific site, you can use the
``-python`` or ``-ruby`` flags

    Usage: python generate.py [-python|-ruby|-h]
    
View website
------------
After generating the website, you can view it by going to the language-specific
directories:
- ruby/index.html
- python/index.html

Staging for deploy
------------------
If you used ``generate.bat``, you already have staged the sites for deployment.
Otherwise, just run ``deploy.rb``::

    ruby deploy.rb
    
The websites are then staged at:
- deploy\IronRubyNet
- deploy\IronPythonNet

These directories are ready to go online, with all dependencies self-contained.

Checking in your changes
------------------------
Before you deploy these changes to the live website(s), they must be checked into
the main repository, or else you risk someone else deploying changes which overwrite
yours. Here's the simple steps:

1. Push your changes back into your own fork.
2. Send a "pull-request", which effectively starts a code-review.
3. When jschementi signs off on the changes, they'll be pulled into the main
   repository, and then you're ready to deploy.

Deploying
---------

Currently deploying is only a manual process, so the completion of the
code review will also include pushing the site live. Please let jschementi
know if the changes are urgent.

..
  Pass the ``-production`` flag to actually push the site online. This requires
  the correct FTP password to be in the passwd file; jschementi will give you
  this password when your code-review is okayed.


Please ask jschementi if you have any additional questions.