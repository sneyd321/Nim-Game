from Row import *
from Player import *

class Game:
    """Holds all objects related to the game, Error validation and user interface."""

    #Feild variables
    _rowList = []
    _row1 = Row("*", 1)
    _row2 = Row("*", 3)
    _row3 = Row("*", 5)
    _row4 = Row("*", 7)
    _player1 = Player()
    _player2 = Player()


    def __init__(self):
        """Initialze Fields"""
        _rowList = []
        self._row1 = Row("*", 1)
        self._row2 = Row("*", 3)
        self._row3 = Row("*", 5)
        self._row4 = Row("*", 7)
        #add rows ro row list
        self._rowList.append(self._row1)
        self._rowList.append(self._row2)
        self._rowList.append(self._row3)
        self._rowList.append(self._row4)
        self._player1 = Player()
        #Give player default name
        self._player1.setName("Player 1")
        self._player2 = Player()
        #Give player default name
        self._player2.setName("Player 2")

   
    def start(self):
        """Starts the game and prompts main menu"""
        while (True):
            #print menu
            print("Welcome to NIM\n\nMain Menu\n\n1.Start Game\n2.Options\n3.Exit\n")
            try:
                #prompt user
                option = int(input("Enter a number: "))
                #if user enters 1
                if option == 1:
                    #start the gamee
                    self.run()
                    while (True):
                        #if the user would like to play again
                        if (self.playAgain("Would you like to play again? Y/N: ")):
                            #rerun the game
                            self.run()
                        #otherwise 
                        else:
                            #end game
                            break
                #if user enteres 2
                elif option == 2:
                    #launch options menu
                    self.custimizeOptions()
                #if user enters 3
                elif option == 3:
                    #exit
                    break
                #if user enters anything else
                else:
                    print("Please enter a number between 1 and 3")
                    continue
                            
            except ValueError:
                print("Please enter a whole number.")
                continue

    def inputValidationForMenu(self, string):
        """validate values for options menu"""
        while (True):
            try:
                #promt user
                option = int(input(string))
                #if option is 1
                if option == 1:
                    #validate name entry
                    self.nameValidation(self._player1, "Enter name for " + self._player1.getName() + "\nType nothing and hit enter to escape.\n")
                    self.nameValidation(self._player2, "Enter name for " + self._player2.getName() + "\nType nothing and hit enter to escape.\n")
                #if option is 2
                elif option == 2:
                    #validate number of rows selcted
                    self.setNumberOfRows("Enter how many rows: ")
                #if option is 3
                elif option == 3:
                    #validate that the correct character is chosen
                    self.setCharacter("Enter a character: ")
                #if option is 4
                elif option == 4:
                    counter = 0
                    #for every row in list
                    for row in self._rowList:
                        #set counter to keep track of which row is being changed
                        counter += 1
                        #set size of row
                        row.setSize(self.setNumberOfCharacters("Enter the number of characters for each row: ", counter))
                #if option is 5
                elif option == 5:
                    break
                #otherwise
                else:
                    print("Please enter a number between 1 and 5")
                    continue
                       
            except ValueError:
                print("Please enter a whole number.")
                continue
   

    def nameValidation(self, player, string):
        """validate name entry from user"""
        while(True):
            try:
                #set name of player
                player.setName(input(string))
                #if name is blank exit
                if (len(player.getName()) == 0): 
                    player.setName("Player 1")
                    break
                #if name is bigger than 20 
                elif (len(player.getName()) > 20): 
                    print("Please enter a name with less than 20 characters.")
                    continue
                #if it works
                else:                   
                    break                      
            except ValueError:
                print("Please enter a whole number.")
                continue

    def setNumberOfRows(self, string):
        """validates user input for seleting the number of rows"""
        while(True):
            try:
                #Take input
                value = int(input(string))
                #if value is less than 4
                if value <= 4:
                    print("Default number of rows are 4. Please enter a number grater than 4")
                #otherwise
                else:
                    
                    for i in range(value - 4):
                        row = Row("*", 1)
                        self._rowList.append(row)  
                    print("Row successfuly added.")
                    break                      
            except ValueError:
                print("Please enter a whole number.")
                continue

    def setCharacter(self, string):
        """Validate user input for setting the type of character used in the game"""
        while(True):
            try:
                #take in input
                character = (input(string))
                #If the input is not a single character
                if (len(character) > 1 or len(character) <= 0): 
                    print("Please enter a single character.")     
                #Otherwise
                else:
                    #for each row
                    for row in self._rowList:
                        #change to the selected character
                        row.setCharacter(character)
                    print("Character changed to", self._rowList[0].getCharacter())
                    break                      
            except ValueError:
                print("Please enter a valid character.")
                continue

    def setNumberOfCharacters(self, string, counter):
        """Validate user input for the number of characters that appear in each row"""
        while(True):
            try:
                #Display row number
                print("Row", counter)
                #Check if input is a number
                value = int(input(string))
                #Check if number is not negetive or greater than 10
                if value <= 0 or value > 10:
                    print("Please enter a value between 1 and 10")
                    continue
                else:
                    return value                   
                
            except ValueError:
                print("Please enter a whole number.")
                continue

    def custimizeOptions(self):
        """Display options menu"""
        print("Options Menu\n")
        self.inputValidationForMenu("1. Set Player Name\n2. Set Number of Rows\n3. Set Character\n4. Set Number of Characters\n5. Exit\nEnter a number: ")


    def inputValidationforRow(self, string, player):
        """Validate user input for the player choosing a row"""
        while(True):
            try:
                #get input from player
                player.setRow(int(input(string)))
                #if the nuber is negative
                if (player.getRow() <= 0): 
                     print("Please enter a number greater than 0.")
                     continue
                #if input is greater than the number of available rows
                if (player.getRow() > len(self._rowList)):
                    print("Please enter a number less than", len(self._rowList), "\n")
                    continue
                #if input is an empty row 
                if self._rowList[player.getRow() - 1].isEmpty():
                    print("Empty Row. Enter another row.")
                    continue            
                break                      
            except ValueError:
                print("Please enter a whole number.\n")
                continue

    def inputValidationForSelection(self, string, player):    
        """Input validation for player choosing a number of charactes in a row"""
        while(True):
            try:
                #user input
                player.setNumberOfSymbols(int(input(string)))
                #If the player enters a negative number
                if (player.getNumberOfSymbols() <= 0): 
                     print("Please enter a number greater than 0.\n")
                     continue
                #if the player enters a valid number remove stick
                if (player.getNumberOfSymbols() <= self._rowList[player.getRow() - 1].getSize()):
                    self._rowList[player.getRow() - 1].removeItem(player.getNumberOfSymbols())
                #if the player enters a number greater than the available nuber of sticks
                else:
                    print("Please enter a number less than ", self._rowList[player.getRow() - 1].getSize())
                    continue
                break                      
            except ValueError:
                print("Please enter a whole number.")
                continue

    
    def playerMove(self, player):
        """Method that manages the players moves"""
        self.inputValidationforRow(player.getName() + " enter a row number: ", player)
        self.inputValidationForSelection(player.getName() + " enter how many symbols: ", player)
        #if the game is over
        if (self.determineWinner()):
            print(player.getName(), "loses")
            return True
        counter = 0
        print("\n")
        #Convert list to string for better UX
        for row in self._rowList:
            counter += 1
            print(str(counter) + ".", " ".join(row.getRow()))

    def determineWinner(self):
        """Method that determines the winner of the game"""
        counter = 0
        #if all rows are empty
        for row in self._rowList:
            if row.isEmpty():
                counter += 1
        if counter == len(self._rowList):
            return True
        else:
            return False

    def initRows(self):
        """Method that initializes all the rows"""
        try:
            counter = 0
            for row in self._rowList:
                row.getRow().remove("Empty")
                counter += 1
                print(str(counter) + ".", row.buildRow())
        except ValueError:
            for row in self._rowList:
                counter += 1
                print(str(counter) + ".", " ".join(row.buildRow()))

    def run(self):
        """Method that starts the game"""
        self.initRows()
    
        while True:
            if self.playerMove(self._player1):
                break
            if self.playerMove(self._player2):
                break
        

    def playAgain(self, string):
        """Method that resets the game"""
        while True:
            try:
                value = input(string)
                for i in value:
                    if ord(i) == 121 or ord(i) == 89:
                        return True
                    else:
                        return False
            except ValueError:
                continue