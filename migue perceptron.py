def main():
    print("Let's print data from Arduino's analogue pins for 10secs.\n")
    sensor_gas()
    sensor_flama()
    sensor_luz()
    inputs = [[0,0,1],[analogPrinter.gas_array[-1],analogPrinter.flama_array[-1],analogPrinter.luz_array[-1]],[analogPrinter.gas_array[-5],analogPrinter.flama_array[-5],analogPrinter.luz_array[-5]],[1,1,1]]
    outputs = [0,1,1,0]

    if perceptron(inputs, outputs):
        servo()
        
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
