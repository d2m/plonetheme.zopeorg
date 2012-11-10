# -*- coding: utf-8 -*-
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

        {'type': 'Image', 'title': 'old.zope.org Screenshot',
         'id': u'Screenshotold.zope.org.png',
         'opts': {'setExcludeFromNav': True},
         'data': {'image': sht.load_file(globals(),
                               'setupdata/Screenshotold.zope.org.png')}},

        {'type': 'Folder', 'title': u'Teasers',
         'opts': {'workflow': None, # leave private
                  'setLocallyAllowedTypes': ['Teaser',],
                  'setImmediatelyAddableTypes':['Teaser',],
                  'setLayout': 'folder_summary_view'},
         'childs': [
             {'type': 'Teaser', 'title': 'The World of Zope',
              'data': {'image': sht.load_file(globals(),
                                'setupdata/teaser_world-of-zope.jpg'),
                       'importance': u'3'}}]},

        {'type': 'Collage', 'title': u'Start', 'id': 'front-page',
         'data': { 'show_title': False, 'show_description': False, },
         'childs': [
             {'type': 'CollageRow', 'title': '', 'id': '1',
              'childs': [
                  # the following column should hold a teaser portlet
                  {'type': 'CollageColumn', 'title': '', 'id': '1'}]},
             {'type': 'CollageRow', 'title': '', 'id': '2',
              'childs': [
                  {'type': 'CollageColumn', 'title': '', 'id': '1',
                   'childs': [
                        {'type': 'Document', 'title': u'Zope Community', 'id': u'front-community',
                         'opts': {'setExcludeFromNav': True},
                         'data': {'text': START_ZOPE_COMMUNITY_TEXT}}]},
                  {'type': 'CollageColumn', 'title': '', 'id': '2',
                   'childs': [
                        {'type': 'Document', 'title': u'Zope Foundation', 'id': u'front-foundation',
                         'opts': {'setExcludeFromNav': True},
                         'data': {'text': START_ZOPE_FOUNDATION_TEXT}}]},
                  {'type': 'CollageColumn', 'title': '', 'id': '3',
                   'childs': [
                        {'type': 'Document', 'title': u'Zope.org legacy', 'id': u'front-legacy',
                         'opts': {'setExcludeFromNav': True},
                         'data': {'text': START_ZOPEORG_LEGACY_TEXT}}]},
            ]},
        ]},

        {'type': 'Document', 'title': u'The World of Zope', 'id': 'the-world-of-zope',
         'data': {'text': THE_WORLD_OF_ZOPE_TEXT}},

        {'type': 'Document', 'title': u'News & Events', 'id': u'news-events',
         'data': {'text': NEWS_EVENTS_TEXT}},

        {'type': 'Document', 'title': u'Community', 'id': u'community',
         'data': {'text': COMMUNITY_TEXT}},

        {'type': 'Document', 'title': u'Resources', 'id': u'resources',
         'data': {'text': RESOURCES_TEXT}},

        {'type': 'Document', 'title': u'Zope Foundation', 'id': u'foundation',
         'data': {'text': ZOPE_FOUNDATION_TEXT}},

        {'type': 'Document', 'title': u'Legal', 'id': u'legal',
         'opts': {'setExcludeFromNav': True},
         'data': {'description':u"""Zope.org Legal Notice.""",
                  'text': LEGAL_TEXT}},
    ]
    sht.create_item_runner(site, content_structure, logger=logger)

    #the collage column will hold a portlet, so the view must be portlets-top
    from Products.Collage.interfaces import IDynamicViewManager
    manager = IDynamicViewManager(site['front-page']['1']['1'])
    manager.setLayout('portlets-top')

    #set the link reference in the teaser
    site['teasers']['the-world-of-zope'].setLink_internal(site['the-world-of-zope'])
    site['teasers']['the-world-of-zope'].reindexObject()

START_ZOPE_COMMUNITY_TEXT = u"""
<p>The Zope community is one of the largest and most professional open-source communities worldwide.</p>
<p><a class="internal-link" href="../community">Learn more...</a></p>
"""
START_ZOPE_FOUNDATION_TEXT = u"""
<p>The Zope Foundation has the goal to promote, maintain, and develop the Zope platform.</p>
<p><a class="internal-link" href="../foundation">Learn more...</a></p>
"""

START_ZOPEORG_LEGACY_TEXT = u"""
<p><a href="http://old.zope.org/" style="padding-left: 0px; "><img alt="old.zope.org" class="image-right" src="Screenshotold.zope.org.png"></a>Looking for the ancient Zope website?</p>
<p>Visit&nbsp;<a class="external-link" href="http://old.zope.org/">old.zope.org</a></p>
"""

