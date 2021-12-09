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




with open('input.txt', 'r') as input_file:
    input = [line.strip() for line in input_file.readlines()]

find_power_consumption(input)
