######### DAY 5 ##########
from itertools import permutations

opcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def run_amplifier(gen_opcode, phase_setting, input_val):
    ###
    first_input_indicator = True

    index = 0
    status = 'running'
    opcode = gen_opcode.copy()

    while status == 'running':
        num_digits = len(str(opcode[index]))
        code = (int(str(opcode[index])[-2:]) if num_digits > 1 else opcode[index])
        mode_1 = (int(str(opcode[index])[-3]) if num_digits > 2 else 0)
        mode_2 = (int(str(opcode[index])[-4]) if num_digits > 3 else 0)
        mode_3 = (int(str(opcode[index])[-5]) if num_digits > 4 else 0)

        if code == 1:
            output_position = opcode[index + 3]
            input_1 = (opcode[opcode[index+1]] if mode_1 == 0 else opcode[index+1])
            input_2 = (opcode[opcode[index+2]] if mode_2 == 0 else opcode[index+2])
            opcode[output_position] = input_1 + input_2
            index = index + 4
        elif code == 2:
            output_position = opcode[index + 3]
            input_1 = (opcode[opcode[index+1]] if mode_1 == 0 else opcode[index+1])
            input_2 = (opcode[opcode[index+2]] if mode_2 == 0 else opcode[index+2])
            opcode[output_position] = input_1 * input_2
            index = index + 4
        elif code == 3:
            if first_input_indicator:
                value = phase_setting
                first_input_indicator = False
            else:
                value = input_val
            output_position = opcode[index + 1]
            #value = int(input("Give me an integer value: "))
            opcode[output_position] = value
            index = index + 2
        elif code == 4:
            output = (opcode[opcode[index + 1]] if mode_1 == 0 else opcode[index + 1])
            #print("this is my output: ", output)
            index = index +2
        elif code == 5:
            test =  (opcode[opcode[index+1]] if mode_1 == 0 else opcode[index+1])
            if test != 0:
                index = (opcode[opcode[index+2]] if mode_2 == 0 else opcode[index+2])
            else:
                index += 3
        elif code == 6:
            test =  (opcode[opcode[index+1]] if mode_1 == 0 else opcode[index+1])
            if test == 0:
                index = (opcode[opcode[index+2]] if mode_2 == 0 else opcode[index+2])
            else:
                index += 3
        elif code == 7:
            input_1 = (opcode[opcode[index+1]] if mode_1 == 0 else opcode[index+1])
            input_2 = (opcode[opcode[index+2]] if mode_2 == 0 else opcode[index+2])
            output_position = opcode[index + 3]
            if input_1 < input_2:
                opcode[output_position] = 1
            else:
                opcode[output_position] = 0
            index += 4
        elif code == 8:
            input_1 = (opcode[opcode[index+1]] if mode_1 == 0 else opcode[index+1])
            input_2 = (opcode[opcode[index+2]] if mode_2 == 0 else opcode[index+2])
            output_position = opcode[index + 3]
            if input_1 == input_2:
                opcode[output_position] = 1
            else:
                opcode[output_position] = 0
            index += 4
            
        elif code == 99:
            status = 'halt'
        else:
            status = "problem"
    return output

def run_amplifier_sequence(opcode, phase_sequence):
    input_val = 0
    for phase in phase_sequence:
        input_val = run_amplifier(opcode, phase, input_val)
    return(input_val)

filename = "data/day7.txt"

if __name__ == '__main__':
    with open(filename) as f:
        opcode = f.readlines()
    opcode = [int(x) for x in opcode[0].split(",")]
    #opcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    max_output = -1
    for perm in permutations([0,1,2,3,4]):
        output = run_amplifier_sequence(opcode, perm)
        if output > max_output:
            print(output, perm)
            max_output = output


