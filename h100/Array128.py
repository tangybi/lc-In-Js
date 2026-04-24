from typing import List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 思路：使用哈希表存储所有数字，遍历每个数字，如果它的前一个数字不存在，则从该数字开始向后查找连续的数字，记录连续长度，更新最长长度。
        if not nums:
            return 0

        nums:Set[int] = set(nums)
        l = 1
        for num in nums:
            if num - 1 not in nums:
                c_n = num
                c_l = 1
                while c_n + 1 in nums:
                    c_n += 1
                    c_l += 1
                l = max(l, c_l)
        return l


def run_self_tests() -> None:
    solution = Solution()
    tests = [
        {'input': [100, 4, 200, 1, 3, 2], 'expected': 4},
        {'input': [], 'expected': 0},
        {'input': [1, 2, 0, 1], 'expected': 3},
        {'input': [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 'expected': 7},
        {'input': [10], 'expected': 1},
    ]

    total = len(tests)
    passed = 0

    for index, case in enumerate(tests, start=1):
        result = solution.longestConsecutive(case['input'])
        success = result == case['expected']
        if success:
            passed += 1
        print(f"Case {index}: input={case['input']!r}, expected={case['expected']}, got={result} -> {'PASS' if success else 'FAIL'}")

    print(f"\nPassed {passed} out of {total} test cases.")


if __name__ == '__main__':
    run_self_tests()
