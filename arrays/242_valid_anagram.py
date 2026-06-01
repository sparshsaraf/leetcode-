# 242. Valid Anagram
# Difficulty: Easy
# Time: O(n) | Space: O(n)

# Approach 1: Two dicts
# Count character frequencies in both strings separately,
# compare if both dicts are equal.

# Approach 2: One dict
# Increment count for characters in s, decrement for characters in t.
# If all values are zero at the end, strings are anagrams.
# Early exit: if lengths differ, cannot be anagram.

class Solution:
    # Approach 1
    def isAnagram_two_dicts(self, s, t):
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for j in t:
            if j in d2:
                d2[j] += 1
            else:
                d2[j] = 1
        return d1 == d2

    # Approach 2
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j in d:
                d[j] -= 1
            else:
                d[j] = -1
        for key in d:
            if d[key] != 0:
                return False
        return True