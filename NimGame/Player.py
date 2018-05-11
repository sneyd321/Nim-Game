class Player:
    """description of class"""

    _rowSelected = 0
    _numberOfSymbols = 0
    _name = ""

    def __init__(self):
        self._rowSelected = 0
        self._numberOfSymbols = 0
        self._name = ""

    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    def setNumberOfSymbols(self, value):
        self._numberOfSymbols = value
    
    def getNumberOfSymbols(self):
        return self._numberOfSymbols

    def setRow(self, value):
        self._rowSelected = value

    def getRow(self):
        return self._rowSelected

