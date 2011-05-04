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


class StringFieldExtender(ExtensionField, atapi.StringField):
    pass

class ImageExtender(object):
    implements(ISchemaExtender)
    adapts(IATImage)

    fields = [
        StringFieldExtender('teaser_url',
            required=False,
            searchable=False,
            accessor='teaser_url',
            validators=('isURL',),
            widget = atapi.StringWidget(
                        description = _(u'help_teaser_url',
                                        default=u"""Link to content for teaser
                                        . Add http:// for external links."""),
                        label = _(u'label_teaser_url', default=u'Teaser URL')
                        )),

        StringFieldExtender('teaser_style',
            required=False,
            searchable=False,
            accessor='teaser_style',
            widget = atapi.StringWidget(
                        description = _(u'help_teaser_style',
                                        default=u"""ONLY FOR TEASER IMAGES:
                                        CSS styles used for the teaser
                                        text"""),
                        label = _(u'label_teaser_css',
                                  default=u'Teaser CSS style')
                        )),

    ]

    def __init__(self, context): self.context = context
    def getFields(self): return self.fields
