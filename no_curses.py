import random
import os

os.system('CLS')

print("\nWelcome to the User Story Generator")

print("\nChose to generate either a random user story, ")
print("or create a custom user story in which you input")
print("the user role, functionality, and benefit.")
print("\nDon't worry, you can always create another random story,")
print("or you can edit any/all of your custom story!")

print("\nChoose an option below:")

print("1. Generate a random user story")

print("2. Generate a custom user story")

print("3. Enter q to quit.\n")

choice = input("Enter selection: ")

def random_story():
    #random_number = random.randint(0, 4)
    roles = ["user", "site visitor", "creator", "teacher", "student"]
    functionalities = ["edit", "save", "create", "read", "learn"]
    benefits = ["make money", "learn something new", "have fun", "go home", "take a vacation"]

    role = roles[random.randint(0, 4)]
    functionality = functionalities[random.randint(0, 4)]
    benefit = benefits[random.randint(0, 4)]

    story = "As a " + role + " I want to " + functionality + " so that I can " + benefit + "."

    return story

if choice == 'q' or choice == 'Q':
    pass
elif choice == "1":
    print("\nYou chose to generate a random story.")
    print("\nHere is your user story:\n")
    story = random_story()
    print(story)
    print("\nKeep story or generate another? Please make a selection.")
    print("\n1. Keep story")
    print("2. Generate new random story")
    keep_story = input("\nEnter selection: ")
    if keep_story == '1':
        print("\nYou chose to keep your user story.")
        print("\nThank you for using the user story generator. Goodbye.")
    else:
        story = random_story()
        print("\nHere is your new random story.\n")
        print(story)
        print("\nThank you for using the user story generator. Goodbye.")

else:
    print("\nYou chose to make a custom story.")
    part_one = input("\nWhat is your role (user, visitor, etc)? ")
    part_two = input("What functionality do you want (read, create, etc)? ")
    part_3 = input("What benefit do you want (edit, save, etc)? ")
    print("\nHere is your custom user story:")
    print("\nAs a " + part_one + " I want to " + part_two + " so that I can " + part_3 + ".")
    choice2 = input("\nKeep story (y or n)? ")

    if choice2 == 'y':
        print("\nThank you for using the user story generator. Goodbye.")
    else:
        print("\nWhich part would you like to edit? Please me a selection:")
        print("1. Role")
        print("2. Functionality")
        print("3. Benefit")
        print("4. Generate an entire new story")
        edit_choice = input("\nEnter selection: ")
        if edit_choice == '1':
            print("\nYou chose to edit role.")
            part_one = input("\nWhat is your role (user, visitor, etc)? ")
            print("\nHere is your new custom story:")
            print("\nAs a " + part_one + " I want to " + part_two + " so that I can " + part_3 + ".")
            print("\nThank you for using the user story generator. Goodbye.")
        elif edit_choice == '2':
            print("\nYou chose to edit functionality.")
            part_two = input("\nWhat functionality do you want (read, create, etc)? ")
            print("\nHere is your new custom story:")
            print("\nAs a " + part_one + " I want to " + part_two + " so that I can " + part_3 + ".")
            print("\nThank you for using the user story generator. Goodbye.")
        elif edit_choice == '3':
            print("\nYou chose to edit benefit.")
            part_3 = input("\nWhat benefit do you want (edit, save, etc)? ")
            print("\nAs a " + part_one + " I want to " + part_two + " so that I can " + part_3 + ".")
            print("\nThank you for using the user story generator. Goodbye.")
        else:
            print("\nYou chose to create a new custom story.")
            part_one = input("\nWhat is your role (user, visitor, etc)? ")
            part_two = input("What functionality do you want (read, create, etc)? ")
            part_3 = input("What benefit do you want (edit, save, etc)? ")
            print("\nAs a " + part_one + " I want to " + part_two + " so that I can " + part_3 + ".")
            print("\nThank you for using the user story generator. Goodbye.")