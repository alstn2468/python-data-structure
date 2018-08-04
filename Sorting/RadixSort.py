# RadixSort.py
'''
기수정렬(RadixSort)
O(n)
'''
def CountingSort(list, exp1) :
    n = len(list)

    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n) :
        index = list[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10) :
        count[i] += count[i - 1]

    i = n - 1

    while i >= 0 :
        index = list[i] // exp1
        output[count[index % 10] - 1] = list[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(list)) :
        list[i] = output[i]

def RadixSort(list) :
    max1 = max(list)

    exp = 1
    while max1 / exp > 0 :
        CountingSort(list,exp)
        exp *= 10

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

    RadixSort(list)

    # 정렬 후 리스트 출력
    print('- After Sorting -')
    print(list)
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
