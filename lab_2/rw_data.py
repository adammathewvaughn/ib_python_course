#Module 1 

def rw_data():
    """
    This function will read in a file and return a list of the lines in the file.
    """
    file_name = input("Enter the name of the file you want to read: ")
    file_object = open(file_name, "r")
    file_lines = file_object.readlines()
    file_object.close()
    return file_lines
 