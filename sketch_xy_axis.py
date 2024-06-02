from input import set_graph_size
from axis import y_numberLine, x_numberLine

yaml_list = [[[] for x in range(set_graph_size[0] + 1)] for y in range(set_graph_size[1] + 1)]  # create
# empty graph first # this is just a list of empty lists


# sketch x-y axis
def x_y_axis():

    # sketch x-axis
    new_x_numberLine = []
    for index in range(len(x_numberLine)):
        new_x_numberLine.append(x_numberLine[index])
        new_x_numberLine.append([])

    # sketch y-axis
    yaml_list_total_length = len(yaml_list) - 1
    for height in range(len(yaml_list)):
        yaml_list[height][0] = y_numberLine[yaml_list_total_length - height]

    # this is for the x-axis
    yaml_list[-1] = new_x_numberLine
    return new_x_numberLine, yaml_list


new_x_number_line, y_axis = x_y_axis()
