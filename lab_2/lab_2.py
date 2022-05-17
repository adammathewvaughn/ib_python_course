#Lab 2




def read_file(file):
    '''
    Reads the file and returns the contents.
    '''
    file = open("random.txt", "r")
    new_file= open("new_random.txt", "w")
    file.read("random.txt")
    for line in file:
        print(next(line))
    new_file.write("new_random.txt")
    file.close(file)
    file.close(new_file)

    return new_contents

print (read_file(new_file))
