file_path = "E:\Visual Studio Code\Python\Advent of Code - 2024\Day 1\Input.txt"

def similarity(file_path):
    left_side = []
    right_side = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_side.append(left)
            right_side.append(right)
        
        left_side.sort()
        right_side.sort()

    right_count = {}
    for num in right_side:
        right_count[num] = right_count.get(num, 0) + 1

    similarity_score = 0
    for num in left_side:
        if num in right_side:
            similarity_score += num * right_count[num]

    return similarity_score

print(similarity(file_path))