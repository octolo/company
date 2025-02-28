from django.utils.translation import gettext_lazy as _

SLICE_EFFECTIVE = (
    (
        '00',
        _(
            "0 salarié (n'ayant pas d'effectif au 31/12 mais ayant employé des salariés au cours de l'année de référence)"
        ),
    ),
    ('01', _('1 ou 2 salariés')),
    ('02', _('3 à 5 salariés')),
    ('03', _('6 à 9 salariés')),
    ('11', _('10 à 19 salariés')),
    ('12', _('20 à 49 salariés')),
    ('21', _('50 à 99 salariés')),
    ('22', _('100 à 199 salariés')),
    ('31', _('200 à 249 salariés')),
    ('32', _('250 à 499 salariés')),
    ('41', _('500 à 999 salariés')),
    ('42', _('1 000 à 1 999 salariés')),
    ('51', _('2 000 à 4 999 salariés')),
    ('52', _('5 000 à 9 999 salariés')),
    ('53', _('10 000 salariés et plus')),
)

CODEREF = (
    ('AFEPMEDEF', _('Afep MEDEF')),
    ('MIDDLENEXT', _('MiddleNext')),
)

INDEX = (
    ('CAC40', _('CAC40')),
    ('NEXT80', _('NEXT80')),
    ('NEXTPP', _('NEXT++')),
)

GOVERNANCE = (
    ('CAWPDG', _('CA avec PDG')),
    ('CAGOVDISLO', _('CA à gouvernance dissociée')),
    ('CSDIRECTOR', _('Conseil de Surveillance/Directoire')),
    ('COMMANDITE', _('Commandite')),
)

EVALUATION = (
    ('AUTOYEAR', _('Auto-évaluation chaque année')),
    ('AUTO2YEAR', _('Auto-évaluation (1 fois tous les 2 ans)')),
    ('AUTO3YEAR', _('Auto-évaluation (1 fois tous les 3 ans)')),
    ('EXTYEAR', _('Consultant externe chaque année')),
    ('EXT2YEAR', _('Consultant externe tous les 2 ans')),
    ('EXT3YEAR', _('Consultant externe tous les 3 ans')),
    (
        'AUTO2YEAREXT',
        _('Auto-évaluation annuelle et consultant externe tous les 2 ans'),
    ),
    (
        'AUTO3YEAREXT',
        _('Auto-évaluation annuelle et consultant externe tous les 3 ans'),
    ),
    (
        'PRESNOTNECESSARY',
        _(
            'Le Président estime qu’il n’est pas nécessaire de procéder à l’évaluation du fonctionnement du Conseil d’administration.'
        ),
    ),
    (
        '0PROCESSENABLE',
        _(
            'A ce jour, aucune procédure d’auto-évaluation du fonctionnement n’est mise en place par le Conseil.'
        ),
    ),
    (
        '0FORMDO',
        _(
            'Aucune évaluation formalisée du Conseil n’a été réalisée jusqu’à aujourd’hui'
        ),
    ),
)

LEGALFORM = (
    (1000, _('Entrepreneur individue')),
    (2110, _('Indivision entre personnes physiques')),
    (2120, _('Indivision avec personne morale')),
    (2210, _('Société créée de fait entre personnes physiques')),
    (2220, _('Société créée de fait avec personne morale')),
    (2310, _('Société en participation entre personnes physiques')),
    (2320, _('Société en participation avec personne morale')),
    (2385, _('Société en participation de professions libérales')),
    (2400, _('Fiducie')),
    (2700, _('Paroisse hors zone concordataire')),
    (
        2900,
        _('Autre groupement de droit privé non doté de la personnalité morale'),
    ),
    (
        3110,
        _(
            "Représentation ou agence commerciale d'état ou organisme public étranger immatriculé au RCS"
        ),
    ),
    (3120, _('Société commerciale étrangère immatriculée au RC')),
    (3205, _('Organisation internationale')),
    (3210, _('État, collectivité ou établissement public étrange')),
    (3220, _('Société étrangère non immatriculée au RCS')),
    (3290, _('Autre personne morale de droit étranger')),
    (
        4110,
        _(
            "Établissement public national à caractère industriel ou commercial doté d'un comptable public"
        ),
    ),
    (
        4120,
        _(
            "Établissement public national à caractère industriel ou commercial non doté d'un comptable public"
        ),
    ),
    (4130, _('Exploitant public')),
    (
        4140,
        _('Établissement public local à caractère industriel ou commercial'),
    ),
    (
        4150,
        _(
            "Régie d'une collectivité locale à caractère industriel ou commercial"
        ),
    ),
    (4160, _('Institution Banque de France')),
    (5191, _('Société de caution mutuelle')),
    (5192, _('Société coopérative de banque populaire')),
    (5193, _('Caisse de crédit maritime mutuel')),
    (5194, _('Caisse (fédérale) de crédit mutuel')),
    (5195, _('Association coopérative inscrite (droit local Alsace Moselle)')),
    (5196, _("Caisse d'épargne et de prévoyance à forme coopérative")),
    (5202, _('Société en nom collectif')),
    (5203, _('Société en nom collectif coopérative')),
    (5306, _('Société en commandite simple')),
    (5307, _('Société en commandite simple coopérative')),
    (5308, _('Société en commandite par actions')),
    (5309, _('Société en commandite par actions coopérative')),
    (
        5370,
        _(
            'Société de Participations Financières de Profession Libérale Société en commandite par actions (SPFPL SCA'
        ),
    ),
    (5385, _("Société d'exercice libéral en commandite par actions")),
    (5410, _('SARL nationale')),
    (5415, _("SARL d'économie mixte")),
    (5422, _("SARL immobilière pour le commerce et l'industrie (SICOMI)")),
    (5426, _('SARL immobilière de gestio')),
    (5430, _("SARL d'aménagement foncier et d'équipement rural (SAFER")),
    (5431, _("SARL mixte d'intérêt agricole (SMIA)")),
    (5432, _("SARL d'intérêt collectif agricole (SICA)")),
    (5442, _("SARL d'attribution")),
    (5443, _('SARL coopérative de construction')),
    (5451, _('SARL coopérative de consommation')),
    (5453, _('SARL coopérative artisanale')),
    (5454, _("SARL coopérative d'intérêt maritime")),
    (5455, _('SARL coopérative de transpor')),
    (5458, _('SARL coopérative ouvrière de production (SCOP')),
    (5459, _('SARL union de sociétés coopératives')),
    (5460, _('Autre SARL coopérative')),
    (
        5470,
        _(
            'Société de Participations Financières de Profession Libérale Société à responsabilité limitée (SPFPL SARL'
        ),
    ),
    (5485, _("Société d'exercice libéral à responsabilité limitée")),
    (5498, _('SARL unipersonnelle')),
    (5499, _('Société à responsabilité limitée (sans autre indication')),
    (5505, _("SA à participation ouvrière à conseil d'administration")),
    (5510, _("SA nationale à conseil d'administration")),
    (5515, _("SA d'économie mixte à conseil d'administration")),
    (5520, _("Fonds à forme sociétale à conseil d'administratio")),
    (
        5522,
        _(
            "SA immobilière pour le commerce et l'industrie (SICOMI) à conseil d'administratio"
        ),
    ),
    (5525, _("SA immobilière d'investissement à conseil d'administratio")),
    (
        5530,
        _(
            "SA d'aménagement foncier et d'équipement rural (SAFER) à conseil d'administratio"
        ),
    ),
    (
        5531,
        _(
            "Société anonyme mixte d'intérêt agricole (SMIA) à conseil d'administration"
        ),
    ),
    (
        5532,
        _("SA d'intérêt collectif agricole (SICA) à conseil d'administratio"),
    ),
    (5542, _("SA d'attribution à conseil d'administratio")),
    (5543, _("SA coopérative de construction à conseil d'administratio")),
    (5546, _("SA de HLM à conseil d'administration")),
    (5547, _("SA coopérative de production de HLM à conseil d'administration")),
    (5548, _("SA de crédit immobilier à conseil d'administration")),
    (5551, _("SA coopérative de consommation à conseil d'administration")),
    (
        5552,
        _(
            "SA coopérative de commerçants-détaillants à conseil d'administratio"
        ),
    ),
    (5553, _("SA coopérative artisanale à conseil d'administration")),
    (5554, _("SA coopérative (d'intérêt) maritime à conseil d'administration")),
    (5555, _("SA coopérative de transport à conseil d'administratio")),
    (
        5558,
        _(
            "SA coopérative ouvrière de production (SCOP) à conseil d'administratio"
        ),
    ),
    (5559, _("SA union de sociétés coopératives à conseil d'administration")),
    (5560, _("Autre SA coopérative à conseil d'administration")),
    (
        5570,
        _(
            "Société de Participations Financières de Profession Libérale Société anonyme à conseil d'administration (SPFPL SA à conseil d'administration"
        ),
    ),
    (
        5585,
        _(
            "Société d'exercice libéral à forme anonyme à conseil d'administration"
        ),
    ),
    (5599, _("SA à conseil d'administration (s.a.i.")),
    (5605, _('SA à participation ouvrière à directoire')),
    (5610, _('SA nationale à directoire')),
    (5615, _("SA d'économie mixte à directoire")),
    (5620, _('Fonds à forme sociétale à directoire')),
    (
        5622,
        _(
            "SA immobilière pour le commerce et l'industrie (SICOMI) à directoire"
        ),
    ),
    (5625, _("SA immobilière d'investissement à directoire")),
    (5630, _('Safer anonyme à directoire')),
    (5631, _("SA mixte d'intérêt agricole (SMIA")),
    (5632, _("SA d'intérêt collectif agricole (SICA")),
    (5642, _("SA d'attribution à directoire")),
    (5643, _('SA coopérative de construction à directoire')),
    (5646, _('SA de HLM à directoire')),
    (5647, _('Société coopérative de production de HLM anonyme à directoire')),
    (5648, _('SA de crédit immobilier à directoire')),
    (5651, _('SA coopérative de consommation à directoire')),
    (5652, _('SA coopérative de commerçants-détaillants à directoire')),
    (5653, _('SA coopérative artisanale à directoire')),
    (5654, _("SA coopérative d'intérêt maritime à directoire")),
    (5655, _('SA coopérative de transport à directoire')),
    (5658, _('SA coopérative ouvrière de production (SCOP) à directoire')),
    (5659, _('SA union de sociétés coopératives à directoire')),
    (5660, _('Autre SA coopérative à directoire')),
    (
        5670,
        _(
            'Société de Participations Financières de Profession Libérale Société anonyme à Directoire (SPFPL SA à directoire)'
        ),
    ),
    (5685, _("Société d'exercice libéral à forme anonyme à directoire")),
    (5699, _('SA à directoire (s.a.i.')),
    (5710, _('SAS, société par actions simplifiée')),
    (
        5720,
        _(
            'Société par actions simplifiée à associé unique ou société par actions simplifiée unipersonnelle'
        ),
    ),
    (
        5770,
        _(
            'Société de Participations Financières de Profession Libérale Société par actions simplifiée (SPFPL SAS)'
        ),
    ),
    (5785, _("Société d'exercice libéral par action simplifiée")),
    (5800, _('Société européenne')),
    (6100, _("Caisse d'Épargne et de Prévoyance")),
    (6210, _("Groupement européen d'intérêt économique (GEIE)")),
    (6220, _("Groupement d'intérêt économique (GIE)")),
    (
        6316,
        _("Coopérative d'utilisation de matériel agricole en commun (CUMA)"),
    ),
    (6317, _('Société coopérative agricole')),
    (6318, _('Union de sociétés coopératives agricoles')),
    (6411, _("Société d'assurance à forme mutuell")),
    (6511, _('Sociétés Interprofessionnelles de Soins Ambulatoires')),
    (6521, _('Société civile de placement collectif immobilier (SCPI)')),
    (6532, _("Société civile d'intérêt collectif agricole (SICA)")),
    (6533, _("Groupement agricole d'exploitation en commun (GAEC)")),
    (6534, _('Groupement foncier agricole')),
    (6535, _('Groupement agricole foncier')),
    (6536, _('Groupement forestier')),
    (6537, _('Groupement pastoral')),
    (6538, _('Groupement foncier et rura')),
    (6539, _('Société civile foncière')),
    (6540, _('Société civile immobilière')),
    (6541, _('Société civile immobilière de construction-vent')),
    (6542, _("Société civile d'attribution")),
    (6543, _('Société civile coopérative de construction')),
    (
        6544,
        _("Société civile immobilière d' accession progressive à la propriété"),
    ),
    (6551, _('Société civile coopérative de consommation')),
    (6554, _("Société civile coopérative d'intérêt maritime")),
    (6558, _('Société civile coopérative entre médecins')),
    (6560, _('Autre société civile coopérative')),
    (6561, _("SCP d'avocats")),
    (6562, _("SCP d'avocats aux conseils")),
    (6563, _("SCP d'avoués d'appel")),
    (6564, _("SCP d'huissiers")),
    (6565, _('SCP de notaires')),
    (6566, _('SCP de commissaires-priseurs')),
    (6567, _('SCP de greffiers de tribunal de commerce')),
    (6568, _('SCP de conseils juridiques')),
    (6569, _('SCP de commissaires aux comptes')),
    (6571, _('SCP de médecins')),
    (6572, _('SCP de dentistes')),
    (6573, _("SCP d'infirmiers")),
    (6574, _('SCP de masseurs-kinésithérapeute')),
    (6575, _("SCP de directeurs de laboratoire d'analyse médicale")),
    (6576, _('SCP de vétérinaires')),
    (6577, _('SCP de géomètres expert')),
    (6578, _("SCP d'architectes")),
    (6585, _('Autre société civile professionnell')),
    (6588, _('Société civile laitière')),
    (6589, _('Société civile de moyens')),
    (6595, _('Caisse locale de crédit mutuel')),
    (6596, _('Caisse de crédit agricole mutuel')),
    (6597, _("Société civile d'exploitation agricole")),
    (6598, _('Exploitation agricole à responsabilité limitée')),
    (6599, _('Autre société civile')),
    (
        6901,
        _(
            'Autre personne de droit privé inscrite au registre du commerce et des société'
        ),
    ),
    (7111, _('Autorité constitutionnelle')),
    (7112, _('Autorité administrative ou publique indépendant')),
    (7113, _('Ministère')),
    (7120, _("Service central d'un ministère")),
    (7150, _('Service du ministère de la Défense')),
    (
        7160,
        _(
            "Service déconcentré à compétence nationale d'un ministère (hors Défense"
        ),
    ),
    (7171, _("Service déconcentré de l'État à compétence (inter) régionale")),
    (
        7172,
        _("Service déconcentré de l'État à compétence (inter) départementale"),
    ),
    (
        7179,
        _("(Autre) Service déconcentré de l'État à compétence territoriale"),
    ),
    (7190, _('Ecole nationale non dotée de la personnalité morale')),
    (7210, _('Commune et commune nouvelle')),
    (7220, _('Département')),
    (7225, _("Collectivité et territoire d'Outre Me")),
    (7229, _('(Autre) Collectivité territoriale')),
    (7230, _('Région')),
    (7312, _('Commune associée et commune déléguée')),
    (7313, _('Section de commune')),
    (7314, _('Ensemble urbain')),
    (7321, _('Association syndicale autorisée')),
    (7322, _('Association foncière urbaine')),
    (7323, _('Association foncière de remembrement')),
    (7331, _("Établissement public local d'enseignement")),
    (7340, _('Pôle métropolitai')),
    (7341, _('Secteur de commune')),
    (7342, _('District urbain')),
    (7343, _('Communauté urbaine')),
    (7344, _('Métropol')),
    (7345, _('Syndicat intercommunal à vocation multiple (SIVOM)')),
    (7346, _('Communauté de communes')),
    (7347, _('Communauté de villes')),
    (7348, _("Communauté d'agglomération")),
    (
        7349,
        _(
            'Autre établissement public local de coopération non spécialisé ou entente'
        ),
    ),
    (7351, _('Institution interdépartementale ou entent')),
    (7352, _('Institution interrégionale ou entente')),
    (7353, _('Syndicat intercommunal à vocation unique (SIVU)')),
    (7354, _('Syndicat mixte fermé')),
    (7355, _('Syndicat mixte ouver')),
    (
        7356,
        _(
            'Commission syndicale pour la gestion des biens indivis des communes'
        ),
    ),
    (7357, _("Pôle d'équilibre territorial et rural (PETR")),
    (7361, _("Centre communal d'action sociale")),
    (7362, _('Caisse des écoles')),
    (7363, _('Caisse de crédit municipal')),
    (7364, _("Établissement d'hospitalisation")),
    (7365, _('Syndicat inter hospitalier')),
    (7366, _('Établissement public local social et médico-social')),
    (7367, _("Centre Intercommunal d'action sociale (CIAS")),
    (7371, _("Office public d'habitation à loyer modéré (OPHLM)")),
    (7372, _("Service départemental d'incendie et de secours (SDIS")),
    (7373, _('Établissement public local culturel')),
    (7378, _("Régie d'une collectivité locale à caractère administratif")),
    (7379, _('(Autre) Établissement public administratif local')),
    (7381, _('Organisme consulaire')),
    (
        7382,
        _(
            "Établissement public national ayant fonction d'administration centrale"
        ),
    ),
    (
        7383,
        _(
            'Établissement public national à caractère scientifique culturel et professionnel'
        ),
    ),
    (7384, _("Autre établissement public national d'enseignement")),
    (
        7385,
        _(
            'Autre établissement public national administratif à compétence territoriale limitée'
        ),
    ),
    (7389, _('Établissement public national à caractère administratif')),
    (7410, _("Groupement d'intérêt public (GIP)")),
    (7430, _("Établissement public des cultes d'Alsace-Lorraine")),
    (
        7450,
        _(
            'Etablissement public administratif, cercle et foyer dans les armées'
        ),
    ),
    (7470, _('Groupement de coopération sanitaire à gestion publique')),
    (7490, _('Autre personne morale de droit administratif')),
    (8110, _('Régime général de la Sécurité Social')),
    (8120, _('Régime spécial de Sécurité Social')),
    (8130, _('Institution de retraite complémentaire')),
    (8140, _('Mutualité sociale agricole')),
    (8150, _('Régime maladie des non-salariés non agricoles')),
    (
        8160,
        _(
            'Régime vieillesse ne dépendant pas du régime général de la Sécurité Social'
        ),
    ),
    (8170, _("Régime d'assurance chômage")),
    (8190, _('Autre régime de prévoyance sociale')),
    (8210, _('Mutuelle')),
    (8250, _('Assurance mutuelle agricole')),
    (8290, _('Autre organisme mutualiste')),
    (8310, _("Comité central d'entreprise")),
    (8311, _("Comité d'établissement")),
    (8410, _('Syndicat de salariés')),
    (8420, _('Syndicat patronal')),
    (8450, _('Ordre professionnel ou assimilé')),
    (
        8470,
        _(
            'Centre technique industriel ou comité professionnel du développement économique'
        ),
    ),
    (8490, _('Autre organisme professionnel')),
    (8510, _('Institution de prévoyance')),
    (8520, _('Institution de retraite supplémentaire')),
    (9110, _('Syndicat de copropriété')),
    (9150, _('Association syndicale libre')),
    (9210, _('Association non déclarée')),
    (9220, _('Association déclarée')),
    (9221, _("Association déclarée d'insertion par l'économiqu")),
    (9222, _('Association intermédiaire')),
    (9223, _("Groupement d'employeurs")),
    (
        9224,
        _("Association d'avocats à responsabilité professionnelle individuell"),
    ),
    (9230, _("Association déclarée, reconnue d'utilité publiqu")),
    (9240, _('Congrégation')),
    (9260, _('Association de droit local (Bas-Rhin, Haut-Rhin et Moselle')),
    (9300, _('Fondation')),
    (9900, _('Autre personne morale de droit privé')),
    (9970, _('Groupement de coopération sanitaire à gestion privée')),
)

