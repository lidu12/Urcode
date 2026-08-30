class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


# Example
solution = Solution()

nums = [1, 2, 3, 1]

result = solution.containsDuplicate(nums)

print(result)