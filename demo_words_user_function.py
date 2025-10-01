def search_word(pattern, file):
    with (open(file, mode="rt") as fh_in):
        for (line_num, line) in enumerate(fh_in, start=1):
            if line.isascii() and pattern in line:
                print(line_num, line, end="")
    return None

search_word("done", r"done.txt")
search_word("done", r"done.txt")