APE = (
    ('01', _('Culture et production animale, chasse et services annexes')),
    ('011', _('Cultures non permanentes')),
    (
        '0111',
        _(
            "Culture de céréales (à l'exception du riz), de légumineuses et de graines oléagineuses"
        ),
    ),
    (
        '0111Z',
        _(
            "Culture de céréales (à l'exception du riz), de légumineuses et de graines oléagineuses"
        ),
    ),
    ('0112', _('Culture du riz')),
    ('0112Z', _('Culture du riz')),
    ('0113', _('Culture de légumes, de melons, de racines et de tubercules')),
    ('0113Z', _('Culture de légumes, de melons, de racines et de tubercules')),
    ('0114', _('Culture de la canne à sucre')),
    ('0114Z', _('Culture de la canne à sucre')),
    ('0115', _('Culture du tabac')),
    ('0115Z', _('Culture du tabac')),
    ('0116', _('Culture de plantes à fibres')),
    ('0116Z', _('Culture de plantes à fibres')),
    ('0119', _('Autres cultures non permanentes')),
    ('0119Z', _('Autres cultures non permanentes')),
    ('012', _('Cultures permanentes')),
    ('0121', _('Culture de la vigne')),
    ('0121Z', _('Culture de la vigne')),
    ('0122', _('Culture de fruits tropicaux et subtropicaux')),
    ('0122Z', _('Culture de fruits tropicaux et subtropicaux')),
    ('0123', _("Culture d'agrumes")),
    ('0123Z', _("Culture d'agrumes")),
    ('0124', _('Culture de fruits à pépins et à noyau')),
    ('0124Z', _('Culture de fruits à pépins et à noyau')),
    (
        '0125',
        _(
            "Culture d'autres fruits d'arbres ou d'arbustes et de fruits à coque"
        ),
    ),
    (
        '0125Z',
        _(
            "Culture d'autres fruits d'arbres ou d'arbustes et de fruits à coque"
        ),
    ),
    ('0126', _('Culture de fruits oléagineux')),
    ('0126Z', _('Culture de fruits oléagineux')),
    ('0127', _('Culture de plantes à boissons')),
    ('0127Z', _('Culture de plantes à boissons')),
    (
        '0128',
        _(
            'Culture de plantes à épices, aromatiques, médicinales et pharmaceutiques'
        ),
    ),
    (
        '0128Z',
        _(
            'Culture de plantes à épices, aromatiques, médicinales et pharmaceutiques'
        ),
    ),
    ('0129', _('Autres cultures permanentes')),
    ('0129Z', _('Autres cultures permanentes')),
    ('013', _('Reproduction de plantes')),
    ('0130', _('Reproduction de plantes')),
    ('0130Z', _('Reproduction de plantes')),
    ('014', _('Production animale')),
    ('0141', _('Élevage de vaches laitières')),
    ('0141Z', _('Élevage de vaches laitières')),
    ('0142', _("Élevage d'autres bovins et de buffles")),
    ('0142Z', _("Élevage d'autres bovins et de buffles")),
    ('0143', _("Élevage de chevaux et d'autres équidés")),
    ('0143Z', _("Élevage de chevaux et d'autres équidés")),
    ('0144', _("Élevage de chameaux et d'autres camélidés")),
    ('0144Z', _("Élevage de chameaux et d'autres camélidés")),
    ('0145', _("Élevage d'ovins et de caprins")),
    ('0145Z', _("Élevage d'ovins et de caprins")),
    ('0146', _('Élevage de porcins')),
    ('0146Z', _('Élevage de porcins')),
    ('0147', _('Élevage de volailles')),
    ('0147Z', _('Élevage de volailles')),
    ('0149', _("Élevage d'autres animaux")),
    ('0149Z', _("Élevage d'autres animaux")),
    ('015', _('Culture et élevage associés')),
    ('0150', _('Culture et élevage associés')),
    ('0150Z', _('Culture et élevage associés')),
    (
        '016',
        _(
            "Activités de soutien à l'agriculture et traitement primaire des récoltes"
        ),
    ),
    ('0161', _('Activités de soutien aux cultures')),
    ('0161Z', _('Activités de soutien aux cultures')),
    ('0162', _('Activités de soutien à la production animale')),
    ('0162Z', _('Activités de soutien à la production animale')),
    ('0163', _('Traitement primaire des récoltes')),
    ('0163Z', _('Traitement primaire des récoltes')),
    ('0164', _('Traitement des semences')),
    ('0164Z', _('Traitement des semences')),
    ('017', _('Chasse, piégeage et services annexes')),
    ('0170', _('Chasse, piégeage et services annexes')),
    ('0170Z', _('Chasse, piégeage et services annexes')),
    ('02', _('Sylviculture et exploitation forestière')),
    ('021', _('Sylviculture et autres activités forestières')),
    ('0210', _('Sylviculture et autres activités forestières')),
    ('0210Z', _('Sylviculture et autres activités forestières')),
    ('022', _('Exploitation forestière')),
    ('0220', _('Exploitation forestière')),
    ('0220Z', _('Exploitation forestière')),
    (
        '023',
        _(
            "Récolte de produits forestiers non ligneux poussant à l'état sauvage"
        ),
    ),
    (
        '0230',
        _(
            "Récolte de produits forestiers non ligneux poussant à l'état sauvage"
        ),
    ),
    (
        '0230Z',
        _(
            "Récolte de produits forestiers non ligneux poussant à l'état sauvage"
        ),
    ),
    ('024', _("Services de soutien à l'exploitation forestière")),
    ('0240', _("Services de soutien à l'exploitation forestière")),
    ('0240Z', _("Services de soutien à l'exploitation forestière")),
    ('03', _('Pêche et aquaculture')),
    ('031', _('Pêche')),
    ('0311', _('Pêche en mer')),
    ('0311Z', _('Pêche en mer')),
    ('0312', _('Pêche en eau douce')),
    ('0312Z', _('Pêche en eau douce')),
    ('032', _('Aquaculture')),
    ('0321', _('Aquaculture en mer')),
    ('0321Z', _('Aquaculture en mer')),
    ('0322', _('Aquaculture en eau douce')),
    ('0322Z', _('Aquaculture en eau douce')),
    ('05', _('Extraction de houille et de lignite')),
    ('051', _('Extraction de houille')),
    ('0510', _('Extraction de houille')),
    ('0510Z', _('Extraction de houille')),
    ('052', _('Extraction de lignite')),
    ('0520', _('Extraction de lignite')),
    ('0520Z', _('Extraction de lignite')),
    ('06', _("Extraction d'hydrocarbures")),
    ('061', _('Extraction de pétrole brut')),
    ('0610', _('Extraction de pétrole brut')),
    ('0610Z', _('Extraction de pétrole brut')),
    ('062', _('Extraction de gaz naturel')),
    ('0620', _('Extraction de gaz naturel')),
    ('0620Z', _('Extraction de gaz naturel')),
    ('07', _('Extraction de minerais métalliques')),
    ('071', _('Extraction de minerais de fer')),
    ('0710', _('Extraction de minerais de fer')),
    ('0710Z', _('Extraction de minerais de fer')),
    ('072', _('Extraction de minerais de métaux non ferreux')),
    ('0721', _("Extraction de minerais d'uranium et de thorium")),
    ('0721Z', _("Extraction de minerais d'uranium et de thorium")),
    ('0729', _("Extraction d'autres minerais de métaux non ferreux")),
    ('0729Z', _("Extraction d'autres minerais de métaux non ferreux")),
    ('08', _('Autres industries extractives')),
    ('081', _("Extraction de pierres, de sables et d'argiles")),
    (
        '0811',
        _(
            "Extraction de pierres ornementales et de construction, de calcaire industriel, de gypse, de craie et d'ardoise"
        ),
    ),
    (
        '0811Z',
        _(
            "Extraction de pierres ornementales et de construction, de calcaire industriel, de gypse, de craie et d'ardoise"
        ),
    ),
    (
        '0812',
        _(
            'Exploitation de gravières et sablières, extraction d’argiles et de kaolin'
        ),
    ),
    (
        '0812Z',
        _(
            'Exploitation de gravières et sablières, extraction d’argiles et de kaolin'
        ),
    ),
    ('089', _('Activités extractives n.c.a.')),
    ('0891', _("Extraction des minéraux chimiques et d'engrais minéraux ")),
    ('0891Z', _("Extraction des minéraux chimiques et d'engrais minéraux ")),
    ('0892', _('Extraction de tourbe')),
    ('0892Z', _('Extraction de tourbe')),
    ('0893', _('Production de sel ')),
    ('0893Z', _('Production de sel ')),
    ('0899', _('Autres activités extractives n.c.a.')),
    ('0899Z', _('Autres activités extractives n.c.a.')),
    ('09', _('Services de soutien aux industries extractives')),
    ('091', _("Activités de soutien à l'extraction d'hydrocarbures")),
    ('0910', _("Activités de soutien à l'extraction d'hydrocarbures")),
    ('0910Z', _("Activités de soutien à l'extraction d'hydrocarbures")),
    ('099', _('Activités de soutien aux autres industries extractives')),
    ('0990', _('Activités de soutien aux autres industries extractives ')),
    ('0990Z', _('Activités de soutien aux autres industries extractives ')),
    ('10', _('Industries alimentaires')),
    (
        '101',
        _(
            'Transformation et conservation de la viande et préparation de produits à base de viande'
        ),
    ),
    ('1011', _('Transformation et conservation de la viande de boucherie')),
    ('1011Z', _('Transformation et conservation de la viande de boucherie')),
    ('1012', _('Transformation et conservation de la viande de volaille')),
    ('1012Z', _('Transformation et conservation de la viande de volaille')),
    ('1013', _('Préparation de produits à base de viande')),
    ('1013A', _('Préparation industrielle de produits à base de viande')),
    ('1013B', _('Charcuterie')),
    (
        '102',
        _(
            'Transformation et conservation de poisson, de crustacés et de mollusques'
        ),
    ),
    (
        '1020',
        _(
            'Transformation et conservation de poisson, de crustacés et de mollusques'
        ),
    ),
    (
        '1020Z',
        _(
            'Transformation et conservation de poisson, de crustacés et de mollusques'
        ),
    ),
    ('103', _('Transformation et conservation de fruits et légumes')),
    ('1031', _('Transformation et conservation de pommes de terre')),
    ('1031Z', _('Transformation et conservation de pommes de terre')),
    ('1032', _('Préparation de jus de fruits et légumes')),
    ('1032Z', _('Préparation de jus de fruits et légumes')),
    ('1039', _('Autre transformation et conservation de fruits et légumes')),
    ('1039A', _('Autre transformation et conservation de légumes')),
    ('1039B', _('Transformation et conservation de fruits')),
    ('104', _('Fabrication d’huiles et graisses végétales et animales')),
    ('1041', _("Fabrication d'huiles et graisses")),
    ('1041A', _("Fabrication d'huiles et graisses brutes")),
    ('1041B', _("Fabrication d'huiles et graisses raffinées")),
    ('1042', _('Fabrication de margarine et graisses comestibles similaires')),
    ('1042Z', _('Fabrication de margarine et graisses comestibles similaires')),
    ('105', _('Fabrication de produits laitiers')),
    ('1051', _('Exploitation de laiteries et fabrication de fromage')),
    ('1051A', _('Fabrication de lait liquide et de produits frais')),
    ('1051B', _('Fabrication de beurre')),
    ('1051C', _('Fabrication de fromage')),
    ('1051D', _("Fabrication d'autres produits laitiers")),
    ('1052', _('Fabrication de glaces et sorbets')),
    ('1052Z', _('Fabrication de glaces et sorbets')),
    ('106', _('Travail des grains ; fabrication de produits amylacés')),
    ('1061', _('Travail des grains')),
    ('1061A', _('Meunerie')),
    ('1061B', _('Autres activités du travail des grains')),
    ('1062', _('Fabrication de produits amylacés')),
    ('1062Z', _('Fabrication de produits amylacés')),
    (
        '107',
        _(
            'Fabrication de produits de boulangerie-pâtisserie et de pâtes alimentaires'
        ),
    ),
    ('1071', _('Fabrication de pain et de pâtisserie fraîche')),
    ('1071A', _('Fabrication industrielle de pain et de pâtisserie fraîche')),
    ('1071B', _('Cuisson de produits de boulangerie')),
    ('1071C', _('Boulangerie et boulangerie-pâtisserie')),
    ('1071D', _('Pâtisserie')),
    (
        '1072',
        _('Fabrication de biscuits, biscottes et pâtisseries de conservation'),
    ),
    (
        '1072Z',
        _('Fabrication de biscuits, biscottes et pâtisseries de conservation'),
    ),
    ('1073', _('Fabrication de pâtes alimentaires')),
    ('1073Z', _('Fabrication de pâtes alimentaires')),
    ('108', _("Fabrication d'autres produits alimentaires")),
    ('1081', _('Fabrication de sucre')),
    ('1081Z', _('Fabrication de sucre')),
    ('1082', _('Fabrication de cacao, chocolat et de produits de confiserie')),
    ('1082Z', _('Fabrication de cacao, chocolat et de produits de confiserie')),
    ('1083', _('Transformation du thé et du café')),
    ('1083Z', _('Transformation du thé et du café')),
    ('1084', _('Fabrication de condiments et assaisonnements')),
    ('1084Z', _('Fabrication de condiments et assaisonnements')),
    ('1085', _('Fabrication de plats préparés')),
    ('1085Z', _('Fabrication de plats préparés')),
    ('1086', _("Fabrication d'aliments homogénéisés et diététiques")),
    ('1086Z', _("Fabrication d'aliments homogénéisés et diététiques")),
    ('1089', _("Fabrication d'autres produits alimentaires n.c.a.")),
    ('1089Z', _("Fabrication d'autres produits alimentaires n.c.a.")),
    ('109', _("Fabrication d'aliments pour animaux")),
    ('1091', _("Fabrication d'aliments pour animaux de ferme")),
    ('1091Z', _("Fabrication d'aliments pour animaux de ferme")),
    ('1092', _("Fabrication d'aliments pour animaux de compagnie")),
    ('1092Z', _("Fabrication d'aliments pour animaux de compagnie")),
    ('11', _('Fabrication de boissons')),
    ('110', _('Fabrication de boissons')),
    ('1101', _('Production de boissons alcooliques distillées')),
    ('1101Z', _('Production de boissons alcooliques distillées')),
    ('1102', _('Production de vin (de raisin)')),
    ('1102A', _('Fabrication de vins effervescents')),
    ('1102B', _('Vinification')),
    ('1103', _('Fabrication de cidre et de vins de fruits  ')),
    ('1103Z', _('Fabrication de cidre et de vins de fruits ')),
    ('1104', _("Production d'autres boissons fermentées non distillées")),
    ('1104Z', _("Production d'autres boissons fermentées non distillées")),
    ('1105', _('Fabrication de bière')),
    ('1105Z', _('Fabrication de bière')),
    ('1106', _('Fabrication de malt')),
    ('1106Z', _('Fabrication de malt')),
    (
        '1107',
        _(
            'Industrie des eaux minérales et autres eaux embouteillées et des boissons rafraîchissantes'
        ),
    ),
    ('1107A', _('Industrie des eaux de table')),
    ('1107B', _('Production de boissons rafraîchissantes')),
    ('12', _('Fabrication de produits à base de tabac')),
    ('120', _('Fabrication de produits à base de tabac')),
    ('1200', _('Fabrication de produits à base de tabac')),
    ('1200Z', _('Fabrication de produits à base de tabac')),
    ('13', _('Fabrication de textiles')),
    ('131', _('Préparation de fibres textiles et filature')),
    ('1310', _('Préparation de fibres textiles et filature')),
    ('1310Z', _('Préparation de fibres textiles et filature')),
    ('132', _('Tissage')),
    ('1320', _('Tissage')),
    ('1320Z', _('Tissage')),
    ('133', _('Ennoblissement textile')),
    ('1330', _('Ennoblissement textile')),
    ('1330Z', _('Ennoblissement textile')),
    ('139', _("Fabrication d'autres textiles")),
    ('1391', _("Fabrication d'étoffes à mailles")),
    ('1391Z', _("Fabrication d'étoffes à mailles")),
    ('1392', _("Fabrication d'articles textiles, sauf habillement")),
    ('1392Z', _("Fabrication d'articles textiles, sauf habillement")),
    ('1393', _('Fabrication de tapis et moquettes')),
    ('1393Z', _('Fabrication de tapis et moquettes')),
    ('1394', _('Fabrication de ficelles, cordes et filets')),
    ('1394Z', _('Fabrication de ficelles, cordes et filets')),
    ('1395', _('Fabrication de non-tissés, sauf habillement')),
    ('1395Z', _('Fabrication de non-tissés, sauf habillement')),
    ('1396', _("Fabrication d'autres textiles techniques et industriels")),
    ('1396Z', _("Fabrication d'autres textiles techniques et industriels")),
    ('1399', _("Fabrication d'autres textiles n.c.a.")),
    ('1399Z', _("Fabrication d'autres textiles n.c.a.")),
    ('14', _("Industrie de l'habillement")),
    ('141', _("Fabrication de vêtements, autres qu'en fourrure")),
    ('1411', _('Fabrication de vêtements en cuir')),
    ('1411Z', _('Fabrication de vêtements en cuir')),
    ('1412', _('Fabrication de vêtements de travail')),
    ('1412Z', _('Fabrication de vêtements de travail')),
    ('1413', _('Fabrication de vêtements de dessus')),
    ('1413Z', _('Fabrication de vêtements de dessus')),
    ('1414', _('Fabrication de vêtements de dessous')),
    ('1414Z', _('Fabrication de vêtements de dessous')),
    ('1419', _("Fabrication d'autres vêtements et accessoires")),
    ('1419Z', _("Fabrication d'autres vêtements et accessoires")),
    ('142', _("Fabrication d'articles en fourrure")),
    ('1420', _("Fabrication d'articles en fourrure")),
    ('1420Z', _("Fabrication d'articles en fourrure")),
    ('143', _("Fabrication d'articles à mailles")),
    ('1431', _("Fabrication d'articles chaussants à mailles")),
    ('1431Z', _("Fabrication d'articles chaussants à mailles")),
    ('1439', _("Fabrication d'autres articles à mailles")),
    ('1439Z', _("Fabrication d'autres articles à mailles")),
    ('15', _('Industrie du cuir et de la chaussure')),
    (
        '151',
        _(
            "Apprêt et tannage des cuirs ; préparation et teinture des fourrures ; fabrication d'articles de voyage, de maroquinerie et de sellerie"
        ),
    ),
    (
        '1511',
        _(
            'Apprêt et tannage des cuirs ; préparation et teinture des fourrures'
        ),
    ),
    (
        '1511Z',
        _(
            'Apprêt et tannage des cuirs ; préparation et teinture des fourrures'
        ),
    ),
    (
        '1512',
        _("Fabrication d'articles de voyage, de maroquinerie et de sellerie"),
    ),
    (
        '1512Z',
        _("Fabrication d'articles de voyage, de maroquinerie et de sellerie"),
    ),
    ('152', _('Fabrication de chaussures')),
    ('1520', _('Fabrication de chaussures')),
    ('1520Z', _('Fabrication de chaussures')),
    (
        '16',
        _(
            "Travail du bois et fabrication d'articles en bois et en liège, à l’exception des meubles ; fabrication d’articles en vannerie et sparterie"
        ),
    ),
    ('161', _('Sciage et rabotage du bois')),
    ('1610', _('Sciage et rabotage du bois')),
    ('1610A', _('Sciage et rabotage du bois, hors imprégnation')),
    ('1610B', _('Imprégnation du bois')),
    ('162', _("Fabrication d'articles en bois, liège, vannerie et sparterie")),
    ('1621', _('Fabrication de placage et de panneaux de bois')),
    ('1621Z', _('Fabrication de placage et de panneaux de bois')),
    ('1622', _('Fabrication de parquets assemblés')),
    ('1622Z', _('Fabrication de parquets assemblés')),
    ('1623', _("Fabrication de charpentes et d'autres menuiseries")),
    ('1623Z', _("Fabrication de charpentes et d'autres menuiseries")),
    ('1624', _("Fabrication d'emballages en bois")),
    ('1624Z', _("Fabrication d'emballages en bois")),
    (
        '1629',
        _(
            "Fabrication d'objets divers en bois ; fabrication d'objets en liège, vannerie et sparterie"
        ),
    ),
    (
        '1629Z',
        _(
            "Fabrication d'objets divers en bois ; fabrication d'objets en liège, vannerie et sparterie"
        ),
    ),
    ('17', _('Industrie du papier et du carton')),
    ('171', _('Fabrication de pâte à papier, de papier et de carton')),
    ('1711', _('Fabrication de pâte à papier')),
    ('1711Z', _('Fabrication de pâte à papier')),
    ('1712', _('Fabrication de papier et de carton')),
    ('1712Z', _('Fabrication de papier et de carton')),
    ('172', _("Fabrication d'articles en papier ou en carton")),
    (
        '1721',
        _(
            "Fabrication de papier et carton ondulés et d'emballages en papier ou en carton"
        ),
    ),
    ('1721A', _('Fabrication de carton ondulé')),
    ('1721B', _('Fabrication de cartonnages ')),
    ('1721C', _("Fabrication d'emballages en papier")),
    (
        '1722',
        _("Fabrication d'articles en papier à usage sanitaire ou domestique"),
    ),
    (
        '1722Z',
        _("Fabrication d'articles en papier à usage sanitaire ou domestique"),
    ),
    ('1723', _("Fabrication d'articles de papeterie")),
    ('1723Z', _("Fabrication d'articles de papeterie")),
    ('1724', _('Fabrication de papiers peints')),
    ('1724Z', _('Fabrication de papiers peints')),
    ('1729', _("Fabrication d'autres articles en papier ou en carton")),
    ('1729Z', _("Fabrication d'autres articles en papier ou en carton")),
    ('18', _("Imprimerie et reproduction d'enregistrements")),
    ('181', _('Imprimerie et services annexes')),
    ('1811', _('Imprimerie de journaux')),
    ('1811Z', _('Imprimerie de journaux')),
    ('1812', _('Autre imprimerie (labeur)')),
    ('1812Z', _('Autre imprimerie (labeur)')),
    ('1813', _('Activités de pré-presse ')),
    ('1813Z', _('Activités de pré-presse ')),
    ('1814', _('Reliure et activités connexes')),
    ('1814Z', _('Reliure et activités connexes')),
    ('182', _("Reproduction d'enregistrements")),
    ('1820', _("Reproduction d'enregistrements")),
    ('1820Z', _("Reproduction d'enregistrements")),
    ('19', _('Cokéfaction et raffinage')),
    ('191', _('Cokéfaction')),
    ('1910', _('Cokéfaction')),
    ('1910Z', _('Cokéfaction')),
    ('192', _('Raffinage du pétrole')),
    ('1920', _('Raffinage du pétrole')),
    ('1920Z', _('Raffinage du pétrole')),
    ('20', _('Industrie chimique')),
    (
        '201',
        _(
            "Fabrication de produits chimiques de base, de produits azotés et d'engrais, de matières plastiques de base et de caoutchouc synthétique"
        ),
    ),
    ('2011', _('Fabrication de gaz industriels')),
    ('2011Z', _('Fabrication de gaz industriels')),
    ('2012', _('Fabrication de colorants et de pigments')),
    ('2012Z', _('Fabrication de colorants et de pigments')),
    ('2013', _("Fabrication d'autres produits chimiques inorganiques de base")),
    ('2013A', _('Enrichissement et  retraitement de matières nucléaires')),
    (
        '2013B',
        _(
            "Fabrication d'autres produits chimiques inorganiques de base n.c.a."
        ),
    ),
    ('2014', _("Fabrication d'autres produits chimiques organiques de base")),
    ('2014Z', _("Fabrication d'autres produits chimiques organiques de base")),
    ('2015', _("Fabrication de produits azotés et d'engrais")),
    ('2015Z', _("Fabrication de produits azotés et d'engrais")),
    ('2016', _('Fabrication de matières plastiques de base')),
    ('2016Z', _('Fabrication de matières plastiques de base')),
    ('2017', _('Fabrication de caoutchouc synthétique')),
    ('2017Z', _('Fabrication de caoutchouc synthétique')),
    ('202', _('Fabrication de pesticides et d’autres produits agrochimiques ')),
    ('2020', _('Fabrication de pesticides et d’autres produits agrochimiques')),
    (
        '2020Z',
        _('Fabrication de pesticides et d’autres produits agrochimiques'),
    ),
    ('203', _('Fabrication de peintures, vernis, encres et mastics')),
    ('2030', _('Fabrication de peintures, vernis, encres et mastics')),
    ('2030Z', _('Fabrication de peintures, vernis, encres et mastics')),
    ('204', _("Fabrication de savons, de produits d'entretien et de parfums")),
    ('2041', _("Fabrication de savons, détergents et produits d'entretien")),
    ('2041Z', _("Fabrication de savons, détergents et produits d'entretien")),
    ('2042', _('Fabrication de parfums et de produits pour la toilette')),
    ('2042Z', _('Fabrication de parfums et de produits pour la toilette')),
    ('205', _("Fabrication d'autres produits chimiques")),
    ('2051', _('Fabrication de produits explosifs')),
    ('2051Z', _('Fabrication de produits explosifs')),
    ('2052', _('Fabrication de colles')),
    ('2052Z', _('Fabrication de colles')),
    ('2053', _("Fabrication d'huiles essentielles")),
    ('2053Z', _("Fabrication d'huiles essentielles")),
    ('2059', _("Fabrication d'autres produits chimiques n.c.a.")),
    ('2059Z', _("Fabrication d'autres produits chimiques n.c.a.")),
    ('206', _('Fabrication de fibres artificielles ou synthétiques')),
    ('2060', _('Fabrication de fibres artificielles ou synthétiques')),
    ('2060Z', _('Fabrication de fibres artificielles ou synthétiques')),
    ('21', _('Industrie pharmaceutique')),
    ('211', _('Fabrication de produits pharmaceutiques de base')),
    ('2110', _('Fabrication de produits pharmaceutiques de base')),
    ('2110Z', _('Fabrication de produits pharmaceutiques de base')),
    ('212', _('Fabrication de préparations pharmaceutiques')),
    ('2120', _('Fabrication de préparations pharmaceutiques')),
    ('2120Z', _('Fabrication de préparations pharmaceutiques')),
    ('22', _('Fabrication de produits en caoutchouc et en plastique')),
    ('221', _('Fabrication de produits en caoutchouc')),
    ('2211', _('Fabrication et rechapage de pneumatiques')),
    ('2211Z', _('Fabrication et rechapage de pneumatiques')),
    ('2219', _("Fabrication d'autres articles en caoutchouc")),
    ('2219Z', _("Fabrication d'autres articles en caoutchouc")),
    ('222', _('Fabrication  de produits en plastique')),
    (
        '2221',
        _(
            'Fabrication de plaques, feuilles, tubes et profilés en matières plastiques'
        ),
    ),
    (
        '2221Z',
        _(
            'Fabrication de plaques, feuilles, tubes et profilés en matières plastiques'
        ),
    ),
    ('2222', _("Fabrication d'emballages en matières plastiques")),
    ('2222Z', _("Fabrication d'emballages en matières plastiques")),
    (
        '2223',
        _("Fabrication d'éléments en matières plastiques pour la construction"),
    ),
    (
        '2223Z',
        _("Fabrication d'éléments en matières plastiques pour la construction"),
    ),
    ('2229', _("Fabrication d'autres articles en matières plastiques")),
    (
        '2229A',
        _('Fabrication de pièces techniques à base de matières plastiques'),
    ),
    (
        '2229B',
        _(
            'Fabrication de produits de consommation courante en matières plastiques'
        ),
    ),
    ('23', _("Fabrication d'autres produits minéraux non métalliques")),
    ('231', _("Fabrication de verre et d'articles en verre")),
    ('2311', _('Fabrication de verre plat')),
    ('2311Z', _('Fabrication de verre plat')),
    ('2312', _('Façonnage et transformation du verre plat')),
    ('2312Z', _('Façonnage et transformation du verre plat')),
    ('2313', _('Fabrication de verre creux')),
    ('2313Z', _('Fabrication de verre creux')),
    ('2314', _('Fabrication de fibres de verre')),
    ('2314Z', _('Fabrication de fibres de verre')),
    (
        '2319',
        _(
            "Fabrication et façonnage d'autres articles en verre, y compris verre technique"
        ),
    ),
    (
        '2319Z',
        _(
            "Fabrication et façonnage d'autres articles en verre, y compris verre technique"
        ),
    ),
    ('232', _('Fabrication de produits réfractaires')),
    ('2320', _('Fabrication de produits réfractaires')),
    ('2320Z', _('Fabrication de produits réfractaires')),
    ('233', _('Fabrication de matériaux de construction en terre cuite')),
    ('2331', _('Fabrication de carreaux en céramique')),
    ('2331Z', _('Fabrication de carreaux en céramique')),
    (
        '2332',
        _(
            'Fabrication de briques, tuiles et produits de construction, en terre cuite'
        ),
    ),
    (
        '2332Z',
        _(
            'Fabrication de briques, tuiles et produits de construction, en terre cuite'
        ),
    ),
    ('234', _("Fabrication d'autres produits en céramique et en porcelaine ")),
    (
        '2341',
        _("Fabrication d'articles céramiques à usage domestique ou ornemental"),
    ),
    (
        '2341Z',
        _("Fabrication d'articles céramiques à usage domestique ou ornemental"),
    ),
    ('2342', _("Fabrication d'appareils sanitaires en céramique")),
    ('2342Z', _("Fabrication d'appareils sanitaires en céramique")),
    ('2343', _("Fabrication d'isolateurs et pièces isolantes en céramique")),
    ('2343Z', _("Fabrication d'isolateurs et pièces isolantes en céramique")),
    ('2344', _("Fabrication d'autres produits céramiques à usage technique")),
    ('2344Z', _("Fabrication d'autres produits céramiques à usage technique")),
    ('2349', _("Fabrication d'autres produits céramiques ")),
    ('2349Z', _("Fabrication d'autres produits céramiques")),
    ('235', _('Fabrication de ciment, chaux et plâtre')),
    ('2351', _('Fabrication de ciment')),
    ('2351Z', _('Fabrication de ciment')),
    ('2352', _('Fabrication de chaux et plâtre')),
    ('2352Z', _('Fabrication de chaux et plâtre')),
    ('236', _("Fabrication d'ouvrages en béton, en ciment ou en plâtre")),
    ('2361', _("Fabrication d'éléments en béton pour la construction")),
    ('2361Z', _("Fabrication d'éléments en béton pour la construction")),
    ('2362', _("Fabrication d'éléments en plâtre pour la construction")),
    ('2362Z', _("Fabrication d'éléments en plâtre pour la construction")),
    ('2363', _("Fabrication de béton prêt à l'emploi")),
    ('2363Z', _("Fabrication de béton prêt à l'emploi")),
    ('2364', _('Fabrication de mortiers et bétons secs')),
    ('2364Z', _('Fabrication de mortiers et bétons secs')),
    ('2365', _("Fabrication d'ouvrages en fibre-ciment")),
    ('2365Z', _("Fabrication d'ouvrages en fibre-ciment")),
    (
        '2369',
        _("Fabrication d'autres ouvrages en béton, en ciment ou en plâtre"),
    ),
    (
        '2369Z',
        _("Fabrication d'autres ouvrages en béton, en ciment ou en plâtre"),
    ),
    ('237', _('Taille, façonnage et finissage de pierres ')),
    ('2370', _('Taille, façonnage et finissage de pierres')),
    ('2370Z', _('Taille, façonnage et finissage de pierres')),
    (
        '239',
        _(
            'Fabrication de produits abrasifs et de produits minéraux non métalliques n.c.a.'
        ),
    ),
    ('2391', _('Fabrication de produits abrasifs')),
    ('2391Z', _('Fabrication de produits abrasifs')),
    (
        '2399',
        _("Fabrication d'autres produits minéraux non métalliques n.c.a."),
    ),
    (
        '2399Z',
        _("Fabrication d'autres produits minéraux non métalliques n.c.a."),
    ),
    ('24', _('Métallurgie')),
    ('241', _('Sidérurgie')),
    ('2410', _('Sidérurgie')),
    ('2410Z', _('Sidérurgie')),
    (
        '242',
        _(
            'Fabrication de tubes, tuyaux, profilés creux et accessoires correspondants en acier '
        ),
    ),
    (
        '2420',
        _(
            'Fabrication de tubes, tuyaux, profilés creux et accessoires correspondants en acier '
        ),
    ),
    (
        '2420Z',
        _(
            'Fabrication de tubes, tuyaux, profilés creux et accessoires correspondants en acier '
        ),
    ),
    (
        '243',
        _(
            "Fabrication d'autres produits de première transformation de l'acier"
        ),
    ),
    ('2431', _('Étirage à froid de barres')),
    ('2431Z', _('Étirage à froid de barres')),
    ('2432', _('Laminage à froid de feuillards')),
    ('2432Z', _('Laminage à froid de feuillards')),
    ('2433', _('Profilage à froid par formage ou pliage')),
    ('2433Z', _('Profilage à froid par formage ou pliage')),
    ('2434', _('Tréfilage à froid')),
    ('2434Z', _('Tréfilage à froid')),
    ('244', _("Production de métaux précieux et d'autres métaux non ferreux")),
    ('2441', _('Production de métaux précieux')),
    ('2441Z', _('Production de métaux précieux')),
    ('2442', _("Métallurgie de l'aluminium")),
    ('2442Z', _("Métallurgie de l'aluminium")),
    ('2443', _("Métallurgie du plomb, du zinc ou de l'étain")),
    ('2443Z', _("Métallurgie du plomb, du zinc ou de l'étain")),
    ('2444', _('Métallurgie du cuivre')),
    ('2444Z', _('Métallurgie du cuivre')),
    ('2445', _('Métallurgie des autres métaux non ferreux')),
    ('2445Z', _('Métallurgie des autres métaux non ferreux')),
    ('2446', _('Élaboration et transformation de matières nucléaires')),
    ('2446Z', _('Élaboration et transformation de matières nucléaires')),
    ('245', _('Fonderie')),
    ('2451', _('Fonderie de fonte')),
    ('2451Z', _('Fonderie de fonte')),
    ('2452', _("Fonderie d'acier")),
    ('2452Z', _("Fonderie d'acier")),
    ('2453', _('Fonderie de métaux légers')),
    ('2453Z', _('Fonderie de métaux légers')),
    ('2454', _("Fonderie d'autres métaux non ferreux")),
    ('2454Z', _("Fonderie d'autres métaux non ferreux")),
    (
        '25',
        _(
            'Fabrication de produits métalliques, à l’exception des machines et des équipements'
        ),
    ),
    ('251', _("Fabrication d'éléments en métal pour la construction")),
    (
        '2511',
        _('Fabrication de structures métalliques et de parties de structures'),
    ),
    (
        '2511Z',
        _('Fabrication de structures métalliques et de parties de structures'),
    ),
    ('2512', _('Fabrication de portes et fenêtres en métal')),
    ('2512Z', _('Fabrication de portes et fenêtres en métal')),
    ('252', _('Fabrication de réservoirs, citernes et conteneurs métalliques')),
    (
        '2521',
        _(
            'Fabrication de radiateurs et de chaudières pour le chauffage central'
        ),
    ),
    (
        '2521Z',
        _(
            'Fabrication de radiateurs et de chaudières pour le chauffage central'
        ),
    ),
    (
        '2529',
        _(
            "Fabrication d'autres réservoirs, citernes et conteneurs métalliques"
        ),
    ),
    (
        '2529Z',
        _(
            "Fabrication d'autres réservoirs, citernes et conteneurs métalliques"
        ),
    ),
    (
        '253',
        _(
            "Fabrication de générateurs de vapeur, à l'exception des chaudières pour le chauffage central"
        ),
    ),
    (
        '2530',
        _(
            "Fabrication de générateurs de vapeur, à l'exception des chaudières pour le chauffage central"
        ),
    ),
    (
        '2530Z',
        _(
            "Fabrication de générateurs de vapeur, à l'exception des chaudières pour le chauffage central"
        ),
    ),
    ('254', _("Fabrication d'armes et de munitions")),
    ('2540', _("Fabrication d'armes et de munitions")),
    ('2540Z', _("Fabrication d'armes et de munitions")),
    ('255', _('Forge, emboutissage, estampage ; métallurgie des poudres')),
    ('2550', _('Forge, emboutissage, estampage ; métallurgie des poudres')),
    ('2550A', _('Forge, estampage, matriçage ; métallurgie des poudres')),
    ('2550B', _('Découpage, emboutissage')),
    ('256', _('Traitement et revêtement des métaux ; usinage')),
    ('2561', _('Traitement et revêtement des métaux')),
    ('2561Z', _('Traitement et revêtement des métaux')),
    ('2562', _('Usinage')),
    ('2562A', _('Décolletage')),
    ('2562B', _('Mécanique industrielle')),
    ('257', _("Fabrication de coutellerie, d'outillage et de quincaillerie")),
    ('2571', _('Fabrication de coutellerie')),
    ('2571Z', _('Fabrication de coutellerie')),
    ('2572', _('Fabrication de serrures et de ferrures')),
    ('2572Z', _('Fabrication de serrures et de ferrures')),
    ('2573', _("Fabrication d'outillage")),
    ('2573A', _('Fabrication de moules et modèles')),
    ('2573B', _("Fabrication d'autres outillages")),
    ('259', _("Fabrication d'autres ouvrages en métaux")),
    ('2591', _('Fabrication de fûts et emballages métalliques similaires')),
    ('2591Z', _('Fabrication de fûts et emballages métalliques similaires')),
    ('2592', _("Fabrication d'emballages métalliques légers")),
    ('2592Z', _("Fabrication d'emballages métalliques légers")),
    (
        '2593',
        _(
            "Fabrication d'articles en fils métalliques, de chaînes et de ressorts"
        ),
    ),
    (
        '2593Z',
        _(
            "Fabrication d'articles en fils métalliques, de chaînes et de ressorts"
        ),
    ),
    ('2594', _('Fabrication de vis et de boulons')),
    ('2594Z', _('Fabrication de vis et de boulons')),
    ('2599', _("Fabrication d'autres produits métalliques n.c.a.")),
    ('2599A', _("Fabrication d'articles métalliques ménagers")),
    ('2599B', _("Fabrication d'autres articles métalliques")),
    (
        '26',
        _('Fabrication de produits informatiques, électroniques et optiques'),
    ),
    ('261', _('Fabrication de composants et cartes électroniques')),
    ('2611', _('Fabrication de composants électroniques')),
    ('2611Z', _('Fabrication de composants électroniques')),
    ('2612', _('Fabrication de cartes électroniques assemblées')),
    ('2612Z', _('Fabrication de cartes électroniques assemblées')),
    ('262', _("Fabrication d'ordinateurs et d'équipements périphériques")),
    ('2620', _("Fabrication d'ordinateurs et d'équipements périphériques")),
    ('2620Z', _("Fabrication d'ordinateurs et d'équipements périphériques")),
    ('263', _("Fabrication d'équipements de communication")),
    ('2630', _("Fabrication d'équipements de communication ")),
    ('2630Z', _("Fabrication d'équipements de communication ")),
    ('264', _('Fabrication de produits électroniques grand public')),
    ('2640', _('Fabrication de produits électroniques grand public')),
    ('2640Z', _('Fabrication de produits électroniques grand public')),
    (
        '265',
        _(
            "Fabrication d'instruments et d'appareils de mesure, d'essai et de navigation ; horlogerie"
        ),
    ),
    (
        '2651',
        _(
            "Fabrication d'instruments et d'appareils de mesure, d'essai et de navigation"
        ),
    ),
    ('2651A', _("Fabrication d'équipements d'aide à la navigation")),
    ('2651B', _("Fabrication d'instrumentation scientifique et technique")),
    ('2652', _('Horlogerie')),
    ('2652Z', _('Horlogerie')),
    (
        '266',
        _(
            "Fabrication d'équipements d'irradiation médicale, d'équipements électromédicaux et électrothérapeutiques"
        ),
    ),
    (
        '2660',
        _(
            "Fabrication d'équipements d'irradiation médicale, d'équipements électromédicaux et électrothérapeutiques "
        ),
    ),
    (
        '2660Z',
        _(
            "Fabrication d'équipements d'irradiation médicale, d'équipements électromédicaux et électrothérapeutiques "
        ),
    ),
    ('267', _('Fabrication de matériels optique et photographique')),
    ('2670', _('Fabrication de matériels optique et photographique')),
    ('2670Z', _('Fabrication de matériels optique et photographique')),
    ('268', _('Fabrication de supports magnétiques et optiques')),
    ('2680', _('Fabrication de supports magnétiques et optiques')),
    ('2680Z', _('Fabrication de supports magnétiques et optiques')),
    ('27', _("Fabrication d'équipements électriques")),
    (
        '271',
        _(
            'Fabrication de moteurs, génératrices et transformateurs électriques et de matériel de distribution et de commande électrique'
        ),
    ),
    (
        '2711',
        _(
            'Fabrication de moteurs, génératrices et transformateurs électriques'
        ),
    ),
    (
        '2711Z',
        _(
            'Fabrication de moteurs, génératrices et transformateurs électriques'
        ),
    ),
    (
        '2712',
        _('Fabrication de matériel de distribution et de commande électrique'),
    ),
    (
        '2712Z',
        _('Fabrication de matériel de distribution et de commande électrique'),
    ),
    ('272', _("Fabrication de piles et d'accumulateurs électriques")),
    ('2720', _("Fabrication de piles et d'accumulateurs électriques")),
    ('2720Z', _("Fabrication de piles et d'accumulateurs électriques")),
    (
        '273',
        _(
            "Fabrication de fils et câbles et de matériel d'installation électrique"
        ),
    ),
    ('2731', _('Fabrication de câbles de fibres optiques')),
    ('2731Z', _('Fabrication de câbles de fibres optiques')),
    (
        '2732',
        _("Fabrication d'autres fils et câbles électroniques ou électriques"),
    ),
    (
        '2732Z',
        _("Fabrication d'autres fils et câbles électroniques ou électriques"),
    ),
    ('2733', _("Fabrication de matériel d'installation électrique")),
    ('2733Z', _("Fabrication de matériel d'installation électrique")),
    ('274', _("Fabrication d'appareils d'éclairage électrique")),
    ('2740', _("Fabrication d'appareils d'éclairage électrique")),
    ('2740Z', _("Fabrication d'appareils d'éclairage électrique")),
    ('275', _("Fabrication d'appareils ménagers")),
    ('2751', _("Fabrication d'appareils électroménagers")),
    ('2751Z', _("Fabrication d'appareils électroménagers")),
    ('2752', _("Fabrication d'appareils ménagers non électriques")),
    ('2752Z', _("Fabrication d'appareils ménagers non électriques")),
    ('279', _("Fabrication d'autres matériels électriques")),
    ('2790', _("Fabrication d'autres matériels électriques")),
    ('2790Z', _("Fabrication d'autres matériels électriques")),
    ('28', _('Fabrication de machines et équipements n.c.a.')),
    ('281', _("Fabrication de machines d'usage général")),
    (
        '2811',
        _(
            "Fabrication de moteurs et turbines, à l'exception des moteurs d’avions et de véhicules"
        ),
    ),
    (
        '2811Z',
        _(
            "Fabrication de moteurs et turbines, à l'exception des moteurs d’avions et de véhicules"
        ),
    ),
    ('2812', _("Fabrication d'équipements hydrauliques et pneumatiques")),
    ('2812Z', _("Fabrication d'équipements hydrauliques et pneumatiques")),
    ('2813', _("Fabrication d'autres pompes et compresseurs")),
    ('2813Z', _("Fabrication d'autres pompes et compresseurs")),
    ('2814', _("Fabrication d'autres articles de robinetterie")),
    ('2814Z', _("Fabrication d'autres articles de robinetterie")),
    (
        '2815',
        _("Fabrication d'engrenages et d'organes mécaniques de transmission"),
    ),
    (
        '2815Z',
        _("Fabrication d'engrenages et d'organes mécaniques de transmission"),
    ),
    ('282', _("Fabrication d'autres machines d'usage général")),
    ('2821', _('Fabrication de fours et brûleurs')),
    ('2821Z', _('Fabrication de fours et brûleurs')),
    ('2822', _('Fabrication de matériel de levage et de manutention')),
    ('2822Z', _('Fabrication de matériel de levage et de manutention')),
    (
        '2823',
        _(
            "Fabrication de machines et d'équipements de bureau (à l'exception des ordinateurs et équipements périphériques)"
        ),
    ),
    (
        '2823Z',
        _(
            "Fabrication de machines et d'équipements de bureau (à l'exception des ordinateurs et équipements périphériques)"
        ),
    ),
    ('2824', _("Fabrication d'outillage portatif à moteur incorporé")),
    ('2824Z', _("Fabrication d'outillage portatif à moteur incorporé")),
    (
        '2825',
        _("Fabrication d'équipements aérauliques et frigorifiques industriels"),
    ),
    (
        '2825Z',
        _("Fabrication d'équipements aérauliques et frigorifiques industriels"),
    ),
    ('2829', _("Fabrication de machines diverses d'usage général")),
    (
        '2829A',
        _(
            "Fabrication d'équipements d'emballage, de conditionnement et de pesage "
        ),
    ),
    ('2829B', _("Fabrication d'autres machines d'usage général")),
    ('283', _('Fabrication de machines agricoles et forestières')),
    ('2830', _('Fabrication de machines agricoles et forestières')),
    ('2830Z', _('Fabrication de machines agricoles et forestières')),
    (
        '284',
        _(
            'Fabrication de machines de formage des métaux et de machines-outils'
        ),
    ),
    ('2841', _('Fabrication de machines de formage des métaux')),
    ('2841Z', _('Fabrication de machines-outils pour le travail des métaux')),
    ('2849', _("Fabrication d'autres machines-outils ")),
    ('2849Z', _("Fabrication d'autres machines-outils ")),
    ('289', _("Fabrication d'autres machines d'usage spécifique")),
    ('2891', _('Fabrication de machines pour la métallurgie')),
    ('2891Z', _('Fabrication de machines pour la métallurgie')),
    ('2892', _("Fabrication de machines pour l'extraction ou la construction")),
    (
        '2892Z',
        _("Fabrication de machines pour l'extraction ou la construction"),
    ),
    ('2893', _("Fabrication de machines pour l'industrie agro-alimentaire")),
    ('2893Z', _("Fabrication de machines pour l'industrie agro-alimentaire")),
    ('2894', _('Fabrication de machines pour les industries textiles')),
    ('2894Z', _('Fabrication de machines pour les industries textiles')),
    (
        '2895',
        _('Fabrication de machines pour les industries du papier et du carton'),
    ),
    (
        '2895Z',
        _('Fabrication de machines pour les industries du papier et du carton'),
    ),
    (
        '2896',
        _(
            'Fabrication de machines pour le travail du caoutchouc ou des plastiques'
        ),
    ),
    (
        '2896Z',
        _(
            'Fabrication de machines pour le travail du caoutchouc ou des plastiques'
        ),
    ),
    ('2899', _("Fabrication d'autres machines d'usage spécifique n.c.a.")),
    ('2899A', _("Fabrication de machines d'imprimerie")),
    ('2899B', _("Fabrication d'autres machines spécialisées")),
    ('29', _('Industrie automobile')),
    ('291', _('Construction de véhicules automobiles')),
    ('2910', _('Construction de véhicules automobiles')),
    ('2910Z', _('Construction de véhicules automobiles')),
    ('292', _('Fabrication de carrosseries et remorques')),
    ('2920', _('Fabrication de carrosseries et remorques')),
    ('2920Z', _('Fabrication de carrosseries et remorques')),
    ('293', _("Fabrication d'équipements automobiles")),
    (
        '2931',
        _("Fabrication d'équipements électriques et électroniques automobiles"),
    ),
    (
        '2931Z',
        _("Fabrication d'équipements électriques et électroniques automobiles"),
    ),
    ('2932', _("Fabrication d'autres équipements automobiles")),
    ('2932Z', _("Fabrication d'autres équipements automobiles")),
    ('30', _("Fabrication d'autres matériels de transport")),
    ('301', _('Construction navale')),
    ('3011', _('Construction de navires et de structures flottantes')),
    ('3011Z', _('Construction de navires et de structures flottantes')),
    ('3012', _('Construction de bateaux de plaisance')),
    ('3012Z', _('Construction de bateaux de plaisance')),
    (
        '302',
        _(
            "Construction de locomotives et d'autre matériel ferroviaire roulant"
        ),
    ),
    (
        '3020',
        _(
            "Construction de locomotives et d'autre matériel ferroviaire roulant "
        ),
    ),
    (
        '3020Z',
        _(
            "Construction de locomotives et d'autre matériel ferroviaire roulant "
        ),
    ),
    ('303', _('Construction aéronautique et spatiale ')),
    ('3030', _('Construction aéronautique et spatiale ')),
    ('3030Z', _('Construction aéronautique et spatiale ')),
    ('304', _('Construction de véhicules militaires de combat')),
    ('3040', _('Construction de véhicules militaires de combat ')),
    ('3040Z', _('Construction de véhicules militaires de combat ')),
    ('309', _('Fabrication de matériels de transport n.c.a.')),
    ('3091', _('Fabrication de motocycles')),
    ('3091Z', _('Fabrication de motocycles')),
    ('3092', _('Fabrication de bicyclettes et de véhicules pour invalides')),
    ('3092Z', _('Fabrication de bicyclettes et de véhicules pour invalides')),
    ('3099', _('Fabrication d’autres équipements de transport n.c.a.')),
    ('3099Z', _('Fabrication d’autres équipements de transport n.c.a.')),
    ('31', _('Fabrication de meubles')),
    ('310', _('Fabrication de meubles')),
    ('3101', _('Fabrication de meubles de bureau et de magasin')),
    ('3101Z', _('Fabrication de meubles de bureau et de magasin')),
    ('3102', _('Fabrication de meubles de cuisine ')),
    ('3102Z', _('Fabrication de meubles de cuisine ')),
    ('3103', _('Fabrication de matelas')),
    ('3103Z', _('Fabrication de matelas')),
    ('3109', _("Fabrication d'autres meubles")),
    ('3109A', _("Fabrication de sièges d'ameublement d'intérieur")),
    (
        '3109B',
        _(
            'Fabrication d’autres meubles et industries connexes de l’ameublement'
        ),
    ),
    ('32', _('Autres industries manufacturières')),
    (
        '321',
        _(
            'Fabrication d’articles de joaillerie, bijouterie et articles similaires'
        ),
    ),
    ('3211', _('Frappe de monnaie')),
    ('3211Z', _('Frappe de monnaie')),
    ('3212', _('Fabrication d’articles de joaillerie et bijouterie')),
    ('3212Z', _('Fabrication d’articles de joaillerie et bijouterie')),
    (
        '3213',
        _(
            'Fabrication d’articles de bijouterie fantaisie et articles similaires'
        ),
    ),
    (
        '3213Z',
        _(
            'Fabrication d’articles de bijouterie fantaisie et articles similaires'
        ),
    ),
    ('322', _("Fabrication d'instruments de musique")),
    ('3220', _("Fabrication d'instruments de musique")),
    ('3220Z', _("Fabrication d'instruments de musique")),
    ('323', _("Fabrication d'articles de sport")),
    ('3230', _("Fabrication d'articles de sport")),
    ('3230Z', _("Fabrication d'articles de sport")),
    ('324', _('Fabrication de jeux et jouets')),
    ('3240', _('Fabrication de jeux et jouets')),
    ('3240Z', _('Fabrication de jeux et jouets')),
    (
        '325',
        _(
            "Fabrication d'instruments et de fournitures à usage médical et dentaire"
        ),
    ),
    (
        '3250',
        _(
            "Fabrication d'instruments et de fournitures à usage médical et dentaire "
        ),
    ),
    ('3250A', _('Fabrication de matériel médico-chirurgical et dentaire')),
    ('3250B', _('Fabrication de lunettes')),
    ('329', _('Activités manufacturières n.c.a.')),
    ('3291', _('Fabrication d’articles de brosserie')),
    ('3291Z', _('Fabrication d’articles de brosserie')),
    ('3299', _('Autres activités manufacturières n.c.a. ')),
    ('3299Z', _('Autres activités manufacturières n.c.a. ')),
    ('33', _("Réparation et installation de machines et d'équipements ")),
    ('331', _("Réparation d'ouvrages en métaux, de machines et d'équipements")),
    ('3311', _("Réparation d'ouvrages en métaux")),
    ('3311Z', _("Réparation d'ouvrages en métaux")),
    ('3312', _('Réparation de machines et équipements mécaniques')),
    ('3312Z', _('Réparation de machines et équipements mécaniques')),
    ('3313', _('Réparation de matériels électroniques et optiques')),
    ('3313Z', _('Réparation de matériels électroniques et optiques')),
    ('3314', _("Réparation d'équipements électriques")),
    ('3314Z', _("Réparation d'équipements électriques")),
    ('3315', _('Réparation et maintenance navale')),
    ('3315Z', _('Réparation et maintenance navale')),
    ('3316', _("Réparation et maintenance d'aéronefs et d'engins spatiaux ")),
    ('3316Z', _("Réparation et maintenance d'aéronefs et d'engins spatiaux ")),
    ('3317', _("Réparation et maintenance d'autres équipements de transport")),
    ('3317Z', _("Réparation et maintenance d'autres équipements de transport")),
    ('3319', _("Réparation d'autres équipements")),
    ('3319Z', _("Réparation d'autres équipements")),
    ('332', _("Installation de machines et d'équipements industriels")),
    ('3320', _("Installation de machines et d'équipements industriels")),
    (
        '3320A',
        _(
            'Installation de structures métalliques, chaudronnées et de tuyauterie'
        ),
    ),
    ('3320B', _('Installation de machines et équipements mécaniques')),
    (
        '3320C',
        _(
            "Conception d'ensemble et assemblage sur site industriel d'équipements de contrôle des processus industriels "
        ),
    ),
    (
        '3320D',
        _(
            "Installation d'équipements électriques, de matériels électroniques et optiques ou d'autres matériels"
        ),
    ),
    (
        '35',
        _(
            "Production et distribution d'électricité, de gaz, de vapeur et d'air conditionné"
        ),
    ),
    ('351', _("Production, transport et distribution d'électricité")),
    ('3511', _("Production d'électricité")),
    ('3511Z', _("Production d'électricité")),
    ('3512', _("Transport d'électricité")),
    ('3512Z', _("Transport d'électricité")),
    ('3513', _("Distribution d'électricité")),
    ('3513Z', _("Distribution d'électricité")),
    ('3514', _("Commerce d'électricité")),
    ('3514Z', _("Commerce d'électricité")),
    ('352', _('Production et distribution de combustibles gazeux')),
    ('3521', _('Production de combustibles gazeux')),
    ('3521Z', _('Production de combustibles gazeux')),
    ('3522', _('Distribution de combustibles gazeux par conduites')),
    ('3522Z', _('Distribution de combustibles gazeux par conduites')),
    ('3523', _('Commerce de combustibles gazeux par conduites')),
    ('3523Z', _('Commerce de combustibles gazeux par conduites')),
    ('353', _("Production et distribution de vapeur et d'air conditionné")),
    ('3530', _("Production et distribution de vapeur et d'air conditionné ")),
    ('3530Z', _("Production et distribution de vapeur et d'air conditionné ")),
    ('36', _("Captage, traitement et distribution d'eau ")),
    ('360', _("Captage, traitement et distribution d'eau")),
    ('3600', _("Captage, traitement et distribution d'eau")),
    ('3600Z', _("Captage, traitement et distribution d'eau")),
    ('37', _('Collecte et traitement des eaux usées')),
    ('370', _('Collecte et traitement des eaux usées')),
    ('3700', _('Collecte et traitement des eaux usées')),
    ('3700Z', _('Collecte et traitement des eaux usées')),
    ('38', _('Collecte, traitement et élimination des déchets ; récupération')),
    ('381', _('Collecte des déchets')),
    ('3811', _('Collecte des déchets non dangereux')),
    ('3811Z', _('Collecte des déchets non dangereux')),
    ('3812', _('Collecte des déchets dangereux')),
    ('3812Z', _('Collecte des déchets dangereux')),
    ('382', _('Traitement et élimination des déchets')),
    ('3821', _('Traitement et élimination des déchets non dangereux')),
    ('3821Z', _('Traitement et élimination des déchets non dangereux')),
    ('3822', _('Traitement et élimination des déchets dangereux')),
    ('3822Z', _('Traitement et élimination des déchets dangereux')),
    ('383', _('Récupération')),
    ('3831', _("Démantèlement d'épaves")),
    ('3831Z', _("Démantèlement d'épaves")),
    ('3832', _('Récupération de déchets triés')),
    ('3832Z', _('Récupération de déchets triés')),
    ('39', _('Dépollution et autres services de gestion des déchets')),
    ('390', _('Dépollution et autres services de gestion des déchets')),
    ('3900', _('Dépollution et autres services de gestion des déchets')),
    ('3900Z', _('Dépollution et autres services de gestion des déchets')),
    ('41', _('Construction de bâtiments ')),
    ('411', _('Promotion immobilière')),
    ('4110', _('Promotion immobilière')),
    ('4110A', _('Promotion immobilière de logements')),
    ('4110B', _('Promotion immobilière de bureaux')),
    ('4110C', _("Promotion immobilière d'autres bâtiments")),
    ('4110D', _('Supports juridiques de programmes')),
    ('412', _('Construction de bâtiments résidentiels et non résidentiels')),
    ('4120', _('Construction de bâtiments résidentiels et non résidentiels')),
    ('4120A', _('Construction de maisons individuelles')),
    ('4120B', _("Construction d'autres bâtiments")),
    ('42', _('Génie civil')),
    ('421', _('Construction de routes et de voies ferrées ')),
    ('4211', _('Construction de routes et autoroutes')),
    ('4211Z', _('Construction de routes et autoroutes')),
    ('4212', _('Construction de voies ferrées de surface et souterraines')),
    ('4212Z', _('Construction de voies ferrées de surface et souterraines')),
    ('4213', _('Construction de ponts et tunnels')),
    ('4213A', _("Construction d'ouvrages d'art")),
    ('4213B', _('Construction et entretien de tunnels')),
    ('422', _('Construction de réseaux et de lignes')),
    ('4221', _('Construction de réseaux pour fluides')),
    ('4221Z', _('Construction de réseaux pour fluides')),
    ('4222', _('Construction de réseaux électriques et de télécommunications')),
    (
        '4222Z',
        _('Construction de réseaux électriques et de télécommunications'),
    ),
    ('429', _("Construction d'autres ouvrages de génie civil ")),
    ('4291', _("Construction d'ouvrages maritimes et fluviaux")),
    ('4291Z', _("Construction d'ouvrages maritimes et fluviaux")),
    ('4299', _("Construction d'autres ouvrages de génie civil n.c.a.")),
    ('4299Z', _("Construction d'autres ouvrages de génie civil n.c.a.")),
    ('43', _('Travaux de construction spécialisés ')),
    ('431', _('Démolition et préparation des sites')),
    ('4311', _('Travaux de démolition')),
    ('4311Z', _('Travaux de démolition')),
    ('4312', _('Travaux de préparation des sites')),
    ('4312A', _('Travaux de terrassement courants et travaux préparatoires')),
    ('4312B', _('Travaux de terrassement spécialisés ou de grande masse')),
    ('4313', _('Forages et sondages')),
    ('4313Z', _('Forages et sondages')),
    (
        '432',
        _(
            "Travaux d'installation électrique, plomberie et autres travaux d'installation"
        ),
    ),
    ('4321', _('Installation électrique')),
    ('4321A', _("Travaux d'installation électrique dans tous locaux")),
    ('4321B', _("Travaux d'installation électrique sur la voie publique")),
    (
        '4322',
        _(
            "Travaux de plomberie et installation de chauffage et de conditionnement d'air"
        ),
    ),
    ('4322A', _("Travaux d'installation d'eau et de gaz en tous locaux")),
    (
        '4322B',
        _(
            "Travaux d'installation d'équipements thermiques et de climatisation"
        ),
    ),
    ('4329', _("Autres travaux d'installation")),
    ('4329A', _("Travaux d'isolation")),
    ('4329B', _("Autres travaux d'installation n.c.a.")),
    ('433', _('Travaux de finition')),
    ('4331', _('Travaux de plâtrerie')),
    ('4331Z', _('Travaux de plâtrerie')),
    ('4332', _('Travaux de menuiserie')),
    ('4332A', _('Travaux de menuiserie bois et PVC')),
    ('4332B', _('Travaux de menuiserie métallique et serrurerie')),
    ('4332C', _('Agencement de lieux de vente')),
    ('4333', _('Travaux de revêtement des sols et des murs')),
    ('4333Z', _('Travaux de revêtement des sols et des murs')),
    ('4334', _('Travaux de peinture et vitrerie')),
    ('4334Z', _('Travaux de peinture et vitrerie')),
    ('4339', _('Autres travaux de finition')),
    ('4339Z', _('Autres travaux de finition')),
    ('439', _('Autres travaux de construction spécialisés')),
    ('4391', _('Travaux de couverture')),
    ('4391A', _('Travaux de charpente')),
    ('4391B', _('Travaux de couverture par éléments')),
    ('4399', _('Autres travaux de construction spécialisés n.c.a.')),
    ('4399A', _("Travaux d'étanchéification")),
    ('4399B', _('Travaux de montage de structures métalliques')),
    ('4399C', _('Travaux de maçonnerie générale et gros œuvre de bâtiment')),
    ('4399D', _('Autres travaux spécialisés de construction')),
    ('4399E', _('Location avec opérateur de matériel de construction')),
    ('45', _("Commerce et réparation d'automobiles et de motocycles")),
    ('451', _('Commerce de véhicules automobiles')),
    ('4511', _('Commerce de voitures et de véhicules automobiles légers')),
    ('4511Z', _('Commerce de voitures et de véhicules automobiles légers')),
    ('4519', _("Commerce d'autres véhicules automobiles")),
    ('4519Z', _("Commerce d'autres véhicules automobiles")),
    ('452', _('Entretien et réparation de véhicules automobiles')),
    ('4520', _('Entretien et réparation de véhicules automobiles')),
    ('4520A', _('Entretien et réparation de véhicules automobiles légers')),
    ('4520B', _("Entretien et réparation d'autres véhicules automobiles")),
    ('453', _("Commerce d'équipements automobiles")),
    ('4531', _("Commerce de gros d'équipements automobiles")),
    ('4531Z', _("Commerce de gros d'équipements automobiles")),
    ('4532', _("Commerce de détail d'équipements automobiles")),
    ('4532Z', _("Commerce de détail d'équipements automobiles")),
    ('454', _('Commerce et réparation de motocycles')),
    ('4540', _('Commerce et réparation de motocycles')),
    ('4540Z', _('Commerce et réparation de motocycles')),
    (
        '46',
        _('Commerce de gros, à l’exception des automobiles et des motocycles'),
    ),
    ('461', _('Intermédiaires du commerce de gros')),
    (
        '4611',
        _(
            'Intermédiaires du commerce en matières premières agricoles, animaux vivants, matières premières textiles et produits semi-finis'
        ),
    ),
    (
        '4611Z',
        _(
            'Intermédiaires du commerce en matières premières agricoles, animaux vivants, matières premières textiles et produits semi-finis'
        ),
    ),
    (
        '4612',
        _(
            'Intermédiaires du commerce en combustibles, métaux, minéraux et produits chimiques'
        ),
    ),
    ('4612A', _("Centrales d'achat de carburant")),
    (
        '4612B',
        _(
            'Autres intermédiaires du commerce en combustibles, métaux, minéraux et produits chimiques'
        ),
    ),
    (
        '4613',
        _('Intermédiaires du commerce en bois et matériaux de construction'),
    ),
    (
        '4613Z',
        _('Intermédiaires du commerce en bois et matériaux de construction'),
    ),
    (
        '4614',
        _(
            'Intermédiaires du commerce en machines, équipements industriels, navires et avions'
        ),
    ),
    (
        '4614Z',
        _(
            'Intermédiaires du commerce en machines, équipements industriels, navires et avions'
        ),
    ),
    (
        '4615',
        _(
            'Intermédiaires du commerce en meubles, articles de ménage et quincaillerie'
        ),
    ),
    (
        '4615Z',
        _(
            'Intermédiaires du commerce en meubles, articles de ménage et quincaillerie'
        ),
    ),
    (
        '4616',
        _(
            'Intermédiaires du commerce en textiles, habillement, fourrures, chaussures et articles en cuir'
        ),
    ),
    (
        '4616Z',
        _(
            'Intermédiaires du commerce en textiles, habillement, fourrures, chaussures et articles en cuir'
        ),
    ),
    ('4617', _('Intermédiaires du commerce en denrées, boissons et tabac')),
    ('4617A', _("Centrales d'achat alimentaires")),
    (
        '4617B',
        _('Autres intermédiaires du commerce en denrées, boissons et tabac'),
    ),
    (
        '4618',
        _(
            "Intermédiaires spécialisés dans le commerce d'autres produits spécifiques"
        ),
    ),
    (
        '4618Z',
        _(
            "Intermédiaires spécialisés dans le commerce d'autres produits spécifiques"
        ),
    ),
    ('4619', _('Intermédiaires du commerce en produits divers')),
    ('4619A', _("Centrales d'achat non alimentaires")),
    ('4619B', _('Autres intermédiaires du commerce en produits divers')),
    (
        '462',
        _("Commerce de gros de produits agricoles bruts et d'animaux vivants"),
    ),
    (
        '4621',
        _(
            "Commerce de gros de céréales, de tabac non manufacturé, de semences et d'aliments pour le bétail "
        ),
    ),
    (
        '4621Z',
        _(
            "Commerce de gros (commerce interentreprises) de céréales, de tabac non manufacturé, de semences et d'aliments pour le bétail "
        ),
    ),
    ('4622', _('Commerce de gros de fleurs et plantes')),
    (
        '4622Z',
        _('Commerce de gros (commerce interentreprises) de fleurs et plantes'),
    ),
    ('4623', _("Commerce de gros d'animaux vivants")),
    (
        '4623Z',
        _("Commerce de gros (commerce interentreprises) d'animaux vivants"),
    ),
    ('4624', _('Commerce de gros de cuirs et peaux')),
    (
        '4624Z',
        _('Commerce de gros (commerce interentreprises) de cuirs et peaux'),
    ),
    (
        '463',
        _('Commerce de gros de produits alimentaires, de boissons et de tabac'),
    ),
    ('4631', _('Commerce de gros de fruits et légumes')),
    (
        '4631Z',
        _('Commerce de gros (commerce interentreprises) de fruits et légumes'),
    ),
    ('4632', _('Commerce de gros de viandes et de produits à base de viande')),
    (
        '4632A',
        _(
            'Commerce de gros (commerce interentreprises) de viandes de boucherie'
        ),
    ),
    (
        '4632B',
        _(
            'Commerce de gros (commerce interentreprises) de produits à base de viande'
        ),
    ),
    (
        '4632C',
        _(
            'Commerce de gros (commerce interentreprises) de volailles et gibier'
        ),
    ),
    (
        '4633',
        _(
            'Commerce de gros de produits laitiers, œufs, huiles et matières grasses comestibles'
        ),
    ),
    (
        '4633Z',
        _(
            'Commerce de gros (commerce interentreprises) de produits laitiers, œufs, huiles et matières grasses comestibles'
        ),
    ),
    ('4634', _('Commerce de gros de boissons')),
    ('4634Z', _('Commerce de gros (commerce interentreprises) de boissons')),
    ('4635', _('Commerce de gros de produits à base de tabac')),
    (
        '4635Z',
        _(
            'Commerce de gros (commerce interentreprises) de produits à base de tabac'
        ),
    ),
    ('4636', _('Commerce de gros de sucre, chocolat et confiserie')),
    (
        '4636Z',
        _(
            'Commerce de gros (commerce interentreprises) de sucre, chocolat et confiserie'
        ),
    ),
    ('4637', _('Commerce de gros de café, thé, cacao et épices')),
    (
        '4637Z',
        _(
            'Commerce de gros (commerce interentreprises) de café, thé, cacao et épices'
        ),
    ),
    (
        '4638',
        _(
            "Commerce de gros d'autres produits alimentaires, y compris poissons, crustacés et mollusques"
        ),
    ),
    (
        '4638A',
        _(
            'Commerce de gros (commerce interentreprises) de poissons, crustacés et mollusques'
        ),
    ),
    (
        '4638B',
        _(
            'Commerce de gros (commerce interentreprises) alimentaire spécialisé divers'
        ),
    ),
    (
        '4639',
        _('Commerce de gros non spécialisé de denrées, boissons et tabac'),
    ),
    (
        '4639A',
        _('Commerce de gros (commerce interentreprises) de produits surgelés'),
    ),
    (
        '4639B',
        _(
            'Commerce de gros (commerce interentreprises) alimentaire non spécialisé'
        ),
    ),
    ('464', _('Commerce de gros de biens domestiques')),
    ('4641', _('Commerce de gros de textiles')),
    ('4641Z', _('Commerce de gros (commerce interentreprises) de textiles')),
    ('4642', _("Commerce de gros d'habillement et de chaussures")),
    (
        '4642Z',
        _(
            "Commerce de gros (commerce interentreprises) d'habillement et de chaussures"
        ),
    ),
    ('4643', _("Commerce de gros d'appareils électroménagers")),
    (
        '4643Z',
        _(
            "Commerce de gros (commerce interentreprises) d'appareils électroménagers"
        ),
    ),
    (
        '4644',
        _("Commerce de gros de vaisselle, verrerie et produits d'entretien"),
    ),
    (
        '4644Z',
        _(
            "Commerce de gros (commerce interentreprises) de vaisselle, verrerie et produits d'entretien"
        ),
    ),
    ('4645', _('Commerce de gros de parfumerie et de produits de beauté')),
    (
        '4645Z',
        _(
            'Commerce de gros (commerce interentreprises) de parfumerie et de produits de beauté'
        ),
    ),
    ('4646', _('Commerce de gros de produits pharmaceutiques')),
    (
        '4646Z',
        _(
            'Commerce de gros (commerce interentreprises) de produits pharmaceutiques'
        ),
    ),
    (
        '4647',
        _("Commerce de gros de meubles, de tapis et d'appareils d'éclairage "),
    ),
    (
        '4647Z',
        _(
            "Commerce de gros (commerce interentreprises) de meubles, de tapis et d'appareils d'éclairage "
        ),
    ),
    ('4648', _("Commerce de gros d'articles d'horlogerie et de bijouterie")),
    (
        '4648Z',
        _(
            "Commerce de gros (commerce interentreprises) d'articles d'horlogerie et de bijouterie"
        ),
    ),
    ('4649', _("Commerce de gros d'autres biens domestiques")),
    (
        '4649Z',
        _(
            "Commerce de gros (commerce interentreprises) d'autres biens domestiques "
        ),
    ),
    (
        '465',
        _(
            "Commerce de gros d'équipements de l'information et de la communication "
        ),
    ),
    (
        '4651',
        _(
            "Commerce de gros d'ordinateurs, d'équipements informatiques périphériques et de logiciels"
        ),
    ),
    (
        '4651Z',
        _(
            "Commerce de gros (commerce interentreprises) d'ordinateurs, d'équipements informatiques périphériques et de logiciels"
        ),
    ),
    (
        '4652',
        _(
            "Commerce de gros de composants et d'équipements électroniques et de télécommunication"
        ),
    ),
    (
        '4652Z',
        _(
            "Commerce de gros (commerce interentreprises) de composants et d'équipements électroniques et de télécommunication"
        ),
    ),
    ('466', _("Commerce de gros d'autres équipements industriels")),
    ('4661', _('Commerce de gros de matériel agricole')),
    (
        '4661Z',
        _('Commerce de gros (commerce interentreprises) de matériel agricole'),
    ),
    ('4662', _('Commerce de gros de machines-outils')),
    (
        '4662Z',
        _('Commerce de gros (commerce interentreprises) de machines-outils'),
    ),
    (
        '4663',
        _(
            "Commerce de gros de machines pour l'extraction, la construction et le génie civil "
        ),
    ),
    (
        '4663Z',
        _(
            "Commerce de gros (commerce interentreprises) de machines pour l'extraction, la construction et le génie civil "
        ),
    ),
    (
        '4664',
        _(
            "Commerce de gros de machines pour l'industrie textile et l'habillement"
        ),
    ),
    (
        '4664Z',
        _(
            "Commerce de gros (commerce interentreprises) de machines pour l'industrie textile et l'habillement"
        ),
    ),
    ('4665', _('Commerce de gros de mobilier de bureau')),
    (
        '4665Z',
        _('Commerce de gros (commerce interentreprises) de mobilier de bureau'),
    ),
    ('4666', _("Commerce de gros d'autres machines et équipements de bureau ")),
    (
        '4666Z',
        _(
            "Commerce de gros (commerce interentreprises) d'autres machines et équipements de bureau "
        ),
    ),
    ('4669', _("Commerce de gros d'autres machines et équipements")),
    (
        '4669A',
        _(
            'Commerce de gros (commerce interentreprises) de matériel électrique'
        ),
    ),
    (
        '4669B',
        _(
            'Commerce de gros (commerce interentreprises) de fournitures et équipements industriels divers'
        ),
    ),
    (
        '4669C',
        _(
            'Commerce de gros (commerce interentreprises) de fournitures et équipements divers pour le commerce et les services'
        ),
    ),
    ('467', _('Autres commerces de gros spécialisés')),
    ('4671', _('Commerce de gros de combustibles et de produits annexes')),
    (
        '4671Z',
        _(
            'Commerce de gros (commerce interentreprises) de combustibles et de produits annexes'
        ),
    ),
    ('4672', _('Commerce de gros de minerais et métaux')),
    (
        '4672Z',
        _('Commerce de gros (commerce interentreprises) de minerais et métaux'),
    ),
    (
        '4673',
        _(
            "Commerce de gros de bois, de matériaux de construction et d'appareils sanitaires "
        ),
    ),
    (
        '4673A',
        _(
            'Commerce de gros (commerce interentreprises) de bois et de matériaux de construction '
        ),
    ),
    (
        '4673B',
        _(
            "Commerce de gros (commerce interentreprises) d'appareils sanitaires et de produits de décoration"
        ),
    ),
    (
        '4674',
        _(
            'Commerce de gros de quincaillerie et fournitures pour plomberie et chauffage'
        ),
    ),
    (
        '4674A',
        _('Commerce de gros (commerce interentreprises) de quincaillerie'),
    ),
    (
        '4674B',
        _(
            'Commerce de gros (commerce interentreprises) de fournitures pour la plomberie et le chauffage'
        ),
    ),
    ('4675', _('Commerce de gros de produits chimiques')),
    (
        '4675Z',
        _('Commerce de gros (commerce interentreprises) de produits chimiques'),
    ),
    ('4676', _("Commerce de gros d'autres produits intermédiaires")),
    (
        '4676Z',
        _(
            "Commerce de gros (commerce interentreprises) d'autres produits intermédiaires"
        ),
    ),
    ('4677', _('Commerce de gros de déchets et débris')),
    (
        '4677Z',
        _('Commerce de gros (commerce interentreprises) de déchets et débris'),
    ),
    ('469', _('Commerce de gros non spécialisé')),
    ('4690', _('Commerce de gros non spécialisé')),
    ('4690Z', _('Commerce de gros (commerce interentreprises) non spécialisé')),
    (
        '47',
        _(
            'Commerce de détail, à l’exception des automobiles et des motocycles'
        ),
    ),
    ('471', _('Commerce de détail en magasin non spécialisé')),
    (
        '4711',
        _(
            'Commerce de détail en magasin non spécialisé à prédominance alimentaire'
        ),
    ),
    ('4711A', _('Commerce de détail de produits surgelés')),
    ('4711B', _("Commerce d'alimentation générale")),
    ('4711C', _('Supérettes')),
    ('4711D', _('Supermarchés')),
    ('4711E', _('Magasins multi-commerces')),
    ('4711F', _('Hypermarchés')),
    ('4719', _('Autre commerce de détail en magasin non spécialisé')),
    ('4719A', _('Grands magasins')),
    ('4719B', _('Autres commerces de détail en magasin non spécialisé')),
    ('472', _('Commerce de détail alimentaire en magasin spécialisé')),
    (
        '4721',
        _('Commerce de détail de fruits et légumes en magasin spécialisé'),
    ),
    (
        '4721Z',
        _('Commerce de détail de fruits et légumes en magasin spécialisé'),
    ),
    (
        '4722',
        _(
            'Commerce de détail de viandes et de produits à base de viande en magasin spécialisé'
        ),
    ),
    (
        '4722Z',
        _(
            'Commerce de détail de viandes et de produits à base de viande en magasin spécialisé'
        ),
    ),
    (
        '4723',
        _(
            'Commerce de détail de poissons, crustacés et mollusques en magasin spécialisé'
        ),
    ),
    (
        '4723Z',
        _(
            'Commerce de détail de poissons, crustacés et mollusques en magasin spécialisé'
        ),
    ),
    (
        '4724',
        _(
            'Commerce de détail de pain, pâtisserie et confiserie en magasin spécialisé'
        ),
    ),
    (
        '4724Z',
        _(
            'Commerce de détail de pain, pâtisserie et confiserie en magasin spécialisé'
        ),
    ),
    ('4725', _('Commerce de détail de boissons en magasin spécialisé')),
    ('4725Z', _('Commerce de détail de boissons en magasin spécialisé')),
    (
        '4726',
        _(
            'Commerce de détail de produits à base de tabac en magasin spécialisé'
        ),
    ),
    (
        '4726Z',
        _(
            'Commerce de détail de produits à base de tabac en magasin spécialisé'
        ),
    ),
    (
        '4729',
        _('Autres commerces de détail alimentaires en magasin spécialisé '),
    ),
    (
        '4729Z',
        _('Autres commerces de détail alimentaires en magasin spécialisé '),
    ),
    ('473', _('Commerce de détail de carburants en magasin spécialisé')),
    ('4730', _('Commerce de détail de carburants en magasin spécialisé')),
    ('4730Z', _('Commerce de détail de carburants en magasin spécialisé')),
    (
        '474',
        _(
            "Commerce de détail d'équipements de l'information et de la communication en magasin spécialisé"
        ),
    ),
    (
        '4741',
        _(
            "Commerce de détail d'ordinateurs, d'unités périphériques et de logiciels en magasin spécialisé"
        ),
    ),
    (
        '4741Z',
        _(
            "Commerce de détail d'ordinateurs, d'unités périphériques et de logiciels en magasin spécialisé"
        ),
    ),
    (
        '4742',
        _(
            'Commerce de détail de matériels de télécommunication en magasin spécialisé'
        ),
    ),
    (
        '4742Z',
        _(
            'Commerce de détail de matériels de télécommunication en magasin spécialisé'
        ),
    ),
    (
        '4743',
        _('Commerce de détail de matériels audio/vidéo en magasin spécialisé'),
    ),
    (
        '4743Z',
        _(
            'Commerce de détail de matériels audio et vidéo en magasin spécialisé'
        ),
    ),
    (
        '475',
        _(
            "Commerce de détail d'autres équipements du foyer en magasin spécialisé"
        ),
    ),
    ('4751', _('Commerce de détail de textiles en magasin spécialisé')),
    ('4751Z', _('Commerce de détail de textiles en magasin spécialisé')),
    (
        '4752',
        _(
            'Commerce de détail de quincaillerie, peintures et verres en magasin spécialisé'
        ),
    ),
    (
        '4752A',
        _(
            'Commerce de détail de quincaillerie, peintures et verres en petites surfaces (moins de 400 m2)'
        ),
    ),
    (
        '4752B',
        _(
            'Commerce de détail de quincaillerie, peintures et verres en grandes surfaces (400 m2et plus)'
        ),
    ),
    (
        '4753',
        _(
            'Commerce de détail de tapis, moquettes et revêtements de murs et de sols en magasin spécialisé'
        ),
    ),
    (
        '4753Z',
        _(
            'Commerce de détail de tapis, moquettes et revêtements de murs et de sols en magasin spécialisé'
        ),
    ),
    (
        '4754',
        _(
            "Commerce de détail d'appareils électroménagers en magasin spécialisé"
        ),
    ),
    (
        '4754Z',
        _(
            "Commerce de détail d'appareils électroménagers en magasin spécialisé"
        ),
    ),
    (
        '4759',
        _(
            "Commerce de détail de meubles, appareils d'éclairage et autres articles de ménage en magasin spécialisé"
        ),
    ),
    ('4759A', _('Commerce de détail de meubles')),
    ('4759B', _("Commerce de détail d'autres équipements du foyer")),
    (
        '476',
        _(
            'Commerce de détail de biens culturels et de loisirs en magasin spécialisé'
        ),
    ),
    ('4761', _('Commerce de détail de livres en magasin spécialisé')),
    ('4761Z', _('Commerce de détail de livres en magasin spécialisé')),
    (
        '4762',
        _('Commerce de détail de journaux et papeterie en magasin spécialisé'),
    ),
    (
        '4762Z',
        _('Commerce de détail de journaux et papeterie en magasin spécialisé'),
    ),
    (
        '4763',
        _(
            "Commerce de détail d'enregistrements musicaux et vidéo en magasin spécialisé"
        ),
    ),
    (
        '4763Z',
        _(
            "Commerce de détail d'enregistrements musicaux et vidéo en magasin spécialisé"
        ),
    ),
    ('4764', _("Commerce de détail d'articles de sport en magasin spécialisé")),
    (
        '4764Z',
        _("Commerce de détail d'articles de sport en magasin spécialisé"),
    ),
    ('4765', _('Commerce de détail de jeux et jouets en magasin spécialisé')),
    ('4765Z', _('Commerce de détail de jeux et jouets en magasin spécialisé')),
    ('477', _('Autres commerces de détail en magasin spécialisé')),
    ('4771', _("Commerce de détail d'habillement en magasin spécialisé")),
    ('4771Z', _("Commerce de détail d'habillement en magasin spécialisé")),
    (
        '4772',
        _(
            "Commerce de détail de chaussures et d'articles en cuir en magasin spécialisé"
        ),
    ),
    ('4772A', _('Commerce de détail de la chaussure')),
    ('4772B', _("Commerce de détail de maroquinerie et d'articles de voyage")),
    (
        '4773',
        _(
            'Commerce de détail de produits pharmaceutiques en magasin spécialisé'
        ),
    ),
    (
        '4773Z',
        _(
            'Commerce de détail de produits pharmaceutiques en magasin spécialisé'
        ),
    ),
    (
        '4774',
        _(
            "Commerce de détail d'articles médicaux et orthopédiques en magasin spécialisé"
        ),
    ),
    (
        '4774Z',
        _(
            "Commerce de détail d'articles médicaux et orthopédiques en magasin spécialisé"
        ),
    ),
    (
        '4775',
        _(
            'Commerce de détail de parfumerie et de produits de beauté en magasin spécialisé'
        ),
    ),
    (
        '4775Z',
        _(
            'Commerce de détail de parfumerie et de produits de beauté en magasin spécialisé'
        ),
    ),
    (
        '4776',
        _(
            'Commerce de détail de fleurs, plantes, graines, engrais, animaux de compagnie et aliments pour ces animaux en magasin spécialisé'
        ),
    ),
    (
        '4776Z',
        _(
            'Commerce de détail de fleurs, plantes, graines, engrais, animaux de compagnie et aliments pour ces animaux en magasin spécialisé'
        ),
    ),
    (
        '4777',
        _(
            "Commerce de détail d'articles d'horlogerie et de bijouterie en magasin spécialisé"
        ),
    ),
    (
        '4777Z',
        _(
            "Commerce de détail d'articles d'horlogerie et de bijouterie en magasin spécialisé"
        ),
    ),
    (
        '4778',
        _('Autre commerce de détail de biens neufs en magasin spécialisé'),
    ),
    ('4778A', _("Commerces de détail d'optique")),
    ('4778B', _('Commerces de détail de charbons et combustibles')),
    ('4778C', _('Autres commerces de détail spécialisés divers')),
    ('4779', _("Commerce de détail de biens d'occasion en magasin")),
    ('4779Z', _("Commerce de détail de biens d'occasion en magasin")),
    ('478', _('Commerce de détail sur éventaires et marchés')),
    ('4781', _('Commerce de détail alimentaire sur éventaires et marchés')),
    ('4781Z', _('Commerce de détail alimentaire sur éventaires et marchés')),
    (
        '4782',
        _(
            "Commerce de détail de textiles, d'habillement et de chaussures sur éventaires et marchés"
        ),
    ),
    (
        '4782Z',
        _(
            "Commerce de détail de textiles, d'habillement et de chaussures sur éventaires et marchés"
        ),
    ),
    ('4789', _('Autres commerces de détail sur éventaires et marchés')),
    ('4789Z', _('Autres commerces de détail sur éventaires et marchés')),
    ('479', _('Commerce de détail hors magasin, éventaires ou marchés')),
    ('4791', _('Vente à distance')),
    ('4791A', _('Vente à distance sur catalogue général')),
    ('4791B', _('Vente à distance sur catalogue spécialisé')),
    (
        '4799',
        _('Autres commerces de détail hors magasin, éventaires ou marchés'),
    ),
    ('4799A', _('Vente à domicile')),
    (
        '4799B',
        _(
            'Vente par automates et autres commerces de détail hors magasin, éventaires ou marchés n.c.a.'
        ),
    ),
    ('49', _('Transports terrestres et transport par conduites')),
    ('491', _('Transport ferroviaire interurbain de voyageurs')),
    ('4910', _('Transport ferroviaire interurbain de voyageurs')),
    ('4910Z', _('Transport ferroviaire interurbain de voyageurs')),
    ('492', _('Transports ferroviaires de fret')),
    ('4920', _('Transports ferroviaires de fret ')),
    ('4920Z', _('Transports ferroviaires de fret ')),
    ('493', _('Autres transports terrestres de voyageurs')),
    ('4931', _('Transports urbains et suburbains de voyageurs')),
    ('4931Z', _('Transports urbains et suburbains de voyageurs')),
    ('4932', _('Transports de voyageurs par taxis')),
    ('4932Z', _('Transports de voyageurs par taxis')),
    ('4939', _('Autres transports terrestres de voyageurs n.c.a.')),
    ('4939A', _('Transports routiers réguliers de voyageurs')),
    ('4939B', _('Autres transports routiers de voyageurs ')),
    ('4939C', _('Téléphériques et remontées mécaniques')),
    ('494', _('Transports routiers de fret et services de déménagement')),
    ('4941', _('Transports routiers de fret')),
    ('4941A', _('Transports routiers de fret interurbains')),
    ('4941B', _('Transports routiers de fret de proximité')),
    ('4941C', _('Location de camions avec chauffeur')),
    ('4942', _('Services de déménagement')),
    ('4942Z', _('Services de déménagement')),
    ('495', _('Transports par conduites')),
    ('4950', _('Transports par conduites')),
    ('4950Z', _('Transports par conduites')),
    ('50', _('Transports par eau')),
    ('501', _('Transports maritimes et côtiers de passagers')),
    ('5010', _('Transports maritimes et côtiers de passagers')),
    ('5010Z', _('Transports maritimes et côtiers de passagers')),
    ('502', _('Transports maritimes et côtiers de fret')),
    ('5020', _('Transports maritimes et côtiers de fret')),
    ('5020Z', _('Transports maritimes et côtiers de fret')),
    ('503', _('Transports fluviaux de passagers')),
    ('5030', _('Transports fluviaux de passagers')),
    ('5030Z', _('Transports fluviaux de passagers')),
    ('504', _('Transports fluviaux de fret')),
    ('5040', _('Transports fluviaux de fret ')),
    ('5040Z', _('Transports fluviaux de fret ')),
    ('51', _('Transports aériens')),
    ('511', _('Transports aériens de passagers')),
    ('5110', _('Transports aériens de passagers')),
    ('5110Z', _('Transports aériens de passagers')),
    ('512', _('Transports aériens de fret et transports spatiaux')),
    ('5121', _('Transports aériens de fret')),
    ('5121Z', _('Transports aériens de fret')),
    ('5122', _('Transports spatiaux')),
    ('5122Z', _('Transports spatiaux')),
    ('52', _('Entreposage et services auxiliaires des transports')),
    ('521', _('Entreposage et stockage')),
    ('5210', _('Entreposage et stockage')),
    ('5210A', _('Entreposage et stockage frigorifique')),
    ('5210B', _('Entreposage et stockage non frigorifique')),
    ('522', _('Services auxiliaires des transports')),
    ('5221', _('Services auxiliaires des transports terrestres')),
    ('5221Z', _('Services auxiliaires des transports terrestres')),
    ('5222', _('Services auxiliaires des transports par eau')),
    ('5222Z', _('Services auxiliaires des transports par eau')),
    ('5223', _('Services auxiliaires des transports aériens')),
    ('5223Z', _('Services auxiliaires des transports aériens')),
    ('5224', _('Manutention')),
    ('5224A', _('Manutention portuaire')),
    ('5224B', _('Manutention non portuaire')),
    ('5229', _('Autres services auxiliaires des transports ')),
    ('5229A', _('Messagerie, fret express')),
    ('5229B', _('Affrètement et organisation des transports ')),
    ('53', _('Activités de poste et de courrier')),
    (
        '531',
        _(
            "Activités de poste dans le cadre d'une obligation de service universel"
        ),
    ),
    (
        '5310',
        _(
            "Activités de poste dans le cadre d'une obligation de service universel "
        ),
    ),
    (
        '5310Z',
        _(
            "Activités de poste dans le cadre d'une obligation de service universel "
        ),
    ),
    ('532', _('Autres activités de poste et de courrier')),
    ('5320', _('Autres activités de poste et de courrier')),
    ('5320Z', _('Autres activités de poste et de courrier')),
    ('55', _('Hébergement')),
    ('551', _('Hôtels et hébergement similaire')),
    ('5510', _('Hôtels et hébergement similaire ')),
    ('5510Z', _('Hôtels et hébergement similaire ')),
    ('552', _('Hébergement touristique et autre hébergement de courte durée ')),
    (
        '5520',
        _('Hébergement touristique et autre hébergement de courte durée '),
    ),
    (
        '5520Z',
        _('Hébergement touristique et autre hébergement de courte durée '),
    ),
    (
        '553',
        _(
            'Terrains de camping et parcs pour caravanes ou véhicules de loisirs'
        ),
    ),
    (
        '5530',
        _(
            'Terrains de camping et parcs pour caravanes ou véhicules de loisirs'
        ),
    ),
    (
        '5530Z',
        _(
            'Terrains de camping et parcs pour caravanes ou véhicules de loisirs'
        ),
    ),
    ('559', _('Autres hébergements ')),
    ('5590', _('Autres hébergements ')),
    ('5590Z', _('Autres hébergements ')),
    ('56', _('Restauration')),
    ('561', _('Restaurants et services de restauration mobile')),
    ('5610', _('Restaurants et services de restauration mobile')),
    ('5610A', _('Restauration traditionnelle')),
    ('5610B', _('Cafétérias et autres libres-services')),
    ('5610C', _('Restauration de type rapide')),
    ('562', _('Traiteurs et autres services de restauration')),
    ('5621', _('Services des traiteurs ')),
    ('5621Z', _('Services des traiteurs ')),
    ('5629', _('Autres services de restauration ')),
    ('5629A', _('Restauration collective sous contrat')),
    ('5629B', _('Autres services de restauration n.c.a.')),
    ('563', _('Débits de boissons')),
    ('5630', _('Débits de boissons')),
    ('5630Z', _('Débits de boissons')),
    ('58', _('Édition')),
    (
        '581',
        _("Édition de livres et périodiques et autres activités d'édition "),
    ),
    ('5811', _('Édition de livres')),
    ('5811Z', _('Édition de livres')),
    ('5812', _("Édition de répertoires et de fichiers d'adresses")),
    ('5812Z', _("Édition de répertoires et de fichiers d'adresses")),
    ('5813', _('Édition de journaux')),
    ('5813Z', _('Édition de journaux')),
    ('5814', _('Édition de revues et périodiques')),
    ('5814Z', _('Édition de revues et périodiques')),
    ('5819', _("Autres activités d'édition")),
    ('5819Z', _("Autres activités d'édition")),
    ('582', _('Édition de logiciels')),
    ('5821', _('Édition de jeux électroniques')),
    ('5821Z', _('Édition de jeux électroniques')),
    ('5829', _("Édition d'autres logiciels")),
    ('5829A', _('Édition de logiciels système et de réseau')),
    ('5829B', _('Edition de logiciels outils de développement et de langages')),
    ('5829C', _('Edition de logiciels applicatifs')),
    (
        '59',
        _(
            'Production de films cinématographiques, de vidéo et de programmes de télévision ; enregistrement sonore et édition musicale'
        ),
    ),
    ('591', _('Activités cinématographiques, vidéo et de télévision')),
    (
        '5911',
        _(
            'Production de films cinématographiques, de vidéo et de programmes de télévision '
        ),
    ),
    ('5911A', _('Production de films et de programmes pour la télévision ')),
    ('5911B', _('Production de films institutionnels et publicitaires')),
    ('5911C', _('Production de films pour le cinéma')),
    (
        '5912',
        _(
            'Post-production de films cinématographiques, de vidéo et de programmes de télévision'
        ),
    ),
    (
        '5912Z',
        _(
            'Post-production de films cinématographiques, de vidéo et de programmes de télévision'
        ),
    ),
    (
        '5913',
        _(
            'Distribution de films cinématographiques, de vidéo et de programmes de télévision '
        ),
    ),
    ('5913A', _('Distribution de films cinématographiques')),
    ('5913B', _('Edition et distribution vidéo')),
    ('5914', _('Projection de films cinématographiques')),
    ('5914Z', _('Projection de films cinématographiques')),
    ('592', _('Enregistrement sonore et édition musicale')),
    ('5920', _('Enregistrement sonore et édition musicale ')),
    ('5920Z', _('Enregistrement sonore et édition musicale ')),
    ('60', _('Programmation et diffusion')),
    ('601', _('Édition et diffusion de programmes radio')),
    ('6010', _('Édition et diffusion de programmes radio')),
    ('6010Z', _('Édition et diffusion de programmes radio')),
    ('602', _('Programmation de télévision et télédiffusion')),
    ('6020', _('Programmation de télévision et télédiffusion')),
    ('6020A', _('Edition de chaînes généralistes')),
    ('6020B', _('Edition de chaînes thématiques')),
    ('61', _('Télécommunications')),
    ('611', _('Télécommunications filaires')),
    ('6110', _('Télécommunications filaires')),
    ('6110Z', _('Télécommunications filaires')),
    ('612', _('Télécommunications sans fil ')),
    ('6120', _('Télécommunications sans fil ')),
    ('6120Z', _('Télécommunications sans fil ')),
    ('613', _('Télécommunications par satellite')),
    ('6130', _('Télécommunications par satellite')),
    ('6130Z', _('Télécommunications par satellite')),
    ('619', _('Autres activités de télécommunication')),
    ('6190', _('Autres activités de télécommunication ')),
    ('6190Z', _('Autres activités de télécommunication ')),
    ('62', _('Programmation, conseil et autres activités informatiques ')),
    ('620', _('Programmation, conseil et autres activités informatiques ')),
    ('6201', _('Programmation informatique')),
    ('6201Z', _('Programmation informatique')),
    ('6202', _('Conseil informatique ')),
    ('6202A', _('Conseil en systèmes et logiciels informatiques')),
    (
        '6202B',
        _('Tierce maintenance de systèmes et d’applications informatiques'),
    ),
    ('6203', _("Gestion d'installations informatiques")),
    ('6203Z', _("Gestion d'installations informatiques")),
    ('6209', _('Autres activités informatiques')),
    ('6209Z', _('Autres activités informatiques')),
    ('63', _("Services d'information")),
    (
        '631',
        _(
            'Traitement de données, hébergement et activités connexes ; portails Internet'
        ),
    ),
    ('6311', _('Traitement de données, hébergement et activités connexes')),
    ('6311Z', _('Traitement de données, hébergement et activités connexes')),
    ('6312', _('Portails Internet')),
    ('6312Z', _('Portails Internet')),
    ('639', _("Autres services d'information")),
    ('6391', _('Activités des agences de presse')),
    ('6391Z', _('Activités des agences de presse')),
    ('6399', _("Autres services d'information n.c.a.")),
    ('6399Z', _("Autres services d'information n.c.a.")),
    (
        '64',
        _(
            'Activités des services financiers, hors assurance et caisses de retraite'
        ),
    ),
    ('641', _('Intermédiation monétaire')),
    ('6411', _('Activités de banque centrale')),
    ('6411Z', _('Activités de banque centrale')),
    ('6419', _('Autres intermédiations monétaires')),
    ('6419Z', _('Autres intermédiations monétaires')),
    ('642', _('Activités des sociétés holding')),
    ('6420', _('Activités des sociétés holding')),
    ('6420Z', _('Activités des sociétés holding')),
    ('643', _('Fonds de placement et entités financières similaires')),
    ('6430', _('Fonds de placement et entités financières similaires')),
    ('6430Z', _('Fonds de placement et entités financières similaires')),
    (
        '649',
        _(
            'Autres activités des services financiers, hors assurance et caisses de retraite'
        ),
    ),
    ('6491', _('Crédit-bail ')),
    ('6491Z', _('Crédit-bail ')),
    ('6492', _('Autre distribution de crédit')),
    ('6492Z', _('Autre distribution de crédit')),
    (
        '6499',
        _(
            'Autres activités des services financiers, hors assurance et caisses de retraite, n.c.a.'
        ),
    ),
    (
        '6499Z',
        _(
            'Autres activités des services financiers, hors assurance et caisses de retraite, n.c.a.'
        ),
    ),
    ('65', _('Assurance')),
    ('651', _('Assurance')),
    ('6511', _('Assurance vie ')),
    ('6511Z', _('Assurance vie')),
    ('6512', _('Autres assurances')),
    ('6512Z', _('Autres assurances')),
    ('652', _('Réassurance')),
    ('6520', _('Réassurance')),
    ('6520Z', _('Réassurance')),
    ('653', _('Caisses de retraite')),
    ('6530', _('Caisses de retraite')),
    ('6530Z', _('Caisses de retraite')),
    ('66', _("Activités auxiliaires de services financiers et d'assurance ")),
    (
        '661',
        _(
            'Activités auxiliaires de services financiers, hors assurance et caisses de retraite'
        ),
    ),
    ('6611', _('Administration de marchés financiers')),
    ('6611Z', _('Administration de marchés financiers')),
    ('6612', _('Courtage de valeurs mobilières et de marchandises')),
    ('6612Z', _('Courtage de valeurs mobilières et de marchandises')),
    (
        '6619',
        _(
            'Autres activités auxiliaires de services financiers, hors assurance et caisses de retraite'
        ),
    ),
    ('6619A', _('Supports juridiques de gestion de patrimoine mobilier')),
    (
        '6619B',
        _(
            'Autres activités auxiliaires de services financiers, hors assurance et caisses de retraite, n.c.a.'
        ),
    ),
    ('662', _("Activités auxiliaires d'assurance et de caisses de retraite")),
    ('6621', _('Évaluation des risques et dommages')),
    ('6621Z', _('Évaluation des risques et dommages')),
    ('6622', _("Activités des agents et courtiers d'assurances")),
    ('6622Z', _("Activités des agents et courtiers d'assurances")),
    (
        '6629',
        _("Autres activités auxiliaires d'assurance et de caisses de retraite"),
    ),
    (
        '6629Z',
        _("Autres activités auxiliaires d'assurance et de caisses de retraite"),
    ),
    ('663', _('Gestion de fonds')),
    ('6630', _('Gestion de fonds')),
    ('6630Z', _('Gestion de fonds')),
    ('68', _('Activités immobilières')),
    ('681', _('Activités des marchands de biens immobiliers')),
    ('6810', _('Activités des marchands de biens immobiliers')),
    ('6810Z', _('Activités des marchands de biens immobiliers')),
    (
        '682',
        _('Location et exploitation de biens immobiliers propres ou loués'),
    ),
    (
        '6820',
        _('Location et exploitation de biens immobiliers propres ou loués '),
    ),
    ('6820A', _('Location de logements')),
    ('6820B', _("Location de terrains et d'autres biens immobiliers")),
    ('683', _('Activités immobilières pour compte de tiers')),
    ('6831', _('Agences immobilières')),
    ('6831Z', _('Agences immobilières')),
    ('6832', _('Administration de biens immobiliers')),
    ('6832A', _("Administration d'immeubles et autres biens immobiliers")),
    ('6832B', _('Supports juridiques de gestion de patrimoine immobilier')),
    ('69', _('Activités juridiques et comptables')),
    ('691', _('Activités juridiques')),
    ('6910', _('Activités juridiques')),
    ('6910Z', _('Activités juridiques')),
    ('692', _('Activités comptables')),
    ('6920', _('Activités comptables')),
    ('6920Z', _('Activités comptables')),
    ('70', _('Activités des sièges sociaux ; conseil de gestion')),
    ('701', _('Activités des sièges sociaux')),
    ('7010', _('Activités des sièges sociaux')),
    ('7010Z', _('Activités des sièges sociaux')),
    ('702', _('Conseil de gestion')),
    ('7021', _('Conseil en relations publiques et communication')),
    ('7021Z', _('Conseil en relations publiques et communication')),
    ('7022', _('Conseil pour les affaires et autres conseils de gestion')),
    ('7022Z', _('Conseil pour les affaires et autres conseils de gestion')),
    (
        '71',
        _(
            "Activités d'architecture et d'ingénierie ; activités de contrôle et analyses techniques"
        ),
    ),
    ('711', _("Activités d'architecture et d'ingénierie")),
    ('7111', _("Activités d'architecture ")),
    ('7111Z', _("Activités d'architecture ")),
    ('7112', _("Activités d'ingénierie")),
    ('7112A', _('Activité des géomètres')),
    ('7112B', _('Ingénierie, études techniques')),
    ('712', _('Activités de contrôle et analyses techniques')),
    ('7120', _('Activités de contrôle et analyses techniques')),
    ('7120A', _('Contrôle technique automobile')),
    ('7120B', _('Analyses, essais et inspections techniques')),
    ('72', _('Recherche-développement scientifique')),
    ('721', _('Recherche-développement en sciences physiques et naturelles')),
    ('7211', _('Recherche-développement en biotechnologie')),
    ('7211Z', _('Recherche-développement en biotechnologie')),
    (
        '7219',
        _('Recherche-développement en autres sciences physiques et naturelles'),
    ),
    (
        '7219Z',
        _('Recherche-développement en autres sciences physiques et naturelles'),
    ),
    ('722', _('Recherche-développement en sciences humaines et sociales')),
    ('7220', _('Recherche-développement en sciences humaines et sociales')),
    ('7220Z', _('Recherche-développement en sciences humaines et sociales')),
    ('73', _('Publicité et études de marché')),
    ('731', _('Publicité')),
    ('7311', _('Activités des agences de publicité')),
    ('7311Z', _('Activités des agences de publicité')),
    ('7312', _('Régie publicitaire de médias')),
    ('7312Z', _('Régie publicitaire de médias')),
    ('732', _('Études de marché et sondages')),
    ('7320', _('Études de marché et sondages')),
    ('7320Z', _('Études de marché et sondages')),
    ('74', _('Autres activités spécialisées, scientifiques et techniques')),
    ('741', _('Activités spécialisées de design')),
    ('7410', _('Activités spécialisées de design')),
    ('7410Z', _('Activités spécialisées de design')),
    ('742', _('Activités photographiques')),
    ('7420', _('Activités photographiques')),
    ('7420Z', _('Activités photographiques')),
    ('743', _('Traduction et interprétation')),
    ('7430', _('Traduction et interprétation')),
    ('7430Z', _('Traduction et interprétation')),
    (
        '749',
        _('Autres activités spécialisées, scientifiques et techniques n.c.a.'),
    ),
    (
        '7490',
        _('Autres activités spécialisées, scientifiques et techniques n.c.a.'),
    ),
    ('7490A', _('Activité des économistes de la construction')),
    (
        '7490B',
        _('Activités spécialisées, scientifiques et techniques diverses'),
    ),
    ('75', _('Activités vétérinaires')),
    ('750', _('Activités vétérinaires')),
    ('7500', _('Activités vétérinaires')),
    ('7500Z', _('Activités vétérinaires')),
    ('77', _('Activités de location et location-bail')),
    ('771', _('Location et location-bail de véhicules automobiles')),
    (
        '7711',
        _(
            'Location et location-bail de voitures et de véhicules automobiles légers'
        ),
    ),
    (
        '7711A',
        _(
            'Location de courte durée de voitures et de véhicules automobiles légers'
        ),
    ),
    (
        '7711B',
        _(
            'Location de longue durée de voitures et de véhicules automobiles légers'
        ),
    ),
    ('7712', _('Location et location-bail de camions')),
    ('7712Z', _('Location et location-bail de camions')),
    ('772', _('Location et location-bail de biens personnels et domestiques')),
    ('7721', _("Location et location-bail d'articles de loisirs et de sport ")),
    (
        '7721Z',
        _("Location et location-bail d'articles de loisirs et de sport "),
    ),
    ('7722', _('Location de vidéocassettes et disques vidéo')),
    ('7722Z', _('Location de vidéocassettes et disques vidéo')),
    (
        '7729',
        _("Location et location-bail d'autres biens personnels et domestiques"),
    ),
    (
        '7729Z',
        _("Location et location-bail d'autres biens personnels et domestiques"),
    ),
    (
        '773',
        _("Location et location-bail d'autres machines, équipements et biens"),
    ),
    (
        '7731',
        _('Location et location-bail de machines et équipements agricoles'),
    ),
    (
        '7731Z',
        _('Location et location-bail de machines et équipements agricoles'),
    ),
    (
        '7732',
        _(
            'Location et location-bail de machines et équipements pour la construction'
        ),
    ),
    (
        '7732Z',
        _(
            'Location et location-bail de machines et équipements pour la construction'
        ),
    ),
    (
        '7733',
        _(
            'Location et location-bail de machines de bureau et de matériel informatique'
        ),
    ),
    (
        '7733Z',
        _(
            'Location et location-bail de machines de bureau et de matériel informatique'
        ),
    ),
    ('7734', _('Location et location-bail de matériels de transport par eau')),
    ('7734Z', _('Location et location-bail de matériels de transport par eau')),
    ('7735', _('Location et location-bail de matériels de transport aérien')),
    ('7735Z', _('Location et location-bail de matériels de transport aérien')),
    (
        '7739',
        _(
            "Location et location-bail d'autres machines, équipements et biens matériels n.c.a. "
        ),
    ),
    (
        '7739Z',
        _(
            "Location et location-bail d'autres machines, équipements et biens matériels n.c.a. "
        ),
    ),
    (
        '774',
        _(
            "Location-bail de propriété intellectuelle et de produits similaires, à l'exception des œuvres soumises à copyright"
        ),
    ),
    (
        '7740',
        _(
            "Location-bail de propriété intellectuelle et de produits similaires, à l'exception des œuvres soumises à copyright"
        ),
    ),
    (
        '7740Z',
        _(
            "Location-bail de propriété intellectuelle et de produits similaires, à l'exception des œuvres soumises à copyright"
        ),
    ),
    ('78', _("Activités liées à l'emploi")),
    ('781', _("Activités des agences de placement de main-d'œuvre")),
    ('7810', _("Activités des agences de placement de main-d'œuvre ")),
    ('7810Z', _("Activités des agences de placement de main-d'œuvre ")),
    ('782', _('Activités des agences de travail temporaire')),
    ('7820', _('Activités des agences de travail temporaire ')),
    ('7820Z', _('Activités des agences de travail temporaire ')),
    ('783', _('Autre mise à disposition de ressources humaines')),
    ('7830', _('Autre mise à disposition de ressources humaines')),
    ('7830Z', _('Autre mise à disposition de ressources humaines')),
    (
        '79',
        _(
            'Activités des agences de voyage, voyagistes, services de réservation et activités connexes'
        ),
    ),
    ('791', _('Activités des agences de voyage et voyagistes')),
    ('7911', _('Activités des agences de voyage')),
    ('7911Z', _('Activités des agences de voyage')),
    ('7912', _('Activités des voyagistes')),
    ('7912Z', _('Activités des voyagistes')),
    ('799', _('Autres services de réservation et activités connexes')),
    ('7990', _('Autres services de réservation et activités connexes')),
    ('7990Z', _('Autres services de réservation et activités connexes')),
    ('80', _('Enquêtes et sécurité')),
    ('801', _('Activités de sécurité privée')),
    ('8010', _('Activités de sécurité privée ')),
    ('8010Z', _('Activités de sécurité privée ')),
    ('802', _('Activités liées aux systèmes de sécurité')),
    ('8020', _('Activités liées aux systèmes de sécurité ')),
    ('8020Z', _('Activités liées aux systèmes de sécurité ')),
    ('803', _("Activités d'enquête")),
    ('8030', _("Activités d'enquête")),
    ('8030Z', _("Activités d'enquête")),
    ('81', _('Services relatifs aux bâtiments et aménagement paysager')),
    ('811', _('Activités combinées de soutien lié aux bâtiments')),
    ('8110', _('Activités combinées de soutien lié aux bâtiments ')),
    ('8110Z', _('Activités combinées de soutien lié aux bâtiments ')),
    ('812', _('Activités de nettoyage')),
    ('8121', _('Nettoyage courant des bâtiments')),
    ('8121Z', _('Nettoyage courant des bâtiments')),
    (
        '8122',
        _(
            'Autres activités de nettoyage des bâtiments et nettoyage industriel'
        ),
    ),
    (
        '8122Z',
        _(
            'Autres activités de nettoyage des bâtiments et nettoyage industriel'
        ),
    ),
    ('8129', _('Autres activités de nettoyage')),
    ('8129A', _('Désinfection, désinsectisation, dératisation')),
    ('8129B', _('Autres activités de nettoyage n.c.a.')),
    ('813', _("Services d'aménagement paysager")),
    ('8130', _("Services d'aménagement paysager ")),
    ('8130Z', _("Services d'aménagement paysager ")),
    (
        '82',
        _(
            'Activités administratives et autres activités de soutien aux entreprises'
        ),
    ),
    ('821', _('Activités administratives ')),
    ('8211', _('Services administratifs combinés de bureau')),
    ('8211Z', _('Services administratifs combinés de bureau')),
    (
        '8219',
        _(
            'Photocopie, préparation de documents et autres activités spécialisées de soutien de bureau'
        ),
    ),
    (
        '8219Z',
        _(
            'Photocopie, préparation de documents et autres activités spécialisées de soutien de bureau'
        ),
    ),
    ('822', _("Activités de centres d'appels")),
    ('8220', _("Activités de centres d'appels")),
    ('8220Z', _("Activités de centres d'appels")),
    ('823', _('Organisation de salons professionnels et congrès')),
    ('8230', _('Organisation de salons professionnels et congrès')),
    ('8230Z', _('Organisation de foires, salons professionnels et congrès')),
    ('829', _('Activités de soutien aux entreprises n.c.a.')),
    (
        '8291',
        _(
            "Activités des agences de recouvrement de factures et des sociétés d'information financière sur la clientèle"
        ),
    ),
    (
        '8291Z',
        _(
            "Activités des agences de recouvrement de factures et des sociétés d'information financière sur la clientèle"
        ),
    ),
    ('8292', _('Activités de conditionnement')),
    ('8292Z', _('Activités de conditionnement')),
    ('8299', _('Autres activités de soutien aux entreprises n.c.a.')),
    ('8299Z', _('Autres activités de soutien aux entreprises n.c.a.')),
    (
        '84',
        _('Administration publique et défense ; sécurité sociale obligatoire'),
    ),
    ('841', _('Administration générale, économique et sociale')),
    ('8411', _('Administration publique générale')),
    ('8411Z', _('Administration publique générale')),
    (
        '8412',
        _(
            'Administration publique (tutelle) de la santé, de la formation, de la culture et des services sociaux, autre que sécurité sociale '
        ),
    ),
    (
        '8412Z',
        _(
            'Administration publique (tutelle) de la santé, de la formation, de la culture et des services sociaux, autre que sécurité sociale '
        ),
    ),
    ('8413', _('Administration publique (tutelle) des activités économiques')),
    ('8413Z', _('Administration publique (tutelle) des activités économiques')),
    ('842', _('Services de prérogative publique')),
    ('8421', _('Affaires étrangères')),
    ('8421Z', _('Affaires étrangères')),
    ('8422', _('Défense')),
    ('8422Z', _('Défense')),
    ('8423', _('Justice')),
    ('8423Z', _('Justice')),
    ('8424', _('Activités d’ordre public et de sécurité')),
    ('8424Z', _('Activités d’ordre public et de sécurité')),
    ('8425', _('Services du feu et de secours')),
    ('8425Z', _('Services du feu et de secours')),
    ('843', _('Sécurité sociale obligatoire')),
    ('8430', _('Sécurité sociale obligatoire')),
    ('8430A', _('Activités générales de sécurité sociale')),
    ('8430B', _('Gestion des retraites complémentaires')),
    ('8430C', _('Distribution sociale de revenus')),
    ('85', _('Enseignement')),
    ('851', _('Enseignement pré-primaire')),
    ('8510', _('Enseignement pré-primaire')),
    ('8510Z', _('Enseignement pré-primaire')),
    ('852', _('Enseignement primaire')),
    ('8520', _('Enseignement primaire')),
    ('8520Z', _('Enseignement primaire')),
    ('853', _('Enseignement secondaire')),
    ('8531', _('Enseignement secondaire général')),
    ('8531Z', _('Enseignement secondaire général')),
    ('8532', _('Enseignement secondaire technique ou professionnel')),
    ('8532Z', _('Enseignement secondaire technique ou professionnel')),
    ('854', _('Enseignement supérieur et post-secondaire non supérieur')),
    ('8541', _('Enseignement post-secondaire non supérieur')),
    ('8541Z', _('Enseignement post-secondaire non supérieur')),
    ('8542', _('Enseignement supérieur')),
    ('8542Z', _('Enseignement supérieur')),
    ('855', _("Autres activités d'enseignement")),
    (
        '8551',
        _("Enseignement de disciplines sportives et d'activités de loisirs"),
    ),
    (
        '8551Z',
        _("Enseignement de disciplines sportives et d'activités de loisirs"),
    ),
    ('8552', _('Enseignement culturel')),
    ('8552Z', _('Enseignement culturel')),
    ('8553', _('Enseignement de la conduite')),
    ('8553Z', _('Enseignement de la conduite')),
    ('8559', _('Enseignements divers')),
    ('8559A', _("Formation continue d'adultes")),
    ('8559B', _('Autres enseignements')),
    ('856', _("Activités de soutien à l'enseignement")),
    ('8560', _("Activités de soutien à l'enseignement")),
    ('8560Z', _("Activités de soutien à l'enseignement")),
    ('86', _('Activités pour la santé humaine')),
    ('861', _('Activités hospitalières')),
    ('8610', _('Activités hospitalières')),
    ('8610Z', _('Activités hospitalières')),
    ('862', _('Activité des médecins et des dentistes')),
    ('8621', _('Activité des médecins généralistes')),
    ('8621Z', _('Activité des médecins généralistes')),
    ('8622', _('Activité des médecins spécialistes')),
    ('8622A', _('Activités de radiodiagnostic et de radiothérapie')),
    ('8622B', _('Activités chirurgicales')),
    ('8622C', _('Autres activités des médecins spécialistes')),
    ('8623', _('Pratique dentaire')),
    ('8623Z', _('Pratique dentaire')),
    ('869', _('Autres activités pour la santé humaine')),
    ('8690', _('Autres activités pour la santé humaine')),
    ('8690A', _('Ambulances')),
    ('8690B', _("Laboratoires d'analyses médicales")),
    ('8690C', _("Centres de collecte et banques d'organes")),
    ('8690D', _('Activités des infirmiers et des sages-femmes')),
    (
        '8690E',
        _(
            'Activités des professionnels de la rééducation, de l’appareillage et des pédicures-podologues'
        ),
    ),
    ('8690F', _('Activités de santé humaine non classées ailleurs')),
    ('87', _('Hébergement médico-social et social')),
    ('871', _('Hébergement médicalisé')),
    ('8710', _('Hébergement médicalisé')),
    ('8710A', _('Hébergement médicalisé pour personnes âgées')),
    ('8710B', _('Hébergement médicalisé pour enfants handicapés ')),
    (
        '8710C',
        _(
            'Hébergement médicalisé pour adultes handicapés et autre hébergement médicalisé'
        ),
    ),
    (
        '872',
        _(
            'Hébergement social pour personnes handicapées mentales, malades mentales et toxicomanes'
        ),
    ),
    (
        '8720',
        _(
            'Hébergement social pour personnes handicapées mentales, malades mentales et toxicomanes'
        ),
    ),
    (
        '8720A',
        _('Hébergement social pour handicapés mentaux et malades mentaux '),
    ),
    ('8720B', _('Hébergement social pour toxicomanes')),
    (
        '873',
        _('Hébergement social pour personnes âgées ou handicapées physiques '),
    ),
    (
        '8730',
        _('Hébergement social pour personnes âgées ou handicapées physiques '),
    ),
    ('8730A', _('Hébergement social pour personnes âgées')),
    ('8730B', _('Hébergement social pour handicapés  physiques')),
    ('879', _('Autres activités d’hébergement social ')),
    ('8790', _('Autres activités d’hébergement social ')),
    ('8790A', _('Hébergement social pour enfants en difficultés ')),
    (
        '8790B',
        _(
            'Hébergement social pour adultes et familles en difficultés et autre hébergement social '
        ),
    ),
    ('88', _('Action sociale sans hébergement')),
    (
        '881',
        _(
            'Action sociale sans hébergement pour personnes âgées et pour personnes handicapées '
        ),
    ),
    (
        '8810',
        _(
            'Action sociale sans hébergement pour personnes âgées et pour personnes handicapées '
        ),
    ),
    ('8810A', _('Aide à domicile  ')),
    (
        '8810B',
        _(
            'Accueil ou accompagnement sans hébergement d’adultes handicapés ou de  personnes âgées'
        ),
    ),
    ('8810C', _('Aide par le travail ')),
    ('889', _('Autre action sociale sans hébergement')),
    ('8891', _('Action sociale sans hébergement pour jeunes enfants')),
    ('8891A', _('Accueil de jeunes enfants')),
    (
        '8891B',
        _('Accueil ou accompagnement sans hébergement d’enfants handicapés'),
    ),
    ('8899', _('Autre action sociale sans hébergement n.c.a.')),
    (
        '8899A',
        _(
            'Autre accueil ou accompagnement sans hébergement d’enfants et d’adolescents'
        ),
    ),
    ('8899B', _('Action sociale sans hébergement n.c.a.')),
    ('90', _('Activités créatives, artistiques et de spectacle ')),
    ('900', _('Activités créatives, artistiques et de spectacle ')),
    ('9001', _('Arts du spectacle vivant')),
    ('9001Z', _('Arts du spectacle vivant')),
    ('9002', _('Activités de soutien au spectacle vivant')),
    ('9002Z', _('Activités de soutien au spectacle vivant')),
    ('9003', _('Création artistique')),
    ('9003A', _('Création artistique relevant des arts plastiques')),
    ('9003B', _('Autre création artistique')),
    ('9004', _('Gestion de salles de spectacles')),
    ('9004Z', _('Gestion de salles de spectacles')),
    (
        '91',
        _('Bibliothèques, archives, musées et autres activités culturelles'),
    ),
    (
        '910',
        _('Bibliothèques, archives, musées et autres activités culturelles'),
    ),
    ('9101', _('Gestion des bibliothèques et des archives')),
    ('9101Z', _('Gestion des bibliothèques et des archives')),
    ('9102', _('Gestion des musées')),
    ('9102Z', _('Gestion des musées')),
    (
        '9103',
        _(
            'Gestion des sites et monuments historiques et des attractions touristiques similaires'
        ),
    ),
    (
        '9103Z',
        _(
            'Gestion des sites et monuments historiques et des attractions touristiques similaires'
        ),
    ),
    (
        '9104',
        _(
            'Gestion des jardins botaniques et zoologiques et des réserves naturelles'
        ),
    ),
    (
        '9104Z',
        _(
            'Gestion des jardins botaniques et zoologiques et des réserves naturelles'
        ),
    ),
    ('92', _("Organisation de jeux de hasard et d'argent")),
    ('920', _("Organisation de jeux de hasard et d'argent")),
    ('9200', _("Organisation de jeux de hasard et d'argent")),
    ('9200Z', _("Organisation de jeux de hasard et d'argent")),
    ('93', _('Activités sportives, récréatives et de loisirs')),
    ('931', _('Activités liées au sport')),
    ('9311', _("Gestion d'installations sportives")),
    ('9311Z', _("Gestion d'installations sportives")),
    ('9312', _('Activités de clubs de sports')),
    ('9312Z', _('Activités de clubs de sports')),
    ('9313', _('Activités des centres de culture physique')),
    ('9313Z', _('Activités des centres de culture physique')),
    ('9319', _('Autres activités liées au sport')),
    ('9319Z', _('Autres activités liées au sport')),
    ('932', _('Activités récréatives et de loisirs')),
    ('9321', _("Activités des parcs d'attractions et parcs à thèmes")),
    ('9321Z', _("Activités des parcs d'attractions et parcs à thèmes")),
    ('9329', _('Autres activités récréatives et de loisirs ')),
    ('9329Z', _('Autres activités récréatives et de loisirs')),
    ('94', _('Activités des organisations associatives')),
    (
        '941',
        _(
            'Activités des organisations économiques, patronales et professionnelles'
        ),
    ),
    ('9411', _('Activités des organisations patronales et consulaires')),
    ('9411Z', _('Activités des organisations patronales et consulaires')),
    ('9412', _('Activités des organisations professionnelles')),
    ('9412Z', _('Activités des organisations professionnelles')),
    ('942', _('Activités des syndicats de salariés')),
    ('9420', _('Activités des syndicats de salariés')),
    ('9420Z', _('Activités des syndicats de salariés')),
    ('949', _('Activités des autres organisations associatives')),
    ('9491', _('Activités des organisations religieuses')),
    ('9491Z', _('Activités des organisations religieuses')),
    ('9492', _('Activités des organisations politiques')),
    ('9492Z', _('Activités des organisations politiques')),
    ('9499', _('Activités des organisations associatives n.c.a.')),
    ('9499Z', _('Autres organisations fonctionnant par adhésion volontaire')),
    ('95', _("Réparation d'ordinateurs et de biens personnels et domestiques")),
    ('951', _("Réparation d'ordinateurs et d'équipements de communication ")),
    ('9511', _("Réparation d'ordinateurs et d'équipements périphériques")),
    ('9511Z', _("Réparation d'ordinateurs et d'équipements périphériques")),
    ('9512', _("Réparation d'équipements de communication")),
    ('9512Z', _("Réparation d'équipements de communication")),
    ('952', _('Réparation de biens personnels et domestiques')),
    ('9521', _('Réparation de produits électroniques grand public')),
    ('9521Z', _('Réparation de produits électroniques grand public')),
    (
        '9522',
        _(
            "Réparation d'appareils électroménagers et d'équipements pour la maison et le jardin"
        ),
    ),
    (
        '9522Z',
        _(
            "Réparation d'appareils électroménagers et d'équipements pour la maison et le jardin"
        ),
    ),
    ('9523', _("Réparation de chaussures et d'articles en cuir")),
    ('9523Z', _("Réparation de chaussures et d'articles en cuir")),
    ('9524', _("Réparation de meubles et d'équipements du foyer")),
    ('9524Z', _("Réparation de meubles et d'équipements du foyer")),
    ('9525', _("Réparation d'articles d'horlogerie et de bijouterie")),
    ('9525Z', _("Réparation d'articles d'horlogerie et de bijouterie")),
    ('9529', _("Réparation d'autres biens personnels et domestiques")),
    ('9529Z', _("Réparation d'autres biens personnels et domestiques")),
    ('96', _('Autres services personnels')),
    ('960', _('Autres services personnels')),
    ('9601', _('Blanchisserie-teinturerie')),
    ('9601A', _('Blanchisserie-teinturerie de gros')),
    ('9601B', _('Blanchisserie-teinturerie de détail')),
    ('9602', _('Coiffure et soins de beauté')),
    ('9602A', _('Coiffure')),
    ('9602B', _('Soins de beauté')),
    ('9603', _('Services funéraires')),
    ('9603Z', _('Services funéraires')),
    ('9604', _('Entretien corporel')),
    ('9604Z', _('Entretien corporel')),
    ('9609', _('Autres services personnels n.c.a.')),
    ('9609Z', _('Autres services personnels n.c.a.')),
    (
        '97',
        _(
            "Activités des ménages en tant qu'employeurs de personnel domestique"
        ),
    ),
    (
        '970',
        _(
            "Activités des ménages en tant qu'employeurs de personnel domestique"
        ),
    ),
    (
        '9700',
        _(
            "Activités des ménages en tant qu'employeurs de personnel domestique"
        ),
    ),
    (
        '9700Z',
        _(
            "Activités des ménages en tant qu'employeurs de personnel domestique"
        ),
    ),
    (
        '98',
        _(
            'Activités indifférenciées des ménages en tant que producteurs de biens et services pour usage propre'
        ),
    ),
    (
        '981',
        _(
            'Activités indifférenciées des ménages en tant que producteurs de biens pour usage propre'
        ),
    ),
    (
        '9810',
        _(
            'Activités indifférenciées des ménages en tant que producteurs de biens pour usage propre'
        ),
    ),
    (
        '9810Z',
        _(
            'Activités indifférenciées des ménages en tant que producteurs de biens pour usage propre'
        ),
    ),
    (
        '982',
        _(
            'Activités indifférenciées des ménages en tant que producteurs de services pour usage propre'
        ),
    ),
    (
        '9820',
        _(
            'Activités indifférenciées des ménages en tant que producteurs de services pour usage propre'
        ),
    ),
    (
        '9820Z',
        _(
            'Activités indifférenciées des ménages en tant que producteurs de services pour usage propre'
        ),
    ),
    ('99', _('Activités des organisations et organismes extraterritoriaux')),
    ('990', _('Activités des organisations et organismes extraterritoriaux')),
    ('9900', _('Activités des organisations et organismes extraterritoriaux')),
    ('9900Z', _('Activités des organisations et organismes extraterritoriaux')),
)

