from input import xpoints, ypoints


# get pairs of (the x-datapoint and its respective y-datapoint)
def get_ordered_pairs_coordinates(x_points, y_points):
    return [(x_points[index], y_points[index]) for index in range(len(x_points))]


ordered_pair_coordinates = get_ordered_pairs_coordinates(xpoints, ypoints)
# print(ordered_pair_coordinates)
