#Business Analytics Course Homework assignment 1
from math import sqrt

import numpy as np
import matplotlib.pyplot as plt


#TASK 1
utility_function = lambda w, y: w**y/y

#Subtask 1.1
x = [0, float('infinity')]

#Subtask 1.2
y_values = (0.5, 1, 0.7)
w_range = np.linspace(0, 10, 1000)

utilities = np.array([[utility_function(w_value, y_values[index]) for w_value in w_range]
                    for index in range(3)])

for index in range(3):
    plt.plot(utilities[index])

plt.show()

#Subtask 1.3


#TASK 2
def choose_consumption(consumption_value_A, consumption_value_B):
    if consumption_value_A > consumption_value_B:
        print('Ланцюжок споживання А', '\n\n')
        return
    
    elif consumption_value_A < consumption_value_B:
        print('Ланцюжок споживання А', '\n\n')
        return
    
    print('Indiffirent', '\n\n')
    

parameters = np.array((0.5, 0.7, 0.85))

prices = np.array((80, 100, 150))

consumption_A = np.array((5, 3, 2))

consumption_B = np.array((3, 3.1, 3))

subjects = lambda consumption_chain: np.power(consumption_chain, parameters)

utility_function_1 = lambda subjects: np.prod(subjects)
utility_function_2 = lambda subjects: np.sum(subjects)

subjects_consumption_chain_A = subjects(consumption_A)
subjects_consumption_chain_B = subjects(consumption_B)

#Subtask 2.1
value_consumption_chain_A  = utility_function_1(subjects_consumption_chain_A)

value_consumption_chain_B = utility_function_1(subjects_consumption_chain_B)

choose_consumption(value_consumption_chain_A, value_consumption_chain_B)

#Subtask 2.2
value_consumption_chain_A  = utility_function_2(subjects_consumption_chain_A)

value_consumption_chain_B = utility_function_2(subjects_consumption_chain_B)

choose_consumption(value_consumption_chain_A, value_consumption_chain_B)



#TASK 3

#Subtask 3.1
probabilities = np.array([0.2, 0.2, 0.3, 0.2, 0.1])

values = np.array([10000, 15000, 25000, 50000, 60000])

expected_value = probabilities.dot(values)

print(expected_value, '\n')

#Subtask 3.2

standart_deviation = sqrt(probabilities.dot(np.power(values - expected_value, 2)))

print(standart_deviation, '\n')
