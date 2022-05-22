def get_prog(file_name):
    try:
        f = open("programs/" + file_name + ".txt", "r")
        prog = []
        for x in f:
            if x != '\n' and x[0] != "#":
                prog.append(x.rstrip('\n'))
        f.close()
        return prog
    except IOError:
        print("Fatal error")
        
    