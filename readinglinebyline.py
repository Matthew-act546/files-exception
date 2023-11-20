files = 'pi.txt'
with open(files) as pi:
    for line in pi:
        print(line.rstrip())

