import numpy as np


def perceptron(inputs, outputs):

    inputs = np.array(inputs)
    outputs = np.array(outputs)

    epochs, num_inputs = 0, 0

    while num_inputs < 4:
        print('---------- epochs {} ---------- '.format(epochs))

        # se generan pesos aleatorios en el rango [-1,1]
        weights = np.array(np.random.uniform(-1, 1, inputs.shape))
        for input,weight, output in zip(inputs, weights, outputs):

            # Realiza la suma ponderada de entradas con pesos
            y_generate = input@weight

            # Función sigmoide
            y_generate = 0 if y_generate < 0 else 1

            if y_generate == output:
                num_inputs +=1
            else:
                num_inputs = 0

            print('entrada: ', input, 'pesos:', weight, 'salida_esperada: ', output, 'salida_obtenida: ',y_generate)

        epochs +=1

    return True


inputs = [[0,0,1],[0,1,1],[1,0,1],[1,1,1]]

outputs = [0,0,0,1]


perceptron(inputs, outputs)
