def triplet_by_targetsum(array, targetsum):
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

def search_pair(array):
    paired = []
    for i, vi in enumerate(array):
        for j, vj in enumerate(array):
            if vi + vj in array:
                paired.append(vi + vj)

    return paired


array = ['radha', 'krishna', 'radhakrishna', 'anuj', 'ram' ,'ramanuj', 'bharat', 'bharatanuj']
t = search_pair(array)
# print(t)


class Tanker:
    def __init__(self, tankers):
        self.tankers = tankers


    def get_tankers(self, capacity):
        cpd_capacity = capacity
        tanks = []
        tankers = sorted(self.tankers, reverse=True)

        i = 0
        while cpd_capacity > 0:
            if tankers[i] <= cpd_capacity:
                tanks.append(tankers[i])
                cpd_capacity -= tankers[i]

            elif tankers[i] > cpd_capacity:
                tanks.append(tankers[i])
                cpd_capacity -= tankers[i]
                break

            i += 1


        if sum(tanks) - capacity > 0:
            # optimize if possible with one level dynamic
            last_tank = tanks[-1]
            tanks = tanks[:-1]
            rtanks = []

            rem_capacity = capacity - sum(tanks)


            j = -1
            while rem_capacity > 0 and j >= - len(self.tankers):
                rtanks.append(self.tankers[j])
                rem_capacity -= sum(rtanks)
                j -= 1

            if sum(rtanks) < last_tank:
                tanks.extend(rtanks)
            else:
                tanks.append(last_tank)

        return tanks

tankers = [10, 8, 7, 6, 4, 2]
capacity = 19
t = Tanker(tankers)
print(t.tankers)
for capacity in [10, 14, 13, 15, 20, 34, 25]:
    tn = t.get_tankers(capacity)
    # print(f"{capacity} : {tn} : {sum(tn)}")

