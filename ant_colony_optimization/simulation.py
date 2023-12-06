from attraction import Attraction


def load_points_from_file(file_path):
    attractions = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.split()
            identifier = int(data[0])
            x = int(data[1])
            y = int(data[2])
            attractions.append(Attraction(identifier, x, y))
    return attractions



file_path = "data/A-n32-k5.txt"
attractions = load_points_from_file(file_path)
