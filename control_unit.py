import ir_lookup
import instruc_mem
import alu
import boot

import data_mem

ins_pointer = 0
ins_reg = ""
hlt_flag = True


def set_flag():
    global hlt_flag
    hlt_flag = True    


def start(prog):
    global ins_pointer
    global hlt_flag
    while hlt_flag:
        fetch(prog)
        input()
        ins_pointer = ins_pointer + 1
        


def fetch(prog):
    global ins_pointer
    instruction = prog[ins_pointer]
    decode(instruction)

def decode(instruction):
    ins_reg = instruction[:3]
    addr = instruction[3:]
    op_code = ir_lookup.get_opcode(ins_reg) 
    execute(op_code,addr)

def execute(op_code, addr):
    print_vals(op_code, addr)
    global ins_pointer

    if op_code == "000" and addr != "":
        # jump if acc is zero
        # minus one because ip will increment
        if not alu.equal_zero(): 
            ins_pointer = int(addr)-1
        return 0

    elif op_code == "001" and addr != "":
        # set dr1 to addr
        alu.set_dp1(int(addr))
        return 0

    elif op_code == "010" and addr != "":
        # set dp2 to addr
        alu.set_dp2(int(addr))
        return 0

    elif op_code == "011":
        # write acc to dm using dp1
        alu.store()
        return 0

    elif op_code == "100":
        # acc <- dr1 + dr2
        alu.add()
        return 0

    elif op_code == "101":
        # acc <- dr1 - dr2
        alu.sub()
        return 0

    elif op_code == "110":
        # acc <- dr1 * dr2
        alu.mlt()
        return 0

    elif op_code == "111":
        # halt
        global hlt_flag
        hlt_flag = False
        return 0



# Not part of the cpu. 
# This is used to print out values of registers
def print_vals(op_code, addr):
    print("ip: " + str(ins_pointer) + " \t" + str(op_code) + " " + str(addr))
    print("dp1: " + str(alu.get_dp1()) + "\t" + "dr1: " + str(data_mem.get_mem(alu.get_dp1())))
    print("dp2: " + str(alu.get_dp2()) + "\t" + "dr2: "+ str(data_mem.get_mem(alu.get_dp2())))
    print("acc: " + str(alu.get_acc()))
    print()
    print()
    print()