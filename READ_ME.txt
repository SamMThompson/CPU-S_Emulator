
===========
| H E L P |
===========


Overview
========
This is a simple CPU-s enumlator

To run a assembly program, you have two choices:
	1. "rf (the name of the text file where your program is stored)"
	   - This option runs the program without any interruption.")
	2. "rs (the name of the text file where your program is stored)"
	   - This option waits for user input after each operation has executed
For example ">rf fib" would run the "fib.txt" code.

The data memory is stored in "dm.txt".
Each line in this dm.txt document corresponds to a memory cell.
This is converted line-wise to a list, and therefore is addressed 

This project is an odd mix of "true" simulation of a cpu and some shortcuts.
	1. Operations (such as add, multiply, etc.) utilize python arithmetic, not Boolean logic, and
	2. The address bus isn't implemented. Instead, components communicate directly.



Main Components
===============
1. Accumulator (acc)	     -- Stores the result of the previous arithmetic operation.
2. Data register 1 (dr1)     -- Stores the value in data memory at data pointer 1 (dp1).
3. Data register 2 (dr2)     -- Stores the value in data memory at data pointer 2 (dp2).
4. Instruction pointer (ip)  -- Points to the next instruction in the program.
5. Data Memory (dm.txt)      -- A txt file that stores integers.


    
Instruction set
===============
jmp <addr> -- Jumps to the instruction line specified by <addr>
ld1 <addr> -- Places <addr> into data pointer 1
ld2 <addr> -- Places <addr> into data pointer 2
sto 	     -- Writes the value in the accumulator into data memory using address specified by data pointer 1
add        -- acc <- DR1 + DR2
sub        -- acc <- DR1 - DR2
mlt        -- acc <- DR1 * DR2
hlt 	     -- Halts the program



Future Directions
=================
The following are a list of instructions that haven't been implemented yet (but might be soon)
	1. irt <val> -- Places <val> into the data memory at data pointer 1.
	2. inp 	 -- Gets input from user and stores in data memory at data pointer 1.
	3. out       -- Prints out the value at data pointer 1.

