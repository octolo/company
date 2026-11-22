import pytest

from company.models.company import company_abbreviation
from octolo.models import Company


def test_company_abbreviation():
    assert company_abbreviation('Société Générale') == 'SG'
    assert company_abbreviation("L'Oréal") == 'L'
    assert company_abbreviation('A BC') == 'B'
    assert company_abbreviation('') == ''


@pytest.mark.django_db
def test_company_abbreviation_is_generated_and_customized():
    generated = Company.objects.create(denomination='Société Générale')
    assert generated.abbreviation == 'SG'

    custom = Company.objects.create(
        denomination='Société Générale',
        abbreviation='socgen',
    )
    assert custom.abbreviation == 'SOCGEN'

    custom.denomination = 'Banque Générale'
    custom.save()
    assert custom.abbreviation == 'SOCGEN'

    custom.abbreviation = ''
    custom.save(update_fields=['abbreviation'])
    assert Company.objects.get(pk=custom.pk).abbreviation == 'BG'
