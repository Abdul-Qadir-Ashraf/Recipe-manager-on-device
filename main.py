import os
from pathlib import Path
from os import system
from os import system



home = os.getcwd()
recipe_directory = Path("C:/Users/qadir/OneDrive/Desktop/Recipes")


def counting():
    count = 0
    for j in os.listdir(Path('C:/Users/qadir/OneDrive/Desktop/Recipes')):
        for i in os.listdir(Path('C:/Users/qadir/OneDrive/Desktop/Recipes') / j):
            count += 1
    return count


def welcome(count):
    system('cls')
    return f'Welcome User,\nThere are total {count} recipes for you.\nThe path to the recipes is: {recipe_directory}\n'

def options():
    print('Choose from the following options:')
    print("1. Read Recipe\n2. Create Recipe\n3. Create Category\n4. Delete Recipe\n5. Delete Category\n6. End Program")
    valid = False
    while not valid:
        try:
            option = int(input("Choose from the above options: "))
            system('cls')
            if option in range(1,7):
                return option
            else:
                continue
        except ValueError:
            continue

def selection1():
    valid = False
    while not valid:
        try:
            read_directory = os.listdir("C:/Users/qadir/OneDrive/Desktop/Recipes")
            read_list = []
            read_list2 = []
            r = 0
            for i in read_directory:
                r+=1
                read_list2.append(i)
                read_list.append(str(r)+'. '+i)
            read_list.append(str(r+1)+'. Return to the main menu')
            print("Which category recipe do you want to read?")
            print(read_list)
            select = int(input(': '))
            system('cls')
            if select in range(1,r+2):
                if select==r+1:
                    return 1
                else:
                    readrecipe = Path("C:\\Users\\qadir\\OneDrive\\Desktop\\Recipes")/read_list2[select-1]
                    helo = os.listdir(readrecipe)
                    mylist = []
                    mylist2 = []
                    n=0
                    for i in helo:
                        n+=1
                        direct= Path(readrecipe/i).stem
                        mylist.append(str(n)+'. '+direct)
                        mylist2.append(i)
                    mylist.append(str(n+1)+'. Back to the previous menu')
                    if len(os.listdir(readrecipe))==0:
                        print("No recipes to read here! Try again.\n")
                        continue
                    else:
                        print(f"Select from the recipes available in {read_list2[select-1]} \n {mylist}")
                    recipes= 0
                    recipes1=len(os.listdir(readrecipe))+2
                    while recipes not in range(1,recipes1):
                        try:
                            recipes= int(input(": "))
                            if recipes == recipes1-1:
                                system('cls')
                                continue
                            elif recipes not in range(1,recipes1):
                                continue
                            else:
                                readrecipefinal = Path(readrecipe)/mylist2[recipes-1]
                                if  os.path.getsize(readrecipefinal)==0:
                                    print('Oops! The Recipe is empty.\n')
                                    print('\n')
                                    return True
                                else:
                                    system('cls')
                                    print(f'Your recipes is:\n"{readrecipefinal.read_text()}"')
                                    return True
                        except ValueError:
                            continue
            else:
                continue
        except ValueError:
            continue

def selection2(recipe):
    print("Which category do you choose?")
    valid = False
    while not valid:
        try:
            read_directory = os.listdir("C:/Users/qadir/OneDrive/Desktop/Recipes")
            read_list = []
            read_list2 = []
            r = 0
            for i in read_directory:
                r += 1
                read_list2.append(i)
                read_list.append(str(r) + '. ' + i)
            read_list.append(str(r + 1) + '. Return to the main menu')
            print(read_list)
            select = int(input(': '))
            dictionary = {1:'Dessert',2:'Meat',3:'Pasta',4:'Salad',5:'True'}
            if select in range(1, r+2):
                if select == r+1:
                    return False
                else:
                    system('cls')
                    name = input("Enter the name of the dish for which you want to create the recipe: ")
                    readrecipe = Path("C:\\Users\\qadir\\OneDrive\\Desktop\\Recipes") / read_list2[select-1]
                    os.chdir(readrecipe)
                    new_data = open(name,'a')
                    my_data = input('Enter your recipe below:\n')
                    new_data.writelines(my_data)
                    new_data.close()
                    os.chdir(home)
                    print("\n Congratulations Your recipe has been saved!")
                    return False
            else:
                continue
        except ValueError:
            continue

