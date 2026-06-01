# 217. Contains Duplicate
# Difficulty: Easy
# Time: O(n) | Space: O(n)

# Approach 1: List — O(n^2) time
# Store seen elements in a list, check membership each time.
# Slow because checking membership in a list is O(n).

# Approach 2: Set — O(n) time
# Use a set instead. Membership check in a set is O(1) due to hashing.
# Hashing converts a value directly to a location, no scanning needed.

# Approach 3: One liner
# Convert to set (removes duplicates), compare length with original.

class Solution:
    # Approach 2
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

    # Approach 3
    def containsDuplicateOneLiner(self, nums):
        return len(set(nums)) != len(nums)