import collections
from collections import Counter
from typing import List

#from requests.utils import from_key_val_list






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
        res = []
        k = 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return res

# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        dict_arr = {}
        for i, e in enumerate(s):
            k = i
            arr_len = 0
            while k <= len(s) - 1:
                if s[k] not in dict_arr:
                    dict_arr[s[k]] = 1
                    arr_len += 1
                    k += 1
                    max_len = max(max_len, arr_len)
                else:
                    dict_arr.clear()
                    break
        return max_len

    def lengthOfLongestSubstring1(self, s: str) -> int:
        max_len = 0
        set_arr = set()
        curr_len = 0
        left = 0
        for i, e in enumerate(s):
            curr_len += 1
            while e in set_arr:
                set_arr.remove(s[left])
                left += 1
                curr_len -= 1
            max_len = max(max_len, curr_len)
            set_arr.add(e)
        return max_len
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cn_p = Counter(p)
        cn_s = Counter()
        ans = []
        for i, e in enumerate(s):
            cn_s[e] += 1
            left = i + 1 - len(p)
            if left < 0:
                #未到窗口长度
                continue
            if cn_s == cn_p:
                ans.append(left)
            #右移左窗口
            cn_s[s[left]] -= 1
        return ans
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
# 示例 1：
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
# 输入：nums = [1,2,3], k = 3
# 输出：2
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         dict_arr = {}
#         count = 0
#         for i, num in enumerate(nums):
#             dict_arr[num] = dict_arr.get(num, 0) + 1
#             if
    #前缀和+哈希表
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        count = 0
        mp = {0: 1}

        for num in nums:
            pre_sum += num
            count += mp.get(pre_sum - k, 0)
            mp[pre_sum] = mp.get(pre_sum, 0) + 1

        return count
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        mur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            mur = max(mur, cur)
        return mur
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 示例 3：
# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return_arr = []
        index_flag = []
        swap_index = []
        for i, interval in enumerate(intervals):
            if i in index_flag:
                continue
            flag = False

            for j in range(i + 1, len(intervals)):
                if (intervals[j][0] <= intervals[i][1] and intervals[j][0] >= intervals[i][0]
                        and intervals[j][1] >= intervals[i][1]):
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[i][0], intervals[j][1]] not in return_arr:
                        return_arr.append([intervals[i][0], intervals[j][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[i][0],intervals[j][1]]
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[j][0],intervals[i][1]] not in return_arr:
                        return_arr.append([intervals[j][0], intervals[i][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[j][0],intervals[i][1]]
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[j][0],intervals[j][1]] not in return_arr:
                        return_arr.append([intervals[j][0], intervals[j][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[j][0],intervals[j][1]]
                elif intervals[j][0] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[i][0],intervals[i][1]] not in return_arr:
                        return_arr.append([intervals[i][0], intervals[i][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[i][0],intervals[i][1]]
                else:
                    continue
            if not flag:
                return_arr.append([intervals[i][0],intervals[i][1]])
        return return_arr

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i, interval in enumerate(intervals):
            if len(res) == 0:
                res.append(interval)
                continue
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max([res[-1][1], intervals[i][1]])
        return res

s = Solution()

#intervals = [[1,3],[2,6],[8,10],[15,18]]
#intervals = [[1,4],[4,5]]
#intervals = [[4,7],[1,4]]
#intervals = [[1,4],[2,3]]
#intervals = [[1,4],[0,2],[3,5]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
arr = s.merge1(intervals)
print(arr)
#len = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#len = s.maxSubArray([1])
#len = s.maxSubArray([5,4,-1,7,8])
#print(len)
#num = s.subarraySum([1,1,1], 2)
#num = s.subarraySum([1,2,3], 3)
#num = s.subarraySum([1], 0)
#num = s.subarraySum([1, 3, 5, 4], 9)
#print(num)
# arr = s.findAnagrams("cbaebabacd", "abc")
# print(arr)
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]

# s = "cbaebabacd"
# p = "abc"
# dict_arr = Counter(p)
# print(dict_arr)
# arr = Counter()
# print(arr)
#len = s.lengthOfLongestSubstring("abcabcbb")
#len = s.lengthOfLongestSubstring("pwwkew")
#len = s.lengthOfLongestSubstring1(" ")
#len = s.lengthOfLongestSubstring("c")
#print(len)
#arr = [1,8,6,2,5,4,8,3,7]
# arr = [4,3,2,1,4]
# #arr = [1,1]
# print(s.maxArea(arr))
# arr = s.threeSum([-1,0,1,2,-1,-4])
# print(arr)
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