class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        i = 0
        while (numbers[i] <= target) and (i < len(numbers)-1):
            j = i + 1
            while (j < len(numbers) and (numbers[j] <= (target - numbers[i])) ):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i+1,j+1]
                j += 1
            i += 1
        return []

    def twoSum1(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:return [l+1,r+1]
            if numbers[l] + numbers[r] < target: l+=1
            if numbers[l] + numbers[r] > target: r-=1
if __name__=='__main__':
    s = Solution()
    numbers = [5,25,75]
    target = 100
    print(s.twoSum(numbers, target))
