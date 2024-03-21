import unittest
import io
import contextlib
import sys
from unittest.mock import Mock

from textadventure import *

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

class TestRoomWithExits(unittest.TestCase):
    def test_a_room_with_exits_can_be_created(self):
        room = RoomWithExits(None, "A small room")
        self.assertEqual("A small room", room._description)

    def test_a_room_with_exits_can_be_entered_and_prints_the_description(self):
        room = RoomWithExits(None, "A small room")
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.enter())
            self.assertTrue("A small room\n" in f.getvalue())

    def test_a_room_with_exits_processInput_does_nothing_by_default(self):
        room = RoomWithExits(None, "A small room")
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.processInput("anything"))
            self.assertTrue("" in f.getvalue())     

    def test_a_room_with_exits_can_have_north_and_south_exits(self):
        room = RoomWithExits(None, "A small room")
        room2 = RoomWithExits(None, "A large room")
        room.setNorth(room2)
        self.assertEqual(room2, room._north)
        self.assertEqual(None, room._south)
        room.setSouth(room2)
        self.assertEqual(room2, room._south)

    def test_a_room_with_exits_can_be_entered_and_prints_the_description_and_exits(self):
        room = RoomWithExits(None, "A small room")
        room2 = RoomWithExits(None, "A large room")
        room.setNorth(room2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.enter())
            self.assertTrue("A small room\n" in f.getvalue())
            self.assertTrue("There is a door to the north.\n" in f.getvalue())  
        room.setSouth(room2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.enter())
            self.assertTrue("A small room\n" in f.getvalue())
            self.assertTrue("There is a door to the north.\n" in f.getvalue())  
            self.assertTrue("There is a door to the south.\n" in f.getvalue())

    def test_a_room_with_exits_processInput_can_move_to_north_and_south_exits(self):
        game = Game()
        room = RoomWithExits(game, "A small room")
        room2 = RoomWithExits(game, "A large room")
        room3 = RoomWithExits(game, "A third room")
        room.setNorth(room2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.processInput("north"))
            self.assertTrue("" in f.getvalue())     
        self.assertEqual(room2, room._game.currentRoom)
        room.setSouth(room3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.processInput("south"))
            self.assertTrue("" in f.getvalue()) 
        self.assertEqual(room3, room._game.currentRoom)

    def test_a_room_with_exits_processInput_does_nothing_if_no_exit(self):
        game = Game()
        room = RoomWithExits(game, "A small room")
        game.currentRoom = room
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.processInput("north"))
            self.assertTrue("" in f.getvalue())     
        self.assertEqual(room, room._game.currentRoom)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.processInput("south"))
            self.assertTrue("" in f.getvalue())     
        self.assertEqual(room, room._game.currentRoom)
    
    def test_a_room_with_exits_processInput_north_calls_Game_moveToRoom(self):
        game = Mock() # create a mock object that we can check was called
        room = RoomWithExits(game, "A small room")
        room2 = RoomWithExits(game, "A large room")
        room.setNorth(room2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.assertEqual(None, room.processInput("north"))
            game.moveToRoom.assert_called_with(room2) # check that the method was called with the correct parameter

class TestChest(unittest.TestCase):
    def test_chest_can_be_constructed_with_initial_start_state(self):
        chest = KnockThreeTimesChest()
        self.assertEqual(ChestState.START,chest.state)

    def test_chest_knocked_once_has_state_once(self):
        chest = KnockThreeTimesChest()
        chest.processInput("knock")
        self.assertEqual(ChestState.ONCE,chest.state)

    def test_chest_knocked_twice_has_state_twice(self):
        chest = KnockThreeTimesChest()
        chest.processInput("knock")
        chest.processInput("knock")
        self.assertEqual(ChestState.TWICE,chest.state)

    def test_chest_knocked_threetimes_has_state_thrice(self):
        chest = KnockThreeTimesChest()
        chest.processInput("knock")
        chest.processInput("knock")
        chest.processInput("knock")
        self.assertEqual(ChestState.THRICE,chest.state)
    
    def test_chest_stays_in_start_state_on_other_input(self):
        chest = KnockThreeTimesChest()
        chest.processInput("open")
        self.assertEqual(ChestState.START,chest.state)
    
    def test_chest_in_once_state_goes_back_to_start_state_on_other_input(self):
        chest = KnockThreeTimesChest()
        chest.processInput("knock")
        self.assertEqual(ChestState.ONCE,chest.state)
        chest.processInput("open")
        self.assertEqual(ChestState.START,chest.state)

    def test_chest_in_twice_state_goes_back_to_start_state_on_other_input(self):
        chest = KnockThreeTimesChest()
        chest.processInput("knock")
        chest.processInput("knock")
        self.assertEqual(ChestState.TWICE,chest.state) # check precondition
        chest.processInput("open")
        self.assertEqual(ChestState.START,chest.state)

    def test_chest_in_thrice_state_goes_back_to_start_state_on_other_input(self):
        chest = KnockThreeTimesChest()
        chest.processInput("knock")
        chest.processInput("knock")
        chest.processInput("knock")
        self.assertEqual(ChestState.THRICE,chest.state)
        chest.processInput("open")
        self.assertEqual(ChestState.START,chest.state)

class TestRoomWithChest(unittest.TestCase):
    def test_a_room_with_a_chest_can_be_constructed(self):
        room = RoomWithChest(None,"There is a chest")

    def test_a_room_with_a_chest_has_chest_state_start(self):
        room = RoomWithChest(None,"There is a chest")
        self.assertEqual(ChestState.START,room._chest.state)

    def test_a_room_with_a_chest_accepts_a_knock_setting_state_to_once(self):
        room = RoomWithChest(None,"There is a chest")
        room.processInput("knock")
        self.assertEqual(ChestState.ONCE,room._chest.state)



if __name__ == '__main__':
    unittest.main()