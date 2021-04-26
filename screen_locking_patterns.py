
cross_points = {(0,0),(-1, 0), (0, -1), (0,1),(1, 0)}
all_points = {(-1,-1),(-1, 0), (-1, 1), (0, -1),(0, 0), (0,1), (1, -1), (1, 0), (1,1)}
basic_dict = { #Dictionary actually shows which points are not in range, instead of storing those which can be reached. This has been found to also generate some bad consequeces. 
    (-1, 1) : {(-1, 1),(1,1), (1, -1), (-1, -1)},
    (1, 1) : {(1, 1),(-1,1), (1, -1), (-1, -1)},
    (-1, -1) : {(1,1), (1, -1), (-1, 1),(-1, -1)},
    (1, -1) : {(1,1), (-1, -1), (1, -1), (-1, 1)},
    (0,1): {(0,1),(0,-1)},
    (0,-1): {(0,-1),(0,1)},
    (1,0): {(1,0),(-1, 0)},
    (-1,0): {(-1, 0),(1,0)},
    (0,0): {(0,0)}
}

def generate_new_dict(dict, new_point):
    ''' Generates copy of a dictionary, in which we add the point we have currently reached, thus preventing it to be reached again. '''
    new_dict = {}
    for key, value in dict.items():
        set = value.copy()
        set.add(new_point)
        new_dict[key] = set

    return new_dict
       
def check_new_lines(new_dict, new_point):
    ''' For every point (except the one we just added) we look to see, if any new connection is possible since the 'new_point' has been added. Here we have taken geometric aproach (as our field of points is structured as a plain), to find the point across the 'new_point' which we cal mirror_point. Maybe this way seems to elaborate for such a simple task but is choosen so that all the casses collapse into one idea. ''' 
    for point in all_points - {new_point} :
        vector = (new_point[0] - point[0], new_point[1] - point[1]) # vec(AB) = B - A
        mirror_point = (vector[0] * 2 + point[0], vector[1] * 2 + point[1]) # mirror_point = point + 2*vec
        if mirror_point not in new_dict[(0,0)] and mirror_point[0] in {-1, 0, 1} and mirror_point[1] in {-1, 0, 1}:
            new_set = new_dict[point].copy()
            new_set.discard(mirror_point)
            new_dict[point] = new_set

def paths(start, length, dict=basic_dict):
    if length <= 1:
        return 1
    else:
        new_dict = generate_new_dict(dict, start)
        if start in cross_points:
            check_new_lines(new_dict, start)

        sum = 0
        for new_line in all_points - dict[start]:
            sum += paths(new_line, length-1, new_dict)

        return sum

#print(paths((0,0), 3, basic_dict))