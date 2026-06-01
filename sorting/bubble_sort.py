# Bubble Sort
# Time: O(n^2) | Space: O(1)
# Approach: Compare adjacent elements, swap if left > right.
# After each pass, largest element bubbles to end.
# Optimization: shrink inner loop by i each pass since end is already sorted.
 
n = [1, 10, 8, 4, 5]
for i in range(len(n)):
    for j in range(len(n)-1-i):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
print(n)
 
