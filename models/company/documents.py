from django.template import Template, Context
from company.apps import CompanyConfig as conf

class Extend:
    @property
    def default_document_header(self):
        header = open(conf.document_header_tpl, encoding='utf-8')
        return header.read()

    @property
    def default_document_footer(self):
        header = open(conf.document_footer_tpl, encoding='utf-8')
        return header.read()

    @property
    def build_document_header(self):
        return self.document_header or self.default_document_header

    @property
    def build_document_footer(self):
        return self.document_footer or self.default_document_footer

    @property
    def header_html(self):
        return Template(self.build_document_header).render(Context({'company': self}))
    
    @property
    def footer_html(self):
        return Template(self.build_document_footer).render(Context({'company': self}))