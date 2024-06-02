# This file gets the coordinates of the datapoints (xpoints and ypoints) in the final graph


from xy_datapoints import ordered_pair_coordinates
from axis import x_numberLine, y_numberLine


# returns the index of the nearest marker
def get_nearest_coordinate(curr_num, first_num, first_index, second_num, second_index):
    diff_a = abs(first_num - curr_num)
    diff_b = abs(second_num - curr_num)
    if diff_a > diff_b:
        return second_index
    return first_index


# get the value of the invisible markers (the space between x1 and x2 on the x-axis).
# They will not appear visually on the final graph.
def get_all_x():
    new_x_number_line_with_invisible_markers_draft = [(x_numberLine[i],
                                                       ((x_numberLine[i] + x_numberLine[i + 1]) / 2))
                                                      for i in range(len(x_numberLine) - 1)]
    new_x_number_line_with_invisible_markers = []
    for x in new_x_number_line_with_invisible_markers_draft:
        new_x_number_line_with_invisible_markers.append(x[0])
        new_x_number_line_with_invisible_markers.append(x[1])
    if x_numberLine[-1] not in new_x_number_line_with_invisible_markers:
        new_x_number_line_with_invisible_markers.append(x_numberLine[-1])
    return new_x_number_line_with_invisible_markers


all_x = get_all_x()


# This function converts the x datapoint into the coordinate on the graph. This function returns a
# dict where the key is a tuple of the given (x-datapoint, y-datapoint) and the value is
# [the final x-coordinate, the given y-datapoint]
def x_datapoint_to_coordinate(ordered_pair):

    dict_of_datapoints_and_coordinates = {}

    for each_xy_pair in ordered_pair:

        if each_xy_pair not in dict_of_datapoints_and_coordinates.keys():  # check if the datapoint
            # is already in the final dict

            for a_index in range(len(all_x)):

                # check if the given x-coordinate is equal to any number on the x-axis
                if all_x[a_index] == each_xy_pair[0]:
                    dict_of_datapoints_and_coordinates[each_xy_pair] = [a_index, each_xy_pair[1]]

                # if not, then choose the nearest number (between the smaller number or the
                # bigger number) using the function get_nearest_coordinate
                else:
                    if all_x[a_index] < each_xy_pair[0] < all_x[a_index + 1]:
                        dict_of_datapoints_and_coordinates[each_xy_pair] = \
                            [get_nearest_coordinate(each_xy_pair[0], all_x[a_index], a_index,
                             all_x[a_index + 1], a_index + 1), each_xy_pair[1]]

    return dict_of_datapoints_and_coordinates


dict_of_xy_to_coordinates = x_datapoint_to_coordinate(ordered_pair_coordinates)


# This function returns a dict where the key is the (given x-coordinate, given y-coordinate) and the
# value is the [final x-coordinate from the x_datapoint_to_coordinate function, final y-coordinate]
def y_datapoint_to_coordinate():

    reversed_y_number_line = y_numberLine[::-1]  # reverse the number line because the final output
    # has a y-axis that 'starts' with the biggest number

    for datapoint, coordinate in dict_of_xy_to_coordinates.items():

        y = datapoint[1]

        for each_y_tick in range(len(reversed_y_number_line)):

            # check if the given y-coordinate is equal to any number on the y-axis
            if y == reversed_y_number_line[each_y_tick]:
                dict_of_xy_to_coordinates[datapoint][1] = each_y_tick

            # if not, then choose the nearest number (between the smaller number or the
            # bigger number)
            elif reversed_y_number_line[each_y_tick] < y < reversed_y_number_line[each_y_tick - 1]:
                dict_of_xy_to_coordinates[datapoint][1] = (
                    get_nearest_coordinate(y, reversed_y_number_line[each_y_tick],
                                           each_y_tick, reversed_y_number_line[each_y_tick - 1],
                                           each_y_tick - 1))

    return dict_of_xy_to_coordinates


dict_of_xy_to_coordinates_final = y_datapoint_to_coordinate()
