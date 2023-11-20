file = "Hello_world.txt"

with open(file, 'a') as file_object:
    file_object.write("I will become a successful programmer \n")
    file_object.write(''.center(50, '*'))