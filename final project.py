import pandas as pd
import json
import os
from person_class import Person
from student_class import Student
from employee_class import Employee
from MENU_enum import Menu

try:
    def errorNumber(name_value, value):
        print("Error: " + name_value + " must be a number. " + value + " is not a number")

    def saveNewEntry(people_dict):
        type_input = input("for saving a student please press 1 \nfor saving a employee please press 2 \nfor saving a person please press 3: ")
        if (type_input != "1") and (type_input != "2") and (type_input != "3"):
            print("Option '" + type_input + "' does not exist. Please try again")
            return 0
        
        id_input = input("ID: ")
        if id_input.isdigit(): #check if id is a integer
            if id_input in people_dict:
                print("Error: ID already exists: " + str(people_dict[id_input]))
                return 0
        else:
            errorNumber("ID", id_input)
            return 0
        
        name_input = input("Name: ")
        age_input = input("Age: ")
        try:
            if type_input == "1":
                person = Student(id_input, name_input, age_input)
            elif type_input == "2":
                person = Employee(id_input, name_input, age_input)
            else:
                person = Person(id_input, name_input, age_input)
            people_dict[person.getId()] = person
            print("ID [" + str(person.getId()) + "] saved successfuly")
            return int(person.getAge())
        except:
            errorNumber("Age", age_input)
            return 0
        
            
    def searchByID(people_dict):
        id_search = input("Please enter the ID you want to look for: ")
        try:
            if id_search in people_dict:
                people_dict[id_search].printType()
                people_dict[id_search].printDetails()
            else:
                print("Error: ID " + id_search +" is not saved")
        except:
            errorNumber("ID", id_search)
            return

    def printAgesAverage(count, sum):
        if count == 0:
            print(count)
        else:
            result = sum / count
            print(result)

    def printAllNames(people_dict):
        for index, id in enumerate(people_dict):
            print(str(index) + ". " + people_dict[id].getName())

    def printAllIDs(people_dict):
        for index, id in enumerate(people_dict):
            print(str(index) + ". " + id)

    def printAllEntries(people_dict):
        for index, id in enumerate(people_dict):
            print(str(index) + ". ")
            people_dict[id].printType()
            people_dict[id].printMySelf()
            
    def printEntryByIndex(people_dict):
        search_index = input("Please enter the index of the entry you want to print: ")
        try:
            if int(search_index) < len(people_dict):
                for index, id in enumerate(people_dict):
                    if search_index == str(index):
                        people_dict[id].printType()
                        people_dict[id].printDetails()
                        break    
            elif len(people_dict) > 0:
                print("Error: Index out of range. The maximum index allowed is " + 
                        str(len(people_dict) - 1))
            else:
                print("Error: The dictionary is empty")
        except:
            errorNumber("index", search_index)

    def saveAllData(people_dict):
        file_name = input("What is your output file name? ")
        people_list = []
        for id in people_dict.keys():
            people_list.append(people_dict[id].getInfoDict())
        df = pd.DataFrame(people_list)
        close_file_flag = True
        while close_file_flag:
            try:
                df.to_csv("C:\\Users\\Tehila\\Desktop\\Easy High-Tech\\PYTHON\\3\\" + file_name + ".csv", index=False)
                print("The file " + file_name + " was saved successfully")
                close_file_flag = False
            except PermissionError:
                print("Error: The file '" + file_name + ".csv' is open")
                input_user = input("Please close the file and then press enter to continue")

    users_dict = {}
    user_choice = ""
    sum_ages = 0
    while True:
        flag_y = False
        flag_n = False
        for option in Menu:
            print("To " + option.name + " please press " + str(option.value))
        user_choice = input("Please enter your choice: ")
        try:
            user_choice = Menu(int(user_choice))
        except:
            print("Option [" + user_choice + "] does not exist. Please try again")  
            user_choice = input("Press Enter to continue ")
            continue
        
        if user_choice == Menu.SAVE_NEW_ENTRY:
            sum_ages += saveNewEntry(users_dict)
        elif user_choice == Menu.SEARCH_ENTRY_BY_ID:
            searchByID(users_dict)
        elif user_choice == Menu.PRINT_AVE_AGES:
            printAgesAverage(len(users_dict), sum_ages)
        elif user_choice == Menu.PRINT_NAMES:
            printAllNames(users_dict)
        elif user_choice == Menu.PRINT_IDS:
            printAllIDs(users_dict)
        elif user_choice == Menu.PRINT_ALL_ENTRIES:
            printAllEntries(users_dict)
        elif user_choice == Menu.PRINT_ENTRY_BY_INDEX:
            printEntryByIndex(users_dict)
        elif user_choice == Menu.SAVE_DATA:
            saveAllData(users_dict)
        elif user_choice == Menu.EXIT:
            while True:
                answer = input("Are you sure? (y/n) ")
                if answer == "y":
                    print("Goodbye!")
                    flag_y = True
                    break
                elif answer == "n":
                    flag_n = True
                    break  
            
        if flag_y: #if the user want to exit
            break
        if flag_n: #if the user want to stay
            continue
        
        user_choice = input("Press Enter to continue ")
except KeyboardInterrupt:
        print("\nError: KeyboardInterrupt")     