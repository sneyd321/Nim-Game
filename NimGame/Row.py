class Row:
    """description of class"""

    _row = []
    _character = ""
    _size = 0

    def __init__(self, character, size):
        self._character = character
        self._size = size
        self._row = []
        
    def getCharacter(self):
        return self._character

    def setCharacter(self, value):
        self._character = value

    def getSize(self):
        return self._size

    def setSize(self, value):
        self._size = value


    def getRow(self):
        return self._row

    def buildRow(self):
        """Builds the rows"""
        for i in range(0, self._size):
            self._row.append(self._character)
        return self._row


    def removeItem(self, input):
        """Removes items from row"""
        for i in range(input):
            self._row.remove(self._character)
            if not self._row:
                self._row.append("Empty")
        return self._row

    def isEmpty(self):
        """Checks if the rows are empty"""
        if self._row[0] == "Empty":
            return True

    