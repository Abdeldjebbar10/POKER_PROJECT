import pytest
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PartieForm, VoteForm, ParticipantForm
from .models import Participant, Fonctionnalite, Partie

@pytest.mark.django_db
class TestPartieForm(TestCase):
    def setUp(self):
        self.admin = Participant.objects.create(pseudo="admin", est_admin=True)
        self.participant = Participant.objects.create(pseudo="player1", est_admin=False)

    def test_valid_partie_form(self):
        file_content = b'[{"name": "Feature1", "description": "Description of Feature1"}]'
        fonctionnalites_json = SimpleUploadedFile("fonctionnalites.json", file_content, content_type="application/json")

        form_data = {
            'nom': 'New Partie',
            'mode_jeu': 'strict',
            'administrateur': self.admin.id,
            'participants': [self.participant.id],
        }
        form_files = {
            'fonctionnalites_json': fonctionnalites_json
        }
        form = PartieForm(data=form_data, files=form_files)
        self.assertTrue(form.is_valid())

    def test_invalid_partie_form_with_invalid_json(self):
        invalid_json_file = SimpleUploadedFile("fonctionnalites.json", b'invalid json', content_type="application/json")

        form_data = {
            'nom': 'New Partie',
            'mode_jeu': 'strict',
            'administrateur': self.admin.id,
            'participants': [self.participant.id],
        }
        form_files = {
            'fonctionnalites_json': invalid_json_file
        }
        form = PartieForm(data=form_data, files=form_files)
        self.assertFalse(form.is_valid())
        self.assertIn('fonctionnalites_json', form.errors)

    def test_exclude_admin_from_participants(self):
        form_data = {
            'nom': 'New Partie',
            'mode_jeu': 'strict',
            'administrateur': self.admin.id,
            'participants': [self.admin.id],  # Admin should not be in participants
        }
        form = PartieForm(data=form_data)
        self.assertFalse(form.is_valid())

@pytest.mark.django_db
class TestVoteForm(TestCase):
    def setUp(self):
        self.fonctionnalite = Fonctionnalite.objects.create(
            name="Feature 1", description="A test feature"
        )

    def test_valid_vote_form(self):
        form_data = {
            'fonctionnalite': self.fonctionnalite.id,
            'vote': 5,  # Valid vote
        }
        form = VoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_vote_form(self):
        form_data = {
            'fonctionnalite': self.fonctionnalite.id,
            'vote': 20,  # Invalid vote (out of range)
        }
        form = VoteForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('vote', form.errors)

@pytest.mark.django_db
class TestParticipantForm(TestCase):
    def setUp(self):
        Participant.objects.create(pseudo="existing_user", est_admin=False)

    def test_valid_participant_form(self):
        form_data = {
            'pseudo': 'new_user',
            'est_admin': False,
        }
        form = ParticipantForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_duplicate_pseudo(self):
        form_data = {
            'pseudo': 'existing_user',  # Already exists
            'est_admin': False,
        }
        form = ParticipantForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('pseudo', form.errors)
