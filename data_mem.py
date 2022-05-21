data_mem = []

def get_data_mem():
    global data_mem
    f = open("resources/dm.txt", "r")
    for x in f:
        data_mem.append(x.rstrip('\n'))
    

def get_mem(addr):
    global data_mem
    return data_mem[addr]

def write_mem(addr, val):
    global data_mem
    data_mem[addr] = val
   