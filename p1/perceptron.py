class Perceptron():
    def __init__(self, name, inputs, weights, bias):
        if len(inputs) != len(weights):
            raise ValueError("The number of inputs must be equal to the number of weights.")
        self.name = name
        self.inputs = inputs
        self.weights = weights
        self.bias = bias

    def __str__(self):
        return f"Perceptron '{self.name}' with input weights {self.weights} and bias {self.bias}."
    
    def output(self):
        for i in range(len(self.inputs)):
            self.inputs[i] *= self.weights[i]
        return int(sum(self.inputs) - self.bias >= 0)