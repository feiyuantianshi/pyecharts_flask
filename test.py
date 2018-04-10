import random


def generate_3d_random_point():
    return [random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)]

data = [generate_3d_random_point() for _ in range(80)]

print(data)