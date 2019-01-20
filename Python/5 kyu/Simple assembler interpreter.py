def simple_assembler(program):
    registers = {}
    instructions = [instruction.split() for instruction in program]
    pc = 0
    
    while 0 <= pc < len(program):
        content = instructions[pc]
        
        if content[0] == "mov":
            if content[2].isalpha():
                registers[content[1]] = registers.get(content[2], 0)
            else:
                registers[content[1]] = int(content[2])
                
        if content[0] == "inc":
            registers[content[1]] = registers.get(content[1], 0) + 1
            
        if content[0] == "jnz":
            if content[1].isalpha():
                if registers.get(content[1], 0) != 0:
                    pc += int(content[2])
                    continue
            elif content[1] != "0":
                pc += int(content[2])
                continue
            
        if content[0] == "dec":
            registers[content[1]] = registers.get(content[1], 0) - 1
        
        pc += 1
        
    return registers
