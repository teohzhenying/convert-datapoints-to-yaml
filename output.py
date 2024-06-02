from spacing import yaml_list, longest_length_of_y
from format_xy_datapoints import xy_formatted


# This function shows the graph in the console and also creates a list of list for the yaml file.
# To get the yaml file, run output_to_yaml_file.py
def show_graph():

    yaml_graph = """"""
    yaml_graph += xy_formatted
    yaml_graph += '\n\n'

    graph_to_yaml = [[xy_formatted]]  # this is for the yaml file

    for each_row in range(len(yaml_list)):

        # this is to print out in the console. You can see the result by calling print(final_graph)
        # at the end of this file.
        curr_list = [str(i) for i in yaml_list[each_row]]
        processed_list_into_string = "".join(curr_list)
        yaml_graph += processed_list_into_string
        yaml_graph += '\n'

        # this is to create the final yaml file. I treat the first value (equal to the length of
        # the markers on the y-axis) as the key and the rest as the value so that it is formatted
        # nicely.
        graph_to_yaml.append([processed_list_into_string[0:longest_length_of_y],
                              processed_list_into_string[longest_length_of_y:]])

    return yaml_graph, graph_to_yaml


final_graph, final_graph_to_yaml = show_graph()  # You can print this function call to see
# the output of the graph in the console but I will be using a list of lists to create the yaml file.
