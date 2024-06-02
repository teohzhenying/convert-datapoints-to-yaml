# USER MUST INPUT THEIR NUMBERS HERE
import random

set_graph_size = (32, 11)  # this will be the size of the final graph
# I used this ratio of x to y so that it looks nice at the end because the y-axis will
# 'extend' longer than the x-axis if the ratio is 1:1

random.seed(44)  # for reproducibility


# this function generates the datapoints. There are two options: to get 5 random datapoints
# for (x,y) or to input your own function and x datapoints (and you will get the y-datapoint).
# If you want to input your own function, change the value of the xpoints and given_function
# variables (marked in ALL CAPS) and enter the parameter random_points as False when calling the
# generate_points function below (also marked in ALL CAPS)
def generate_points(random_points=True):

    if random_points:
        xpoints = [random.randrange(-10, 39) for _ in range(5)]
        ypoints = [random.randrange(-10, 39) for _ in range(5)]

    else:
        xpoints = [-5, 5, 10, -20, -25, -30]  # ENTER X COORDINATES HERE

        def get_y_val(x):
            given_function = 2 * x + 3  # ENTER FUNCTION HERE (in mx+c format)
            y_val = given_function
            return y_val

        ypoints = [get_y_val(x) for x in xpoints]

    return xpoints, ypoints


xpoints, ypoints = generate_points()  # ENTER False HERE
