import operations
"""
main module

"""


# Banner
print("""

                    ████████ ███████   █████  ██   ██ ███   ██  █████     ███████ ███████   █████ ███████  ██████ ███████ ████████ ██    ██
                       ██    ██       ██   ██ ██   ██ ████  ██ ██   ██     ██   ██ ██   ██ ██   ██ ██   ██ ██      ██   ██   ██     ██  ██
                       ██    █████    ██      ███████ ██ ██ ██ ██   ██     ██████  ██████  ██   ██ ██████  █████   ██████    ██      ████
                       ██    ██       ██   ██ ██   ██ ██  ████ ██   ██     ██      ██   ██ ██   ██ ██      ██      ██   ██   ██       ██
                       ██    ███████   █████  ██   ██ ██   ███  █████      ██      ██   ██  █████  ██      ███████ ██   ██   ██       ██""")
                                              
                                              
                                              
while(True):
    # Options
    print("""
                                ||*******************************************************||
                                ||                     1. Display Lands                  ||
                                ||                     2. Rent Land                      ||
                                ||                     3. Return Land                    ||
                                ||                     4. Exit Program                   ||
                                ||*******************************************************||""")
    # Exception Handling
    try:
        user_input = int(input("\t\t\t\t\t\tEnter your choice:  "))
        
        if (user_input) == 1:
            operations.display_data()
        elif (user_input) == 2:
            operations.rent_land()
        elif (user_input) == 3:
            operations.return_land()
        elif (user_input) == 4:
            print("--------------------------EXITING PROGRAM-------------------------")
            break       #Exit loop and program
        else:
            print("""
                    Invalid Input!
                Please Enter Valid Value""")
    except Exception as exception:
        # Exception message
        print(""" 
                                ||*******************************************************||
                                ||                                                       ||
                                ||                    Invalid Input!                     ||
                                ||               Please Enter Correct Value              ||
                                ||                                                       ||
                                ||                                                       ||
                                ||*******************************************************||
                                
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")