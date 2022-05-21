data_mem = [
    1,
    5,
    1,
    1,
    1,
    1,
    9,
    1
]

def get_mem(addr):
    global data_mem
    return data_mem[addr]

def write_mem(addr, val):
    global data_mem
    data_mem[addr] = val
   