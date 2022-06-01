def rw_names(file):
    """
    This function loops through the given file and counts each character, returning the count as an integer.

    """
    with open("names.txt", "r") as names:
        with open("new_names.txt", "w") as new_names:
            for line in names:
                for c in line:
                    line =  c + line
                    new_names.write(line)
                                        
                                        
                return(line)

print(rw_names("rw_names.txt"))
