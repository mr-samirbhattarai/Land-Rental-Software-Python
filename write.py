import datetime


def write_to_file(lands_data):
    """
    Write the updated land data to the lands.txt file.
    """
    try:
        write_file = open("lands.txt", "w")
        for land_info in lands_data:
            each_line = ",".join(land_info) + "\n"
            write_file.write(each_line)
        write_file.close()
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
        
    
        
        
def rent_bill(lands_data, rented_land, kitta_num, customer_name, customer_address, customer_ph_no, selected_land, rental_duration):
    """
    create rent bill
    returns: bill
    """
    
    
    print(rented_land)
    # date and time
    date_year = datetime.datetime.now().year
    date_month = datetime.datetime.now().month
    date_day = datetime.datetime.now().day
    
    time_hour = datetime.datetime.now().hour
    time_minute = datetime.datetime.now().minute
    
    total_amount = 0
    for land in rented_land:
        total_amount += float(float(land[4]) * float(land[6]))
    
    
    # total_amount = sum((float(land[4]) * float(rental_duration)) for land in rented_land)
    
    
    # Generate invoice
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
    
    bill_middle = ""
    sn = 1
    for land in rented_land:
        bill_middle += f"""||| {sn:^4} |  {land[0]:^8} | {land[1]:^12} | {land[2]:^13} | {land[3]:^4} | {land[6]:^8} | {land[4]:^12}|||\n"""
        sn += 1
    
    bill_footer = f"""
|||---------------------------------------------------------------------------------|||
||                                                                                   ||
||                                                   Total Amount:    {total_amount:<15}||
||                                                    VAT Amount :    {0.13 * total_amount:<15}||
||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
||                                                                                   ||
||                  Late return can be fined 40% of monthly price                    ||
||===================================================================================||"""
    
    bill = bill_top + bill_middle + bill_footer
            
    # Creating the text file of the bill
    invoice_file = open(f"rent_bills/{kitta_num}_{customer_name}.txt","w")
    invoice_file.write(bill)
    invoice_file.close()

    # Update lands data in file
    write_to_file(lands_data)
    
    return bill

            
def return_bill(lands_data, rented_land, kitta_num, customer_name, customer_address, customer_ph_no, selected_land, rented_duration, returned_duration):
    # date and time
    date_year = datetime.datetime.now().year
    date_month = datetime.datetime.now().month
    date_day = datetime.datetime.now().day
    
    time_hour = datetime.datetime.now().hour
    time_minute = datetime.datetime.now().minute
    
    
    
    total_amount = 0
    for land in rented_land:
        # total price of land
            if(returned_duration == rented_duration):
                total_amount = (float(land[4]) * rented_duration) - float((land[4])) * returned_duration     # price of that land X months
            elif(returned_duration > rented_duration):
                total_amount = (((float(land[4]) * returned_duration) - (float((land[4])) * returned_duration)) + (0.40 * float(land[4])))         # 40% fine added for late submission
            else:
                print("Please Enter Correct Value")
    
    # Generate invoice
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
    
    bill_middle = ""
    sn = 1
    for land in rented_land:
        bill_middle += f"""||| {sn:^4} |  {land[0]:^8} | {land[1]:^12} | {land[2]:^13} | {land[3]:^4} | {returned_duration:^8} | {land[4]:^12}|||\n"""
        sn += 1
    
    bill_footer = f"""
|||---------------------------------------------------------------------------------|||
||                                                                                   ||
||                                                   Total Amount:    {total_amount:<15}||
||                                                    VAT Amount :    {0.13 * total_amount:<15}||
||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
||                                                                                   ||
||                  Late return can be fined 40% of monthly price                    ||
||===================================================================================||"""
    
    return_bill = bill_top + bill_middle + bill_footer
    # Creating the text file of the bill
    try:
        invoice_file = open(f"return_bills/{kitta_num}_{customer_name}.txt","w")
        invoice_file.write(return_bill)
        invoice_file.close()
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
    
        
    # Update lands data in file
    write_to_file(lands_data)
    return return_bill