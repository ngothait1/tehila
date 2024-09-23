def errorNumber(name_value, value):
    print("Error: " + name_value + " must be a number. " + value + " is not a number")

def SavenewEntry(dict1):
    id_input = input("ID: ")
    if id_input.isdigit():
        if id_input in dict1:
            print("Error: ID already exists: " + str(dict1[id_input]))
            return 0
    else:
        errorNumber("ID", id_input)
        return 0
    
    name_input = input("Name: ")
    age_input = input("Age: ")
    if age_input.isdigit() == False:
        errorNumber("Age", age_input)
        return 0
    
    dict1[id_input] = {"name": name_input, "age": age_input}
    print("ID [" + str(id_input) + "] saved successfuly")
    return float(age_input)

def searchByID(dict1):
    id_search = input("Please enter the ID you want to look for: ")
    if id_search.isdigit():
        if id_search in dict1:
            print("ID: " + id_search)
            print("Name: " + dict1[id_search]["name"])
            print("Age: " + dict1[id_search]["age"])
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

def printAllNames(dict1):
    for index, id in enumerate(dict1):
        print(str(index) + ". " + dict1[id]["name"])

def printAllIDs(dict1):
    for index, id in enumerate(dict1):
        print(str(index) + ". " + id)

def printAllEntries(dict1):
    for index, id in enumerate(dict1):
        print(str(index) + ". " + id)
        print("    Name: " + dict1[id]["name"])
        print("    Age: " + dict1[id]["age"])

def printEntryByIndex(dict1):
    search_index = input("Please enter the index of the entry you want to print: ")
    if search_index.isdigit():
        for index, id in enumerate(dict1):
            if search_index == str(index):
                print("ID: " + id)
                print("Name: " + dict1[id]["name"])
                print("Age: " + dict1[id]["age"])
            else:
                print("Error: Index out of range. The maximum index allowed is " + 
                       str(len(dict1)-1))
    else:
        errorNumber("index", search_index)


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
    print("8. Exit")
    user_choice = input("Please enter your choice: ")

    if user_choice == "1":
        sum_ages += SavenewEntry(users_dict)
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
        
