from unittest import TestCase

from constants import verse_one, verse_two, verse_99, verse_100
from song import Song


class TestSong(TestCase):

    def test_is_song_instance(self):
        song_object: Song = Song()
        self.assertIsInstance(song_object, Song)

    def test_get_verse_one(self):
        song: Song = Song()
        self.assertEqual(song.get_verse(1), verse_one)

    def test_get_verse_two(self):
        song: Song = Song()
        self.assertEqual(song.get_verse(2), verse_two)

    def test_get_verse_99(self):
        song: Song = Song()
        self.assertEqual(song.get_verse(99), verse_99)

    def test_get_verse_100(self):
        song: Song = Song()
        self.assertEqual(song.get_verse(100), verse_100)