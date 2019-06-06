# Cuidadado!!
# [a.delete() for a in Election.objects.all()]
# [a.delete() for a in Area.objects.all()]

# from elections.models import Election

# distritos = [
#     u"Distrito Central",
#     u"Guatemala",
#     u"Sacatepéquez",
#     u"El Progreso",
#     u"Chimaltenango",
#     u"Escuintla",
#     u"Santa Rosa",
#     u"Sololá",
#     u"Totonicapán",
#     u"Quetzaltenango",
#     u"Suchitepéquez",
#     u"Retalhuleu",
#     u"San Marcos",
#     u"Huehuetenango",
#     u"Quiché",
#     u"Baja Verapaz",
#     u"Alta Verapaz",
#     u"Petén",
#     u"Izabal",
#     u"Zacapa",
#     u"Chiquimula",
#     u"Jalapa",
#     u"Jutiapa",
# ]

# guatemala, createdGuatemalaArea = Area.objects.get_or_create(name="Guatemala", identifier="GT", classification="country")
# for distrito in distritos:
#     try:
#         area, createdArea = Area.objects.get_or_create(
#             name=distrito,
#             classification='departamento',
#             parent=guatemala,
#             identifier=distrito.replace(" ", "")[:5])
#     except Exception as identifier:
#         print('Area')
#         print(distrito)
#         print(identifier)
#     try:
#         election, createdElection = Election.objects.get_or_create(name="Diputado distrito {}".format(distrito.encode('utf-8')), area=area)
#     except Exception as identifier:
#         print('Election')
#         print(distrito)
#         print(identifier)

municipios = Area.objects.filter(classification=u"municipio")

for municipio in municipios:
    municipioName = municipio.name
    try:
        election, createdElection = Election.objects.get_or_create(name="Alcadía {}".format(municipioName.encode('utf-8')), area=municipio)
    except Exception as identifier:
        print('Election')
        print(municipio)
        print(identifier)
