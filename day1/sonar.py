def find_increased_depth(depth_arr):
    count = 0
    for i in range(1, len(depth_arr)):
        if depth_arr[i] > depth_arr[i-1]:
            count+=1
    return count

def find_incresed_window_depth(depth_arr):
    count = 0
    for i in range(len(depth_arr) - 3):
        first_window = depth_arr[i] + depth_arr[i + 1] + depth_arr[i + 2]
        second_window = depth_arr[i+1] + depth_arr[i + 2] + depth_arr[i + 3]
        if second_window > first_window:
            count+=1
    return count

with open('input.txt', 'r') as input_file:
    input = [int(line.strip()) for line in input_file.readlines()]
    print("Depth increases",find_increased_depth(input), "times." )
    print("Depth WINDOW increases",find_incresed_window_depth(input), "times." )
