import sys
from collections import deque

# _ _ _ 

# -[----->+<]>--.-..+++++++++.-------.--.+.++++++++.

# ++++++++++[>++++++++++<-]>.
# ++[>++++++<-]>.
# ++++++++++[>++[>++++++<-]<-]>>.

# ++++[>+++++<-]>[<+++++>-]+<+[
# >[>+>+<<-]++>>[<<+>>-]>>>[-]++>[-]+
# >>>+[[-]++++++>>>]<<<[[<++++++++<++>>-]+<.<[>----<-]<]
# <<[>>>>>[>>>[-]+++++++++<[>-<-]+++++++++>[-[<->-]+[<<<]]<[>+<-]>]<<-]<<-
# ]


class Brainfuck:

    tape = None
    ptr = None

    def bfloop(self, program, startIndex):
        i = startIndex
        while i < len(program):
            token = program[i]

            if token == "[":
                endofloop = self.bfloop(program, i+1)
                i = endofloop
            elif token == "]":
                if self.tape[self.ptr] == 0:
                    return i+1
                else:
                    # print(self.tape[self.ptr])
                    i = startIndex
            else:
                self.runtoken(program, i)
                i += 1

            # print(i)

    def loopend(self, program, startIndex):
        stack = 1
        i = startIndex
        while stack > 0:
            if program[i] == "[":
                stack += 1
            elif program[i] == "]":
                stack -= 1
            i += 1
        return i-1

    def runtoken(self, program: str, startIndex: int):

        token = program[startIndex]

        if token == ">":
            self.ptr += 1
        elif token == "<":
            self.ptr -= 1
        elif token == "+":
            self.tape[self.ptr] = (self.tape[self.ptr] + 1) % 256
        elif token == "-":
            self.tape[self.ptr] = (self.tape[self.ptr] - 1) % 256
        elif token == ".":
            print( chr(self.tape[self.ptr]), end="" )
        elif token == ",":
            s = input()
            if len(s) > 1:
                s = s[0]

    def runbf(self, program: str):
        
        # initialise the self.tape and pointer
        self.ptr = 0
        self.tape = [0] * 300_000
        returnStack = deque()

        i = 0
        while i < len(program):
            # print(i, self.ptr)
            token = program[i]
            # print(i)
            if token == "[":
                
                endofloop = self.loopend(program, i+1)
                if self.tape[self.ptr] == 0:
                    i = endofloop+1
                else:
                    returnStack.append(i)
                    i += 1
            elif token == "]":
                i = returnStack.pop()
            else:
                self.runtoken(program, i)
                i += 1

            # print(i)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        # read program from file
        program_file = sys.argv[1]
        program = open(program_file).readlines()
        program = "".join(program)
        Brainfuck().runbf(program)
    else:
        # stdin run
        print("enter your program (Ctrl-D when done):")
        program = sys.stdin.readlines()
        program = "".join(program)
        Brainfuck().runbf(program)



