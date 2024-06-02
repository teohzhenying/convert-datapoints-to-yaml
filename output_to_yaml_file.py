from ruamel.yaml import YAML
from output import final_graph_to_yaml


# Run this file to get the yaml file
yaml = YAML()
yaml.preserve_quotes = True

data = {"Coordinates": final_graph_to_yaml[
    0]}  # Since I am using a dict, and they have to be ordered, this is only suitable for Python 3.7
# and above.

# separate out the other lines into key and value
other_lines = final_graph_to_yaml[1:]
for each_line in other_lines:
    key = each_line[0]
    value = each_line[1]
    data[key] = value

with open('graph.yaml', 'w') as file:
    yaml.dump(data, file)

with open('graph.yaml', 'r') as file:
    loaded_data = yaml.load(file)
