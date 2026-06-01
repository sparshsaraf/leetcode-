# Selection Sort
# Time: O(n^2) | Space: O(1)
# Approach: Find the minimum element in the unsorted portion,
# swap it into its correct position. At most n swaps total.

n = [20, 323, 1234, 12, 312, 4345, 6543, 75635, 3434]
for i in range(len(n)):
    min_idx = i
    for j in range(i+1, len(n)):
        if n[min_idx] > n[j]:
            min_idx = j
    n[i], n[min_idx] = n[min_idx], n[i]
print(n)