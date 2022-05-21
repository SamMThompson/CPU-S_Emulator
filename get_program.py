def get_prog(file_name):
    f = open(file_name + ".txt", "r")
    prog = []
    for x in f:
        if x != '\n' and x[0] != "#":
            prog.append(x.rstrip('\n'))
    return prog
    f.close()
