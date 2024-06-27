# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
#  representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2
#  into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
#  To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
#  should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def swap(x: int, y: int):
    return y, x

def flag_bubble_sort(a: list):
    for i in range(len(a)):
        swap_flag = False
        for j in range(len(a) - i - 1):
            if(a[j] > a[j + 1]):
                swap_flag = True
                a[j], a[j + 1] = swap(a[j], a[j +1])
        if swap_flag is False:
            return None
    return None

def merge(nums1: list, m: int, nums2: list, n: int):
    # cancella pass e scrivi il tuo codice
    topop = len(nums1) - m
    for i in range(topop):
        nums1.pop()
    for i in range(n):
        nums1.append(nums2[i])
    flag_bubble_sort(nums1)

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) # [1, 2, 2, 3, 5, 6]

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1) # [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1) # [1]