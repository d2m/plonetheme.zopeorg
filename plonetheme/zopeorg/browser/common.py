# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from collective.teaser.browser.common import get_teasers

from zope.interface import Interface

class IZopeorgTheme(Interface):
    """Zope.org theme layer
    """

class FooterViewlet(ViewletBase):
    def update(self):
        super(FooterViewlet, self).update()
        self.navigation_root_url = self.portal_state.navigation_root_url()

class CollageTeaserView(BrowserView):
    title = u"Teaser View"

    @property
    def teasers(self):
        return get_teasers(self.context, self.context.data, self.request)
