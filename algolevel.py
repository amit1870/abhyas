def triplet_with_targetsum(array, targetsum):
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
t = triplet_with_targetsum(array, targetsum)
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
for capacity in [10, 14, 13, 15, 20, 34, 25]:
    tn = t.get_tankers(capacity)
    # print(f"{capacity} : {tn} : {sum(tn)}")


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        max_length = 0

        prv_ch = s[0]
        substring = [prv_ch]
        for ch in s[1:]:
            if prv_ch != ch and ch not in substring:
                substring.append(ch)

            else:
                if len(substring) > max_length:
                    max_length = len(substring)

                i = 0
                while i < len(substring):
                    if substring[i] == ch:
                        break
                    i += 1

                substring = substring[i+1 : ]
                substring.append(ch)

            prv_ch = ch

        if len(substring) > max_length:
            max_length = len(substring)

        return max_length


    def twoSum(self, nums, target: int):
        pair = {}
        for idx, item in enumerate(nums):

            for k, v in pair.items():
                if item + v == target:
                    return [k, idx]

            pair[idx] = item




nums = [3,2,4]
target = 6
soultion = Solution()
lens = soultion.twoSum(nums, target)
# print(lens)


def longest_substring(vstring):
    longest_length = 0
    longest = []

    if len(vstring) == 0:
        return longest_length

    prevchar = vstring[0]
    holder = [prevchar]

    for index, char in enumerate(vstring[1:]):
        if prevchar != char and char not in holder:
            holder.append(char)

        else:
            if longest == []:
                longest = holder

            if longest and len(longest) < len(holder):
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

vstring = "amitpatelsachinpatel"
longest = longest_substring(vstring)
# print(longest)



