This code accepts either a random range of numbers (for x and y) or an equation
that consists of an x variable (in the form of y = mx^n +c or anything else that has a dependent
variable and an independent variable) and returns a graph in the form of a string that can be
printed out to the console or a dict that will be processed into a yaml file.

If you want to change the inputs, you can change the variables xpoints, given_function and the
random_points parameter in input.py. They will all be marked in ALL CAPS. Then, run either the output.py 
(and print final_graph) OR run output_to_yaml.file to get the graph.

Files (in turn of order):
input.py, 
scale.py, 
axis.py, 
xy_datapoints.py, 
format_xy_datapoints.py, 
sketch_xy_axis.py, 
datapoint_to_coordinate.py, 
plot_datapoints.py, 
spacing.py, 
output.py, 
output_to_yaml_file.py

The example of an output is graph.yaml.

Note: If you are using anything below Python 3.7, your yaml file might not appear correctly because I used the characteristic of an ordered dict, but your graph should still be able to be printed out to your console.
