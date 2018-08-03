# CountingSort.py
'''
계수정렬(CountingSort)
O(n)
'''
def CountingSort(list) :
    result = []
    count = [0] * 100001

    for i in list :
        count[i] += 1

    for i in range(1, 10001) :
        if count[i] > 0 :
            for j in range(count[i]) :
                result.append(i)

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
    print(CountingSort(list))
    '''
    - After Sorting -
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
