def count_words(filename):
    """Counting the words of a txt"""
    try:
        with open(filename, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        pass
        #print(f"Your file {filename} not found, check if you misspeled it")
    else:
        words = content.split()
        num_words = len(words)
        print(f"This book contain {num_words} words")

filename = ["files_exception/exception/alice.txt", "asd.txt",  "files_exception/pi.txt",
             "files_exception/Hello_world.txt", "weygs.txt","files_exception/pi_million_digits.txt"]
for filenames in filename:
    count_words(filenames)