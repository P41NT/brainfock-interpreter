program = list(open('input.txt', 'r').read())
prog_pos = 0
mem_pos = 0
memory = [0]

while(prog_pos < len(program)):
    if program[prog_pos] == '>':
        mem_pos += 1
        if mem_pos >= len(memory):
            memory.append(0)

    elif program[prog_pos] == '<':
        mem_pos -= 1
        if mem_pos < 0:
            print("Invalid Memory Adressed")
            break

    elif program[prog_pos] == '-':
        memory[mem_pos] -= 1

        if memory[mem_pos] == -1:
            memory[mem_pos] = 255

    elif program[prog_pos] == '+':
        memory[mem_pos] += 1
        if memory[mem_pos] == 256:
            memory[mem_pos] = 0

    elif program[prog_pos] == '[':
        if memory[mem_pos] == 0:
            depth = 0
            prog_pos += 1
            while prog_pos < len(program) :
                if program[prog_pos] == ']' and depth == 0:
                    break
                elif program[prog_pos] == '[':
                    depth += 1
                elif program[prog_pos] == ']':
                    depth -= 1
                prog_pos += 1

    elif program[prog_pos] == ']':
        if memory[mem_pos] != 0:
            depth = 0
            prog_pos -= 1
            while prog_pos >= 0:
                if program[prog_pos] == '[' and depth == 0:
                    break
                elif program[prog_pos] == ']':
                    depth += 1
                elif program[prog_pos] == '[':
                    depth -= 1
                prog_pos -= 1

    elif program[prog_pos] == '.':
        print(chr(memory[mem_pos]), end = "")

    elif program[prog_pos] == ',':
        inp = input("Input Requested. : ")
        memory[mem_pos] = ord(inp)

    prog_pos += 1