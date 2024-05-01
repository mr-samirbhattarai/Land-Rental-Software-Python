
from read import read_file
from write import rent_bill, return_bill, write_to_file
import datetime


def display_data():
    """
    display_data method prints all the data from .txt file
    returns: land details in tabular form
    """
    data  =  read_file()
    
    print("------------------------------------------------------------------------------------------------------")
    print("|   Kitta No.   ||     City      ||   Direction   ||     Anna      ||     Price     ||    Status     |")
    print("------------------------------------------------------------------------------------------------------")
    for each in data:
        for i in each:
                print(f"|{i:^15}", end="|")
        print()
        print("------------------------------------------------------------------------------------------------------")
        
        

def display_available_land():
    """
    display available land only
    """

    data = read_file()
    
    print("------------------------------------------------------------------------------------------------------")
    print("|   Kitta No.   ||     City      ||   Direction   ||     Anna      ||     Price     ||    Status     |")
    print("------------------------------------------------------------------------------------------------------")
    for each in data:
        for i in each:
            if each[-1]==" Available":
                print(f"|{str(i):^15}", end="|")
        if each[-1]==" Available":
            print()
            print("------------------------------------------------------------------------------------------------------")


def display_unavailable_land():
    """
    display unavailable land only
    """

    print("------------------------------------------------------------------------------------------------------")
    print("|   Kitta No.   ||     City      ||   Direction   ||     Anna      ||     Price     ||    Status     |")
    print("------------------------------------------------------------------------------------------------------")
    data = read_file()
    for each in data:
        for i in each:
            if each[-1]==" Not Available":
                print(f"|{str(i):^15}", end="|")
        if each[-1]==" Not Available":
            print()
            print("------------------------------------------------------------------------------------------------------")
    return
    
    

    
def rent_land():
    """
    Rent land to customer.
    prints bill
    returns bill
    """
    lands_data = read_file()
   
    # Display lands
    display_available_land()
    
    rented_land = []
    # total_price = []
    while True:
    
        # user input kitta number of land
        kitta_num = input("Enter the Kitta Number of the land you want to rent: ")
        
        selected_land = None
        for land in lands_data[0:]:         # data[1:]  from 1 to last index [starting: step: end] slicing concept
            # print(land) #for testing
            if land[0] == kitta_num and land[-1] == " Available":
                selected_land = land
                try:
                    rental_duration = int(input("Enter duration (in months) of land to be rented:  "))
                except Exception as ex:
                    print("""
                                ||*******************************************************||
                                ||                                                       ||
                                ||                    Invalid Input!                     ||
                                ||               Please Enter Correct Value              ||
                                ||                                                       ||
                                ||                                                       ||
                                ||*******************************************************||
                                
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
   
                break
        if selected_land:
            # land status is set to "Not Available" (if land is rented)
            selected_land[-1] = " Not Available"
            
            # append selected_land in return_land list
            rented_land.append(selected_land)
        else:
            print("land not available!")
        more_land = input("Do you want to rent another land? (y/n)")
        if more_land.lower().strip() != "y":
            print("Thank you! ")
            break
        
        
    if selected_land:
        customer_name = input("Enter your full name:  ")
        customer_address = input("Enter your current address:  ")
        customer_ph_no = input("Enter your phone number:  ")
            
        if(customer_name.isdigit() or customer_address.isdigit() or len(customer_ph_no) != 10 or customer_ph_no.isalpha()):
            print("""
                                ||*******************************************************||
                                ||                                                       ||
                                ||                    Invalid Input!                     ||
                                ||           Please Enter Correct information            ||
                                ||                                                       ||
                                ||                                                       ||
                                ||*******************************************************||
                                
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
        
        else:
            # print rental invoice
            print(rent_bill(lands_data,rented_land, kitta_num, customer_name, customer_address, customer_ph_no, selected_land, rental_duration))

            # Update lands data in file
            write_to_file(lands_data)
            print("""
                                ||*******************************************************||
                                ||                                                       ||
                                ||                Land rented successfully               ||
                                ||                                                       ||
                                ||                                                       ||
                                ||*******************************************************||
                                
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
            
    else:
        print("""
                                ||*******************************************************||
                                ||                                                       ||
                                ||                Invalid land selection!                ||
                                ||              Land not available for rent              ||
                                ||              Please Select another land!              ||
                                ||                                                       ||
                                ||                                                       ||
                                ||*******************************************************||
                                
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
        
    return








def return_land():
    """
    return land if land is rented
    prints and returns bill created after returning land
    """
    lands_data = read_file()
    
    # display not available land
    display_unavailable_land()
    
    # user input kitta number of land
    kitta_num = input("Enter the Kitta Number of the land you want to return: ")
    
    selected_land = None
    for land in lands_data[0:]:         # data[1:]  from 1 to last index [starting: step: end] slicing concept
        # print(land) #for testing
        if land[0] == kitta_num and land[-1] == " Not Available":
            selected_land = land
            break
    
    if selected_land:
        # user details
        customer_name = input("Enter your full name:  ")
        customer_address = input("Enter your address:  ")
        customer_ph_no = input("Enter your phone number:  ")
        try:
            rented_duration = int(input("Enter duration of land rented for:  "))
            returned_duration = int(input("Enter duration of land returned:  "))
        except Exception as exception:
             print("""
                                ||*******************************************************||
                                ||                                                       ||
                                ||                    Invalid Input!                     ||
                                ||               Please Enter Correct Value              ||
                                ||                                                       ||
                                ||                                                       ||
                                ||*******************************************************||
                                
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
        
        if(customer_name.isdigit() or customer_address.isdigit())  or len(customer_ph_no) != 10 or customer_ph_no.isalpha():
            print("""
                                ||*******************************************************||
                                ||                                                       ||
                                ||                    Invalid Input!                     ||
                                ||         Please Enter Correct Name and Address         ||
                                ||                                                       ||
                                ||                                                       ||
                                ||*******************************************************||
                                
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
            

        else:
            
            selected_land[-1] = " Available"
            
            # total price of land
            if(returned_duration == rented_duration):
                total_amount = (float(selected_land[4]) * rented_duration) - float((selected_land[4])) * returned_duration     # price of that land X months
            elif(returned_duration > rented_duration):
                total_amount = ((float(selected_land[4]) * rented_duration) + (0.40 * selected_land[4])) - (float((selected_land[4])) * returned_duration)          # 40% fine added for late submission
            else:
                print("Please Enter Correct Value")

            # print rental invoice
            print(f"Your Bill is: \n {return_bill(lands_data, kitta_num, customer_name,customer_address, customer_ph_no, selected_land, rented_duration,returned_duration, total_amount)})")
               
            # Update lands data in file
            write_to_file(lands_data)
            
            print("""
                                    ||*******************************************************||
                                    ||                                                       ||
                                    ||              Land successfully returned               ||
                                    ||                                                       ||
                                    ||                                                       ||
                                    ||*******************************************************||
              
                                    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    else:
        print("""
                                    ||*******************************************************||
                                    ||                                                       ||
                                    ||                Invalid land selection!                ||
                                    ||               Please select another Land              ||
                                    ||                                                       ||
                                    ||*******************************************************||
                                    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    return