# InsertionSort.py
'''
삽입정렬(Insertion Sort)
O(n²)
'''

def InsertionSort(list) :
    for i in range(1, len(list)) :
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j] :
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key

    return list

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
    print(InsertionSort(list))
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
