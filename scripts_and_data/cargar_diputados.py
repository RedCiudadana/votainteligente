import csv

from elections.models import Candidate, Election, PersonalData, Area

from backend_candidate.models import CandidacyContact
from backend_candidate.models import send_mail_with_user_and_password
from backend_candidate.send_mails_to_candidates import send_user_to_candidates

from votai_utils.send_mails import validateEmail

reader = csv.DictReader(open('scripts_and_data/8may.csv'))

counter = 0

for info_diputado in reader:
    diputado, isCreated = Candidate.objects.get_or_create(name=unicode(info_diputado['NOMBRE'], 'utf-8'))
    # print(diputado)
    partido = info_diputado['PARTIDO']
    # print(partido)
    if partido:
        PersonalData.objects.get_or_create(candidate=diputado, label=u'Partido', value=partido)
    
    email = unicode(info_diputado['CORREO ELECTRÓNICO'], 'utf-8')
    if email and validateEmail(email):
        contacto, isCreated = CandidacyContact.objects.get_or_create(candidate=diputado, mail=email)
        if not isCreated:
            contacto.send_mail_with_user_and_password()


    counter += 1
    send_candidate_username_and_password(diputado)
    if not counter % 5:
        print(counter)
