import time

print("Hello, This is the final project")
user_name = input("What is your name? ")
print("Hi " + user_name + " nice to meet you")
print("This is a special calculator, I would need two numbers from you")
first_num = int(input("First number "))
second_num = int(input("Second number "))
print("Thank you for putting in your numbers, " + str(first_num) + " and " + str(second_num))

#defule: number's types =odd
type_first_num ="odd"
type_second_num ="odd"

#recognaze if the numbers are odd or even:
if first_num % 2 == 0:
    type_first_num = "even"
if second_num % 2 == 0:
    type_second_num = "even"

flag = True #A flag variable if the user selected "/" and the second number is zero

print("I can see thet the first number is " + type_first_num)
print("And the second is " + type_second_num)

if (type_first_num=="even" and type_second_num=="even") or (type_first_num=="odd" and type_second_num=="odd"):
    print("So both of them are " + type_first_num)
else:
    print("So one of them is even, and one is odd")

operator = str(input("Operator (+, -, *, /): ")) #choosing operator

#checking if there is an error by choosing operator
if (operator != "+") and (operator != "-") and (operator != "*") and (operator != "/") : 
    print("Error: Operator " + operator + " is not supported")
    print("An error had occured, please try again")
else: #if there is no an error 
    if operator == "+" :
        sum = first_num + second_num

    elif operator == "-":
        sum = first_num - second_num

    elif operator == "*":
        sum = first_num * second_num

    else: # elif operator == "/":
        answer = input("You chose division, should the result be integer? (y/n) ") 
        if second_num == 0:
            print("Error: num_2 is zero")
            print("An error had occured, please try again")
            flag= False #flag updating
        else:   
            sum = first_num / second_num #if the user chose "n"
            if answer == "y": #if the user chose "y"
                sum = first_num // second_num
    if flag:
        #print the final calculation by the chosen operator
        print(str(first_num) + " " + operator + " " + str(second_num) + " = " + str(sum))

print("thank you for using the calculator on " + time.ctime())