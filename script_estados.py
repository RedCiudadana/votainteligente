# -*- coding: utf-8 -*-

estados = [
 {"name":  u"Guatemala", "identifier":  u"DIC"},
 {"name":  u"Sacatepéquez", "identifier":  u"SAC"},
 {"name":  u"El Progreso", "identifier":  u"ELP"},
 {"name":  u"Chimaltenango", "identifier":  u"CHI"},
 {"name":  u"Escuintla", "identifier":  u"ESC"},
 {"name":  u"Santa Rosa", "identifier":  u"SAN"},
 {"name":  u"Sololá", "identifier":  u"SOL"},
 {"name":  u"Totonicapán", "identifier":  u"TOT"},
 {"name":  u"Quetzaltenango", "identifier":  u"QUE"},
 {"name":  u"Suchitepéquez", "identifier":  u"SUC"},
 {"name":  u"Retalhuleu", "identifier":  u"RET"},
 {"name":  u"San Marcos", "identifier":  u"SAN"},
 {"name":  u"Huehuetenango", "identifier":  u"HUE"},
 {"name":  u"Quiché", "identifier":  u"QUI"},
 {"name":  u"Baja Verapaz", "identifier":  u"BAJ"},
 {"name":  u"Alta Verapaz", "identifier":  u"ALT"},
 {"name":  u"Petén", "identifier":  u"PET"},
 {"name":  u"Izabal", "identifier":  u"IZA"},
 {"name":  u"Zacapa", "identifier":  u"ZAC"},
 {"name":  u"Chiquimula", "identifier":  u"CHI"},
 {"name":  u"Jalapa", "identifier":  u"JAL"},
 {"name":  u"Jutiapa", "identifier":  u"JUT"},
]

