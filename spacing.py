from sketch_xy_axis import y_numberLine
from plot_datapoints import yaml_list


# returns the longest y datapoint in length when all the y datapoints have been converted to a string
def return_largest_y_point_in_str():
    y_numberLine_in_str = [str(y) for y in y_numberLine]
    longest = max(y_numberLine_in_str, key=len)
    return len(longest)


longest_length_of_y = return_largest_y_point_in_str()


# this function aligns the spacing of all list in the list. Every list or string in list must
# have the same length as the current x marker.
def spacing():
    new_x_numberLine = yaml_list[-1]
    for row_index in range(len(yaml_list)):
        for index in range(len(yaml_list[row_index])):

            # This is for the y-axis. Every marker in the y-axis must have the same length as the
            # longest str(y-marker) so that when plotting, the x-coordinate does not 'run'.
            if index == 0:
                yaml_list[row_index][index] = str(yaml_list[row_index][index])
                len_of_curr_y_mark = len(yaml_list[row_index][index])
                if len_of_curr_y_mark < longest_length_of_y:
                    yaml_list[row_index][index] += (" " * (longest_length_of_y - len_of_curr_y_mark))

            # This is for the x-axis. If all list has the coordinate x=3, it needs to have the same
            # length as str(3).
            if type(yaml_list[row_index][index]) is list:
                x_mark = new_x_numberLine[index]
                length_of_x_mark = len(str(x_mark))
                curr_space_list = [" " for _ in range(length_of_x_mark)]
                yaml_list[row_index][index] = "".join(curr_space_list)

    return yaml_list


spacing_in_graph = spacing()
