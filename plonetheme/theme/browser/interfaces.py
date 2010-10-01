# -*- coding: utf-8 -*-
from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

from plone.portlets.interfaces import IPortletManager



class IPagePortlets(IPortletManager):

    """we need our own portlet manager above the content area.

    """

class IFrontPage(Interface):
    """ This is a marker interface for my frontpage
    """


