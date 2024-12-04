file_path = "E:\Visual Studio Code\Python\Advent of Code - 2024\Day 1\Input.txt"

def distance_calculator(file_path):
    left_side = []
    right_side = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_side.append(left)
            right_side.append(right)
        
        left_side.sort()
        right_side.sort()

    total_distance = 0
    for i in range(len(left_side)):
        total_distance += abs(left_side[i] - right_side[i])

    return total_distance


print(distance_calculator(file_path))