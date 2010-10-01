# -*- coding: utf-8 -*-
 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Archetypes import atapi

class PagePortletView(BrowserView):
    """Default view of a PSJ document.
    """
    __call__ = ViewPageTemplateFile('templates/pageportlets.pt')
