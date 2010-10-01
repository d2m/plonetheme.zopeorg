from zope import schema
from zope.component import getMultiAdapter, getUtility
from zope.formlib import form
from zope.interface import implements, Interface

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.app.portlets.utils import assignment_from_key
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.utils import unhashPortletInfo
from plone.portlets.interfaces import IPortletManager, IPortletRenderer
from Products.CMFPlone import utils
from Acquisition import aq_inner
from DateTime.DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets.portlets.rss import Renderer
import time, socket

from DateTime import DateTime

class RSSRenderer(Renderer):
    
    render_full = ViewPageTemplateFile('templates/rss.pt')
    def __init__(self, context, request, view, manager, data):
	self.context = context
	self.request = request 
	self.view = view
	self.manager = manager
	self.data = data
	self.site_properties = getToolByName(context, "portal_properties")


    def cropText(self, text, length, ellipsis='...'):
        """Crop text on a word boundary
        """
        converted = False
        if not isinstance(text, unicode):
            encoding = utils.getSiteEncoding(aq_inner(self.context))
            text = unicode(text, encoding)
            converted = True


	htmlTagOpened = False
	lastChar = "#"
	result = ""
	index = 0
	for i in text:
		index += 1
		if lastChar == "<":
			if i == "/":
				htmlTagOpened -= 1
			else:	
				htmlTagOpened += 1
		result += i
			
		if index >= length and htmlTagOpened == 0:
			if lastChar == "<":
				result += text[index:].split(">")[0]+">" #add the end of the tag. e.g. 'div>'
			else:
				result += "<span>"+ellipsis+"</span>"
			text = result
        		if converted:
        		    # encode back from unicode
        		    text = text.encode(encoding)
        		return text
		lastChar = i