ANNOUNCE = (
    ('1', _('EMISSIONS ET COTATIONS')),
    ('1.1', _('Valeurs françaises')),
    ('1.2', _('Valeurs étrangères')),
    ('2', _('AVIS DE CONVOCATION/AVIS DE REUNION')),
    ('3', _('DROITS DE VOTE')),
    ('4', _('PUBLICATIONS PERIODIQUES')),
    ('4.1', _('Comptes annuels')),
    ('4.2', _('Chiffres d’affaires et situations trimestrielles')),
    ('4.3', _('Comptes intermédiaires')),
    ('4.4', _('Entreprises d’assurances et organismes de retraites')),
    ('5', _('AUTRES OPERATIONS')),
    ('5.1', _('Réduction de capital')),
    ('5.2', _('Regroupement d’actions/d’obligations')),
    ('5.3', _('Offre de remboursement d’obligations')),
    (
        '5.4',
        _(
            'Décisions prises par des assemblées d’obligataires et homologation de résolutions'
        ),
    ),
    ('5.5', _('Désignation de teneurs de comptes de titres nominatifs')),
    ('5.6', _('Fusions et scissions')),
    ('5.7', _('Liquidations')),
    ('6', _('AVIS DIVERS')),
    ('7', _('BULLETIN OFFICIEL DE L’AMF')),
)
