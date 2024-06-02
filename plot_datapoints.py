from sketch_xy_axis import yaml_list
from datapoint_to_coordinate import dict_of_xy_to_coordinates_final


# This function loops through the graph list of lists and if it reaches a list where the index
# is in the dict, it plots an 'x'
def plot_points():
    for y in range(len(yaml_list)):
        for x in range(len(yaml_list[y])):
            if [x, y] in dict_of_xy_to_coordinates_final.values():
                yaml_list[y][x] = "x"
    return yaml_list


plot_datapoints_on_graph = plot_points()
