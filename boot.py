from sys import float_repr_style
import ir_lookup
import get_program
import control_unit
import help

def init_print():
     f = open('START.txt', 'r')
     file_contents = f.read()
     print (file_contents)
     f.close()


def main():
     init_print()
     while True:
          user_in = input("> ")
          if user_in == "quit":
               break
          if user_in == "help":
               help.print_help()
          else:
               prog_loc = user_in[3:]
               if user_in[:2] == "rs":
                    control_unit.set_slow_flag()
               elif user_in[:3] != "rf ":
                    print("Error")
                    break

               prog=[]
               prog = get_program.get_prog(prog_loc)
               control_unit.start(prog)
               control_unit.set_flag()



if __name__ == '__main__':
    main()