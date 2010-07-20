===================
New release process
===================

Here's how to add a new IronPython release to the website:

1. Add a new announcement to python/index.rst, as well as python/announcements/index.rst. For
   example

  .. admonition:: July 16, 2010
     :class: strip

     `IronPython 2.7 Alpha 1 <http://ironpython.codeplex.com/releases/view/42434>`_
     was released, supporting Python 2.7 features and now being licensed under
     the `Apache License (Version 2) <http://ironpython.codeplex.com/license>`_.

2. If this is a new stable version, update the ``language_info`` entry for IronPython
   in generate.py.
   
3. If this is a Alpha or Beta release, update the "Latest Release" section of
   python/download/index.rst. Make sure the links at the bottom of the file
   are correct.

4. Update python/tools/download/index.html with the new release location,
   if IronPython tools is included in this release. Also add a new entry to
   python/tools/download/versions.html.