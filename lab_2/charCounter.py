def char_counter(file):
    """
    This function loops through the given file and counts each character, returning the count as an integer.

    """
    with open("names.txt", "r") as names:
      with open("new_names.txt", "w") as new_names:
        count = 0
        for line in names:
          count += len(line)
          len(line) + 1
          new_names.write(line)

    
    return int(count)


print(char_counter("names.txt"))
