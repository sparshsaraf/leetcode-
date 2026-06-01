# Insertion Sort
# Time: O(n^2) | Space: O(1)
# Approach: Pick each element, shift all larger elements
# in the sorted portion one step right, drop element in place.
# Like sorting a hand of playing cards.

n = [7, 10, 3, 5, 9, 14]
for i in range(1, len(n)):
    current = n[i]
    j = i - 1
    while j >= 0 and n[j] > current:
        n[j+1] = n[j]
        j = j - 1
    n[j+1] = current
print(n)