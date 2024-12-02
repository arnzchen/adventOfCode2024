import os
import time
from collections import Counter

dirname = os.path.dirname(__file__)
input_file = filename = os.path.join(dirname, "input.txt")

input = open(input_file, "r")

list1, list2 = [], []

for row in input:
    item1, item2 = row.split()
    list1.append(int(item1))
    list2.append(int(item2))

# part 1 - O(nlogn)
def findDifferenceOfListItems(list1, list2) -> int:
    sortedList1, sortedList2 = sorted(list1), sorted(list2)

    totalDiff = 0
    for i in range(len(sortedList1)):
        totalDiff += abs(sortedList1[i] - sortedList2[i])

    return totalDiff

# part 2 - O(n)
def findSimilarityScore(list1, list2) -> int:
    list2Counter = Counter(list2)

    simScore = 0
    for k in list1:
        simScore += (k * list2Counter[k]) if k in list2Counter else 0

    return simScore

print("Total Distance:", findDifferenceOfListItems(list1, list2))
print("Similarity Score:", findSimilarityScore(list1, list2))