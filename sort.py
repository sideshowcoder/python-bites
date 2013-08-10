def qsort(list):
    if len(list) < 2:
        return list
    pivot = list.pop(0)
    lower = qsort([x for x in list if x <= pivot])
    higher = qsort([x for x in list if x > pivot])
    return lower + [pivot] + higher

def merge_sort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = merge_sort(list[0:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result += left
            del left[:]
        elif len(right) > 0:
            result += right
            del right[:]
    return result

print qsort([])
print qsort([1])
print qsort([2,1])
print qsort([5,12,1,9,2321,2,23,123,1,4,5,6,99])

print merge_sort([])
print merge_sort([1])
print merge_sort([2,1])
print merge_sort([5,12,1,9,2321,2,23,123,1,4,5,6,99])


