
# from operations import display_data, rent_land, return_land
import operations
import write



""""""



print("""

                    ████████ ███████   █████  ██   ██ ███   ██  █████     ███████ ███████   █████ ███████  ██████ ███████ ████████ ██    ██
                       ██    ██       ██   ██ ██   ██ ████  ██ ██   ██     ██   ██ ██   ██ ██   ██ ██   ██ ██      ██   ██   ██     ██  ██
                       ██    █████    ██      ███████ ██ ██ ██ ██   ██     ██████  ██████  ██   ██ ██████  █████   ██████    ██      ████
                       ██    ██       ██   ██ ██   ██ ██  ████ ██   ██     ██      ██   ██ ██   ██ ██      ██      ██   ██   ██       ██
                       ██    ███████   █████  ██   ██ ██   ███  █████      ██      ██   ██  █████  ██      ███████ ██   ██   ██       ██""")
                                              
                                              
                                              
while(True):
    print("""
                                ||*******************************************************||
                                ||                     1. Display Lands                  ||
                                ||                     2. Rent Land                      ||
                                ||                     3. Return Land                    ||
                                ||                     4. Exit Program                   ||
                                ||*******************************************************||""")
    try:
        user_input = int(input("\t\t\t\t\t\tEnter your choice:  "))

        if (user_input) == 1:
            operations.display_data()
        elif (user_input) == 2:
            operations.rent_land()
        elif (user_input) == 3:
            operations.return_land()
        elif (user_input) == 4:
            break
        else:
            print("""
                    Invalid Input!
                Please Enter Valid Value""")
    except Exception as exception:
        print(f"Cannot load land. Please Try again. Exception {exception}")
        