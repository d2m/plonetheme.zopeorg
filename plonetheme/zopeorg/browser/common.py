# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/footer.pt')

    def update(self):
        super(FooterViewlet, self).update()
        self.navigation_root_url = self.portal_state.navigation_root_url()