def selection3():
    new_category = input("Enter the category you want to create \tor\t Enter \'1\' to return to the previous option\n:")
    if int(new_category) ==1:
       return False
    else:
        os.mkdir(recipe_directory/new_category)
        print('\n')
        print("Congratulations '"+new_category+"' category has been created!")

def selection4(recipe):
    print("Which category do you choose?")
    valid = False
    while not valid:
        try:
            m = 0
            listing = []
            directories = os.listdir("C:/Users/qadir/OneDrive/Desktop/Recipes")
            for i in directories:
                m += 1
                print(str(m) + '. ' + i)
                listing.append(i)
            print(str(m + 1) + '. Return to previous menu')
            select = int(input(': '))
            if select in range(1, m + 2):
                if select == m + 1:
                    valid = True
                else:
                    readrecipe = Path("C:\\Users\\qadir\\OneDrive\\Desktop\\Recipes") / listing[select - 1]
                    helo = os.listdir(readrecipe)
                    mylist = []
                    mylist2 = []
                    n = 0
                    for i in helo:
                        n += 1
                        direct = Path(readrecipe / i).stem
                        mylist.append(str(n) + '. ' + direct)
                        mylist2.append(i)
                    mylist.append(str(n + 1) + '. Back to the main menu')
                    if len(os.listdir(readrecipe)) == 0:
                        system('cls')
                        print('No recipes to delete here!\nPlease Select again:')
                        continue
                    else:
                        print(f"Select from the recipes available from {listing[select - 1]} \n {mylist}")
                    recipes = 0
                    while recipes not in range(1, n + 2):
                        try:
                            recipes = int(input(": "))
                            if recipes == n + 1:
                                return False
                            else:
                                readrecipefinal = Path(readrecipe) / mylist2[recipes - 1]
                                os.remove(readrecipefinal)
                                print(f'The recipes "{Path(readrecipefinal).stem}" has been removed!')
                                return True
                        except ValueError:
                            continue
            else:
                continue
        except ValueError:
            continue

def selection5():
    valid1 = False
    while not valid1:
        try:
            jello = os.listdir(Path(recipe_directory))
            deletelist= []
            deletelist2=[]
            n = 0
            for i in jello:
                n+=1
                deletelist.append(i)
                deletelist2.append(str(n)+'. '+i)
            deletelist2.append(str(n+1)+". "+"Return to the main menu")
            print(deletelist2)
            category_del = int(input(f'Enter the category number you want to delete:\n'))
            if category_del == n+1:
                return False
            else:
                os.rmdir(Path(recipe_directory)/deletelist[category_del-1])
                print(f"The Category '{deletelist[category_del-1]}' has been deleted!")
                return True
        except ValueError:
            continue

def selection6(program):
    program = True

def repititon():
    valid = False
    while not valid:
        try:
            option = int(input("1. Return to the main menu\t2. End the program\n"))
            if option in range(1, 3):
                return option
            else:
                continue
        except ValueError:
            continue

program = False
while not program:
    count = counting()
    print(welcome(count))
    option = options()
    if option==1:
        what =selection1()
        repeat = repititon()
        if repeat ==2:
            program = True
        else:
            program = what
    elif option==2:
        repeat = repititon()
        if repeat ==2:
            program = True
        else:
            program = what
    elif option==3:
        repeat = repititon()
        if repeat ==2:
            program = True
        else:
            program = what
    elif option==4:
        repeat = repititon()
        if repeat ==2:
            program = True
        else:
            program = what
    elif option==5:
        repeat = repititon()
        if repeat ==2:
            program = True
        else:
            program = what
    elif option==6:
        print('Good Bye!')
        program=True
