from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        接雨水 - 双指针解法
        时间复杂度 O(n)，空间复杂度 O(1)

        核心思想：
        - 维护 left 和 right 两个指针，以及 left_max 和 right_max 两个变量
        - 对于每个位置，能接的雨水取决于该位置左侧最高柱子和右侧最高柱子的较小值减去当前高度
        - 每次移动高度较小的一侧指针，并更新对应侧的最大值
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max = right_max = 0
        total_water = 0

        while left < right:
            # 左侧柱子较矮，处理左侧
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            # 右侧柱子较矮或相等，处理右侧
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water


if __name__ == "__main__":
    solver = Solution()

    # 测试用例 1：经典示例
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected = 6
    result = solver.trap(height)
    assert result == expected, f"测试用例1失败: 期望 {expected}, 实际 {result}"
    print("测试用例1通过")

    # 测试用例 2：简单情况
    height = [4, 2, 0, 3, 2, 5]
    expected = 9
    result = solver.trap(height)
    assert result == expected, f"测试用例2失败: 期望 {expected}, 实际 {result}"
    print("测试用例2通过")

    # 测试用例 3：递增数组（无凹陷，不能接水）
    height = [1, 2, 3, 4, 5]
    expected = 0
    result = solver.trap(height)
    assert result == expected, f"测试用例3失败: 期望 {expected}, 实际 {result}"
    print("测试用例3通过")

    # 测试用例 4：递减数组
    height = [5, 4, 3, 2, 1]
    expected = 0
    result = solver.trap(height)
    assert result == expected, f"测试用例4失败: 期望 {expected}, 实际 {result}"
    print("测试用例4通过")

    # 测试用例 5：所有柱子等高
    height = [3, 3, 3, 3]
    expected = 0
    result = solver.trap(height)
    assert result == expected, f"测试用例5失败: 期望 {expected}, 实际 {result}"
    print("测试用例5通过")

    # 测试用例 6：空数组
    height = []
    expected = 0
    result = solver.trap(height)
    assert result == expected, f"测试用例6失败: 期望 {expected}, 实际 {result}"
    print("测试用例6通过")

    # 测试用例 7：只有一个元素
    height = [2]
    expected = 0
    result = solver.trap(height)
    assert result == expected, f"测试用例7失败: 期望 {expected}, 实际 {result}"
    print("测试用例7通过")

    # 测试用例 8：左右两边高，中间低
    height = [5, 0, 5]
    expected = 5  # 两边高5，中间0，接水 5
    result = solver.trap(height)
    assert result == expected, f"测试用例8失败: 期望 {expected}, 实际 {result}"
    print("测试用例8通过")

    print("所有测试用例通过！")