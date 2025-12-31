# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(num1 + num2)
# name = "Oluwadarasimi"
# word = "d47451m1"
# username = input("Enter your name: ")
# if username == name:
#     password = input("Enter your password: ")
#     if password == word:
#         print("WELCOME TO KWASU PORTAL!")
#     else:
#         print("Wrong password")
# else:
#     print("Wrong username")
'''
print("WELCOME TO DARA'S RESTAURANT!\nWhat would you like to order?")
menu = "\n1. Rice and Beans with assorted meat\n2. Jollof rice and chicken\n3. Beans and plantain"
    
print("We serve " + menu)
order = int(input("Enter your order: "))
if order == 1:
    print("That will be #5000\nComing right up!")
elif order == 2:
    print("That's #7000\nYour plate of jollof rice will be ready soon ")
elif order == 3:
    print("That's #4000\nThe pate of beans will take a while please be patient")
else:
    print("Sorry we do not serve that\nThank you for dining with us")

'''
'''
import random

chealseascore = random.randint(0,5)
arsenalscore = random.randint(0,5)
print("CHE " + str(chealseascore) + "-" + str(arsenalscore) + " ARS")
if chealseascore > arsenalscore:
    print("Chelsea wins!")
elif chealseascore == arsenalscore:
    print("It's a draw")
else:
    print("Arsenal wins!")'
'''
'''
food = ["Beans", "Rice", "Bread", "Yam", "Amala"]
i = 0
lengthoffoods = len(food)
foodstr = ""
print("we offer:" , foodstr, end = "")
while lengthoffoods > 0:
    foodstr += food[i]
    if food[i] != food[4] :
        foodstr += ","
    i += 1
    lengthoffoods -= 1
print(foodstr)
'''
'''
#write a function to create a note
def create_note():
    title = input("Enter the title of your note: ")
    content = input("Enter your content:\n ")
    filename = f"{title}.txt"
    with open(filename, "w") as file:
        file.write(content)
    
    print("\nYour note " + title + "has been saved successfully as " + filename + ".")
create_note()
'''
