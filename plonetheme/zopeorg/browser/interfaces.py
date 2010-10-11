# -*- coding: utf-8 -*-
from zope.interface import Interface
from plone.portlets.interfaces import IPortletManager

class IZopeorgTheme(Interface):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IPagePortlets(IPortletManager):
    """we need our own portlet manager above the content area.
    """

class IFrontPage(Interface):
    """ This is a marker interface for my frontpage
    """


