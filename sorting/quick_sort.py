# Quick Sort
# Time: O(n log n) average, O(n^2) worst | Space: O(n)
# Approach: Pick first element as pivot. Collect elements smaller
# than pivot in left, larger in right. Recursively sort both sides.
# Pivot ends up in its correct final position each call.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if pivot < i:
            right.append(i)
        elif pivot > i:
            left.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))