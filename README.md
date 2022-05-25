# CPU-S Emulator
This is a simple CPU emulator -- based on the CPU-S.

This project is an odd mix of "true" simulation of a cpu and some shortcuts.
1. Operations (such as add, multiply, etc.) utilize python arithmetic, not Boolean logic, and
2. The address bus isn't implemented. Instead, components communicate directly.

Data memory is "volatile". 
That is, a program that changes data memory, only changes memory for that session.
If you wish to make permanent changes to the data memory, you must change the "dm.txt" file in the resources directory.


## Main Components
1. Data register 1 (dr1)     -- Stores the value in data memory at data pointer 1 (dp1).
2. Data register 2 (dr2)     -- Stores the value in data memory at data pointer 2 (dp2).
3. Accumulator (acc)	     -- Stores the result of the previous arithmetic operation.
4. Instruction pointer (ip)  -- Points to the next instruction in the program.
5. Data Memory (dm.txt)      -- A txt file that stores integers.

## Instruction Set
- jnz (addr) -- If dr1 != 0, jump to the instruction line specified by <addr>
- ld1 (addr) -- Places (addr) into data pointer 1
- ld2 (addr) -- Places (addr) into data pointer 2
- sto 	     -- Writes the value in the accumulator into data memory using address specified by data pointer 1
- add        -- acc <- DR1 + DR2
- sub        -- acc <- DR1 - DR2
- mlt        -- acc <- DR1 * DR2
- hlt 	     -- Halts the program

The assembly is white-space sensitive.
Do not have a space before an instruction, only have one space between an operator and the address, and blank lines should not have any spaces.
		       
Note that all comments and blank lines do not count towards the instruction memory.
Therefore, if you are using jnz, the address should be the line number, assuming comments and blank lines have been stripped.
		       
For examples, see the "program" directory.
		       
## Using the emulator

To write an assembly program, add a txt file to the programs directory and write your code there.
See the example programs.


To run a assembly program, you have two choices:
1. "rf (the name of the text file where your program is stored)"
	   - This option runs the program without any interruption.")
2. "rs (the name of the text file where your program is stored)"
	   - This option waits for user input after each operation has executed
For example ">rf fib" would run the "fib.txt" code.


The data memory is stored in "dm.txt".
Each line in this dm.txt document corresponds to a memory cell.
This is converted line-wise to a list, and therefore is addressed as RAM would be.
To write your own data memory, simply add an integer to each line.

To run the emulator, launch the "boot.py" file using the method of your choice.                      
