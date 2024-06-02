import math
from input import set_graph_size, xpoints, ypoints


# get the x scale and y scale by dividing the (max-min numbers in the range) by the set_graph_size
# variable that was set in input.py
def scale(x_points, y_points):

    min_x_point = min(x_points)
    max_x_point = max(x_points)

    min_y_point = min(y_points)
    max_y_point = max(y_points)

    x_graph_size = set_graph_size[0]/2  # divide the scale by 2 to leave a spacing between each x-tick
    y_graph_size = set_graph_size[1]

    range_of_x_values = abs(max_x_point - min_x_point)
    range_of_y_values = abs(max_y_point - min_y_point)

    space_between_each_x_value = math.ceil(range_of_x_values / (x_graph_size - 1))  # .ceil because
    # a scale that covers a bigger range of numbers is better than a scale that covers a smaller
    # range of numbers
    space_between_each_y_value = math.ceil(range_of_y_values / (y_graph_size - 1))

    return min_x_point, min_y_point, space_between_each_x_value, space_between_each_y_value


min_x, min_y, x_tick_marks_diff, y_tick_marks_diff = scale(xpoints, ypoints)
