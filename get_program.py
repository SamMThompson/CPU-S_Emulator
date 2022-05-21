def get_prog(file_name):
    f = open(file_name + ".txt", "r")
    prog = []
    for x in f:
        prog.append(x.rstrip('\n'))
    return prog
    f.close()
