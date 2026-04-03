import collections
from typing import List

from requests.utils import from_key_val_list






class Solution:
    # 1：给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
    # 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right - left) // 2 + left
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值target的那两个整数，
#并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictArr = {}
        for i, num in enumerate(nums):
            if num not in dictArr:
                dictArr[num] = i
        for i, num in enumerate(nums):
            if target - num in dictArr and dictArr[target - num] != i:
                return [dictArr[target - num], i]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        dictArr = {}
        for i, num in enumerate(nums):
            if target - num in dictArr:
                return [dictArr[target-num],i]
            dictArr[num] = i


#给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 解释：
# 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
# 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listParent = []
        listReturn = []
        for i, str in enumerate(strs):
            dictArr = {}
            listReturnChild = []
            flag = False
            for ch in str:
                if ch not in dictArr:
                    dictArr[ch] = 1
                else:
                    dictArr[ch] += 1

            for i, ch in enumerate(listParent):
                if ch == dictArr:
                    list = listReturn[i]
                    list.append(str)
                    flag = True
                    break
            if flag:
                continue
            listParent.append(dictArr)
            listReturnChild.append(str)
            listReturn.append(listReturnChild)
        return listReturn

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 示例 3：
# 输入：nums = [1,0,1,2]
# 输出：3
 #   0 1 3 4 5
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums.sort()
        nums = sorted(set(nums))
        len = 0
        maxLen = 0
        beforeNum = 0
        for i, num in enumerate(nums):
            if i == 0:
                beforeNum = num
                len += 1
                maxLen = len
                continue
            if beforeNum + 1 == num:
                len += 1
                if len > maxLen:
                    maxLen = len
            else:
                if len - 1 != 0:
                    len = 1
            beforeNum = num
        return maxLen

    def longestConsecutive1(self, nums: List[int]) -> int:
        numsSet = set(nums)
        len_max = 0
        for e in numsSet:
            if e - 1 not in numsSet:
                current_len = 1
                current_value = e
                while current_value + 1 in numsSet:
                    current_len += 1
                    current_value += 1
                if current_len > len_max:
                    len_max = current_len
        return len_max


#     给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:
# 输入: nums = [0]
# 输出: [0]
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while left < right:
            if len(nums) < 2:
                break
            if right > len(nums) - 1:
                break
            if nums[left] == 0 and nums[right] == 0:
                right += 1
                continue
            if nums[left] == 0 and nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
            left += 1
            right += 1
        print(nums)

    def moveZeroes1(self, nums: List[int]) -> None:
        slow_pointer = 0
        for i, num in enumerate(nums):
            if num != 0:
                p = nums[slow_pointer]
                nums[slow_pointer] = num
                nums[i] = p
                slow_pointer += 1
        print(nums)
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 示例 2：
# 输入：height = [1,1]
# 输出：1
    def maxArea(self, height: List[int]) -> int:
        #实际就是求 索引距离*数组值 的两个元素最大值
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0
        while left_pointer < right_pointer:
            area_value = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
            max_area = max(max_area, area_value)
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area
        #解法111
        # max_area = 0
        # left_pointer = 0
        # right_pointer = 1
        # index_area = 1
        # while left_pointer < len(height) - 1:
        #     max_area = max(max_area, (min(height[right_pointer], height[left_pointer])) * index_area)
        #     if right_pointer < len(height) - 1:
        #         right_pointer += 1
        #         index_area += 1
        #         continue
        #     else:
        #         left_pointer += 1
        #         right_pointer = left_pointer + 1
        #         index_area = 1
        # return max_area

        #解法222
        # max_area = 0
        # for i, e in enumerate(height):
        #     for loop in range(1, len(height)):
        #         if (loop - i) * min(height[loop], e) > max_area:
        #             max_area = (loop - i) * min(height[loop], e)
        # return max_area

# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        return_list = []
        list_dict_arr = []
        for i, num in enumerate(nums):
            return_child = []
            if len(nums) < 3:
                if len(nums) == 3 and nums[0] + nums[1] + nums[2] == 0:
                    return_child.append(nums)
                    return return_list.append(nums)
                else:
                    return return_list
            left_pointer = i+1
            right_pointer = i+2
            while left_pointer < right_pointer:
                dict_arr = {}
                #and left_pointer < len(nums) and right_pointer < len(nums)
                if num + nums[left_pointer] + nums[right_pointer] == 0:
                    dict_arr[num] == None



                    right_pointer +=1




s = Solution()

#arr = [1,8,6,2,5,4,8,3,7]
arr = [4,3,2,1,4]
#arr = [1,1]
print(s.maxArea(arr))

# arr = [1,3,2,6]
# for loop in range(1, len(arr)):
#     print(loop)
#     print(arr[loop])

#s.moveZeroes([1,0,1])
#s.moveZeroes1([0,1,0,3,12])
# str = s.search1(nums=[6,7,8,9], target=9)
# print(str)

# arr = s.twoSum1([3,2,4], 6)
# print(arr)
# for i in range(0,10):
#     print(i)

# sttr = s.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"])
# print(sttr)
# arr = [1,3,2,0]
# arr.sort()
# print(arr)
# len = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
# print(len)
#len = s.longestConsecutive([1,0,1,2])
#len = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
#len = s.longestConsecutive1([9,1,4,7,3,-1,0,5,8,-1,6])
#-1 0 1 3 4 5 6 7 8 9
#len = s.longestConsecutive([100,4,200,1,3,2])
#print(len)
# arr = [9,1,4,7,3,-1,0,5,8,-1,6]
# print(len(arr))