class Fish:

    def __init__(self, pettype, name, birthdate, type, color):
        self.__pettype = pettype
        self.__name = name
        self.__birthdate = birthdate
        self.__type = type
        self.__color = color

    def getPettype(self):
        return self.__pettype

    def getName(self):
        return self.__name

    def getBirthdate(self):
        return self.__birthdate

    def getType(self):
        return self.__type

    def getColor(self):
        return self.__color

    def setPettype(self):
        return self.__pettype

    def setName(self, name):
        self.__name = name

    def setBirthdate(self, birthdate):
        self.__birthdate = birthdate

    def setType(self, type):
        self.__type = type

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        outputstring = ""
        outputstring += "Pet Type: " + self.__pettype
        outputstring += " Name: " + self.__name
        outputstring += " Birthdate: " + self.__birthdate
        outputstring += " Type: " + self.__type
        outputstring += " Color: " + self.__color

        return outputstring
