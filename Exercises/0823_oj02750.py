def calculate_animals(num_legs):
    if num_legs % 2 != 0:
        return 0, 0
    if num_legs % 4 == 0:
        min_animals = num_legs // 4
    else:
        min_animals = num_legs // 4 + 1

    max_animals = num_legs // 2
    return min_animals, max_animals


num_legs = int(input())

min_animals, max_animals = calculate_animals(num_legs)
print(min_animals, max_animals)
