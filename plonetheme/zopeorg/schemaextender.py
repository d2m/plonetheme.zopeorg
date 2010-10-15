# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.component import adapts
from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

from Products.Archetypes import PloneMessageFactory as _
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from Products.ATContentTypes.interfaces import IATImage


class ImageField(ExtensionField, atapi.StringField):
    pass

class ImageExtender(object):
    implements(ISchemaExtender)
    adapts(IATImage)

    fields = [
        atapi.ImageField('teaser_url',
            required=False,
            searchable=False,
            accessor='teaser_url',
            validators=('isURL',),
            widget = atapi.StringWidget(
                        description = _(u'help_teaser_url',
                                        default=u"Link to content for teaser. Add http:// for external links."),
                        label = _(u'label_teaser_url', default=u'Teaser URL')
                        )),

    ]

    def __init__(self, context): self.context = context
    def getFields(self): return self.fields
