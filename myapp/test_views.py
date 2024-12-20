from django.test import TestCase, Client
from django.urls import reverse
from .models import Participant, Partie, Fonctionnalite

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = Participant.objects.create(pseudo="admin", est_admin=True)
        self.participant = Participant.objects.create(pseudo="player1", est_admin=False)
        self.partie = Partie.objects.create(
            nom="Game Night",
            admin=self.admin,
            statut="new",
            mode_jeu="strict",
        )
        self.partie.participants.add(self.admin, self.participant)
        self.fonctionnalite = Fonctionnalite.objects.create(
            name="Feature 1",
            description="A test feature",
            valide=False,
        )
        self.partie.fonctionnalites.add(self.fonctionnalite)

    def test_liste_parties_view(self):
        response = self.client.get(reverse('lister_parties'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parties/liste_parties.html')
        self.assertContains(response, self.partie.nom)

    def test_creer_participant_view_get(self):
        response = self.client.get(reverse('creer_participant'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'participants/creer_participant.html')

    def test_creer_participant_view_post(self):
        form_data = {
            'pseudo': 'new_user',
            'est_admin': False,
        }
        response = self.client.post(reverse('creer_participant'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Participant.objects.filter(pseudo='new_user').exists())

    def test_liste_participants_view(self):
        response = self.client.get(reverse('lister_participants'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'participants/liste_participants.html')
        self.assertContains(response, self.participant.pseudo)
