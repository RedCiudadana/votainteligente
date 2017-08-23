# coding=utf-8
from elections.tests import VotaInteligenteTestCase as TestCase
from django.test import override_settings
from elections.models import Candidate
from backend_candidate.forms import get_candidate_profile_form_class
from backend_candidate.models import Candidacy
from django.contrib.auth.models import User
from elections.models import PersonalData, Election
from django.template import Template, Context
from django.core.urlresolvers import reverse
from backend_candidate.forms import get_candidate_profile_form_class
from popolo.models import ContactDetail
import datetime
from django.utils import timezone


class AgendaViewTestCase(TestCase):
    def setUp(self):
        self.feli = User.objects.get(username='feli')
        self.feli.set_password('alvarez')
        self.feli.save()
        self.candidate = Candidate.objects.get(pk=1)
        self.candidacy = Candidacy.objects.create(user=self.feli,
                                                  candidate=self.candidate)

    def test_get_create_an_activity_from_view(self):
        url = reverse('backend_candidate:add_activity', kwargs={'slug': self.candidate.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
        
        not_the_right_candidate = Candidate.objects.create(name='Not the right candidate')
        self.client.login(username=self.feli,
                          password='alvarez')
        not_the_right_url = reverse('backend_candidate:add_activity',
                                    kwargs={'slug': not_the_right_candidate.pk})
        response = self.client.get(not_the_right_url)
        self.assertEquals(response.status_code, 404)
        
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend_candidate/add_activity.html')
        
    def test_posting_to_create_an_activity(self):
        url = reverse('backend_candidate:add_activity', kwargs={'slug': self.candidate.pk})
        self.client.login(username=self.feli,
                          password='alvarez')
        tomorrow = timezone.now() + datetime.timedelta(days=1)
        ## '%Y-%m-%d %H:%M:%S'
        data = {
            'date': tomorrow.strftime('%Y-%m-%d %H:%M:%S'),
            'url': 'https://perrito.cl/actividad_secreta',
            'description': 'This is a description',
            'location': 'secret location'
        }
        response = self.client.post(url, data=data)
        url_complete_profile = reverse('backend_candidate:complete_profile',
                                       kwargs={'slug': self.candidate.election.slug,
                                               'candidate_id': self.candidate.id})
        self.assertRedirects(response, url_complete_profile)
        self.assertTrue(self.candidate.agenda.all())