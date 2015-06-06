from django.test import TestCase

from .models import Player


class TestTalk(TestCase):

    def test_player_save(self):
        """
        Player can be created and loaded
        """
        p = Player.objects.create(name='James')

        self.assertEqual(Player.objects.count(), 1)
        self.assertEqual(Player.objects.first().name, 'James')
