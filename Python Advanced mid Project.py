import os
import json
import pandas as pd

def menu():
    print("1. Save a new entry") 
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entrys")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")
    return input("Please enter you choice: ")

def checkFileExists(file_path):
    if not os.path.exists(file_path):
        print("Error: Config file conf.json is missing in path " + main_path)
        return False
    else:
        return True
    
def saveDataAsCsv(info_list, path, json_path):
    output_file = input("What is your output file name? ")
    if not checkFileExists(json_path):
        return False
    with open(json_path) as conf_file:
        columns_list = json.load(conf_file)
    column_1 = columns_list["id"]
    column_2 = columns_list["name"]
    column_3 = columns_list["age"]
    
    data = []
    for info in info_list:
        data.append({column_1: info[0], column_2: info[1], column_3: info[2]})
    
    csv_path = os.path.join(path, output_file)
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(csv_path, index=False)         

        
    
def validChoice(user_choice):
    if not user_choice.isdigit():
        return False
    user_choice = int(user_choice)
    
    if user_choice > 8:
        return False
    elif user_choice <= 0:
        return False
    else:
        return True

def exitConfirmation():
    while True:
        answer = input("Are you sure? (y/n)")
        if answer == "n":
            return False
        if answer == "y":
            return True

def getAgesSum(ages_list, current_sum):
    current_sum += int(ages_list[len(ages_list) - 1][2])
    return current_sum

def notNumError(user_input, key):
    print("Error: " + key + " must be a number. " + str(user_input) + " is not a number")

def saveNewEntry(info_dicsh, info_list): # 1
    id = input("ID: ")
    if id in info_dicsh:
        print("Error: ID already exists: " + str(info_dicsh[id]))
        return False
    
    if not id.isdigit():
        notNumError(id, "ID")
        return False
    
    name = input("Name: ")
    age = input("Age: ")

    if not age.isdigit():
        notNumError(age, "Age")
        return False
    
    person = [id, name, age]
    info_list.append(person)
    info_dicsh[id] = person
    print("ID [" + str(id) + "] saved successfuly")
    return True

def searchById(info_dicsh): #3
    id_to_search = input("Please enter the ID you want to look for: ")
    if not id_to_search.isdigit():
        notNumError(id_to_search, "ID")
        return 
        
    if id_to_search not in info_dicsh:
        print("ID " + id_to_search + " is not saved")
        return 
    else:
        printChosenEntry(info_dicsh, id_to_search)
        

def printChosenEntry(people_data, key):
    print("ID: " + str(people_data[key][0]))
    print("Name: " + str(people_data[key][1]))
    print("Age: " + str(people_data[key][2]))
    

def printAgesAvg(sum, people_amount):
    if people_amount == 0:
        ages_avg = 0
    else:
        ages_avg = sum / people_amount
    print(ages_avg)

def printAllNames(info_list):
    for idx, name in enumerate(info_list):
        print(str(idx) + ". " + name[1])

def printAllIds(info_list):
    for idx, id in enumerate(info_list):
        print(str(idx) + ". " + id[0])

def printAllEntrys(info_list):
    for idx, entry in enumerate(info_list):
        print(str(idx) + ". ")
        printChosenEntry(info_list, idx)

def printEntryByIndex(info_list):
    idx = input("Please enter the index of the entry you want to print: ")
    if not idx.isdigit():
        notNumError(idx, "Index")
        return
    idx = int(idx)
    if idx >= len(info_list):
        print("Error: Index out of range. the maximum index allowed is " + str(len(info_list) - 1))
        return
    printChosenEntry(info_list, idx)


id_list = []
id_dicsh ={}
ages_sum = 0
main_path = "C:\\Users\\treec\\Desktop\\forward\\Python\\projects\\advanced\\mid project"
conf_path = os.path.join(main_path, "conf.json")

while True:
    choice = menu()

    if not validChoice(choice):
        print("Error: Option [" + str(choice) + "] does not exist. Please try again")

    elif choice == "1":
        if saveNewEntry(id_dicsh, id_list):
            ages_sum = getAgesSum(id_list, ages_sum)

    elif choice == "2":
        searchById(id_dicsh)
  
    elif choice == "3":
        printAgesAvg(ages_sum, len(id_list))

    elif choice == "4":
        printAllNames(id_list)
    
    elif choice == "5":
        printAllIds(id_list)

    elif choice == "6":
        printAllEntrys(id_list)

    elif choice == "7":
        printEntryByIndex(id_list)

    elif choice == "8":
        saveDataAsCsv(id_list, main_path, conf_path)

    else: # "9"
        if exitConfirmation():
            print("Goodbye!")
            break

    input("Press Enter to continue ")