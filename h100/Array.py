# 两数之和
# 输入数组和目标和，输出2数的下标
# 利用dict字典降低复杂度到n
class Methods:
    def twoSum(self, nums: List[int],target:int) -> List[int]:
        seem = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if(diff in seem):
                return [seem[diff], idx]
            seem[diff] = idx




