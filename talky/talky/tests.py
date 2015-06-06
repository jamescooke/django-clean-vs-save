from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from .models import Passport, Player


class TestTalk(TestCase):

    # `blank=False` is the default settings, but is not checked on DB or by
    # lots of functions in the system

    def test_blank_not_checked_by_managers(self):
        """
        Player manager will happily save players with no name
        """
        Player.objects.create()

        self.assertEqual(Player.objects.count(), 1)

    def test_blank_not_checked_by_save(self):
        """
        Player ``save`` happily saves without name as well
        """
        new_player = Player()

        new_player.save()

        self.assertEqual(Player.objects.count(), 1)

    def test_remember_to_use_full_clean(self):
        """
        Player should be run through ``full_clean`` to find these errors
        """
        new_player = Player()

        with self.assertRaises(ValidationError):
            new_player.full_clean()

    # Uniqueness is on DB and so much stronger - let's change the name to be
    # unique instead.

    def test_player_names_collide(self):
        """
        Uniqueness is tested at the database level so exceptions pop out fine
        """
        NewPlayer.objects.create(name='James')

        with self.assertRaises(IntegrityError):
            NewPlayer.objects.create(name='James')

    def test_passport_number_required(self):
        """
        And because it's unique it's also now required - it's been set as NOT
        NULL in the DB.
        """
        with self.assertRaises(IntegrityError):
            Passport.objects.create()
