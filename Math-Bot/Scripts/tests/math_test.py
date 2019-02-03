from sympy import *
import numpy as np
import matplotlib.pyplot as plt
class graph:
    def __init__(self, message):
        self.do_action, self.function_1, self.function_2 = message.split()
        self.function_1 = list(self.function_1)
        self.function_2 = list(self.function_2)
        # Organize
        self.counter = 0
        while self.counter < len(self.function_1):
            if self.function_1[self.counter] == '+' or self.function_1[self.counter] == '-':
                self.function_1.insert(self.counter, ' ')
                self.function_1.insert(self.counter+2, ' ')
                self.counter += 3
            self.counter += 1
        
        self.counter = 0
        while self.counter < len(self.function_2):
            if self.function_2[self.counter] == '+' or self.function_2[self.counter] == '-':
                self.function_2.insert(self.counter, ' ')
                self.function_2.insert(self.counter+2, ' ')
                self.counter += 3
            self.counter += 1

        self.function_1 = ''.join(self.function_1)
        self.function_2 = ''.join(self.function_2)

    def plot(self):
        self.x = symbols('x')
        self.trig = ['sin']
        if self.function_1 != 'None' and self.function_2 != 'None':
            self.function_1 = sympify(self.function_1)
            self.function_2 = sympify(self.function_2)
            # Convert to numpy functions
            self.np_function_1 = lambdify(self.x, self.function_1, 'numpy')
            self.np_function_2 = lambdify(self.x, self.function_2, 'numpy')
            # Coordinates
            self.x_coor = np.arange(0, 12.56, 0.01)
            self.y_coor_f_1 = self.np_function_1(self.x_coor)
            self.y_coor_f_2 = self.np_function_2(self.x_coor)
            # Plot
            plt.style.use('ggplot')
            plt.plot(self.x_coor, self.y_coor_f_1, label='{}'.format(self.function_1), color='red')
            plt.plot(self.x_coor, self.y_coor_f_2, label='{}'.format(self.function_2), color='blue')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Graph of {} and {}'.format(self.function_1, self.function_2))
            plt.legend()
            plt.show(block=False)
            plt.savefig('graph')
            plt.pause(1)
            plt.close()
        elif self.function_2 == 'None':
            self.function_1 = sympify(self.function_1)
            self.np_function_1 = lambdify(self.x, self.function_1, 'numpy')
            self.x_coor = np.arange(0, 12.56, 0.01)
            self.y_coor_f_1 = self.np_function_1(self.x_coor)
            # Plot
            plt.style.use('ggplot')
            plt.plot(self.x_coor, self.y_coor_f_1, label='{}'.format(self.function_1), color='red')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Graph of {}'.format(self.function_1))
            plt.legend()
            plt.show(block=False)
            plt.savefig('graph')
            plt.pause(1)
            plt.close()


x = graph('!graph sin(x) cos(x)')
x.plot()