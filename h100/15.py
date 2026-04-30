from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move left and right, skipping duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
    def test(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        i = 0
        n = len(nums)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            # 和不用重复计算
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            while(left < right):
                target = nums[left] + nums[right]
                if(target == -nums[i]):
                    arr.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while(left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while(left < right and nums[right] == nums[right - 1]):
                        right -= 1
                elif(target < -nums[i]):
                    left += 1
                else:
                    right -= 1
        return arr
    
def run_self_tests() -> None:
    solution = Solution()  
    tests = [
        {'input': [-2,0,1,1,2], 'expected': [[-2,0,2],[-2,1,1]]},
        
    ]

    total = len(tests)
    passed = 0

    for index, case in enumerate(tests, start=1):
        result = solution.test(case['input'])
        success = result == case['expected']
        if success:
            passed += 1
        else:
            print(f"Case {index}: input={case['input']!r}, expected={case['expected']}, got={result} -> {'PASS' if success else 'FAIL'}")

    print(f"\nPassed {passed} out of {total} test cases.")
if __name__ == '__main__':
    run_self_tests()

