def read_file():
    """
    reads file form .txt file
    returns: list (of land details)
    """
    # Exception Handling
    try:
        open_file = open("lands.txt")       # open txt file
        
        read_land = open_file.readlines()
        
        lands_data = []
        for row in read_land:
            land_info_list = row.strip().split(",")   #strip removes unwanted spaces and split separates two str
            lands_data.append(land_info_list)
        open_file.close()
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
        
    
    return lands_data