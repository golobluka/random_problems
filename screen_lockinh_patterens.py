
cross_points = {(0,0),(-1, 0), (0, -1), (0,1),(1, 0)}
all_points = {(-1,-1),(-1, 0), (-1, 1), (0, -1),(0, 0), (0,1), (1, -1), (1, 0), (1,1)}
basic_dict = {
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
    new_dict = {}
    for key, value in dict.items():
        set = value.copy()
        set.add(new_point)
        new_dict[key] = set

    return new_dict

        
def check_new_lines(new_dict, new_point):
    for point in all_points - {new_point} :
        vector = (new_point[0] - point[0], new_point[1] - point[1])
        mirror_point = (vector[0] * 2 + point[0], vector[1] * 2 + point[1])
        if mirror_point not in new_dict[(0,0)] and mirror_point[0] in {-1, 0, 1} and mirror_point[1] in {-1, 0, 1}:
            print(point, new_point, mirror_point)
            new_set = new_dict[point].copy()
            new_set.discard(mirror_point)
            new_dict[point] = new_set




def paths(start, length, dict=basic_dict):
    if length == 0:
        return 1

    else:
        results = []
        for new_point in (all_points - dict[start]):
            new_dict = generate_new_dict(dict, new_point)
            if new_point in cross_points:
                check_new_lines(new_dict, new_point)

            results.append(paths(new_point, length-1, new_dict))
        return sum(results)

def calculate(point, length):
    our_dict = generate_new_dict(basic_dict, point)
    check_new_lines(our_dict, point)

    print(paths(point, length, our_dict))


calculate((0,0), 2)