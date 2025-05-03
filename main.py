import sys
import os
def read_file():
    data = b""
    if len(sys.argv) == 2 and sys.argv[1].endswith(".mf"):
        file = open(sys.argv[1])
        data = file.read().replace("\n","").replace(" ","")
        return data

code_pointer = 0
memory_stack = [0] * 30000
memory_pointer = 0
code = read_file()

def code_exec(memory_stack,code_pointer,code,memory_pointer):
    while code_pointer < len(code):
        
        if code[code_pointer] == "+":
            if memory_stack[memory_pointer] < 255:
                memory_stack[memory_pointer] += 1
            
        elif code[code_pointer] == "-":
            if memory_stack[memory_pointer] > 0:
                memory_stack[memory_pointer] -= 1

        elif code[code_pointer] == "*":
            result = memory_stack[memory_pointer] * memory_stack[memory_pointer]
            if result <= 255:
                memory_stack[memory_pointer] = result

        elif code[code_pointer] == "/":
            if code[code_pointer] != 0:
                result = int(code[code_pointer-1]/code[code_pointer])
                if result < 255:
                    memory_stack[memory_pointer] = result

        elif code[code_pointer] == "<":
            if memory_pointer > 0:
                memory_pointer -= 1
            
        elif code[code_pointer] == ">":
            if memory_pointer < 30000:
                memory_pointer += 1

        elif code[code_pointer] == "$":
            get_in = input()
            if len(get_in) == 1 and ord(get_in) <= 255:
                memory_stack[memory_pointer] = get_in

        elif code[code_pointer] == ":":
            print(chr(memory_stack[memory_pointer]))
        
        elif code[code_pointer] == "L":
            if memory_pointer != 0:
                if memory_stack[memory_pointer - 1] < memory_stack[memory_pointer]:
                    memory_stack[memory_pointer] = 1
                else:
                    memory_stack[memory_pointer] = 0
            
        elif code[code_pointer] == "G":
            if memory_pointer != 0 :
                if memory_stack[memory_pointer - 1] > memory_stack[memory_pointer]:
                    memory_stack[memory_pointer] = 1
                else:
                    memory_stack[memory_pointer] = 0

        elif code[code_pointer] == "(":
            if memory_stack[memory_pointer] == 0:
                count = 1
                while count > 0:
                    code_pointer += 1
                    if code[code_pointer] == "(":
                        count += 1
                    elif code[code_pointer] == ")":
                        count -= 1

        elif code[code_pointer] == ")":
            if memory_stack[memory_pointer] != 0:
                count = 1
                while count > 0:
                    code_pointer -= 1
                    if code[code_pointer] == ")":
                        count += 1
                    elif code[code_pointer] == "(":
                        count -= 1
        else:
            pass
        
        code_pointer += 1


code_exec(memory_stack,code_pointer,code,memory_pointer)
