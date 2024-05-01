import datetime


def write_to_file(lands_data):
    """
    Write the updated land data to the lands.txt file.
    """
    try:
        file = open("lands.txt", "w")
        for land_info in lands_data:
            line = ",".join(land_info) + "\n"
            file.write(line)
        file.close()
    except Exception as exception:
        print(f"Error occurred while writing to file: {exception}")
        
        
        
def rent_bill(lands_data, rented_land, kitta_num, customer_name, customer_address, customer_ph_no, selected_land, rental_duration):
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
    
    
    
    total_amount = sum((float(land[4]) * float(rental_duration)) for land in rented_land)
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
        bill_middle += f"""\t||| {sn:^4} |  {land[0]:^8} | {land[1]:^12} | {land[2]:^13} | {land[3]:^4} | {rental_duration:^8} | {land[4]:^12}|||\n\t\t\t\t\t\t\t\t\t"""
        sn += 1
    
    bill_footer = f"""
                                        |||---------------------------------------------------------------------------------|||
                                        ||                                                                                   ||
                                        ||                                                   Total Amount:    {total_amount:<15}||
                                        ||                                                    VAT Amount :    {0.13 * total_amount:<15}||
                                        ||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
                                        ||                                                                                   ||
                                        ||                  Late return can be fined 40% of monthly price                    ||
                                        ||===================================================================================||
        """
    
    bill = bill_top + bill_middle + bill_footer
            
    # Creating the text file of the bill
    invoice_file = open(f"rent_bills/{kitta_num}_{customer_name}.txt","w")
    invoice_file.write(bill)
    invoice_file.close()

    # Update lands data in file
    write_to_file(lands_data)
    
    return bill

            
def return_bill(lands_data, kitta_num, customer_name, customer_address, customer_ph_no, selected_land, rented_duration, returned_duration, total_amount):
    # date and time
    date_year = datetime.datetime.now().year
    date_month = datetime.datetime.now().month
    date_day = datetime.datetime.now().day
    
    time_hour = datetime.datetime.now().hour
    time_minute = datetime.datetime.now().minute
    
    
    
    
    # Generate rental invoice
    
    return_bill = f"""
                                        ||===================================================================================||
                                        ||                                                                                   ||
                                        ||                               Techno Property Nepal                               ||
                                        ||                              ICP-001, Pokhara, Nepal                              ||
                                        ||-----------------------------------------------------------------------------------||
                                        ||                                                                                   ||
                                        ||    VAT: 9759437                                        Date: {date_year:>4}-{date_month:>2}-{date_day:<13}||
                                        ||                                                        Time: {time_hour:>2}:{time_minute:<18}||
                                        ||                                                                                   ||
                                        ||               Name:  {customer_name:<61}||
                                        ||            Address:  {customer_address:<61}||
                                        ||              Phone:  {customer_ph_no:<61}||
                                        ||                                                                                   ||
                                        |||---------------------------------------------------------------------------------|||
                                        ||| Kitta No. |      City      | Direction |  Anna  |  Duration  |       Price      |||
                                        |||---------------------------------------------------------------------------------|||
                                        |||{selected_land[0]:^11}|{selected_land[1]:^16}|{selected_land[2]:^11}|{selected_land[3]:^7} | {rented_duration:^3} months | {selected_land[4]:^17}|||
                                        |||           |                |           |        |            |                  |||
                                        |||---------------------------------------------------------------------------------|||
                                        ||                                                                                   ||
                                        ||                                                   Total Amount:    {total_amount:<15}||
                                        ||                                                    VAT Amount :    {0.13 * total_amount:<15}||
                                        ||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
                                        ||                                                                                   ||
                                        ||                  Late return can be fined 40% of monthly price                    ||
                                        ||===================================================================================||
        """
    # Creating the text file of the bill
    invoice_file = open(f"return_bills/{kitta_num}_{customer_name}.txt","w")
    invoice_file.write(return_bill)
    invoice_file.close()
    
    # Update lands data in file
    write_to_file(lands_data)
    return return_bill