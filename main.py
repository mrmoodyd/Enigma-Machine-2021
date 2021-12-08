#Engima Machine 2021
#David Moody

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

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

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(900,700)
        self.center()

        self.setWindowTitle('Virtual Enigma Machine')

        outerLayout = QVBoxLayout()

        topLayout = QFormLayout()
        topLayout.addRow('Input Message', QLineEdit())        

        gearHeadings = QHBoxLayout()
        label1 = QLabel('Gear 1')
        label1.setFont(QFont('Ariel', 14))
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Gear 2')
        label2.setFont(QFont('Ariel', 14))
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel('Gear 3')
        label3.setFont(QFont('Ariel', 14))
        label3.setAlignment(Qt.AlignCenter)

        gearHeadings.addWidget(label1)
        gearHeadings.addWidget(label2)
        gearHeadings.addWidget(label3)

        gearLayout = QHBoxLayout()

        initalGearPos = 50
        display1 = QLCDNumber(self)
        display1.setDigitCount(2)
        display1.display(initalGearPos)
        slider1 = QSlider(Qt.Vertical, self)
        slider1.setMinimum(0)
        slider1.setMaximum(94)
        slider1.setValue(initalGearPos)
        slider1.valueChanged.connect(display1.display)

        display2 = QLCDNumber(self)
        display2.setDigitCount(2)
        display2.display(initalGearPos)
        slider2 = QSlider(Qt.Vertical, self)
        slider2.setMinimum(0)
        slider2.setMaximum(94)
        slider2.setValue(initalGearPos)
        slider2.valueChanged.connect(display2.display)

        display3 = QLCDNumber(self)
        display3.setDigitCount(2)
        display3.display(initalGearPos)
        slider3 = QSlider(Qt.Vertical, self)
        slider3.setMinimum(0)
        slider3.setMaximum(94)
        slider3.setValue(initalGearPos)
        slider3.valueChanged.connect(display3.display)
        
        gearLayout.addWidget(display1)
        gearLayout.addWidget(slider1)
        gearLayout.addWidget(display2)
        gearLayout.addWidget(slider2)
        gearLayout.addWidget(display3)
        gearLayout.addWidget(slider3)

        outputLayout = QHBoxLayout()
        outputLabel = QLabel('Encrypted Message:  ____________')
        outputLabel.setFont(QFont('Ariel', 14))
        outputLabel.setAlignment(Qt.AlignCenter)

        outputLayout.addWidget(outputLabel)


        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(gearHeadings)
        outerLayout.addLayout(gearLayout)
        outerLayout.addLayout(outputLayout)
        self.setLayout(outerLayout)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GUI()
    sys.exit(app.exec_())

    # inputMessage, gear1pos, gear2pos, gear3pos = getInputs()

    # gear1 = turnGear(gear1,gear1pos)
    # gear2 = turnGear(gear2,gear2pos)
    # gear3 = turnGear(gear3,gear3pos)

    # outputMessage = encrypt(inputMessage, inputGear, gear1, gear2, gear3, reflector)
    # print('Encrypted message:  '+outputMessage)