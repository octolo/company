from django.utils.translation import gettext_lazy as _

YESNO = (
("YES", _('yes')),
("NO", _('no')),
)

ICB = (
("MATERIALBASE", _("Matériaux de base")),
("INDUSTRY", _("Industries")),
("SERVICESCONS", _("Services aux consommateurs")),
("GOODCONS", _("Biens de consommation")),
("COMPANYFINANCIAL", _("Sociétés Financières")),
("SERVICESCOLLECT", _("Services aux collectivités")),
("HEALTH", _("Santé")),
("TECHNOLOGIES", _("Technologies")),
("PETROLGAS", _("Pétrole et gaz")),
("TELECOM", _("Télécommunications")),
)

MARKET = (
("SRD", _("SRD")),
("COMPA", _("Compartiment A")),
("COMPB", _("Compartiment B")),
("COMPC", _("Compartiment C")),
("EURONEXT_GROWTH", _("Euronext Growth")),
("EURONEXT_ACCESS", _("Euronext Access")),
("OTHERS", _("Autres titres")),
("EXCEPT", _("Hors titres")),
("COMPASPECIAL", _("Compartiment spécial")),
("DELISTED", _("Valeurs Radiées")),
)