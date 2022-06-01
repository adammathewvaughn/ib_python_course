# Module 1


def rw_data(file):
    """
    This function will read in a file and return a list of the lines in the file.
    """
    with open("random.txt", "r") as file:
      with open("new_random.txt", "w") as new_file:
         for line in file:            
           new_file.write(line)
  
   
    
    
    return(line)

print(rw_data("random.txt"))
