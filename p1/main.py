from perceptron import Perceptron

input = [1, 1]
p_and = Perceptron(input, [0.5, 0.5], 1)

print(p_and.output())

truth_table = [(0, 0), (0, 1), (1, 0), (1, 1)]