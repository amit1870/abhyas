def get_permutation(array):
    permutation = []

    if len(array) < 3:
        return array

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            permutation.append((array[i], array[j]))

    return permutation


def get_triplet(array):
    permutation = []

    if len(array) < 4:
        return array

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                permutation.append((array[i], array[j], array[k]))

    return permutation


def longest_substring(vstring):
    longest = []

    if len(vstring) == 0:
        return longest, len(longest)

    prevchar = vstring[0]
    holder = [prevchar]

    for index, char in enumerate(vstring[1:]):
        if prevchar != char and char not in holder:
            holder.append(char)

        else:
            if longest == []:
                longest = holder

            elif longest and len(longest) < len(holder):
                longest = []
                longest = holder

            i = 0
            while i < len(holder):
                if holder[i] == char:
                    break
                i += 1

            holder = holder[i+1:]
            holder.append(char)

        prevchar = char

    if longest and len(longest) < len(holder):
        longest = []
        longest = holder


    return longest, len(longest)


def tankers_triplet(tankers, capacity):
    triplets = get_triplet(tankers)

    prevdiff = sum(triplets[0]) - capacity
    prevtriplet = triplets[0]

    if prevdiff == 0:
        return prevtriplet

    for index, triplet in enumerate(triplets[1:], start=1):
        diff = sum(triplet) - capacity

        if diff == 0:
            return triplet

        elif diff > 0 and prevdiff > 0 and diff < prevdiff:
            prevdiff = diff
            prevtriplet = triplet

        elif diff > 0 and prevdiff < 0:
            prevdiff = diff
            prevtriplet = triplet

    if prevdiff >= 0:
        return prevtriplet


def matrix_sum(MX, MY, MZ):
    matrix_length = max(len(MX), len(MY), len(MZ))

    MM = [[], [], []]

    for i in range(matrix_length):
        if type(MX[i]) != type([]):
            MX[i] = [MX[i]]

        if type(MY[i]) != type([]):
            MY[i] = [MY[i]]

        if type(MZ[i]) != type([]):
            MZ[i] = [MZ[i]]

        row_length = max(len(MX[i]), len(MY[i]), len(MZ[i]))


        for j in range(row_length):
            col_sum = 0
            if j < len(MX[i]):
                col_sum += MX[i][j]

            if j < len(MY[i]):
                col_sum += MY[i][j]

            if j < len(MZ[i]):
                col_sum += MZ[i][j]

            MM[i].append(col_sum)

    return MM


if __name__ == "__main__":
    tankers = [10, 20, 5, 15, 25, 40, 35, 50]
    capacity = 90
    MX = [[8,9,10], [8,7,6], [1,2,3] ]
    MY = [[0,2,3],  [8,2,6], [1,4,3] ]
    MZ = [0, [8,7,6], [1,2,3] ]

    print(matrix_sum(MX, MY, MZ))
