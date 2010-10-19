# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


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
    def get_teasers(self):
        cat = getToolByName(self.context, 'portal_catalog')
        path =  '/'.join(self.context.getPhysicalPath())
        query = {}
        query['portal_type'] = 'Image'
        query['path'] = {'query': path, 'depth':1}
        query['sort_on'] = 'getObjPositionInParent'
        # query['review_state'] = 'published'
        brains = cat(**query)
        return [{'tag':obj.tag(),
                 'title':obj.Title(),
                 'description':obj.Description(),
                 'url': getattr(obj, 'teaser_url', None),
                 'style': getattr(obj, 'teaser_style', None)
                 } for obj in [obj.getObject() for obj in brains]]