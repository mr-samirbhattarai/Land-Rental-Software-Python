import datetime


def write_to_file(lands_data):
    """
    Write the updated land data to the lands.txt file.
    """
    # Exception Handling
    try:
        write_file = open("lands.txt", "w")     # open txt file in write mode
        # update land data
        for land_info in lands_data:
            each_line = ",".join(land_info) + "\n"
            write_file.write(each_line)
        write_file.close()
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
        
    
        
        
def rent_bill(lands_data, rented_land, kitta_num, customer_name, customer_address, customer_ph_no, rental_duration):
    """
    create rent bill
    returns: bill
    """

    # date and time
    date_year = datetime.datetime.now().year
    date_month = datetime.datetime.now().month
    date_day = datetime.datetime.now().day
    
    time_hour = datetime.datetime.now().hour
    time_minute = datetime.datetime.now().minute
    
    # calculate total amount
    total_amount = 0
    for land, duration in rented_land:
        total_amount += float(float(land[4]) * float(duration))
    
    # Generate invoice
    #invoice header
    bill_top = f"""
||===================================================================================||
||                                                                                   ||
||                               Techno Property Nepal                               ||
||                              ICP-001, Pokhara, Nepal                              ||
||-----------------------------------------------------------------------------------||
||                                                                                   ||
||    VAT: 9759437                                        Date: {date_year:>4}-{date_month:>02}-{date_day:<13}||
||                                                        Time: {time_hour:>02}:{time_minute:<18}||
||                                                                                   ||
||               Name:  {customer_name:<61}||
||            Address:  {customer_address:<61}||
||              Phone:  {customer_ph_no:<61}||
||                                                                                   ||
|||---------------------------------------------------------------------------------|||
||| S.N. | Kitta No. |     City     |   Direction   | Anna | Duration |    Price    |||
|||---------------------------------------------------------------------------------|||
"""

    # invoice body
    bill_middle = ""
    sn = 1
    for land, duration in rented_land:
        bill_middle += f"""||| {sn:^4} |  {land[0]:^8} | {land[1]:^12} | {land[2]:^13} | {land[3]:^4} | {duration:^8} | {land[4]:^12}|||\n"""
        sn += 1
    
    # invoice footer
    bill_footer = f"""|||---------------------------------------------------------------------------------|||
||                                                                                   ||
||                                                   Total Amount:    {total_amount:<15}||
||                                                    VAT Amount :    {0.13 * total_amount:<15}||
||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
||                                                                                   ||
||                  Late return can be fined 40% of monthly price                    ||
||===================================================================================||"""
    
    bill_rent = bill_top + bill_middle + bill_footer
            
    # Creating the text file of the bill
    # Exception Handling
    try:
        invoice_file = open(f"rent_bills/{kitta_num}_{customer_name}.txt","w")
        invoice_file.write(bill_rent)
        invoice_file.close()
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
    
    # Update lands data in file
    write_to_file(lands_data)
    
    return bill_rent

            
def return_bill(lands_data, rented_land, kitta_num, customer_name, customer_address, customer_ph_no):
    # date and time
    date_year = datetime.datetime.now().year
    date_month = datetime.datetime.now().month
    date_day = datetime.datetime.now().day
    time_hour = datetime.datetime.now().hour
    time_minute = datetime.datetime.now().minute
    
    # calculate total_amount
    total_amount = 0
    for land, rent_duration, return_duration in rented_land:
        # total price of land
        if(return_duration == rent_duration):
            total_amount += (float(land[4]) * rent_duration) - float((land[4])) * return_duration     # price of that land X months
        elif(return_duration > rent_duration):
            total_amount += ((float(land[4]) * return_duration) - (float((land[4])) * rent_duration)) + (0.40 * float(land[4]))         # 40% fine added for late submission
        else:
            print("Please Enter Correct Value")
    # Generate invoice
    # invoice header
    bill_top = f"""
||===================================================================================||
||                                                                                   ||
||                               Techno Property Nepal                               ||
||                              ICP-001, Pokhara, Nepal                              ||
||-----------------------------------------------------------------------------------||
||                                                                                   ||
||    VAT: 9759437                                        Date: {date_year:>4}-{date_month:>02}-{date_day:<13}||
||                                                        Time: {time_hour:>02}:{time_minute:<18}||
||                                                                                   ||
||               Name:  {customer_name:<61}||
||            Address:  {customer_address:<61}||
||              Phone:  {customer_ph_no:<61}||
||                                                                                   ||
|||---------------------------------------------------------------------------------|||
||| S.N. | Kitta No. |     City     |   Direction   | Anna | Duration |    Price    |||
|||---------------------------------------------------------------------------------|||
"""
    
    # invoice body
    bill_middle = ""
    sn = 1
    for land,rent_duration, return_duration in rented_land:
        bill_middle += f"""||| {sn:^4} |  {land[0]:^8} | {land[1]:^12} | {land[2]:^13} | {land[3]:^4} | {return_duration:^8} | {land[4]:^12}|||\n"""
        sn += 1
    
    # invoice footer
    bill_footer = f"""|||---------------------------------------------------------------------------------|||
||                                                                                   ||
||                                            Total Amount (Fine):    {total_amount:<15}||
||                                                    VAT Amount :    {0.13 * total_amount:<15}||
||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
||                                                                                   ||
||                  Late return can be fined 40% of monthly price                    ||
||===================================================================================||"""
    
    return_bill = bill_top + bill_middle + bill_footer
   
    # Creating the text file of the bill
    # Exception Handling
    try:
        invoice_file = open(f"return_bills/{kitta_num}_{customer_name}.txt","w")
        invoice_file.write(return_bill)
        invoice_file.close()
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
        
    # Update lands data in file
    write_to_file(lands_data)
    
    return return_bill