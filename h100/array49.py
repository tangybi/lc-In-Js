from typing import List

class Solution:
    # 字母异位词分组. 1、排序 2、计数 
    # 排序 O(n²)
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # 1、遍历数组，新建2个空数组，一个一维存排序后的不重复的对比，另一个存二维输出 
        # 2、sorted排序后判断 判断空数组是否包含，不包含就push到另一个数组
        # 3、包含就插入index对应的数组   O(n²)
        # 排序会导致复杂度增加，性能❌
        # 优化方向：使用计数编码确认唯一key
        ls = []
        ls_a = []
        for item in strs:
            item_s = "".join(sorted(item))
            if item_s in ls:
                index = ls.index(item_s)
                ls_a[index].append(item)
            else:
                ls.append(item_s)
                ls_a.append([item])
        return ls_a
    # 计数 O(n·K log K)
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            item_s = "".join(sorted(item)) #O(K log K)，K是字符串的平均长度 排序会增加遍历
            if item_s in dict:
                dict[item_s].append(item)
            else:
                dict[item_s] = [item]
        return list(dict.values())
    # 计数优化 O(n·K log K)
    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            count = [0] * 26  # 统计每个字母出现的次数，每个item都要重置
            for c in item:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # 将计数列表转换为元组作为字典的键
            if key not in dict:
                dict[key] = [item]
            else:
                dict[key].append(item)  # O(1)
        return list(dict.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict 的正确名称是 defaultdict（首字母小写），它来自 Python 标准库的 collections 模块。它是一个带有默认值的字典，当你访问一个不存在的键时，它会自动生成一个默认值，而不是抛出 KeyError。
        
        from collections import defaultdict
        s_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26  # 统计每个字母出现的次数，每个item都要重置
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count) 
            s_dict[key].append(s)
        return list(s_dict.values())

# 自测用例
if __name__ == "__main__":
    sol = Solution()
    
    def normalize(res):
        return sorted([sorted(group) for group in res])

    # 用例列表: (输入, 目标)
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]),
        ([""], [[""]]),
        (["abc", "abc", "abc"], [["abc", "abc", "abc"]]),
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    ]

    pass_count = 0
    for idx, (input_case, target) in enumerate(test_cases, 1):
        result = sol.groupAnagrams(input_case)
        print(f"\n测试用例 {idx}:")
        print("输入:", input_case)
        print("输出:", result)
        print("目标:", target)
        if normalize(result) == normalize(target):
            print("结果: 通过")
            pass_count += 1
        else:
            print("结果: 未通过")

    total = len(test_cases)
    print(f"\n总用例数: {total}，通过: {pass_count}，通过率: {pass_count/total:.2%}")
