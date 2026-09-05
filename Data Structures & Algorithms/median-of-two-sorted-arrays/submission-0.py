class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # iterate through both arrays starting at the middle of both of them 
        a, b = nums1, nums2 
        #need to run binary search on both a and b

        total = len(nums1) + len(nums2)
        half = total // 2
        if len(b) < len(a): #need the smaller array to be a
            a, b = b, a

        l, r = 0 , len(a) - 1

        while True: #run binary search on A
            i = (l + r) // 2 #middle of array A

            #middle array of B
            j = half - i -2 # left partion is half of the total , -2 - both start at 0

            # middle index array A (smaller one) (left partition of A)
            Aleft = a[i] if i >= 0 else float("-infinity") #edgecase if goes out of bounds
            Aright = a[i + 1] if (i+1) < len(a) else float("infinity") #right partition of A
            Bleft = b[j] if j >= 0 else float("-infinity")
            Bright = b[j + 1] if (j+1) < len(b) else float("infinity") #edgecase if gone too far to the right

            if Aleft <= Bright and Bleft <= Aright:
                #odd num of elements
                if total % 2:
                    return min(Aright, Bright) #return the num in the middle
                # even num of elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: #too many elemetns from A, reduce size
                r = i - 1
            else:
                l = i + 1

