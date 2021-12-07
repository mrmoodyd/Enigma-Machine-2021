#Engima Machine 2021
#David Moody

inputGear = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', "'", '{', '|', '}', '~', ' ']

gear1 = ['%', 'h', ';', '0', ':', '#', '^', '3', ',', 'g', 'e', 'r', 'S', 'q', 'p', 'C', 'i', 'd', 'o', '2', '+', '8', 's', 'U', 'l', 'F', 'z', 'M', '"', 'f', 'j', ' ', '5', 'K', 'b', 'k', 'H', '=', 'J', '/', 'N', 'L', 'B', 'W', '@', '_', 'n', 'w', 'Y', 'X', '~', '9', 'c', 'P', 't', '}', '<', 'E', 'm', 'I', ')', 'Q', 'v', '6', "'", 'D', '$', 'O', 'R', '*', '.', '!', 'T', '[', '{', '1', "'", '>', 'u', '-', ']', '?', 'x', '|', '7', 'V', 'Z', 'y', '(', 'a', '4', 'A', '&', 'G']
gear2 = ['8', 'f', "'", '{', 'c', 'b', 'u', 'x', '&', '5', 'J', 'S', '<', '$', 'G', 'R', 'F', '6', 'C', 'e', 'o', 'i', 'L', '_', '-', 'p', '7', 's', '@', 'T', "'", 'y', 'V', 'j', 'E', 'w', ';', 'N', 'd', 'P', 'q', 'A', '3', '^', 'O', ']', 'M', 'U', '=', '(', 'm', '9', 'B', 't', 'h', 'D', '1', '*', '/', '2', 'z', 'n', ':', '}', '4', 'Z', '|', '.', 'Y', 'K', '~', 'I', '#', 'g', 'X', 'k', '>', 'W', '0', '!', 'Q', 'l', '?', 'v', 'r', '%', ')', 'a', '"', ' ', ',', '[', 'H', '+']
gear3 = ['"', 'R', '=', ')', '|', ':', 'X', 'M', ']', 'D', '7', '.', '}', '3', 'x', 'Z', 'I', '@', '_', '8', '#', 'P', 'L', 'n', 't', '&', '$', '+', 'i', '{', 'Q', '^', '~', 'O', 'g', 'W', 'o', 'd', 'h', '[', '4', 'e', 'Y', 'H', '*', 'T', '(', 'a', 'U', 'G', '<', 'c', 'y', '9', 'b', 'E', 'v', "'", 'w', '?', 'm', 'N', 's', ' ', '5', 'k', '>', 'S', '0', 'f', 'J', 'A', 'K', 'C', 'r', '1', '-', 'F', "'", 'p', ',', '2', '6', ';', 'q', 'V', '/', 'l', 'z', '%', 'u', 'B', '!', 'j']

reflector = [['!', 'q'], ['m', 'Q'], ['Z', '^'], ['d', 'I'], ['D', 'f'], [')', '%'], ['F', 'g'], ['P', '{'], ['J', '+'], ['L', '>'], ['2', 'K'], ['6', '@'], ['[', 't'], ['H', 'l'], ['U', '<'], ['G', 'o'], ['8', 'R'], ['=', 'X'], ['M', 'h'], ['7', '5'], ['p', '*'], ['u', 'W'], ['Y', '/'], [',', '-'], ['_', ';'], ['c', '~'], ['C', '"'], ['E', 'e'], ['1', 'O'], ["'", ' '], ['y', 'V'], [':', '3'], ['A', '?'], ['a', '&'], ['r', 'i'], ['|', '#'], ['.', 'B'], ['b', '$'], ["'", 'z'], ['x', 'S'], ['4', 'w'], ['j', '}'], ['0', '9'], ['(', 'v'], ['k', 'n'], [']', 's'], ['N', 'T']]

def getInputs():
    """
    Recieves inputs for the message to encrypt, and the positions of the three gears.
    """
    inputMessage = str(input('Enter message to be encrypted:  '))
    gear1pos = int(input('Enter position of gear 1:  '))
    gear2pos = int(input('Enter position of gear 2:  '))
    gear3pos = int(input('Enter position of gear 3:  '))

    return inputMessage, gear1pos, gear2pos, gear3pos

def gearOutput(gearSide1, gearSide2, inputChar):
    """
    Calculates the output of passing a given input into a gear.
    """
    return gearSide1[gearSide2.index(inputChar)]

def turnGear(gear, n=1):
    """
    Turns the specified gear n times.  Returns the turned gear.
    """
    a = n % len(gear)
    return gear[-a:] + gear[:-a]

def encrypt(inputMessage, inputGear, gear1, gear2, gear3, reflector):
    """
    Encrypts the input message and returns the encrypted message.
    """
    outputMessage = ''
    count1 = 0
    count2 = 0

    for char in inputMessage:
        char = gearOutput(gear1, inputGear, char)
        char = gearOutput(gear2, inputGear, char)
        char = gearOutput(gear3, inputGear, char)
        for pair in reflector:
            if pair[0] == char:
                char = pair[1]
            elif pair[1] == char:
                char = pair[0]
        char = gearOutput(inputGear, gear3, char)
        char = gearOutput(inputGear, gear2, char)
        char = gearOutput(inputGear, gear1, char)

        gear1 = turnGear(gear1)
        count1 += 1

        if count1 == len(gear1):
            count1 = 0

            gear2 = turnGear(gear2)
            count2 += 1
        if count2 == len(gear2):
            count2 = 0

            gear3 = turnGear(gear3)

        outputMessage += char
    
    return outputMessage

if __name__ == '__main__':
    inputMessage, gear1pos, gear2pos, gear3pos = getInputs()

    gear1 = turnGear(gear1,gear1pos)
    gear2 = turnGear(gear2,gear2pos)
    gear3 = turnGear(gear3,gear3pos)

    outputMessage = encrypt(inputMessage, inputGear, gear1, gear2, gear3, reflector)
    print('Encrypted message:  '+outputMessage)