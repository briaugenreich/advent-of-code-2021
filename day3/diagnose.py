def find_power_consumption(input_arr):
    STRING_LENGTH = len(input_arr[0])
    gamma = ""
    epsilon = ""
    for pos in range(STRING_LENGTH):
        pos_bits = list(map(lambda x: x[pos], input_arr))
        # print(pos_bits)
        zeros = pos_bits.count('0')
        ones = pos_bits.count('1')
        if zeros > ones :
            gamma+= '0'
            epsilon += '1'
        else:
            gamma+= '1'
            epsilon += '0'


    print ("Gamma:", gamma, "-->", int(gamma, 2),  "Epsilon:", epsilon, "-->", int(epsilon, 2))
    print ("Power Consumption=", int(gamma, 2)*int(epsilon, 2))

def oxygen_generator_rating(pos, arr):
    if len(arr) == 1:
        print("Oxygen Generator Rating", arr[0], "-->", int(arr[0], 2))
        return int(arr[0], 2)
    else:
        pos_bits = list(map(lambda x: x[pos], arr))
        zeros = pos_bits.count('0')
        ones = pos_bits.count('1')
        if ones >= zeros:
            remaining_vals = list(filter(lambda x: x[pos] == '1', arr))
        else:
            remaining_vals = list(filter(lambda x: x[pos] == '0', arr))
        new_pos = pos + 1
        return oxygen_generator_rating(new_pos, remaining_vals)

def co2_scrubber_rating(pos, arr):
    if len(arr) == 1:
        print("CO2 Scrubber Rating", arr[0], "-->", int(arr[0], 2))
        return int(arr[0], 2)
    else:
        pos_bits = list(map(lambda x: x[pos], arr))
        zeros = pos_bits.count('0')
        ones = pos_bits.count('1')
        if ones < zeros:
            remaining_vals = list(filter(lambda x: x[pos] == '1', arr))
        else:
            remaining_vals = list(filter(lambda x: x[pos] == '0', arr))
        new_pos = pos + 1
        return co2_scrubber_rating(new_pos, remaining_vals)

def find_life_support_rating(input_arr):
    #oxygen generator rating x CO2 scrubber rating.
    print("Life Support Rating", oxygen_generator_rating(0,input_arr ) * co2_scrubber_rating(0, input_arr))




with open('input.txt', 'r') as input_file:
    input = [line.strip() for line in input_file.readlines()]

find_power_consumption(input)
find_life_support_rating(input)
