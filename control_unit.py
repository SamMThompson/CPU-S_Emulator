import ir_lookup
#import instruc_mem
import alu
import boot
import data_mem

ins_ptr = 0
hlt_flag = True
slw_flag = False

def set_flag():
    global hlt_flag
    hlt_flag = True    

def set_slow_flag():
    global slw_flag 
    slw_flag = True


def start(prog):
    data_mem.get_data_mem()
    global ins_ptr
    ins_ptr = 0
    global hlt_flag
    while hlt_flag:
        fetch(prog)
        if slw_flag:
            input()
        ins_ptr = ins_ptr + 1
        

def fetch(prog):
    global ins_ptr
    instruction = prog[ins_ptr]
    decode(instruction)


def decode(instruction):
    ins_reg = instruction[:3]
    addr = instruction[3:]
    op_code = ir_lookup.get_opcode(ins_reg) 
    execute(op_code,addr)


def execute(op_code, addr):
    print_vals(op_code, addr)
    global ins_ptr

    if op_code == "000" and addr != "":
        # jump if acc is zero
        if not alu.equal_zero(): ins_ptr=int(addr)-1

    elif op_code == "001" and addr != "":
        # set dr1 to addr
        alu.set_dp1(int(addr))

    elif op_code == "010" and addr != "":
        # set dp2 to addr
        alu.set_dp2(int(addr))

    elif op_code == "011":
        # write acc to dm using dp1
        alu.store()

    elif op_code == "100":
        # acc <- dr1 + dr2
        alu.add()

    elif op_code == "101":
        # acc <- dr1 - dr2
        alu.sub()

    elif op_code == "110":
        # acc <- dr1 * dr2
        alu.mlt()

    elif op_code == "111":
        # halt
        global hlt_flag
        hlt_flag = False



# Not part of the cpu. 
# This is used to print out values of registers
def print_vals(op_code, addr):
    print("ip: " + str(ins_ptr) + " \t" + "Ins:  " + str(op_code) + " " + str(addr))
    print("dp1: " + str(alu.get_dp1()) + "\t" + "dr1: " + str(data_mem.get_mem(alu.get_dp1())))
    print("dp2: " + str(alu.get_dp2()) + "\t" + "dr2: "+ str(data_mem.get_mem(alu.get_dp2())))
    print("acc: " + str(alu.get_acc()))
    print("\n\n\n")