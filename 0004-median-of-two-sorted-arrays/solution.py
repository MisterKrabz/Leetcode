class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        even = False
        if (len(nums1) + len(nums2)) % 2 == 0: 
            even = True

        current = 0
        previous = 0

        for i in range((len(nums1) + len(nums2)) // 2 + 1):
            if nums1 and nums2: 
                if nums1[0] > nums2[0]: 
                    previous = current
                    current = nums2.pop(0)
                else: 
                    previous = current
                    current = nums1.pop(0)
            elif nums1 and not nums2:
                previous = current
                current = nums1.pop(0)
            else: 
                previous = current
                current = nums2.pop(0)
            
        print(current)
        print(previous)
        if even: 
            return (current + previous) / 2
        else: 
            return current

         



            
            
            
            



