Longest Consecutive Sequence
Find the length of the longest consecutive numbers sequence in an unsorted list.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4 (sequence: [1, 2, 3, 4])

Approach:
Use a set for fast lookups. For each number, only start counting if it’s the start of a sequence (num-1 not in set). Count consecutive numbers and track the longest streak.