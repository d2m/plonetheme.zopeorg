==================
plonetheme.zopeorg
==================

Introduction
============

``plonetheme.zopeorg`` is an installable Plone Theme developed by the 2010 www.zope.org 
relaunch. It is based on the ``dzug.theme`` as used for www.zope.de using the **theming** 
and **packaging** features available in `plone.app.theming`_.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/d2m/plonetheme.zopeorg/raw/master/preview.png

Examples
========

This add-on can be seen in action at the following sites:

- http://www.zope.org/
- http://www.zope.de/


Features
========

- It's an installable Plone Theme package.
- Adds support for allows editors to align new or existing content from multiple sources 
  in a layout. An example of such a page is one that shows a document along with one or 
  more collections using `Products.Collage`_.
- Adds support for a column layout that allows the local assignment of portlets that 
  will display in that column using `collective.collage.portlets`_.
- Adds support Teaser/Banner content type for Plone using `collective.teaser`_.
- After installation from Add-ons controlpanel, this theme is enabled with the basic styles, 
  then you need to create and enabled the default layout and created the contents, please 
  read the *Usage* section.


Installation
============


If you are a developer, you might enjoy installing it via buildout.

For install ``plonetheme.zopeorg`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.zopeorg


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.zopeorg',
    ],


Deployment
----------

* Import the Generic Setup default profile via ``portal_setup``.

  * Go to ``ZMI`` > ``portal_setup`` > ``Import`` tab > Select Profile or Snapshot 
    ``plonetheme.zopeorg: setup content`` from the list and ``Import all steps``.

  * Go to ``ZMI`` > ``portal_setup`` > ``Import`` tab > Select Profile or Snapshot 
    ``plonetheme.zopeorg: setup portlets`` from the list and ``Import all steps``.

* Clear and Rebuild the catalog.


Usage
=====

* For add default layout builded with `Products.Collage`_ product, go to the 
  **/select_default_page** view and select a ``Start`` content type and save it.

* Using the `collective.teaser`_ product, you can manage teaser portlets, go to the 
  **@@manage-teaserportlets** view, then add a ``Teaser Portlet`` just select 
  from the ``Image Scale`` list the ``1_full(952, 952)`` option and unchecking the 
  ``Show title`` option,  and save it.


Contribute
==========

- Issue Tracker: https://github.com/d2m/plonetheme.zopeorg/issues
- Source Code: https://github.com/d2m/plonetheme.zopeorg


License
=======

``plonetheme.zopeorg`` is published under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 license.


Copyright
---------

``plonetheme.zope.org`` is (C) 2010, Zope Foundation and Contributors


Contributors
------------

* Andreas Jung (Lead)
* Michael Haubenwallner
* Kai Mertens (Design)
* Johannes Raggam
* Jan Filip Tristan Hasecke (zope.de Theme)
* Leonardo Caballero 

.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Products.Collage`: https://pypi.org/project/Products.Collage/
.. _`collective.collage.portlets`: https://pypi.org/project/collective.collage.portlets/
.. _`collective.teaser`: https://pypi.org/project/collective.teaser/
