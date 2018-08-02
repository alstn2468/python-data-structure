# HeapSort.py
'''
힙정렬(HeapSort)
O(nlogn)
'''
def heapify(list, n, i) :
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and list[i] < list[l] :
        largest = l

    if r < n and list[largest] < list[r] :
        largest = r

    if largest != i :
        list[i], list[largest] = list[largest], list[i]

        heapify(list, n, largest)

def HeapSort(list) :
    n = len(list)

    for i in range(n, -1, -1) :
        heapify(list, n, i)

    for i in range(n - 1, 0, -1) :
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)


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

    HeapSort(list)

    # 정렬 후 리스트 출력
    print('- After Sorting -')
    print(list)
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
