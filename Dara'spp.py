animal = ["Dog", "Cat", "Bunny", "Snake", "Monkey"]
place = ["Kwara", "Abuja", "Lagos", "Benin", "Port.h"]
thing = ["Table", "Chair", "Vase", "Cup", "Door"] 

def noundet():
    Result = input("Enter noun: ")
    for ani in animal:
        if Result == ani:
            print(Result + " is an animal")
    for plac in place:
        if Result == plac:
            print(Result + " is a place")
    for th in thing:
        if Result == th:
            print(Result + " is a thing")
    else:
        print("Not available in database")

    
noundet()
