#Lab 2

def file_copier(file):
    """
    This function reads a file and writes the information into a new file.
    """

    file_name = input(randomlist.txt)
    file_name_new = input(randomlist_new.txt)
    with open(file_name, "r") as file_to_copy:
        with open(file_name_new, "w") as new_file:
            for line in file_to_copy:
                new_file.write(line)
    return new_file(file)[:]