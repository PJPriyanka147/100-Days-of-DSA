#using brute force --
def median_of_sorted_array(nums1, nums2):
    merged = []
    i, j = 0 , 0

    #merge the two arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    #appending remaining elements of nums1 
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    #appending remaining elements of nums2
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    #finding the median
    n = len(merged)
    if n % 2 == 1:
        return float(merged[n//2])
    else:
        return float(merged[(n//2) - 1] + merged[n//2]) / 2.0

nums1 = list(map(int, input("Enter nums1 elements: ").split()))
nums2 = list(map(int, input("Enter nums2 elements: ").split()))
result = median_of_sorted_array(nums1, nums2)
print(result)