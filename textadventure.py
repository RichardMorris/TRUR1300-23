class Room:
    # constructor used to create the object​
    # first parameter is a reference to the current object
    # The second refers to the whole game, 
    # the third is a description of the room
    def __init__(self, game, descript): 
        self._game = game # a back reference to the whole game
        self._description = descript # description of the room

    # method run when we first enter a room
    # default implementation just prints the description
    def enter(self): 
        print(self._description)

    def processInput(self,command): # handle user input for this room
        pass # do nothing by default

#class RichRoom(Room):
#    def enter(self): # override the enter method from the parent class
#        super().enter()



# a subclass of Room, this has posible exits N S E W
# inherits all its methods and fields from Room
class RoomWithExits(Room): 
    def __init__(self, game, descript):
        super().__init__(game,descript) # call the constructor of the parent class
        self._north = None # possible exit to the north, set to nothing by default
        self._south = None

    def setNorth(self, room): # set the room to the north
        self._north = room

    def setSouth(self, room): # set the room to the south
        self._south = room

    def enter(self): # override the enter method from the parent class
        super().enter()
        if self._north != None:
            print("There is a door to the north.")
        if self._south != None:
            print("There is a door to the south.")

    def processInput(self,command): # override the processInput method from the parent class
        if command == "north" and self._north != None:
            self._game.moveToRoom(self._north)
        elif command == "south" and self._south != None:
            self._game.moveToRoom(self._south)
        else:
            super().processInput(command)
            
class Game: # represents the whole game
    # Constructor, sets up the game
    def __init__(self): 
        room1 = RoomWithExits(self,"A small room")
        room2 = RoomWithExits(self,"A large room")
        room3 = RoomWithExits(self,"A tiny room")
        room1.setNorth(room2)
        room2.setSouth(room1)
        room2.setNorth(room3)
        room3.setSouth(room2)
        self.rooms = [room1, room2]
        self.currentRoom = self.rooms[0]
        self.currentRoom.enter()

    # move to a new room
    def moveToRoom(self, room): 
        self.currentRoom = room
        self.currentRoom.enter()

    # Main game loop
    # repeatidly asks for input 
    # the input is then processed by the current room
    # typing exit allows the user to leave the game   
    def mainLoop(self): 
        while True:
            command = input("What do you want to do? ")
            if command == "exit":
                print("goodbye")
                break;
            self.currentRoom.processInput(command)

# entry point of the program
if __name__ == "__main__":
    app = Game()    # create a new game
    app.mainLoop()  # start the game loop