municipios = {'Alta Verapaz': [
    u'Chahal',
    u'Lanquín',
    u'San Juan Chamelco',
    u'Santa María Cahabón',
    u'Tucurú',
    u'Chisec',
    u'Panzós',
    u'San Pedro Carchá',
    u'Senahú',
    u'Cobán',
    u'Raxruhá',
    u'Santa Catalina La Tinta',
    u'Tactic',
    u'Fray Bartolomé de las Casas',
    u'San Cristóbal Verapaz',
    u'Santa Cruz Verapaz',
    u'Tamahú'],
  u'Baja Verapaz': [
    u'Cubulco',
    u'Salamá',
    u'Granados',
    u'San Jerónimo',
    u'Purulhá',
    u'San Miguel Chicaj',
    u'Rabinal',
    u'Santa Cruz el Chol'],
  u'Chimaltenango': [
    u'Acatenango',
    u'Patzicía',
    u'San José Poaquil',
    u'Santa Cruz Balanyá',
    u'Chimaltenango',
    u'Patzún',
    u'San Juan Comalapa',
    u'Tecpán',
    u'El Tejar',
    u'Pochuta',
    u'San Martín Jilotepeque',
    u'Yepocapa',
    u'Parramos',
    u'San Andrés Itzapa',
    u'Santa Apolonia',
    u'Zaragoza' ],
  u'Chiquimula': [
    u'Camotán',
    u'Ipala',
    u'San Jacinto',
    u'Chiquimula',
    u'Jocotán',
    u'San José La Arada',
    u'Concepción Las Minas',
    u'Olopa',
    u'San Juan Ermita',
    u'Esquipulas',
    u'Quezaltepeque'],
  u'El Progreso': [
    u'El Jícaro',
    u'San Antonio La Paz',
    u'Guastatoya',
    u'San Cristóbal Acasaguastlán',
    u'Morazán',
    u'Sanarate',
    u'San Agustín Acasaguastlán',
    u'Sansare'],
  u'Escuintla': [
    u'Escuintla',
    u'La Gomera',
    u'San José',
    u'Tiquisate',
    u'Guanagazapa',
    u'Masagua',
    u'San Vicente Pacaya',
    u'Iztapa',
    u'Nueva Concepción',
    u'Santa Lucía Cotzumalguapa',
    u'La Democracia',
    u'Palín',
    u'Siquinalá'],
  u'Guatemala': [
    u'Amatitlán',
    u'Guatemala',
    u'San José Pinula',
    u'San Pedro Sacatepéquez',
    u'Villa Nueva',
    u'Chinautla',
    u'Mixco',
    u'San Juan Sacatepéquez',
    u'San Raymundo',
    u'Chuarrancho',
    u'Palencia',
    u'San Miguel Petapa',
    u'Santa Catarina Pinula',
    u'Fraijanes',
    u'San José del Golfo',
    u'San Pedro Ayampuc',
    u'Villa Canales'],
  u'Huehuetenango': [
    u'Aguacatán',
    u'Cuilco',
    u'La Libertad',
    u'San Gaspar Ixchil',
    u'San Mateo Ixtatán',
    u'San Rafael La Independencia',
    u'Santa Ana Huista',
    u'Santiago Chimaltenango',
    u'Chiantla',
    u'Huehuetenango',
    u'Malacatancito',
    u'San Ildefonso Ixtahuacán',
    u'San Miguel Acatán',
    u'San Rafael Petzal',
    u'Santa Bárbara',
    u'Tectitán',
    u'Colotenango',
    u'Jacaltenango',
    u'Nentón',
    u'San Juan Atitán',
    u'San Pedro Necta',
    u'San Sebastián Coatán',
    u'Santa Cruz Barillas',
    u'Todos Santos Cuchumatánes',
    u'Concepción Huista',
    u'La Democracia',
    u'San Antonio Huista',
    u'San Juan Ixcoy',
    u'San Pedro Soloma',
    u'San Sebastián',
    u'Santa Eulalia',
    u'Unión Cantinil'],
  u'Izabal': [
    u'El Estor',
    u'Puerto Barrios',
    u'Livingston',
    u'Los Amates',
    u'Morales'],
  u'Jalapa': [
    u'Jalapa',
    u'San Luis Jilotepeque',
    u'Mataquescuintla',
    u'San Manuel Chaparrón',
    u'Monjas',
    u'San Pedro Pinula',
    u'San Carlos Alzatate'],
  u'Jutiapa': [
    u'Agua Blanca',
    u'Conguaco',
    u'Jerez',
    u'Quesada',
    u'Zapotitlán',
    u'Asunción Mita',
    u'El Adelanto',
    u'Jutiapa',
    u'San José Acatempa',
    u'Atescatempa',
    u'El Progreso',
    u'Moyuta',
    u'Santa Catarina Mita',
    u'Comapa',
    u'Jalpatagua',
    u'Pasaco',
    u'Yupiltepeque'],
  u'Petén': [
    u'Dolores',
    u'Melchor de Mencos',
    u'San Francisco',
    u'Sayaxché',
    u'Flores',
    u'Poptún',
    u'San José',
    u'La Libertad',
    u'San Andrés',
    u'San Luis',
    u'Las Cruces',
    u'San Benito',
    u'Santa Ana'],
  u'Quetzaltenango': [
    u'Almolonga',
    u'Coatepeque',
    u'Flores Costa Cuca',
    u'Olintepeque',
    u'San Carlos Sija',
    u'San Mateo',
    u'Cabricán',
    u'Colomba',
    u'Génova',
    u'Palestina de Los Altos',
    u'San Francisco La Unión',
    u'San Miguel Sigüilá',
    u'Cajolá',
    u'Concepción Chiquirichapa',
    u'Huitán',
    u'Quetzaltenango',
    u'San Juan Ostuncalco',
    u'Sibilia',
    u'Cantel',
    u'El Palmar',
    u'La Esperanza',
    u'Salcajá',
    u'San Martín Sacatepéquez',
    u'Zunil'],
  u'Quiché': [
    u'Canillá',
    u'Chichicastenango',
    u'Joyabaj',
    u'Sacapulas',
    u'San Juan Cotzal',
    u'Zacualpa',
    u'Chajul',
    u'Chinique',
    u'Nebaj',
    u'San Andrés Sajcabajá',
    u'San Pedro Jocopilas',
    u'Chicamán',
    u'Cunén',
    u'Pachalum',
    u'San Antonio Ilotenango',
    u'Santa Cruz del Quiché',
    u'Chiché',
    u'Ixcán',
    u'Patzité',
    u'San Bartolomé Jocotenango',
    u'Uspantán'],
  u'Retalhuleu': [
    u'Champerico',
    u'San Andrés Villa Seca',
    u'Santa Cruz Muluá',
    u'El Asintal',
    u'San Felipe',
    u'Nuevo San Carlos',
    u'San Martín Zapotitlán',
    u'Retalhuleu',
    u'San Sebastián'],
  u'Sacatepéquez': [
    u'Alotenango',
    u'Magdalena Milpas Altas',
    u'San Lucas Sacatepéquez',
    u'Santa María de Jesús',
    u'La Antigua Guatemala',
    u'Pastores',
    u'San Miguel Dueñas',
    u'Santiago Sacatepéquez',
    u'Ciudad Vieja',
    u'San Antonio Aguas Calientes',
    u'Santa Catarina Barahona',
    u'Santo Domingo Xenacoj',
    u'Jocotenango',
    u'San Bartolomé Milpas Altas',
    u'Santa Lucía Milpas Altas',
    u'Sumpango'],
  u'San Marcos': [
    u'Ayutla',
    u'El Quetzal',
    u'Ixchiguán',
    u'Ocós',
    u'San Cristóbal Cucho',
    u'San Miguel Ixtahuacán',
    u'Sibinal',
    u'Tejutla',
    u'Catarina',
    u'El Rodeo',
    u'La Reforma',
    u'Pajapita',
    u'San José Ojetenam',
    u'San Pablo',
    u'Sipacapa',
    u'Comitancillo',
    u'El Tumbador',
    u'Malacatán',
    u'Río Blanco',
    u'San Lorenzo',
    u'San Pedro Sacatepéquez',
    u'Tacaná',
    u'Concepción Tutuapa',
    u'Esquipulas Palo Gordo',
    u'Nuevo Progreso',
    u'San Antonio Sacatepéquez',
    u'San Marcos',
    u'San Rafael Pie de La Cuesta',
    u'Tajumulco'],
  u'Santa Rosa': [
    u'Barberena',
    u'Guazacapán',
    u'San Juan Tecuaco',
    u'Santa Rosa de Lima',
    u'Casillas',
    u'Nueva Santa Rosa',
    u'San Rafaél Las Flores',
    u'Taxisco',
    u'Chiquimulilla',
    u'Oratorio',
    u'Santa Cruz Naranjo',
    u'Cuilapa',
    u'Pueblo Nuevo Viñas',
    u'Santa María Ixhuatán'],
  u'Sololá': [
    u'Concepción',
    u'San Antonio Palopó',
    u'San Marcos La Laguna',
    u'Santa Catarina Palopó',
    u'Santa María Visitación',
    u'Nahualá',
    u'San José Chacayá',
    u'San Pablo La Laguna',
    u'Santa Clara La Laguna',
    u'Santiago Atitlán',
    u'Panajachel',
    u'San Juan La Laguna',
    u'San Pedro La Laguna',
    u'Santa Cruz La Laguna',
    u'Sololá',
    u'San Andrés Semetabaj',
    u'San Lucas Tolimán',
    u'Santa Catarina Ixtahuacan',
    u'Santa Lucía Utatlán'],
  u'Suchitepéquez': [
    u'Chicacao',
    u'Pueblo Nuevo',
    u'San Bernardino',
    u'San Juan Bautista',
    u'Santa Bárbara',
    u'Cuyotenango',
    u'Río Bravo',
    u'San Francisco Zapotitlán',
    u'San Lorenzo',
    u'Santo Domingo',
    u'Mazatenango',
    u'Samayac',
    u'San Gabriel',
    u'San Miguel Panán',
    u'Santo Tomás La Unión',
    u'Patulul',
    u'San Antonio',
    u'San José El Ídolo',
    u'San Pablo Jocopilas',
    u'Zunilito'],
  u'Totonicapán': [
    u'Momostenango',
    u'San Francisco El Alto',
    u'San Andrés Xecul',
    u'Santa Lucía La Reforma',
    u'San Bartolo',
    u'Santa María Chiquimula',
    u'San Cristóbal Totonicapán',
    u'Totonicapán'],
  u'Zacapa': [
    u'Cabañas',
    u'La Unión',
    u'Usumatlán',
    u'Estanzuela',
    u'Río Hondo',
    u'Zacapa',
    u'Gualán',
    u'San Diego',
    u'Huité',
    u'Teculután']
}

