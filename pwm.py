from pyfirmata2 import Arduino


PORT = 'COM5'


board = Arduino(PORT)

pwm = board.get_pin('p:3:o')

pwm.write(0.5)
