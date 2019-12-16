import operator


day2_data = []

day2_data = open("day2.in").read().rstrip().split(",")

day2_data = [int(i) for i in day2_data]

def opcodecomp(day2_input, noun = None, verb = None):

    #Preset Computer to 1202 state
    day2_input[1] = noun
    day2_input[2] = verb

    i= 0
    temp = 0

    for i in range (0, len(day2_input), 4):
        operator = day2_input[i]
        position1 =  day2_input[day2_input[i+1]]
        position2 =  day2_input[day2_input[i+2]]
        if operator == 99:
            break
        elif  operator == 1:
            day2_input[day2_input[i+3]] = position1 + position2
        elif operator == 2:
            day2_input[day2_input[i+3]] = position1 * position2


    return day2_input[0]


part1 = opcodecomp(day2_data[:],12,2)


print("Part 1: ", part1)

def part2():
    for noun in range(1,100):
        for verb in range(1,100):
            #print(noun, verb)
            if opcodecomp(day2_data[:], noun, verb) == 19690720:
                print("Part 2", 100*noun+verb)
                break



part2()