from elections.models import Topic, QuestionCategory

from elections.models import Area, Election
guatemala = Area.objects.get(name="Guatemala", identifier="GT", classification="country")

imposibles = []
for e in estados:
    # a, created = Area.objects.get_or_create(name=e['name'], identifier=e['identifier'], classification=u'state', parent=guatemala)
    # position = 'Diputado ' + e['name']
    # d_e, created = Election.objects.get_or_create(name=position, area=a, position="Diputado")
    print('\n' + e['name'] + '\n')
    _municipios = municipios[e['name']]
    for municipio in _municipios:
        name = e['name'] + ', '+ municipio
        print(name)
        print(municipio.replace(' ', '').replace(',','')[0:10:3])
        if len(name) < 35:
            Area.objects.get_or_create(name=name, identifier=municipio.replace(' ', '').replace(',','')[0:10:3], classification=u'municipio', parent=guatemala)
        else:
            imposibles.append(name)
    print(imposibles)

# Municipios que faltan
# [u'Sacatep\xe9quez, Magdalena Milpas Altas', u'Sacatep\xe9quez, San Lucas Sacatep\xe9quez', u'Sacatep\xe9quez, Santiago Sacatep\xe9quez', u'Sacatep\xe9quez, San Antonio Aguas Calientes', u'Sacatep\xe9quez, Santa Catarina Barahona', u'Sacatep\xe9quez, Santo Domingo Xenacoj', u'Sacatep\xe9quez, San Bartolom\xe9 Milpas Altas', u'Sacatep\xe9quez, Santa Luc\xeda Milpas Altas', u'El Progreso, San Crist\xf3bal Acasaguastl\xe1n', u'El Progreso, San Agust\xedn Acasaguastl\xe1n', u'Chimaltenango, San Mart\xedn Jilotepeque', u'Escuintla, Santa Luc\xeda Cotzumalguapa', u'Totonicap\xe1n, Santa Luc\xeda La Reforma', u'Totonicap\xe1n, Santa Mar\xeda Chiquimula', u'Totonicap\xe1n, San Crist\xf3bal Totonicap\xe1n', u'Quetzaltenango, Palestina de Los Altos', u'Quetzaltenango, San Francisco La Uni\xf3n', u'Quetzaltenango, Concepci\xf3n Chiquirichapa', u'Quetzaltenango, San Juan Ostuncalco', u'Quetzaltenango, San Mart\xedn Sacatep\xe9quez', u'Suchitep\xe9quez, San Francisco Zapotitl\xe1n', u'Suchitep\xe9quez, Santo Tom\xe1s La Uni\xf3n', u'San Marcos, San Antonio Sacatep\xe9quez', u'San Marcos, San Rafael Pie de La Cuesta', u'Huehuetenango, San Rafael La Independencia', u'Huehuetenango, Santiago Chimaltenango', u'Huehuetenango, San Ildefonso Ixtahuac\xe1n', u'Huehuetenango, San Sebasti\xe1n Coat\xe1n', u'Huehuetenango, Todos Santos Cuchumat\xe1nes', u'Alta Verapaz, Santa Catalina La Tinta', u'Alta Verapaz, Fray Bartolom\xe9 de las Casas', u'Alta Verapaz, San Crist\xf3bal Verapaz']
