# this file is to format the datapoints to write at the top of the file
from xy_datapoints import ordered_pair_coordinates


def format_xy():
    string_of_formatted_datapoints = ""
    for z in ordered_pair_coordinates:
        string_of_formatted_datapoints += ("(" + str(z[0]) + ", " + str(z[1]) + ")" + " ")
    return string_of_formatted_datapoints


xy_formatted = format_xy()
