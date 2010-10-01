# -*- coding: utf-8 -*-
 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Archetypes import atapi
from Products.CMFCore.utils import getToolByName
import operator

class FrontPageView(BrowserView):
    """Default view of a PSJ document.
    """
    __call__ = ViewPageTemplateFile('templates/frontpage.pt')

    def getLinks(self):
	query = []
	catalog = getToolByName(self.context, 'portal_catalog')
	
	results = catalog(path="/".join(self.context.getPhysicalPath()[:-1])+"/frontpage-stuff")
	for i in results:
	    l = i.getId.split("-")
	    if l[0] == "teaser":
		query.append([i,l[0],l[1]])

	query.sort(key = operator.itemgetter(2))
	endResult = []
	for i in query:
	    endResult.append(i[0])
	
	return endResult
