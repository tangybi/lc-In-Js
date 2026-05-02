#%% 接雨水 双指针
#  min(maxLeft, maxRight) - height[i]
from typing import List
import math


class Solution:
    def trap(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        maxL = -math.inf
        maxR = -math.inf
        nums = 0
        while(left < right):
            if(arr[left] <= arr[right]):
                
                if(arr[left] > maxL):
                    maxL = arr[left]
                nums += maxL - arr[left]
                left += 1
            else:
                
                if(arr[right] > maxR):
                    maxR = arr[right]
                nums += maxR - arr[right]
                right -= 1
        return nums
if __name__ == "__main__":    
    solver = Solution()
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 0),
        ([3, 3, 3, 3], 0),
        ([], 0),
        ([2], 0),
        ([5, 0, 5], 5),
    ]

    for i, (height, expected) in enumerate(test_cases):
        result = solver.trap(height)
        status = (
            "通过"
            if result == expected
            else f"失败 (期望 {expected}, 实际 {result})"
        )
        print(f"测试用例{i + 1}: {status}")

#%% 每日温度 单调栈
# 单调栈适用于 上（下）一个最大（小）元素
from typing import List

class solution:
    def every_tem(self, tmp: List[int]) -> List[int]:
        n = len(tmp)
        # 记录索引差
        arr = [0] * n
        # 记录当前栈
        st = []
        for i,t in enumerate(tmp):
            # 大于栈顶
            while st and t > tmp[st[-1]]:
                j = st.pop()
                # 记录大于最大值时的天数差 
                arr[j] = i - j
            st.append(i)
        return arr
    def trap(self, height: List[int]) -> int:
        n = len(height)
        nums = 0
        st = []
        for i,t in enumerate(height):
            while st and t > height[st[-1]]:
                top = st.pop()
                nums += height[top] - height[i]
            st.append(i)
        return nums
    
# 请将原有的 if __name__ == "__main__": 部分替换为以下代码：

if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 0),
        ([3, 3, 3, 3], 0),
        ([], 0),
        ([2], 0),
        ([5, 0, 5], 5),
    ]

    for i, (height, expected) in enumerate(test_cases):
        result = solver.trap(height)
        status = (
            "通过"
            if result == expected
            else f"失败 (期望 {expected}, 实际 {result})"
        )
        print(f"测试用例{i + 1}: {status}")






    
    
    
    
    
    



    
    