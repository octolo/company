from company import get_company_model

def new_company(input_obj, accept_duplicate=False):
    CompanyModel = get_company_model()
    CompanyCountry = get_company_model("CompanyFR")
    CompanyAddress = get_company_model("CompanyAddressFR")
    address = None
    if 'address' in input_obj:
        address = input_obj['address']
        del input_obj['address']
    del input_obj['ape_str']
    del input_obj['legalform_str']
    del input_obj['slice_str']
    del input_obj['raw_address']
    data = {key: value for key,value in input_obj.items()}
    if accept_duplicate:
        companyC = CompanyCountry(**data)
        companyC.save()
    else:
        companyC, created = CompanyCountry.objects.get_or_create(**data)
    if address:
        address['company'] = companyC.company
        companyA, created = CompanyAddress.objects.get_or_create(**address)
    return {
        "url": companyC.company.named_id,
        "siret": companyC.siret,
        "denomination":  companyC.siret,
        "legalform": companyC.legalform,
        "ape": companyC.ape,
        "ape_noun": companyC.ape_noun,
        "since": companyC.since,
        "category": companyC.category,
        "slice_effective": companyC.slice_effective,
        "siege": companyC.siege,
        "rna": companyC.rna,
    }, companyC.company
