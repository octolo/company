from company.apps import CompanyConfig as conf

company = (
    'denomination',
    'since',
    'icb',
    'market',
    'capital_socnomtotal',
    'capital_division',
    'share_capital',
    'floating',
    'site',
    'current',
    'effective',
    'purpose',
    'secretary',
    'settle_internal',
    'duration_mandate',
    'matrix_skills',
    'instance_comex',
    'age_limit_pdg',
    'age_limit_dg',
    'stock_min_rule',
    'stock_min_status',
    'resume'
)

if conf.named_id:
    company += ('named_id',)

country = ('denomination', 'since')
country_params = ('denomination', 'since')

serializer = (
    'uid',
    'denomination',
    'image_url',
    'capital_socnomtotal',
    'since',
    'site',
    'effective',
    'secretary',
    'resume',
    'infos',
    'marketplace',
    'rules',
    'siege_fr',
)


###
# FR
###
fr = (
    'siret',
    'rna',
    'ape',
    'ape_noun',
    'category',
    'legalform',
    'governance',
    'slice_effective',
    'isin',
    'ticker',
    'coderef',
    'index',
    'siege',
    'evaluation',
)
balo =  ('announce', 'company', 'case', 'link', 'file_link', 'date')