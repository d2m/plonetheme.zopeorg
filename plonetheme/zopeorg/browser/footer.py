# -*- coding: utf-8 -*-
 
from zope.interface import implements, alsoProvides
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewlet
from zope.deprecation.deprecation import deprecate

from plone.app.layout.globals.interfaces import IViewView 

from AccessControl import getSecurityManager
from Acquisition import aq_base, aq_inner
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from cgi import escape
from urllib import quote_plus

from plone.app.layout.viewlets.common import ViewletBase


class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/footer.pt')

    def update(self):
        super(FooterViewlet, self).update()

        self.navigation_root_url = self.portal_state.navigation_root_url()

     
