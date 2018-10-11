# SelectionSort.py
'''
선택정렬(Selection Sort)
O(n²)
'''

def SelectionSort(list) :
    result = []

    while(list) :
        result.append(list.pop(list.index(min(list))))

    return result

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
    print(SelectionSort(list))
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
