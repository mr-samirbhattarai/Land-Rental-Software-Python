def read_file():
    """
    
    """
    try:
        open_file = open("lands.txt")
        
        read_land = open_file.readlines()
        
        lands_list = []
        for row in read_land:
            land_info_list = row.strip().split(",")   #strip removes unwanted spaces and split separates two str
            lands_list.append(land_info_list)
        open_file.close()
    except Exception as exception:
        print(f"Cannot load land. Please Try again. Exception {exception}")
            
    return lands_list