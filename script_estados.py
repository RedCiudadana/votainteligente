estados = [
 {"name": u"Distrito central (Ciudad de Guatemala)", "identifier": u"DIC"},
 {"name": u"Distrito de Guatemala (Municipios)", "identifier": u"DIM"},
 {"name": u"Sacatepéquez", "identifier": u"SAC"},
 {"name": u"El Progreso", "identifier": u"ELP"},
 {"name": u"Chimaltenango", "identifier": u"CHI"},
 {"name": u"Escuintla", "identifier": u"ESC"},
 {"name": u"Santa Rosa", "identifier": u"SAN"},
 {"name": u"Sololá", "identifier": u"SOL"},
 {"name": u"Totonicapán", "identifier": u"TOT"},
 {"name": u"Quetzaltenango", "identifier": u"QUE"},
 {"name": u"Suchitepéquez", "identifier": u"SUC"},
 {"name": u"Retalhuleu", "identifier": u"RET"},
 {"name": u"San Marcos", "identifier": u"SAN"},
 {"name": u"Huehuetenango", "identifier": u"HUE"},
 {"name": u"Quiché", "identifier": u"QUI"},
 {"name": u"Baja Verapaz", "identifier": u"BAJ"},
 {"name": u"Alta Verapaz", "identifier": u"ALT"},
 {"name": u"Petén", "identifier": u"PET"},
 {"name": u"Izabal", "identifier": u"IZA"},
 {"name": u"Zacapa", "identifier": u"ZAC"},
 {"name": u"Chiquimula", "identifier": u"CHI"},
 {"name": u"Jalapa", "identifier": u"JAL"},
 {"name": u"Jutiapa", "identifier": u"JUT"},
]

from elections.models import Topic, QuestionCategory

from elections.models import Area, Election
guatemala = Area.objects.create(name="Guatemala", identifier="GT", classification="country")

for e in estados:
    a, created = Area.objects.get_or_create(name=e['name'], identifier=e['identifier'], classification=u'state', parent=guatemala)
    position = 'Diputado ' + e['name']
    d_e, created = Election.objects.get_or_create(name=position, area=a, position="Diputado")

