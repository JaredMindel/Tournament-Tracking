introduction_file = open(r'Introduction.txt')
introduction_text = introduction_file.read()
introduction_file.close()

menu_file = open(r'Main_Menu.txt')
menu_text = menu_file.read()
menu_file.close()

total_number = int(input("How many participants will there be?"))

print(f'{introduction_text} \nThere are {total_number} participants')

def menu_interactive(choice = 0):
    
    participant_dictionary = {}
    exit_game = False

    for x in range(total_number + 1):
        participant_dictionary[x] = None
    
    while exit_game == False:
        
        choice = int(input(f"{menu_text}"))
        if choice == 1:
            participant_name = input("Give a name")
            participant_number = int(input(f"Give the corresponding number between 1 and {total_number}"))
            participant_dictionary[participant_number] = participant_name
            continue
        elif choice == 2:
            for x in participant_dictionary:
                print(f'{x}: {participant_dictionary[x]}')
            remove_name = str(input("Who do you want to remove?"))
            for x in participant_dictionary:
                if participant_dictionary[x] == remove_name:
                    participant_dictionary[x] = None
        elif choice == 3:
            for x in participant_dictionary:
                print(f'{x}: {participant_dictionary[x]}')


menu_interactive()