THE_WORLD_OF_ZOPE_TEXT = u"""
<p>During more than a decade Zope Corp. and the Zope Community have grown an outstanding set of products and technologies, influencing the general development of Python based Web application servers and tools.</p>

<h2 class="accordion">Frameworks</h2>

<p><strong>ZCA<br /></strong>The Zope Component Architecture provides facilities for defining, registering and looking up components. It's perfect for building enterprise applications based on loosely coupled components.</p>
<p>More information at <a class="external-link" href="http://wiki.zope.org/zope3/ComponentArchitectureOverview">Component Architecture Overview</a>, <a class="external-link" href="http://docs.zope.org/zope.component/">zope.component documentation</a> and <a class="external-link" href="http://docs.zope.org/zope.interface/">zope.interface documentation</a></p>

<p><strong>ZTK<br /></strong>The Zope Toolkit (ZTK) is a set of libraries intended for reuse by projects to develop web applications or web frameworks. The ZCA is part of it.</p>
<p>More information at the <a class="external-link" href="http://docs.zope.org/zopetoolkit/">Zopetoolkit documentation</a></p>

<p><strong>ZPT<br /></strong>Zope Page Templates is Zope's templating mechanism.</p>
<p>More information at the <a class="external-link" href="ZPT documentation in Zope2 Book">docs.zope.org/zope2/zope2book/AppendixC.html</a>. An alternative implementation provides <a class="external-link" href="http://chameleon.repoze.org/">Chameleon</a>.</p>

<p><strong>CMF</strong><br />The Content Management Framework (CMF) for Zope provides a powerful, tailorable platform for building content management applications together with the Zope Application Server.</p>
<p>More information at the <a class="external-link" href="http://old.zope.org/Products/CMF/">CMF Product Page</a></p>

<p><strong>Repoze<br /></strong>Repoze integrates Zope technologies with WSGI and reusable Python middleware.</p>
<p>More information at <a class="external-link" href="http://repoze.org">repoze.org</a></p>

<h2 class="accordion">Databases</h2>
<p><strong>ZODB</strong><br />The Zope Object DataBase (ZODB) is a native object database, that stores your objects while allowing you to work with any paradigms that can be expressed in Python.</p>
<p>More information at <a class="external-link" href="http://zodb.org">zodb.org</a></p>

<h2 class="accordion">Application Servers</h2>
<p><strong>Zope<br /></strong>Zope is a Python-based application server for building secure and highly scalable web applications.</p>
<p>More information at <a class="external-link" href="http://zope2.zope.org">zope2.zope.org</a></p>
<p><strong>BlueBream</strong><br />BlueBream – formerly known as Zope 3 – is a web framework written in the Python programming language.</p>
<p>More information at <a class="external-link" href="http://bluebream.zope.org">bluebream.zope.org</a></p>
<p><strong>Grok<br /></strong>Grok is a web application framework for Python developers.</p>
<p>More information at <a class="external-link" href="http://grok.zope.org">grok.zope.org</a></p>

<h2 class="accordion">Tools</h2>
<p><strong>Buildout</strong><br />Buildout is a Python-based build system for creating, assembling and deploying applications from multiple parts, some of which may be non-Python-based.</p>
<p>More information at <a class="external-link" href="http://www.buildout.org">Buildout.org</a></p>

<h2 class="accordion">Zope based Software</h2>
<p><strong>Plone</strong><br />
Plone is a user friendly Content Management System running on top of Python, Zope and the CMF. It's a perfect fit in collaborative, enterprise environments but also for small sites.</p>
<p>More information at <a class="external-link" href="http://www.plone.org">Plone.org</a></p>
<p><strong>Pyramid</strong><br />Pyramid is a small, fast, down-to-earth, open source Python web application development framework. It makes real-world web application development and deployment more fun, more predictable, and more productive.</p>
<p>More information at <a class="external-link" href="http://www.pylonsproject.org/projects/pyramid/about">Pyramid</a></p>
<p><strong>Twisted</strong><br />An asynchronous, extensible networking framework, with special focus on event-based programming and multiprotocol integration.</p>
<p>More information at <a class="external-link" href="http://twistedmatrix.com/">twistedmatrix.com</a></p>
<p><strong>Mailman 3</strong><br />Mailman is free software for managing electronic mail discussion and e-newsletter lists.</p>
<p>More information at <a class="external-link" href="https://launchpad.net/mailman">Mailman</a></p>
<p><strong>Silva</strong><br /><span>Silva is a powerful CMS for organizations that manage multiple or complex websites.</span></p>
<p>More information at <a class="external-link" href="http://infrae.com/products/silva">Silva</a></p>
<p><strong>ERP5</strong><br /><span>ERP5 is a full featured Open Source ERP/CRM application framework, based on an unified Model to describe its implementation.
<p>More information at <a class="external-link" href="http://www.erp5.com/">ERP5.com</a></p>
"""

