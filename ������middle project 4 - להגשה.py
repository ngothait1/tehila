import pandas as pd
import json
import os
from person_file import Person
from student_class import Student
from employee_class import Employee

def errorNumber(name_value, value):
    print("Error: " + name_value + " must be a number. " + value + " is not a number")

def printDetails(id, name, age, space=""):
    print(space + "ID: " + id)
    print(space + "Name: " + name)
    print(space + "Age: " + age)

def saveNewEntry(people_dict):
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
    if age_input.isdigit() == False:
        errorNumber("Age", age_input)
        return 0
    
    type_input = input(name_input + " is a person/ student/ employee? ")
    if type_input == "student":
        field_of_study = input("Field of study: ")
        year_of_study = input("Year of study: ")
        score_avg = input("Score average: ")
        person = Student(id_input, name_input, age_input, field_of_study, year_of_study, score_avg)
    elif type_input == "employee":
        field_of_work = input("Field of work: ")
        salary = input("Salary: ")
        person = Employee(id_input, name_input, age_input, field_of_work, salary)
    else:
        person = Person(id_input, name_input, age_input)

    people_dict[person.getId()] = {"person": person}
    print("ID [" + str(person.getId()) + "] saved successfuly")
    return int(person.getAge())

def searchByID(people_dict):
    id_search = input("Please enter the ID you want to look for: ")
    if id_search.isdigit():
        if id_search in people_dict:
            printDetails(id_search, people_dict[id_search]["person"].getName(), people_dict[id_search]["person"].getAge())
        else:
            print("Error: ID " + id_search +" is not saved")
    else:
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
        print(str(index) + ". " + people_dict[id]["person"].getName())

def printAllIDs(people_dict):
    for index, id in enumerate(people_dict):
        print(str(index) + ". " + id)

def printAllEntries(people_dict):
    for index, id in enumerate(people_dict):
        print(str(index) + ". ")
        people_dict[id]["person"].printMySelf()
        people_dict[id]["person"].myFunc()

def printEntryByIndex(people_dict):
    search_index = input("Please enter the index of the entry you want to print: ")
    if search_index.isdigit():
        if int(search_index) < len(people_dict):
            for index, id in enumerate(people_dict):
                if search_index == str(index):
                    printDetails(id, people_dict[id]["person"].getName(), people_dict[id]["person"].getAge())
                    break    
        else:
            print("Error: Index out of range. The maximum index allowed is " + 
                    str(len(people_dict) - 1))
    else:
        errorNumber("index", search_index)

def saveAllData(people_dict):
    file_name = input("What is your output file name? ")
    path = "C:\\Users\\Tehila\\Desktop\\Easy High-Tech\\PYTHON\\3\\conf.json.json"
    if os.path.exists(path):
        df = pd.DataFrame.from_dict(people_dict, orient='index')
        df['id'] = df.index

        with open(path) as column_file:
            data = json.load(column_file)
        df = df[['id', 'name', 'age']]
        df.columns = data.values()
        df.to_csv("C:\\Users\\Tehila\\Desktop\\Easy High-Tech\\PYTHON\\3\\" + file_name + ".csv", index=False)
    else:
        print("Error: config file conf.json is missing in path " + os.getcwd())

users_dict = {}
user_choice = ""
sum_ages = 0
while True:
    flag_y = False
    flag_n = False
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")
    user_choice = input("Please enter your choice: ")

    if user_choice == "1":
        sum_ages += saveNewEntry(users_dict)
    elif user_choice == "2":
        searchByID(users_dict)
    elif user_choice == "3":
        printAgesAverage(len(users_dict), sum_ages)
    elif user_choice == "4":
        printAllNames(users_dict)
    elif user_choice == "5":
        printAllIDs(users_dict)
    elif user_choice == "6":
        printAllEntries(users_dict)
    elif user_choice == "7":
        printEntryByIndex(users_dict)
    elif user_choice == "8":
        saveAllData(users_dict)
    elif user_choice == "9":
        while True:
            answer = input("Are you sure? (y/n) ")
            if answer == "y":
                print("Goodbye!")
                flag_y = True
                break
            elif answer == "n":
                flag_n = True
                break        
    else:
        print("Option [" + user_choice + "] does not exist. Please try again")
        continue

    if flag_y: #if the user want to exit
        break
    if flag_n: #if the user want to stay
        continue

    user_choice = input("Press Enter to continue ")
        
