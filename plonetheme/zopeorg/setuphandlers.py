# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__docformat__ = 'plaintext'

import collective.setuphandlertools as sht
import logging
logger = logging.getLogger("plonetheme.zopeorg")

def setup_content(context):
    if sht.isNotThisProfile(context, 'plonetheme.zopeorg_setup_content.txt'):
        return

    site = context.getSite()
    sht.delete_items(site, ('front-page', 'news', 'events'), logger)
    sht.hide_and_retract(site['Members'], logger)

    content_structure = [

        {'type': 'Collage', 'title': u'Start', 'id': 'front-page',
         'data': { 'show_title': False, 'show_description': False, },
         'childs': [
             {'type': 'CollageRow', 'title': '', 'id': '1',
              'childs': [
                  {'type': 'CollageColumn', 'title': '', 'id': '1',
                   'opts': {'setLayout': 'collage_teaser_view',},
                   'childs': [
                       {'type': 'Image', 'title': 'The World of Zope',
                        'data': {'description':
u"""Zope is a free and opensource web application server written in the object-oriented
programming language "Python". Since its release in 1998 Zope continued to grow and
evolved into many distinct applications, frameworks, libraries and tools.""",
                        'image': sht.load_file(globals(), 'setupdata/teaser_world-of-zope-plain.jpg'),
                        'teaser_url': u'../the-world-of-zope',
                        'teaser_style': u'position: absolute; left: 480px; top: 167px; font-size: 12pt; color: white;',
                                },
                        },
                       ],
                   },
                  ],
              },
             {'type': 'CollageRow', 'title': '', 'id': '2',
              'childs': [
                  {'type': 'CollageColumn', 'title': '', 'id': '1',},
                  {'type': 'CollageColumn', 'title': '', 'id': '2',},
                  ],
              },

             ],
         },

# THE WORLD OF ZOPE
        {'type': 'Folder', 'title': u'The World of Zope',
         'childs': [
###
             {'type': 'Folder', 'title': u'Application Servers',
              'childs': [

              {'type': 'Document', 'title': u'Zope',
              'data': {'description':u"""Zope is a Python-based application server for building secure and highly scalable web applications.""",
                       'text':
u"""<p>The Zope 2 Application Server: <a class="external-site" href="http://zope2.zope.org/">zope2.zope.org</a></p>"""}},

              {'type': 'Document', 'title': u'BlueBream',
              'data': {'description':u"""BlueBream, the successor of Zope3.""",
                       'text':
u"""<p>BlueBream is a web framework written in the Python programming language.
BlueBream is free/open source software, owned by the Zope Foundation, licensed
under the Zope Public License (BSD like, GPL compatible license). BlueBream was
previously known as Zope 3.</p>
<p>BlueBream: <a class="external-site" href="http://bluebream.zope.org/">bluebream.zope.org</a></p>"""}},

                  ]},
###
             {'type': 'Folder', 'title': u'Zope based CMS',
              'childs': [

              {'type': 'Document', 'title': u'Plone',
              'data': {'description':u"""Plone, the enterprise ready Content Management System based on Zope.""",
                       'text':
u"""<p>A powerful, flexible Content Management solution that is easy to install,
use and extend. Plone lets non-technical people create and maintain information
using only a web browser. Perfect for web sites or intranets, Plone offers
superior security without sacrificing extensibility or ease of use</p>
<p>Plone CMS: <a class="external-site" href="http://plone.org/">plone.org</a></p>"""}},

              {'type': 'Document', 'title': u'Silva',
              'data': {'description':u"""Silva - content management for organizations.""",
                       'text':
u"""<p>Silva is a powerful CMS for organizations that manage multiple or complex
websites. Content is stored in clean and futureproof XML, independent of layout
and presentation. Features include versioning, workflow system, integral visual
editor, content reuse, sophisticated access control, multi-site management,
extensive import/export facilities, fine-grained templating, and hi-res image
storage and manipulation. Silva has an open source (BSD) license.</p>
</p>
<p>The Silva Content Management System: <a class="external-site" href="http://infrae.com/products/silva">infrae.com/products/silva</a></p>"""}},
                  ]},
###
             {'type': 'Folder', 'title': u'Databases',
              'childs': [

              {'type': 'Document', 'title': u'ZODB',
              'data': {'description':u"""Zope Object DataBase, since 1998.""",
                       'text':
u"""<p>The Zope Object Database (ZODB) provides seamless object persistence in
Python. It gets rid of requiring a relational database for your object-oriented
application and provides you with a powerful and safe object store: persistence,
transactions, scalability, and more.</p>
<p>Zope Object Database - a native object database for Python: <a class="external-site" href="http://zodb.org/">zodb.org</a></p>"""}},
                  ]},

             {'type': 'Folder', 'title': u'Tools',
              'childs': [

              {'type': 'Document', 'title': u'Buildout',
              'data': {'description':u"""Software build system for repeatable deployments.""",
                       'text':
u"""<p>Buildout is a Python-based build system for creating, assembling and
deploying applications from multiple parts, some of which may be
non-Python-based. It lets you create a buildout configuration and reproduce the
same software later.</p>
<p>Buildout software build system: <a class="external-site" href="http://buildout.org/">buildout.org</a></p>"""}},
                  ]},
###
             {'type': 'Folder', 'title': u'Frameworks',
              'childs': [

              {'type': 'Document', 'title': u'CMF',
              'data': {'description':u"""Content Management Framework (CMF) for Zope""",
                       'text':
u"""<p>The Content Management Framework (CMF) for Zope provides a powerful,
tailorable platform for building content management applications.</p>
<p>Zope Content Management Framework <a class="external-site" href="http://zope.org/Products/CMF/">zope.org/Products/CMF</a></p>"""}},

              {'type': 'Document', 'title': u'Five',
              'data': {'description':u"""Use Zope3 technologies in Zope2, 3+2=5.""",
                       'text':
u"""<p>Five is a Zope 2 product that allows you to integrate Zope 3 technologies
into Zope 2, today. After its start as an independent product Five is now fully
integrated with Zope 2.</p>
<p>Five - The Zope 3 in Zope 2 project: <a class="external-site" href="http://codespeak.net/z3/five/">codespeak.net/z3/five</a></p>"""}},

              {'type': 'Document', 'title': u'Grok',
              'data': {'description':u"""Grok's Zope made easy.""",
                       'text':
u"""<p>Grok is a web application framework for Python developers. It is aimed at
both beginners and very experienced web developers. Grok has an emphasis on
agile development. Grok is easy and powerful.</p>
<p>Grok - A Smashing Web Framework: <a class="external-site" href="http://grok.zope.org/">grok.zope.org</a></p>"""}},

              {'type': 'Document', 'title': u'Repoze',
              'data': {'description':u"""Repoze integrates Zope technologies with WSGI and reusable Python middleware.""",
                       'text':
u"""Plumbing Zope into the WSGI Pipeline: <p><a class="external-site" href="http://repoze.org/">repoze.org</a></p>"""}},

              {'type': 'Document', 'title': u'ZCA',
              'data': {'description':u"""The Zope Component Architecture.""",
                       'text':
u"""<p>The Zope Component Architecture (ZCA) was introduced in Zope3, which
evolved from Zope 2. It improves the development experience through highly
reusable components.</p>
<p>ZCA / Zope3: <a class="external-site" href="http://wiki.zope.org/zope3">wiki.zope.org/zope3</a></p>"""}},

              {'type': 'Document', 'title': u'ZPT',
              'data': {'description':u"""Zope Page Templates, the best you can get.""",
                       'text':
u"""<p>Zope Page Templates is Zope's templating mechanism. ZPT allows reusable
Template snippets through macros, object and view-context attribute access and a
good seperation from logic. They were introduced after Zope invented the
meanwhile deprecated DTML language.</p>
<p>Zope Page Templates: <a class="external-site" href="http://docs.zope.org/zope2/zope2book/AppendixC.html">docs.zope.org/zope2/zope2book/AppendixC.html</a></p>"""}},

              {'type': 'Document', 'title': u'ZTK',
              'data': {'description':u"""The Zope Tool Kit libraries.""",
                       'text':
u"""<p>The Zope Toolkit (ZTK) is a set of libraries intended for reuse by
projects to develop web applications or web frameworks. It is developed by the
contributors of the Zope Foundation. The whole collection of ZTK libraries are
used in various web frameworks and web application servers. Two of these are
managed by the Zope project: Zope 3 and Grok. If you install one of these
systems, you will get the ZTK along with it automatically.</p>
<p>Zope Toolkit: <a class="external-site" href="http://docs.zope.org/zopetoolkit/">docs.zope.org/zopetoolkit</a></p>"""}},

                  ]},

         ]},

# NEWS AND EVENTS
        {'type': 'Folder', 'title': u'News & Events'},

# COMMUNITY
        {'type': 'Folder', 'title': u'Community',
         'childs': [

             {'type': 'Document', 'title': u'Mailing Lists',
              'data': {'description':u"""Zope related mailing lists.""",
                       'text':
u"""<p>Main Zope related mailing list collection: <a class="external-site" href="https://mail.zope.org/mailman/listinfo">https://mail.zope.org/mailman/listinfo</a></p>"""}},

             {'type': 'Document', 'title': u'IRC',
              'data': {'description':u"""Meet Zopistas in Internet Relay Chat channels""",
                       'text':
u"""<p>freenode.net hosts lots of Zope and Zope products/application related
IRC channels. Visit <a class="external-site" href="http://irc.freenode.net/">irc.freenode.net</a>
and try one of the following channels:</p>
<ul>
<li>#zope</li>
<li>#zope.de</li>
<li>#zope3-dev</li>
<li>#plone</li>
<li>#plone-framework</li>
<li>#plone-tuneup</li>
</ul>"""}},

             {'type': 'Document', 'title': u'Websites',
              'data': {'description':u"""Other Zope related websites""",
                       'text':
u"""<p>German Zope website: <a class="external-site" href="http://zope.de/">zope.de</a></p>"""}},

             {'type': 'Document', 'title': u'Planets',
              'data': {'description':u"""News collections from differnt Zope related blogs.""",
                       'text':
u"""<p>Planet Zope: <a class="external-site" href="http://planet.zope.org/">planet.zope.org</a></p>
<p>Planet Plone: <a class="external-site" href="http://planet.zope.org/">planet.plone.org</a></p>
<p>Planet Python: <a class="external-site" href="http://planet.zope.org/">planet.python.org</a></p>"""}},

             {'type': 'Document', 'title': u'Google Wave',
              'data': {'description':u"""The next big thing in collaborative computing.""",
                       'text':
u"""<p>Visit Google Wave and get in touch with Zope developers and Users:#
<a class="external-site" href="https://wave.google.com/wave/#restored:search:with%253Apublic+zope,restored:wave:googlewave.com!w%252Bkt1bTmUmA">Public Zope Wave</a></p>"""}},
             ]},

# RESOURCES
        {'type': 'Folder', 'title': u'Resources',
         'childs': [

             {'type': 'Document', 'title': u'Code Repositories',
              'data': {'description':u"""Code Repositories for Zope and related projects.""",
                       'text':
u"""<p>Zope public subversion repository provides read-only and selective write
access to the source code for Zope's and related projects.<br />
<a class="external-site" href="http://svn.zope.org/">svn.zope.org</a></p>"""}},

             {'type': 'Document', 'title': u'PyPI',
              'data': {'description':u"""Zope projects @ Python Package Index""",
                       'text':
u"""<p>Zope2 related projects: <a class="external-site" href="http://pypi.python.org/pypi?:action=browse&show=all&c=514">Framework :: Zope2</a></p>
<p>ZTK, ZCA and other Zope3 related projects: <a class="external-site" href="http://pypi.python.org/pypi?:action=browse&show=all&c=515">Framework :: Zope3</a></p>"""}},

             {'type': 'Document', 'title': u'Bug tracking',
              'data': {'description':u"""Search for Bugs and file them there, if you finde some.""",
                       'text':
u"""<p>Launchpad is an open source suite of tools that help people and teams to
work together on software projects. Launchpad is built with Zope 3.<br />
<a class="external-site" href="https://launchpad.net/zope/">Zope project hub @ Launchpad</a></p>"""}},

             {'type': 'Document', 'title': u'Documentation',
              'data': {'description':u"""Get documentation about Zope and it's tools here""",
                       'text':
u"""<p>Hub site to Zope community documentation projects:
<a class="external-site" href="http://docs.zope.org/">docs.zope.org</a>.</p>"""}},

             {'type': 'Document', 'title': u'Wiki',
              'data': {'description':u"""Community maintained documentation, scratchpad and further information.""",
                       'text':
u"""<p>Hub site to Zope community wiki documentation:
<a class="external-site" href="http://wiki.zope.org/">wiki.zope.org</a>.</p>"""}},

             {'type': 'Document', 'title': u'Books',
              'data': {'description':u"""Get Books about Zope for online and offline reading.""",
                       'text':
u"""<h2>Zope</h2>
<h2>Plone</h2>
<h2>Grok</h2>
<h2>Zope3</h2>
<h2>Bluebream</h2>
<h2>Repoze</h2>
<h2>Component Architecture</h2>"""}},

             {'type': 'Document', 'title': u'Archive',
              'data': {'description':u"""Looking for the ancient Zope website? Visit old.zope.org.""",
                       'text':
u"""<p>Old Zope website: <a class="external-site" href="http://old.zope.org/">old.zope.org</a>.</p>"""}},

         ]},

# ZOPE FOUNDATION
        {'type': 'Folder', 'title': u'Foundation',
         'childs': [

             {'type': 'Document', 'title': u'Zope Foundation',
              'setDefault': True,
              'data': {'description':u"""The Zope Foundation has the goal to promote, maintain, and develop the Zope platform. It does this by supporting the Zope community.""",
                       'text':
u"""<p>Our community includes the open source community of contributors to the
Zope software, contributors to the documentation and web infrastructure, as well
as the community of businesses and organizations that use Zope. The Zope
Foundation is the copyright holder of the Zope software and many extensions and
associated software. The Zope Foundation also manages the zope.org website, and
manages the infrastructure for open source collaboration.</p>
<p>For more information, visit:
<a class="external-site" href="http://foundation.zope.org/">foundation.zope.org</a>."""}},

             {'type': 'Document', 'title': u'Contact',
              'data': {'description':u"""Contacting the Zope Foundation""",
                       'text':
u"""<p>Zope Foundation<br />
901 Tyrrell Road<br />
Raleigh, NC 27609<br />
USA</p>
<p><b>Email</b>: 
<a href="mailto:foundation-info@zope.org">foundation-info@zope.org</a></p> 
<p><b>Fax</b>:     +1 (703) 842-8076</p>"""}},

         ]},

        {'type': 'Document', 'title': u'Legal', 'id': u'legal',
         'opts': {'setExcludeFromNav': True},
         'data': {'description':u"""Zope.org Legal Notice.""",
                  'text':
u"""<p>All materials found on this web site are the property of Zope Foundation 
and all rights are reserved. The information contained in and on the various pages 
of the Zope.org web site have been issued for general distribution under 
the protection of United States copyright laws. In addition to US copyright laws, 
the information presented on Zope.org web site is protected under the 
Berne Convention for the Protection of Literature and Artistic works, as well as 
under other international conventions and under national laws on copyright and 
neighboring rights.</p>
<p>Extracts of the information in the web site may be reviewed, reproduced or 
translated for research or private study but not for sale or for use in conjunction 
with commercial purposes. Any use of information in the web site should be 
accompanied by an acknowledgment of Zope.org as the source, citing the 
uniform resource locator (URL) of the article. Reproduction, translation or any 
use of this website requires explicit prior authorization in writing. Applications 
and inquiries should be addressed to <a href="mailto:foundation-info@zope.org">foundation-info@zope.org</a>.</p>
<p>Any mention of specific companies or of certain manufacturers' products on 
Zope.org's web site does not imply that they are endorsed or recommended 
by Zope Foundation in preference to others of a similar nature that are not 
mentioned. Errors and omissions excepted, the names of proprietary products are 
distinguished by initial capital letters.</p>
<p>Zope Foundation does not warrant that the information contained in the web 
site is complete and correct and shall not be liable whatsoever for any damages 
incurred as a result of its use.</p>
<p>For further inquiry, please contact <a href="mailto:foundation-info@zope.org">foundation-info@zope.org</a>.</p>"""}},

    ]
    sht.create_item_runner(site, content_structure, logger=logger)
