from company.backends.search import SearchBackend
from company.choices import fr as choices


class SearchBackendFr(SearchBackend):
    search_types = {
        'siren': r'^[0-9]{9}$',
        'siret': r'^[0-9]{14}$',
        'rna': r'^W|w[0-9]{9}$',
    }
    data_format = [
        'siren',
        'rna',
        'siret',
        'denomination',
        'legalform',
        'ape',
        'ape_noun',
        'since',
        'category',
        'slice_effective',
        'siege',
        {
            'address': [
                'address',
                'complement',
                'locality',
                'postal_code',
                'country',
                'country_code',
                'cedex',
                'cedex_code',
                'special',
                'index',
                'nic',
            ]
        },
    ]

    def get_ape_str(self, code):
        return dict(choices.APE).get(code)

    def get_legalform_str(self, code):
        return dict(choices.LEGALFORM).get(int(code))

    def get_slice_str(self, code):
        return dict(choices.SLICE_EFFECTIVE).get(code)

    def get_value_country(self, obj):
        value = 'france'
        if 'country' in self.fields_association:
            value = self.getattr_recursive(obj, self.fields_association['country'])
        return value.lower() if value else 'france'

    def get_value_country_code(self, obj):
        value = 'fr'
        if 'country_code' in self.fields_association:
            value = self.getattr_recursive(obj, self.fields_association.get('country_code'))
        return value.lower() if value else 'fr'

    def get_value_ape(self, obj):
        return self.getattr_recursive(obj, self.fields_association.get('ape')).replace('.', '')

    def get_entities_json(self, data):
        entities = []
        for entity in data:
            data_entity = self.get_data_json(entity)
            data_entity.update({
                'rna_or_siren': data_entity.get('rna') or data_entity.get('siren'),
                'raw_address': self.raw_address % (data_entity['address']),
                'ape_str': self.get_ape_str(data_entity['ape']),
                'legalform_str': self.get_legalform_str(data_entity['legalform']),
                'slice_str': self.get_slice_str(data_entity['slice_effective']),
            })
            entities.append(data_entity)
        return entities
