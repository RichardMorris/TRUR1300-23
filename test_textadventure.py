import unittest
import io
import contextlib
import sys

from textadventure import Room

class TestRoom(unittest.TestCase):
    def test_a_room_can_be_created(self):
        room = Room(None, "A small room")
        self.assertEqual("A small room", room._description)

    def test_a_room_can_be_entered_and_prints_the_description(self):
        room = Room(None, "A small room")
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.enter())
            self.assertTrue("A small room\n" in f.getvalue())

    def test_a_room_processInput_does_nothing_by_default(self):
        room = Room(None, "A small room")
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.processInput("anything"))
            self.assertTrue("" in f.getvalue())



if __name__ == '__main__':
    unittest.main()