from sys import float_repr_style
import ir_lookup
import get_program
import control_unit

def print_help():
    print("TODO: Write help.")

def init_print():
     print()
     print("----------------------")
     print("|  A CPU-S Emulator  |")
     print("| by Sam M. Thompson |")
     print("----------------------")
     print()


def main():
     init_print()
     while True:
          query = input("> ")
          if query == "quit":
               break
          if query == "help":
               print_help()
          else:
               prog=[]
               prog = get_program.get_prog(query)
               control_unit.start(prog)
               control_unit.set_flag()


if __name__ == '__main__':
    main()