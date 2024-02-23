class Room:
    def __init__(self, descript,game): # constructor used to create the object​
        self._description = descript # private fields, prevent modification
        self._game = game # a back reference to the whole game

    def enter(self): # method run when we first enter a room
        print(self._description)


    def processInput(self,command): 
        pass

class Game: # represents the whole game

    def __init__(self):
        self.currentRoom = Room("The enterance to the world",self)
        self.currentRoom.enter()

    def mainLoop(self):
        while True:
            command = input("What do you want to do? ")
            if command == "exit":
                print("goodbye")
                break;
            self.currentRoom.processInput(command)


if __name__ == "__main__":
    app = Game()
    app.mainLoop()
