import data_mem

data_ptr1 = 0
data_ptr2 = 0
data_reg1 = 0
data_reg2 = 0
acc = 0

def add():
    global acc
    global data_reg1
    global data_reg2
    acc = int(data_reg1) + int(data_reg2)
    return acc

def sub():
    global acc
    global data_reg1
    global data_reg2
    acc = int(data_reg1) - int(data_reg2)
    return acc

def mlt():
    global acc
    global data_reg1
    global data_reg2
    acc = int(data_reg1) * int(data_reg2)
    return acc

def equal_zero():
    global acc
    return int(acc) == 0

def set_dp1(addr):
    global data_ptr1
    global data_reg1
    data_ptr1 = addr
    data_reg1 = data_mem.get_mem(data_ptr1)

def set_dp2(addr):
    global data_ptr2
    global data_reg2
    data_ptr2 = addr
    data_reg2 = data_mem.get_mem(data_ptr2)

def store():
    global acc
    global data_ptr1
    global data_reg1
    data_reg1 = acc 
    data_mem.write_mem(data_ptr1, acc)




# Used for printing
def get_dp1():
    global data_ptr1
    return data_ptr1

# Used for printing
def get_dp2():
    global data_ptr2
    return data_ptr2

# Used for printing
def get_acc():
    global acc
    return acc