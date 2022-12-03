with open("input.txt", "r") as f:
    lines = f.readlines()    
    lptr = 0
    rptr = 2

    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

    while rptr < len(lines):
        lines[lptr] = sum(lines[lptr:lptr+3])
        lptr += 1
        rptr += 1

    total_sum = 0
    previous = lines[0]

    for i in range(len(lines)):
        if i == lptr:
            break
        line = lines[i]

        if line > previous:
            total_sum += 1

        previous = line

    print(total_sum)
