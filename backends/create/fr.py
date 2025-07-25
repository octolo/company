from django.db import transaction

from company import get_company_model

Company = get_company_model()
CompanyFR = get_company_model('CompanyFR')
CompanyAddrFR = get_company_model('CompanyAddressFR')


def create(input_obj, accept_duplicate=False, user=None):  # noqa: FBT002
    """
    Persist the company hit returned by the INSEE API and (optionally)
    its address, then return a lightweight dict for immediate use plus
    the newly-created Company instance.
    """
    with transaction.atomic():
        company = Company(
            denomination=input_obj.get('denomination'),
            since=input_obj.get('since'),
        )
        if user is not None:
            company.user_tmp = user

        # An association gets a different flag
        if input_obj.get('rna'):
            company.is_type = 'ASSOCIATION'

        company.save()

        addr_blob = input_obj.pop('address', None)

        # Drop noisy helper fields coming from the search hit
        for key in (
            'ape_str',
            'legalform_str',
            'slice_str',
            'raw_address',
            'rna_or_siren',
        ):
            input_obj.pop(key, None)

        company_fr_data = dict(input_obj)
        company_fr_data['company'] = company

        if accept_duplicate:
            company_fr = CompanyFR.objects.create(**company_fr_data)
        else:
            company_fr, _ = CompanyFR.objects.get_or_create(**company_fr_data)

        if addr_blob:
            addr_blob['company'] = company
            CompanyAddrFR.objects.get_or_create(**addr_blob)

    payload = {
        'url': company_fr.company.named_id,
        'siret': company_fr.siret,
        'denomination': company_fr.siret,
        'legalform': company_fr.legalform,
        'ape': company_fr.ape,
        'ape_noun': company_fr.ape_noun,
        'since': company_fr.since,
        'category': company_fr.category,
        'slice_effective': company_fr.slice_effective,
        'siege': company_fr.siege,
        'rna': company_fr.rna,
    }
    return payload, company
