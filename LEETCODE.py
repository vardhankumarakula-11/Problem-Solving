#------- Problem no.1 --------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
                
#------- Problem no.4 --------

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        add = nums1+nums2
        add.sort()
        n = len(add)
        if n%2==1:
            return (add[n//2])
        else:
            return (((add[n//2-1])+(add[n//2]))/2.0)

#------- Problem no.344 --------

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        return s

#------- Problem no.9 --------  

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        y = 0
        while x>0:
            a = x%10
            y = (y*10) + a
            x//=10
        if temp==y:
            return True
        else:
            return False
        
#------- Problem no.2154 --------

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            if original in nums:
                original = original * 2 
            else:
                return original
            
#------- Problem no.283 --------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while j<len(nums):
            if (nums[j]!=0):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            j+=1
        return nums
    
#------- Problem no.26 --------

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1],nums[j] = nums[j],nums[i+1]
                i+=1
                j+=1
        return i+1
    
#------- Problem no.268 --------

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            
#-------- Problem no.189 ----------

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k=k%n
        emp = []
        for i in range(n-k,n):
            emp.append(nums[i])
        for j in range(n-1,k-1,-1):
            nums[j] = nums[j-k]
        for i in range(k):
            nums[i] = emp[i]
        return emp
    
#------- Problem no.287 --------

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                return i

#------- Problem no.704 --------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if (nums[mid]==target):
                return mid
            elif (target<nums[mid] and target>=nums[l]):
                h = mid-1
            else:
                l = mid+1
        return -1
    
#------- Problem no.34 --------

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        h = len(nums)-1
        first = -1
        while l<=h:
            mid = (l+h)//2
            if (target==nums[mid]):
                first = mid
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                
                h = mid - 1
        
        l = 0
        h = len(nums)-1
        last = -1
        while l<=h:
            mid = (l+h)//2
            if (nums[mid]==target):
                l = mid + 1
                last = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1   
        return first,last
    
#------- Problem no.540 --------
    
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if (nums[0]!=nums[1]):
            return nums[0]
        if (nums[-1]!=nums[-2]):
            return nums[-1]
        
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]!=nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if (mid%2 == 0):
                if nums[mid]==nums[mid+1]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if nums[mid] == nums[mid-1]:
                    l = mid + 1
                else:
                    h = mid - 1

#------- Problem no.58 --------

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])
    
#------- Problem no.33 --------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            if (nums[l]<=nums[mid]):
                if (nums[l]<=target and target<=nums[mid]):
                    h = mid -1
                else:
                    l = mid + 1
            else:
                if (target>=nums[mid] and nums[h]>=target):
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
    
#------- Problem no.81 --------

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if (target==nums[mid]):
                return True
            elif (nums[l]==nums[mid]==nums[h]):
                l+=1
                h-=1
            elif(nums[mid]>=nums[l]):
                if (nums[l]<=target and nums[mid]>=target):
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if (target>=nums[mid] and target<=nums[h]):
                    l = mid +1 
                else:
                    h = mid - 1
        return False
    
#------- Problem no.153 --------

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        ans = float("inf")
        while l<=h:
            mid = (l+h)//2
            if (nums[l]<=nums[mid]):
                if nums[l]<ans:
                    ans = nums[l]
                l = mid + 1
            else:
                if nums[mid]<ans:
                    ans = nums[mid]
                h = mid - 1
        return ans
        