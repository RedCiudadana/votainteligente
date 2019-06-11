# coding=utf-8
import unicodecsv as csv
import io
import codecs

from elections.models import Candidate, Election, PersonalData, Area

from backend_candidate.models import CandidacyContact
from backend_candidate.send_mails_to_candidates import send_user_to_candidates
from backend_candidate.models import send_candidate_username_and_password

from votai_utils.send_mails import validateEmail

reader = codecs.open('scripts_and_data/data/nuestraeleccion3.csv', 'r', encoding='utf-8')

for info_diputado in reader:
    info_diputado = info_diputado.split(u',')
    print(info_diputado)
    # Seleccionamos la elección a la cual pertenece este candidato
    try:
        election, created = Election.objects.get(name=info_diputado[2])
    except Exception as identifier:
        print(info_diputado[2])
        raise ValueError('Elección no encontrada {}'.format(info_diputado[2]))
    # Creamos candidato, o lo obtenemos por su nombre (posible conflicto con candidatos con el mismo nombre),
    # preferiblemente ser cuidadosos y utilizar "create".
    candidate, created = Candidate.objects.get_or_create(name=info_diputado[1])
    if created:
        election.candidates.add(candidate)
    # Verificamos si tiene partido, si es el caso, le asignamos ese partido
    partido = info_diputado[0]
    if partido:
        PersonalData.objects.get_or_create(candidate=candidate, label=u'Partido', value=partido)
    # Verificamos si tiene correo electrónico, si es el caso, le asignamos ese correo.
    email = info_diputado[5]
    print(email)
    if email:
        contacto, isCreated = CandidacyContact.objects.get_or_create(candidate=candidate, mail=email)
        # Si es nuevo contacto, nueva llave entre candidato y correo. * Pueden haber correos iguales para diferentes candidatos.
        if isCreated:
            send_candidate_username_and_password(candidate)

# [a.delete() for a in Candidate.objects.all()]
# [a.delete() for a in CandidacyContact.objects.all()]
