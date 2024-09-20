from company.apps import CompanyConfig as conf

company = (
    'denomination',
    'since',
    'icb',
    'market',
    'capital_socnomtotal',
    'is_capital_variable',
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
    'resume',
    'stackholder_kind',
    'stock_kind',
)

form =(
    'is_type',
    'stackholder_kind',
    'stock_kind',
)

comex_purpose = ('purpose', 'instance_comex', 'matrix_skills')
market = (
    'capital_socnomtotal',
    'capital_division',
    'current',
    'share_capital',
    'turnover',
    'floating',
    'icb',
    'market',
    'dowjones',
    'nasdaq',
    'gaia'
)

rules = (
    'duration_mandate',
    'settle_internal',
    'age_limit_pdg',
    'age_limit_dg',
    'stock_min_rule',
    'stock_min_status'
)

countryfr = ("siege_fr", "siege_fr_address")

if conf.named_id:
    company += ('named_id',)

country = ('denomination', 'since')
country_params = ('denomination', 'since')

serializer = (
    'uid',
    'named_id',
    'denomination',
    'image_url',
    'capital_socnomtotal',
    'valorisation',
    'nominal',
    'since',
    'site',
    'effective',
    'secretary',
    'resume',
    'infos',
    'marketplace',
    'rules',
    'siege_fr',
    'is_type',
    'is_association',
    'stackholder_kind',
    'get_stackholder_kind_display',
    'stock_kind',
    'get_stock_kind_display',
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
    'phone',
)
balo =  ('announce', 'company', 'case', 'link', 'file_link', 'date')
