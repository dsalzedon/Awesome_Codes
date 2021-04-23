from pyfirmata2 import Arduino
import time

PORT = Arduino.AUTODETECT


class AnalogPrinter:
    
    def __init__(self):
        # sampling rate: 10Hz
        self.samplingRate = 10
        self.timestamp = 0
        self.gas = 0
        self.flama = 0
        self.luz = 0

    def start_gas(self):
        self.board = Arduino(PORT)
        self.board.analog[0].register_callback(self.myPrintCallback)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[0].enable_reporting()

    def start_flama(self):
        self.board = Arduino(PORT)
        self.board.analog[1].register_callback(self.myPrintCallback_2)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[1].enable_reporting()

    def start_luz(self):
        self.board = Arduino(PORT)
        self.board.analog[2].register_callback(self.myPrintCallback_3)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[2].enable_reporting()

    def myPrintCallback(self, data):
        data1 = data * (5 / 1023) * 1000
        self.timestamp += 1 / self.samplingRate
        if data1 <= 0.2:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es menor al muestreo",)
            self.board.digital[2].write(0)
            print("no hay gas")
            self.gas = 0
        else:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es menor al muestreo",)
            self.board.digital[2].write(1)
            print("aqui hubo gas!")
            self.gas = 1

    def myPrintCallback_2(self, data):
        data1 = data * (5 / 1023) * 1000
        self.timestamp += 1 / self.samplingRate
        if data1 >= 2:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es mayor al muestreo",)
            self.board.digital[3].write(0)
            self.flama = 1
            print("no hay fuego")
        else:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es menor al muestreo",)
            self.board.digital[3].write(1)
            print("fuego!!")
            self.flama = 1

    def myPrintCallback_3(self, data):
        data1 = data * (5 / 1023) * 1000
        self.timestamp += 1 / self.samplingRate
        if data1 >= 1:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es menor al muestreo",)
            self.board.digital[4].write(0)

            if self.gas == 1 :
                self.board.digital[2].write(1)

            if self.flama == 1:
                self.board.digital[3].write(1)

            if self.luz == 1:
                self.board.digital[4].write(1)

            if self.luz == 1 and self.gas == 1 and self.flama == 1:
                self.board.digital[5].write(1)

        else:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es mayor al muestreo",)
            self.board.digital[4].write(1)
            self.luz = 1

            if self.gas == 1 :
                self.board.digital[2].write(1)

            if self.flama == 1:
                self.board.digital[3].write(1)

            if self.luz == 1 and self.gas == 1 and self.flama == 1:
                self.board.digital[5].write(1)
            

    def stop(self):
        self.board.samplingOff()
        self.board.exit()

analogPrinter = AnalogPrinter()

print("Let's print data from Arduino's analogue pins for 10secs.")

#  START SENSOR GAS
analogPrinter.start_gas()
time.sleep(10)
analogPrinter.stop()

print("Sensor de gas terminado correctamente")

#  START SENSOR FLAME
analogPrinter.start_flama()
time.sleep(10)
analogPrinter.stop()
print("Sensor de flama terminado correctamente")

#  START SENSOR LIGHT
analogPrinter.start_luz()
time.sleep(10)
analogPrinter.stop()
print("Sensor de luminosidad terminado correctamente")
