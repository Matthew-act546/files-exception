absolute = 'C:/Users/User/Desktop/dave_folder/python/files_exception/pi.txt'

# ----------------ABSOLUTE-----------------------
with open(absolute) as pi:
    contents = pi.read()
# ----------------RELATIVE-----------------------
# with open('files_exception/pi.txt') as file_object:
#     contents = file_object.read()
print(contents.rstrip())
