import os

def  show_menu():
    os.system ('cls')
    print("\nWelcome to Los Milagros Veterinary Clinic")
    print("1. Animal input")
    print("2. Animal output")
    print("3. Query animals")
    print("4. Exit")
def  animals_entry():
    global animals
    name = input("Enter the name of the animal: ")
    species = input("Enter the species of the animal: ")
    reason = input("Enter the reason for the query: ")
    animals[name] = {
        "species": species,
        "reason": reason
    }
    print(f"{name} has been registered in the office.")

def animals_output():
    global animals
    name = input("Enter the name of the animal to be output: ")
    if name in animals:
        del animals[name]
        print(f"{name} has left the office.")
    else:
        print(f"{name} is not in the office.")

def consult_animals():
    global animals
    if  animals:
        print("Animals in the office:")
        for name, details in animals.items():
            print(f"Name: {name}, Species: {details['species']}, Reason: {details['reason']}")
    else:
        print("There are no animals in the office.")
    input('<ENTER>')

animals = {}
while True:
    show_menu()
    option = input("Select an option: ")
    if option == "1":
        animals_entry()
    elif option == "2":
        animals_output()
    elif option == "3":
        consult_animals()
    elif option == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")
