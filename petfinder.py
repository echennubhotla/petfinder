#imports the different classes of pets
#created and csv

import dog
import cat
import fish
import bird
import csv

#this main function reads the file into the program and adds the object
#to a list. The list contains different types of pets, such as dogs, cats, fish, and bird

def main():

    list = []

    with open('pets.csv', 'r', newline='') as mycsvfile:

        thedatareader = csv.reader(mycsvfile, delimiter=',', quotechar = ',')

        for row in thedatareader:

            if 'Dog' == row[0]:
                writedog = dog.Dog(row[0],row[1], row[2], row[3], row[4])
                list.append(writedog)
            if 'Cat' == row[0]:
                writecat = cat.Cat(row[0], row[1], row[2], row[3], row[4])
                list.append(writecat)
            if 'Fish' == row[0]:
                writefish = fish.Fish(row[0], row[1], row[2], row[3], row[4])
                list.append(writefish)
            if 'Bird' == row[0]:
                writebird = bird.Bird(row[0], row[1], row[2], row[3], row[4])
                list.append(writebird)

    option = 0

    #this displays the menu until the user chooses to exit
    while option != 6:

        print("1. Print only the names of all the pets")
        print("2. Show only pets of a certain type")
        print("3. Search for a pet")
        print("4. Sort the list based on the pet name")
        print("5. Sort list based on pet color")
        print("6. Exit the program")

        option = float(input("Pick your option from 1-6: "))

        while option < 1 or option > 6:

            option = float(input("That was an incorrect option. Pick a valid option from 1-6: "))

        if option == 1:
            print(printnames(list))

        elif option == 2:
            petlist = []
            showpets(list,petlist)

            for item in petlist:
                print(item)

        elif option == 3:
            print(searchpets(list))

        elif option == 4:
           newlist = list
           sortname(list, newlist)

           for item in newlist:
                print(item)

        elif option == 5:
            newlist = list
            sortcolor(list,newlist)

            for item in newlist:
                print(item)
    else:
        exit(0)


#this function only prints the names of all the pets from the list of pets

def printnames(list):

    namelist = []

    for i in list:
        namelist.append(i.getName().strip())

    return namelist

#this function shows only the pets of a certain type

def showpets(list,petlist):

    for index in range(0, len(list)):
        currentvalue = list[index]

        position = index

        while position > -1 and list[position-1].getPettype().strip() > currentvalue.getPettype().strip():
            list[position] = list[position-1]
            position = position-1
        list[position] = currentvalue

    newlist = list

    targetvalue = input("What kind of pets are you looking for (Dog, Cat, Fish, or Bird)?: ")

    while targetvalue != 'Dog' and targetvalue != 'Cat' and targetvalue != 'Fish' and targetvalue != 'Bird':
        print("That is not a valid option")
        targetvalue = input("What kind of pets are you looking for(Dog, Cat ,Fish, or Bird)?: ")

    for i in list:
        types = i.getPettype().strip()
        if types == targetvalue:
            petlist.append(i)

    return petlist

#this function uses binary search to look for a certain pet. The function
#asks the user for the name of the pet and looks through the list and gets the
#information of the certain pet

def searchpets(list):

    for index in range(1, len(list)):
        currentvalue = list[index]

        position = index


        while position > 0 and list[position-1].getName().strip() > currentvalue.getName().strip():
            list[position] = list[position-1]
            position = position-1
        list[position] = currentvalue

    newlist = list

    min = 0
    max = len(list)-1
    targetvalue = input("What is the name of the pet that you are looking for?: ")
    guess = 0

    found = False

    while min <= max and not found:

        guess = int((min+max)/2)

        if list[guess].getName().strip() == targetvalue:
            found = True
            print(guess)
            return list[guess]


        elif list[guess].getName().strip() < targetvalue:
            min = guess + 1

        else:
            max = guess -1

    return ("There is no pet with that name in your list.")


#this function sorts the pets with insertion sort in alphabetical order by the pet's name

def sortname(list, newlist):

    for index in range(1, len(list)):
        currentvalue = list[index]

        position = index


        while position > 0 and list[position-1].getName().strip() > currentvalue.getName().strip():
            list[position] = list[position-1]
            position = position-1
        list[position] = currentvalue

    newlist = list
    return newlist

#this function sorts the pet with insertion sort in alphabetical order by the pet's color

def sortcolor(list,newlist):

    for index in range(1, len(list)):
        currentvalue = list[index]

        position = index

        while position > 0 and list[position-1].getColor().strip() > currentvalue.getColor().strip():
            list[position] = list[position-1]
            position = position-1
        list[position] = currentvalue

    newlist = list
    return newlist

#calls main
main()








