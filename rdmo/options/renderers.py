from rdmo.core.renderers import BaseXMLRenderer
from rdmo.core.utils import get_languages


class OptionsRenderer(BaseXMLRenderer):

    def render_optionset(self, xml, optionset):
        xml.startElement('optionset', {'dc:uri': optionset['uri']})
        self.render_text_element(xml, 'uri_prefix', {}, optionset['uri_prefix'])
        self.render_text_element(xml, 'key', {}, optionset['key'])
        self.render_text_element(xml, 'dc:comment', {}, optionset['comment'])
        self.render_text_element(xml, 'order', {}, optionset['order'])
        self.render_text_element(xml, 'provider_key', {}, optionset['provider_key'])
        xml.startElement('conditions', {})
        for condition_uri in optionset['conditions']:
            self.render_text_element(xml, 'condition', {'dc:uri': condition_uri}, None)
        xml.endElement('conditions')
        xml.endElement('optionset')

        if 'options' in optionset and optionset['options']:
            for option in optionset['options']:
                self.render_option(xml, option)

    def render_option(self, xml, option):
        xml.startElement('option', {'dc:uri': option['uri']})
        self.render_text_element(xml, 'uri_prefix', {}, option['uri_prefix'])
        self.render_text_element(xml, 'key', {}, option['key'])
        self.render_text_element(xml, 'path', {}, option['path'])
        self.render_text_element(xml, 'dc:comment', {}, option['comment'])
        self.render_text_element(xml, 'optionset', {'dc:uri': option['optionset']}, None)
        self.render_text_element(xml, 'order', {}, option['order'])

        for lang_code, lang_string, lang_field in get_languages():
            self.render_text_element(xml, 'text', {'lang': lang_code}, option['text_%s' % lang_code])

        self.render_text_element(xml, 'additional_input', {}, option['additional_input'])
        xml.endElement('option')


class OptionSetRenderer(OptionsRenderer):

    def render_document(self, xml, optionsets):
        xml.startElement('rdmo', {
            'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
            'created': self.created
        })
        for optionset in optionsets:
            self.render_optionset(xml, optionset)
        xml.endElement('rdmo')


class OptionRenderer(OptionsRenderer):

    def render_document(self, xml, options):
        xml.startElement('rdmo', {
            'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
            'created': self.created
        })
        for option in options:
            self.render_option(xml, option)
        xml.endElement('rdmo')
