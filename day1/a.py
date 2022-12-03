with open("input.txt", "r") as f:
    lines = f.readlines()

    total_sum = 0
    previous = int(lines[0].strip())
    
    for line in lines:
        l = line.strip()
        
        if int(l) > previous:
            total_sum += 1

        previous = int(l)

    print(total_sum)