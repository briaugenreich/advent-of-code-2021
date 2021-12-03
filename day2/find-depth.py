with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

    depth=0
    forward=0

    for direction in lines:
        direction_arr = direction.split(" ")
        if direction_arr[0] == "forward":
            forward+= int(direction_arr[1])
        elif direction_arr[0] == "down":
            depth+= int(direction_arr[1])
        else:
            depth-= int(direction_arr[1])
    print("DEPTH:", depth, "FORWARD:", forward)
    print("Solution:", depth*forward)

    aim=0
    horizontal_pos=0
    depth=0
    for direction in lines:
        direction_arr = direction.split(" ")
        if direction_arr[0] == "forward":
            horizontal_pos+= int(direction_arr[1])
            depth= depth + (aim * int(direction_arr[1]))
        elif direction_arr[0] == "down":
            aim+= int(direction_arr[1])
        else:
            aim-= int(direction_arr[1])

    print("DEPTH:", depth, "HORIZANTAL POSITION:", horizontal_pos)
    print("Solution:", depth*horizontal_pos)
