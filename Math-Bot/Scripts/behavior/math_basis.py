from sympy import *
import numpy as np
import matplotlib.pyplot as plt
expressions = { 'Exponent:': '**', 
                'Add or Sub:': '+ or -', 
                'Division:': '/', 
                'Natural log:': 'exp(variable)',
                'Transcendtal Function:': 'sin(variable)',
                'Infinite Bounds:': '-oo, oo',
                'Example:': '-> sin(x) + 2*x**2',
                'Sums and Subs:' : 'sin(x)+cos(x): Space in between terms (Not applicable for multiplication)',
                'Solve equation:' : 'y=x**2+x-1'
             }
class calculus():
    def __init__(self, message):
        self.do_action, self.function, self.bound_a, self.to,  self.bound_b = message.split()
        self.x, self.y = symbols('x y')
    def message_decoder(self):
        '''
            Message decoder is in charged of determining which 
            calclulus action to take do. Determines if a graph is
            needed, and provies useful infoimrastion to the user.
        '''
        # Fixed users input 
        self.function = list(self.function)
        self.counter = 0
        # Space out both + and - symbols
        while self.counter < len(self.function):
            if self.function[self.counter] == '+':
                self.function.insert(self.counter,  ' ')
                self.function.insert(self.counter+2, ' ')
                self.counter += 3
            elif self.function[self.counter] == '-':
                self.function.insert(self.counter, ' ')
                self.function.insert(self.counter+2, ' ')
                self.counter += 3
            self.counter += 1

        
        self.function = ''.join(self.function)
        self.function = sympify(self.function)

        # Decision
        if self.do_action == '!integrate':
            if self.bound_a != 'None' and self.bound_b != 'None':
                self.bound_a = float(self.bound_a)
                self.bound_b = float(self.bound_b)
                self.data = calculus.integration(self, '')
                return self.data, calculus.integration(self, None)
            else:
                self.bound_a = None
                self.bound_b = None
                self.data = calculus.integration(self, None)
                return self.data
        elif self.do_action == '!diff':
            self.data = calculus.differentiation(self)
            return self.data

    def integration(self, trigger):
        self.trigger = trigger
        print(self.trigger)
        if self.trigger != None:
            self.definitive_integral = integrate(self.function, (self.x, self.bound_a, self.bound_b))
            calculus.evaluate(self)
            return self.definitive_integral
        else:
            self.indefinitive_integral = integrate(self.function, self.x)
            return self.indefinitive_integral

    def differentiation(self):
        self.derivative = diff(self.function, self.x)
        return self.derivative

    def evaluate(self):
        # Get integration
        self.function_ = calculus.integration(self, None)
        # Transform SymPy Function to numpy function
        self.np_function = lambdify(self.x, self.function_, 'numpy')
        self.np_orignal_function = lambdify(self.x, self.function, 'numpy')
        # Coordinates
        self.x_coor = np.arange(self.bound_a, self.bound_b, 0.01)
        self.y = self.np_function(self.x_coor)
        self.x_original = np.arange(self.bound_a, self.bound_b, 0.01)
        self.y_original = self.np_orignal_function(self.x_original)
        # Displaying Data
        print('The integration of ' + str(self.function) + ' is \n' + str(self.function_))
        print('From ' + str(self.bound_a) + ' and ' + str(self.bound_b))
        plt.style.use('ggplot')
        plt.plot(self.x_coor, self.y, label='{}'.format(self.function_), color='red')
        plt.plot(self.x_original, self.y_original, label='{}'.format(self.function), color='blue')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(r'$\int {}dx = {} + C $'.format(self.function, self.function_))
        plt.fill_between(self.x_coor, 0, self.y)
        plt.legend()
        plt.show(block=False)
        plt.savefig('integration')
        plt.pause(1)
        plt.close()

class algebra:
    def __init__(self, message):
        self.do_action, self.function = message.split()
        print('My function', self.function)
        self.x, self.y = symbols('x y')
    def solver(self):
        # Separate y and x
        self.y_equation, self.x_equation = self.function.split('=')
        self.y_equation = sympify(self.y_equation)
        self.x_equation = sympify(self.x_equation)
        print(self.x_equation, self.y_equation)
        self.data = solveset(Eq(self.x_equation, self.y_equation), self.y)
        return self.data

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