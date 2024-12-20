from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Partie, Participant, Fonctionnalite

class PartieTests(TestCase):
    def setUp(self):
        self.joueur = Participant.objects.create(pseudo='Alice', est_admin=False)
        self.admin = Participant.objects.create(pseudo='Admin', est_admin=True)
        self.partie = Partie.objects.create(nom='Test Partie', admin=self.admin)
        self.partie.participants.add(self.joueur)
        self.fonctionnalite_data = [
            {"name": "Authentification", "description": "Se connecter avec email et mot de passe"},
            {"name": "Création de profil", "description": "Créer et modifier un profil utilisateur"}
        ]
        for data in self.fonctionnalite_data:
            Fonctionnalite.objects.create(**data)

    # def test_creation_partie(self):
    #     """Test de la création de partie et de l'ajout de participants"""
    #     response = self.client.get(reverse('lister_parties'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Test Partie')
