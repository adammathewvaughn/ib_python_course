


def char_counter(file):
    """
    This function loops through the given file and counts each character, returning the count as an integer.

    """
    file = open(file, 'r')
    for i in file:
        count = 0
        count = count + 1
    file.close()
    return int(count)

print (char_counter("names.txt"))
