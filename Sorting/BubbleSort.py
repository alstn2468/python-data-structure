# BubbleSort.py
'''
버블정렬 (Bubble Sort)
O(n²)
'''
def swap(val1, val2) :
    temp = val1
    val1 = val2
    val2 = temp

def BubbleSort(list) :
    for i in range(len(list)) :

        for j in range(len(list)) :
            if list[i] < list[j] :
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

if __name__ == '__main__' :
    # 정렬할 리스트 선언
    list = [1, 5, 4, 3, 2, 6, 8, 7, 9, 10]

    # 정렬 전 데이터 출력
    print('- Before Bubble Sorting -')
    print(list)

    # 데이터 정렬
    BubbleSort(list)

    # 정렬 후 데이터 출력
    print('- After Bubble Sorting -')
    print(list)
