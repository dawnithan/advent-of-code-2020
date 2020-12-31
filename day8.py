def trial_n_error(index):
    with open('day8-input.txt') as file:
        data = [d.strip() for d in file.readlines()]

    # example = [
    #     'nop +0',
    #     'acc +1',
    #     'jmp +4',
    #     'acc +3',
    #     'jmp -3',
    #     'acc -99',
    #     'acc +1',
    #     'jmp -4',
    #     'acc +6'
    # ]

    success = True
    acc = 0 # accumulator
    pc = 0 # program counter

    pc_seen = []

    while True:
        # reached end of file
        if pc >= len(data):
            success = True
            break

        # detected infinite loop
        if pc in pc_seen:
            success = False
            break

        pc_seen.append(pc)

        if (pc == index):
            curr_opcode = data[pc].split(' ')[0]
            val = data[pc].split(' ')[1]
            if curr_opcode == 'jmp': curr_opcode = 'nop'
            elif curr_opcode == 'nop': curr_opcode = 'jmp'
            data[pc] = curr_opcode + ' ' + val
        
        # print(data[pc])
        opcode = data[pc].split(' ')[0]
        val = data[pc].split(' ')[1]

        if opcode  == 'nop':
            # print(f'No Operation, acc = {acc}')
            pc += 1
        elif opcode  == 'acc':
            acc += int(val)
            # print(f'Add to acc, acc = {acc}')
            pc += 1
        elif opcode  == 'jmp':
            pc += int(val)
            # print(f'Jumping to {pc}, acc = {acc}')
    
    if success:
        print(f'{success}: Acc before loop: {acc}')
    # else:
    #     print(f'{success}: Infinite loop at {index}')

for i in range(660):
    trial_n_error(i)