from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：双指针
        # 初步：先删除0再补0，缺点：delete操作会增加复杂度最多n-1，性能❌
        left = 0
        for right in range(0,len(nums)):
            if(nums[right] != 0):
                nums[left], nums[right] = nums[right], nums[left]
                # 关键：right非零时，left和right同步，实际不交换，right为0时，left不同步，开始对比交换位置
                left += 1  
        
        return nums

def run_self_tests() -> None:
    solution = Solution()  
    tests = [
        {'input': [100, 4, 0, 1, 0, 2], 'expected': [100, 4, 1, 2, 0, 0]},
        {'input': [], 'expected': []},
        {'input': [0, 0, 1], 'expected': [1,0,0]},
        {'input': [1, 2, 0, 1], 'expected': [1, 2, 1, 0]},
        {'input': [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 'expected': [9, 1, 4, 7, 3, -1, 5, 8, -1, 6, 0]},
        {'input': [10], 'expected': [10]},
        {'input': [1,2,3], 'expected': [1,2,3]},
        {'input': [0,0,0], 'expected': [0,0,0]},
    ]

    total = len(tests)
    passed = 0

    for index, case in enumerate(tests, start=1):
        result = solution.moveZeroes(case['input'])
        success = result == case['expected']
        if success:
            passed += 1
        else:
            print(f"Case {index}: input={case['input']!r}, expected={case['expected']}, got={result} -> {'PASS' if success else 'FAIL'}")

    print(f"\nPassed {passed} out of {total} test cases.")
if __name__ == '__main__':
    run_self_tests()
            