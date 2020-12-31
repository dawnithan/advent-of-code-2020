with open("day1-input.txt") as data:
    lines = data.readlines()
    lines = [int(d.strip()) for d in lines]

    example = [
        '1721',
        '979',
        '366',
        '299',
        '675',
        '1456'
    ]

    example = [int(x) for x in example]

    # Part 1:
    for i in range(len(lines)):
        for j in range(len(lines)):
            x = lines[i]
            y = lines[j]
            if x + y == 2020:
                print(f'{x} + {y} = 2020, so {x} * {y} = {x*y}')

    # Part 2:
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                x = lines[i]
                y = lines[j]
                z = lines[k]
                if x + y + z == 2020:
                    print(f'{x} + {y} + {z} = 2020, so {x} * {y} * {z} = {x*y*z}')