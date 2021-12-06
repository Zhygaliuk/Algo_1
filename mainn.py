def find_sum(array, sum):
    array.sort()
    first = 0
    last = len(array) - 1
    while first < last:
        i = binarySearch(array, sum - array[first] - array[last], first + 1, last)
        love_sum = array[first] + array[i] + array[last]
        if love_sum == sum and first != i:
            print(array[first],array[last],array[i])
            return True
        else:
            if love_sum < sum:
                first += 1
            elif love_sum>sum:
                last -= 1
    print(False)
    return False


def binarySearch(a, x, lo=0, hi=None):
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid

        return lo


array = [1, 2, 5, 6, 7, 8, 9]
find_sum(array,8 )
