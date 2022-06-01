# Lab 2

# Module 1

def rw_random(file):
    """
    This function will read through a file, line by line and return a list of the lines in a new file.
    """
    with open("random.txt", "r") as file:
        with open("new_random.txt", "w") as new_file:
            for line in file:
                new_file.write(line)

    return(line)


print(rw_random("random.txt"))



# Module 2

def rw_names(file):
    """
    This function loops through the individual lines and then the characters in a file and writes the characters into a new file in reversed order. .

    """
    with open("names.txt", "r") as names:
        with open("new_names.txt", "w") as new_names:
            for line in names:
                for c in line:
                    line = c + line
                new_names.write(line)

                return(line)


print(rw_names("names.txt"))