NEWS_EVENTS_TEXT = u"""
<p>Find interesting news and events listed at <a class="external-link" href="http://calendar.zope.org">calendar.zope.org</a>.</p>
<p>Additional information is available from the major RSS feeds</p>
<ul>
<li><a class="external-link" href="http://planet.plone.org">Planet Plone</a></li>
<li><a class="external-link" href="http://planet.python.org">Planet Python</a></li>
</ul>
"""
# Planet Zope doesn't exist any more
# <li><a class="external-link" href="http://planetzope.org">Planet Zope</a></li>

COMMUNITY_TEXT = u"""
<p>The Zope community is one of the largest and most professional open-source communities worldwide.</p>
<h2>Mailing Lists</h2>
<p>Main Zope related mailing list collection is available at <a class="external-link" href="https://mail.zope.org/mailman/listinfo">mail.zope.org/mailman/listinfo</a></p>
<h2>IRC</h2>
<p style="padding-left: 0px; ">freenode.net hosts lots of Zope and Zope products/application related IRC channels. Visit <a class="external-link" href="http://irc.freenode.net">irc.freenode.net</a> and try one of the following channels: #zope, #zope.de, #zope3-dev, #plone, #bluebream, #grok</p>
<h2 style="padding-left: 0px; ">Websites</h2>
<p style="padding-left: 0px; ">Localized Zope related websites, e.g. <a class="external-link" href="http://www.zope.de">www.zope.de<br /></a>Audience/Tool/Product targeted websites, e.g. <a class="external-link" href="http://zope2.zope.org">zope2.zope.org</a>, <a class="external-link" href="http://bluebream.zope.org">bluebream.zope.org</a>, <a class="external-link" href="http://grok.zope.org">grok.zope.org</a>, <a class="external-link" href="http://docs.zope.org">docs.zope.org</a>, <a class="external-link" href="http://buildout.zope.org">buildout.zope.org</a></p>
<h2 style="padding-left: 0px; ">Planets</h2>
<p style="padding-left: 0px; ">News collections from different Zope related blogs, like <a class="external-link" href="http://planetzope.org">Planet Zope</a>, <a class="external-link" href="http://planet.plone.org">Planet Plone</a> and <a class="external-link" href="http://planet.python.org">Planet Python</a>.</p>
"""

RESOURCES_TEXT = u"""
<h2>Code Repositories</h2>
<p>Zope public subversion repository provides read-only and selective write access to the source code for Zope's and related projects: <a class="external-link" href="http://svn.zope.org">svn.zope.org</a></p>
<h2>PyPI</h2>
<p>Zope projects @ Python Package Index: <a class="external-link" href="http://pypi.python.org/pypi?:action=browse&amp;amp;show=all&amp;amp;c=514">Zope2 related projects</a>, <a class="external-link" href="http://pypi.python.org/pypi?:action=browse&amp;amp;show=all&amp;amp;c=515">Zope3 related projects</a></p>
<h2>Bug tracking</h2>
<p>Launchpad is an open source suite of tools that help people and teams to work together on software projects. Launchpad itself is built with Zope 3. Look at the <a class="external-link" href="https://launchpad.net/zope/">Zope project hub @ Launchpad</a></p>
<h2>Documentation</h2>
<p>The hub website to Zope community documentation projects is at <a class="external-link" href="http://docs.zope.org/">docs.zope.org</a></p>
<h2>Wiki</h2>
<p>Community maintained documentation, scratchpad and further information. Hub site to Zope community wiki documentation: <a class="external-link" href="http://wiki.zope.org/">wiki.zope.org</a></p>
<h2>Books</h2>
<p>Get Books about Zope for online and offline reading.</p>
<p>Books on Zope, Plone, Grok, Zope3, Bluebream, Repoze, Zope Component Architecture</p>
<h2>Archive</h2>
<p>Looking for the ancient Zope website? Visit <a class="external-link" href="http://old.zope.org">http://old.zope.org</a>.</p>
"""

ZOPE_FOUNDATION_TEXT = u"""
<p>The Zope Foundation has the goal to promote, maintain, and develop the Zope platform. It does this by supporting the Zope community.</p>
<p>Our community includes the open source community of contributors to the Zope software, contributors to the documentation and web infrastructure, as well as the community of businesses and organizations that use Zope. The Zope Foundation is the copyright holder of the Zope software and many extensions and associated software. The Zope Foundation also manages the zope.org website, and manages the infrastructure for open source collaboration.</p>
<p>For more information, visit <a class="external-link" href="http://foundation.zope.org">foundation.zope.org</a>.</p>
<h2>Contacting the Zope Foundation</h2>
<p style="padding-left: 30px; ">
    <strong>Zope Foundation</strong><br />
    Email: <a class="mail-link" href="mailto:foundation-info@zope.org">foundation-info@zope.org</a><br />
    Fax: +1 (703) 842-8076<br />
</p>
"""

LEGAL_TEXT = u"""
<p>All materials found on this web site are the property of Zope Foundation
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
<p>For further inquiry, please contact <a href="mailto:foundation-info@zope.org">foundation-info@zope.org</a>.</p>
"""
