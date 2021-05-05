# Find Gradient Descent for X and Y datapoints with loss function MeanSquared Error
import numpy as np
import matplotlib.pyplot as plt

def calculate_mean_squared_error(points, slope,bias):
    total_errors = 0
    for i in np.arange(len(points)):
        point_x =points[i][0]
        points_y = points[i][1]
        y_predicted = (slope * point_x) + bias
        total_errors += np.square(points_y - y_predicted)
    mean_squared_error = total_errors/len(points)
    return mean_squared_error

def calculate_gradient_descent(points,initial_bias , initial_slope,learning_rate,n_estimator):
    current_bias = initial_bias
    current_slope = initial_slope
    n = len(points)
    for j in np.arange(n_estimator):
        gradient_slope = 0
        gradient_bias = 0
        for i in np.arange(len(points)):
            x = points[i][0]
            y = points[i][1]
            gradient_slope += (-2/n) *x *(y-((current_slope * x) + current_bias))
            gradient_bias += (-2/n) * (y-(current_slope *x) + current_bias)
        current_bias = current_bias -(learning_rate*gradient_bias)
        current_slope = current_slope -(learning_rate*gradient_slope)
        print('Epoch : {}, Slope :{} , bias: {} , mean_squared_error :{}'.format(j,current_slope, current_bias,
                                                                                 calculate_mean_squared_error(points,current_slope,current_bias)))
    return current_slope, current_bias

def run():
    points = np.genfromtxt('C:\CV\Machine_Learning\Data\GD.csv',delimiter=',')
    learning_rate = 0.0001
    initial_bias = 0
    initial_slope = 0
    n_estimators = 100
    print("Starting gradient descent at slope {} bias {} and errors {} ".format(initial_slope, initial_bias,calculate_mean_squared_error(points,initial_slope,initial_bias)))
    slope , bias = calculate_gradient_descent(points,initial_bias,initial_slope,learning_rate, n_estimators)
    print("After 1000 Epochs : slope {} bias {} and errors {} ".format(slope, bias,calculate_mean_squared_error(points,slope,bias)))

if __name__ == '__main__':
    run()