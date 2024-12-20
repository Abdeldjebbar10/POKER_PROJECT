from django.test import TestCase
from django.conf import settings
from .models import Participant, Fonctionnalite, Partie, Vote
import os
import json

class ModelTestCase(TestCase):
    def setUp(self):
        # Set up data for the tests
        self.participant = Participant.objects.create(pseudo='JohnDoe', est_admin=True)
        self.fonctionnalite = Fonctionnalite.objects.create(
            name='Feature 1',
            description='A test feature',
            valide=True,
            difficulte=2.5
        )
        self.partie = Partie.objects.create(
            nom='Game Night',
            admin=self.participant,
            statut='new',
            mode_jeu='strict'
        )
        self.partie.participants.add(self.participant)
        self.partie.fonctionnalites.add(self.fonctionnalite)
        self.vote = Vote.objects.create(
            participant=self.participant,
            fonctionnalite=self.fonctionnalite,
            partie=self.partie,
            vote='5',
            mode_jeu='strict'
        )

    def test_participant_creation(self):
        self.assertEqual(self.participant.pseudo, 'JohnDoe')
        self.assertTrue(self.participant.est_admin)

    def test_fonctionnalite_creation(self):
        self.assertEqual(self.fonctionnalite.name, 'Feature 1')
        self.assertTrue(self.fonctionnalite.valide)

    def test_partie_creation(self):
        self.assertEqual(self.partie.nom, 'Game Night')
        self.assertEqual(self.partie.admin.pseudo, 'JohnDoe')

    def test_vote_creation(self):
        self.assertEqual(self.vote.vote, '5')
        self.assertEqual(self.vote.participant.pseudo, 'JohnDoe')
        self.assertEqual(self.vote.fonctionnalite.name, 'Feature 1')

    def test_sauvegarder_backlog(self):
        # Mock the opening and writing to a file
        path = self.partie.sauvegarder_backlog()
        expected_path = os.path.join(settings.BASE_DIR, 'static/data/backlog_valide.json')
        self.assertTrue(os.path.exists(path))
        # Ensure the file is written correctly
        with open(path, 'r') as file:
            data = json.load(file)
        self.assertIsInstance(data, list)
        self.assertNotEqual(len(data), 0)

    def test_calculer_moyenne_votes(self):
        votes = [Vote(vote=5, partie=self.partie, fonctionnalite=self.fonctionnalite) for _ in range(5)]
        moyenne = self.partie.calculer_moyenne_votes(votes)
        self.assertEqual(moyenne, 5.0)

    def test_sauvegarder_etat_partie(self):
        path = self.partie.sauvegarder_etat_partie()
        expected_path = os.path.join(settings.BASE_DIR, 'static/data/etat_partie.json')
        self.assertTrue(os.path.exists(path))
        # Check the file content
        with open(path, 'r') as file:
            data = json.load(file)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['partie'], self.partie.nom)
        self.assertIn('fonctionnalites', data)

