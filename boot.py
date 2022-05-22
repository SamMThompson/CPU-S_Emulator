import os.path
import ir_lookup
import get_program
import control_unit
import help


def init_print():
     f = open('resources/START.txt', 'r')
     file_contents = f.read()
     print (file_contents)
     f.close()



def prog_boot(file_name):
     if not os.path.exists("programs/"+file_name+".txt"):
          print("Error - No Such file exists")
     else:
          prog=[]
          prog = get_program.get_prog(file_name)
          control_unit.start(prog)
          control_unit.set_flag()
                    


def start_up():
     init_print()
     while True:
          user_in = input("> ")
          if user_in == "quit":
               break
          elif user_in == "help":
               help.print_help()
          elif user_in[:2] == "rs":
               # run with steppping
               prog_loc = user_in[3:]
               control_unit.set_slow_flag()
               prog_boot(prog_loc)
          elif user_in[:2] == "rf":
               # run fully
               prog_loc = user_in[3:]
               prog_boot(prog_loc)
          else:
               print("Please enter a valid command.")
               print("Type help for more details.")
               print()



if __name__ == '__main__':
    start_up()