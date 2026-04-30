from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 面积更新和指针移动解耦，左右滑动的目的只是为了方便计算面积
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            area = max(currentArea, area)
            if(height[left] > height[right]):
                right -= 1
            else:
                left += 1
            
        return area
    

def run_self_tests() -> None:
    solution = Solution()  
    tests = [
        {'input': [100, 4, 0, 1, 0, 2], 'expected': 10},
        {'input': [], 'expected': 0},
        {'input': [1,8,6,2,5,4,8,3,7], 'expected': 49},
        {'input': [1,1], 'expected': 1},
    ]

    total = len(tests)
    passed = 0

    for index, case in enumerate(tests, start=1):
        result = solution.maxArea(case['input'])
        success = result == case['expected']
        if success:
            passed += 1
        else:
            print(f"Case {index}: input={case['input']!r}, expected={case['expected']}, got={result} -> {'PASS' if success else 'FAIL'}")

    print(f"\nPassed {passed} out of {total} test cases.")
if __name__ == '__main__':
    run_self_tests()

            

