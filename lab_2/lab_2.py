#Lab 2




def char_counter(file):
    """
    This function loops through the given file and counts each character, returning the count as an integer.

    """

    file = open("names.txt", 'r')
    count = 0
    for count in file:
        count = count + 1
    return int(count)

print (char_counter("names.txt"))