from input import set_graph_size
from scale import min_x, min_y, x_tick_marks_diff, y_tick_marks_diff


# This function creates the markers for the x and y-axis. They should all have the same difference
# between each marker.
def get_number_lines(min_x, min_y, x_tick_marks_diff, y_tick_marks_diff):

    # start the number line with the smallest number in the given range of datapoints
    x_number_line = [min_x]
    y_number_line = [min_y]

    # this is for the x-axis
    for x in range(int(set_graph_size[0] / 2)):  # divided by 2 so that in the final graph, there
        # is some space between each x-axis marker
        min_x += x_tick_marks_diff
        x_number_line.append(round(min_x))

    # this is for the y-axis
    for y in range(set_graph_size[1]):
        min_y += y_tick_marks_diff
        y_number_line.append(round(min_y))

    return x_number_line, y_number_line


x_numberLine, y_numberLine = get_number_lines(min_x, min_y, x_tick_marks_diff, y_tick_marks_diff)
