# QuickSort.py
'''
퀵정렬(QuickSort)
O(nlogn)
'''

def partition(list, low, high) :
    i = low - 1
    pivot = list[high]

    for j in range(low, high) :

        if list[j] < pivot :
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]

    return i + 1

def QuickSort(list, low, high) :
    if low < high :
        pi = partition(list, low, high)

        QuickSort(list, low, pi - 1)
        QuickSort(list, pi + 1, high)


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

    # 데이터 정렬
    QuickSort(list, 0, len(list) - 1)

    # 정렬 후 리스트 출력
    print('- After Sorting -')
    print(list)
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
