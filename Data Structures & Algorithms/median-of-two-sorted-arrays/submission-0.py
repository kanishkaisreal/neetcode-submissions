class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = nums1
        B = nums2

        total = len(A) + len(B)
        half = total // 2

        left = 0
        right = len(A)

        while True:

            # Partition A
            i = (left + right) // 2

            # Partition B
            j = half - i

            # Values around partition
            Aleft  = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft  = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total length
                if total % 2:
                    return min(Aright, Bright)

                # Even total length
                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            # Too many elements taken from A
            elif Aleft > Bright:
                right = i - 1

            # Too few elements taken from A
            else:
                left = i + 1