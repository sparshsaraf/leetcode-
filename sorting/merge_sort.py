# Merge Sort
# Time: O(n log n) | Space: O(n)
# Approach: Recursively split array in half until single elements,
# then merge sorted halves back together using two pointers.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_arr = len(arr) // 2
    left = merge_sort(arr[:mid_arr])
    right = merge_sort(arr[mid_arr:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([7, 3, 5, 1, 9, 14]))