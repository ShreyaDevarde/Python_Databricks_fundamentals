class Solution:
    def mostFrequentEven(self, nums):

        even_nums = []

        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)

        if len(even_nums) == 0:
            return -1

        max_count = 0
        answer = float('inf')

        for num in even_nums:
            count = even_nums.count(num)

            if count > max_count:
                max_count = count
                answer = num

            elif count == max_count:
                answer = min(answer, num)

        return answer