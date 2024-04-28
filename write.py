# from operations import rent_land
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
        
        
def rent_bill(lands_data, kitta_num, customer_name, customer_address, customer_ph_no, selected_land, rental_duration, total_amount):
    # date and time
    date_year = datetime.datetime.now().year
    date_month = datetime.datetime.now().month
    date_day = datetime.datetime.now().day
    
    time_hour = datetime.datetime.now().hour
    time_minute = datetime.datetime.now().minute
    # Generate rental invoice
    
    # bill = 1
    # for i in bill:
    #     if bill == len(kitta_num):
    #         bill_no = +1

    bill = f"""
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
                            ||| Kitta No. |      City      | Direction |  Anna  |  Duration  |      Price       |||
                            |||---------------------------------------------------------------------------------|||
                            |||{selected_land[0]:^11}|{selected_land[1]:^16}|{selected_land[2]:^11}|{selected_land[3]:^7} | {rental_duration:^3} months | {selected_land[4]:^17}|||
                           
                            |||           |                |           |        |            |                  |||
                            |||---------------------------------------------------------------------------------|||
                            ||                                                                                   ||
                            ||                                                   Total Amount:    {total_amount:<15}||
                            ||                                                 13% VAT Amount :    {0.13 * total_amount:<13}||
                            ||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
                            ||                                                                                   ||
                            ||                                                                                   ||
                            ||===================================================================================||
            """
            
    # Creating the text file of the bill
    invoice_file = open(f"rent_bills/{kitta_num}_{customer_name}.txt","w")
    invoice_file.write(bill)
    invoice_file.close()
    
    
    
    
    # Update lands data in file
    write_to_file(lands_data)
            
            
            
def return_land(lands_data, kitta_num, customer_name, customer_address, customer_ph_no, selected_land, rented_duration, returned_duration, total_amount):
    # date and time
    date_year = datetime.datetime.now().year
    date_month = datetime.datetime.now().month
    date_day = datetime.datetime.now().day
    
    time_hour = datetime.datetime.now().hour
    time_minute = datetime.datetime.now().minute
    
    
    # Generate rental invoice
    
    bill = f"""
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
                                        ||| Kitta No. |      City      | Direction |  Anna  |  Duration  |       n Price      |||
                                        |||---------------------------------------------------------------------------------|||
                                        |||{selected_land[0]:^11}|{selected_land[1]:^16}|{selected_land[2]:^11}|{selected_land[3]:^7} | {rented_duration:^3} months | {selected_land[4]:^17}|||
                                        |||           |                |           |        |            |                  |||
                                        |||---------------------------------------------------------------------------------|||
                                        ||                                                                                   ||
                                        ||                                                   Total Amount:    {total_amount:<15}||
                                        ||                                                    VAT Amount :    {0.13 * total_amount:<15}||
                                        ||                                                   Grand Total :    {total_amount + (0.13 * total_amount):<15}||
                                        ||                                                                                   ||
                                        ||                                                                                   ||
                                        ||===================================================================================||
        """
    # Creating the text file of the bill
    invoice_file = open(f"returned_bills/{kitta_num}_{customer_name}.txt","w")
    invoice_file.write(bill)
    invoice_file.close()
    
    # Update lands data in file
    write_to_file(lands_data)