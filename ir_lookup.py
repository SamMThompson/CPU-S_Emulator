ir_lookup = {
    "jnz": "000",
    "ld1": "001",
    "ld2": "010",
    "sto": "011",
    "add": "100",
    "sub": "101",
    "mlt": "110",
    "hlt": "111"
}


def get_opcode(operator):
    return ir_lookup[operator]
