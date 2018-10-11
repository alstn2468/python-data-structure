# MergeSort.py
'''
병합정렬(MergeSort)
O(nlogn)
'''

def Merge(left, right) :
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            result.append(left[i])
            i += 1

        else :
            result.append(right[j])
            j += 1

    while i < len(left) :
        result.append(left[i])
        i += 1

    while j < len(right) :
        result.append(right[j])
        j += 1

    return result

def MergeSort(list) :
    if len(list) <= 1 :
        return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    l = MergeSort(left)
    r = MergeSort(right)

    return Merge(l, r)

if __name__ == '__main__' :

    # 정렬할 리스트 선언
    list = [1, 3, 2, 4, 5, 7, 6, 9, 8]

    # 정렬 전 리스트 출력
    print('- Before Sorting -')
    print(list)
    '''
    - Before Sorting -
    [1, 3, 2, 4, 5, 7, 6, 9, 8]
    '''

    # 정렬 후 리스트 출력
    print('- After Sorting -')
    print(MergeSort(list))
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
