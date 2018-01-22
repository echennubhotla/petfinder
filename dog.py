class Dog:

    def __init__(self, pettype, name, birthdate, breed, color):
        self.__pettype = pettype
        self.__name = name
        self.__birthdate = birthdate
        self.__breed = breed
        self.__color = color

    def getPettype(self):
        return self.__pettype

    def getName(self):
        return self.__name

    def getBirthdate(self):
        return self.__birthdate

    def getBreed(self):
        return self.__breed

    def getColor(self):
        return self.__color

    def setPettype(self):
        return self.__pettype

    def setName(self, name):
        self.__name = name

    def setBirthdate(self, birthdate):
        self.__birthdate = birthdate

    def setBreed(self,breed):
        self.__breed = breed

    def setColor(self,color):
        self.__color = color

    def __str__(self):
        outputstring = ""
        outputstring += "Pet type: " + self.__pettype
        outputstring += " Name: " + self.__name
        outputstring += " Birthdate: " + self.__birthdate
        outputstring += " Breed: " + self.__breed
        outputstring += " Color: " + self.__color

        return outputstring

