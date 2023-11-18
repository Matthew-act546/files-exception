# file = "files_exception/pi.txt"
# with open(file) as file_object:
#     line = file_object.readlines()
#     pi_string = ''
#     for lines in line:
#         pi_string += lines.strip()
#     print(pi_string)
#     print(len(pi_string))

filename = "files_exception/pi_million_digits.txt"
with open(filename) as file:
    line = file.readlines()

    pi_string = ''
    for lines in line:
        pi_string += lines
    
    birthday = input("Enter your birthday (MM/DD/YY): ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi.")
    else:
        print("Your birthday does not appears in the first million digits of pi.")