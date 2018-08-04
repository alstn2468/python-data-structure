# QuickSort.py
'''
퀵정렬(QuickSort)
O(nlogn)
'''
def QuickSort(list) :
    less = []
    pivotList = []
    more = []

    if len(list) <= 1 :
        return list

    else :
        pivot = list[0]
        for i in list :
            if i < pivot :
                less.append(i)

            elif i > pivot :
                more.append(i)

            else :
                pivotList.append(i)

        less = QuickSort(less)
        more = QuickSort(more)

        return less + pivotList + more

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
    print(QuickSort(list))
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
