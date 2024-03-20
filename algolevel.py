def choose_triplet(array, targetsum):
    triplet = []
    for i, vi in enumerate(array):
        for j, vj in enumerate(array):
            for k, vk in enumerate(array):
                if i != j != k != i and sum([vi, vj, vk]) == targetsum:
                    t = sorted([vi, vj, vk])
                    if t not in triplet:
                        triplet.append(t)


    return triplet

array = [4, 7, 8, 1, 7, 8, 9]
targetsum = 23
t = choose_triplet(array, targetsum)
# print(t)
