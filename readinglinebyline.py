files = 'files_exception/pi.txt'
with open(files) as pi:
    for line in pi:
        print(line.rstrip())

