from pyfirmata2 import Arduino
import time

PORT = "COM5"

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
        self.board.analog[0].register_callback(self.sampling_gas)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[0].enable_reporting()

    def start_flama(self):
        self.board = Arduino(PORT)
        self.board.analog[1].register_callback(self.sampling_flama)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[1].enable_reporting()

    def start_luz(self):
        self.board = Arduino(PORT)
        self.board.analog[2].register_callback(self.sampling_luz)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[2].enable_reporting()

    def sampling_gas(self, data):
        data1 = data * (5 / 1023) * 1000
        self.timestamp += 1 / self.samplingRate

        if data1 <= 0.2:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es menor al muestreo",)
            self.board.digital[2].write(0)

        else:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es mayor al muestreo",)
            self.board.digital[2].write(1)
            self.gas = 1

    def sampling_flama(self, data):
        data1 = data * (5 / 1023) * 1000
        self.timestamp += 1 / self.samplingRate

        if data1 >= 2:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es mayor al muestreo",)
            self.board.digital[3].write(0)


        else:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es menor al muestreo",)
            self.board.digital[3].write(1)
            self.flama = 1

    def sampling_luz(self, data):
        data1 = data * (5 / 1023) * 1000
        self.timestamp += 1 / self.samplingRate

        if data1 >= 1:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es mayor al muestreo",)
            self.board.digital[4].write(0)

        else:
            print(f"{round(self.timestamp, 2)}, {round(data1,2)} El valor del sensor es menor al muestreo",)
            self.board.digital[4].write(1)
            self.luz = 1

    def stop(self):
        self.board.samplingOff()
        self.board.exit()

    def start_servo(self):
        self.board = Arduino(PORT)
        self.pwm = self.board.get_pin('d:5:p')
        self.pwm.write(0.3)
        time.sleep(5)
        self.pwm.write(0.9)


def main():
    print("Let's print data from Arduino's analogue pins for 10secs.\n")
    sensor_gas()
    sensor_flama()
    sensor_luz()
    inputs = [[0,0,1],[analogPrinter.gas_array[-1],analogPrinter.flama_array[-1],analogPrinter.luz_array[-1]],[analogPrinter.gas_array[-5],analogPrinter.flama_array[-5],analogPrinter.luz_array[-5]],[1,1,1]]
    outputs = [0,1,1,0]

    if perceptron(inputs, outputs):
        servo()


# START SENSOR GAS
def sensor_gas():
    print("Sensor de gas\n")
    analogPrinter.start_gas()
    time.sleep(10)
    analogPrinter.stop()
    print("Sensor de gas terminado correctamente")
    print(analogPrinter.gas, analogPrinter.flama, analogPrinter.luz, '\n')


# START SENSOR FLAME
def sensor_flama():
    print("Sensor de flama\n")
    analogPrinter.start_flama()
    time.sleep(10)
    analogPrinter.stop()
    print("Sensor de flama terminado correctamente")
    print(analogPrinter.gas, analogPrinter.flama, analogPrinter.luz, '\n')


# START SENSOR LIGHT
def sensor_luz():
    print("Sensor de luz\n")
    analogPrinter.start_luz()
    time.sleep(10)
    analogPrinter.stop()
    print("Sensor de luminosidad terminado correctamente")
    print(analogPrinter.gas, analogPrinter.flama, analogPrinter.luz, '\n')


# Correr Servo
def servo():
    if analogPrinter.luz == 1 and analogPrinter.gas == 1 and analogPrinter.flama == 1:
        analogPrinter.start_servo()
        analogPrinter.stop()
        print('El sensado a terminado')


# Perceptron
def perceptron(inputs, outputs):

    inputs = np.array(inputs)
    outputs = np.array(outputs)

    epochs, num_inputs = 0, 0

    while num_inputs < 4:
        print('---------- epochs {} ---------- '.format(epochs))

        weights = np.array(np.random.uniform(-1, 1, inputs.shape))

        for input,weight, output in zip(inputs, weights, outputs):

            y_generate = input@weight
            y_generate = 0 if y_generate < 0 else 1

            if y_generate == output:
                num_inputs +=1
            else:
                num_inputs = 0

            print('entrada: ', input, 'pesos:', weight, 'salida_esperada: ', output, 'salida_obtenida: ',y_generate)

        epochs +=1

    return True


if __name__ == '__main__':
    analogPrinter = AnalogPrinter()
    main()
