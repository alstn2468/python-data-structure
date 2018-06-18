# ArrayBaseList.py

class ArrayBaseList :

    def __init__(self) :
        self.list = []
        self.count = 0

    # 데이터 삽입 함수
    def add(self, data) :
        self.list.append(data)
        self.count += 1

    # 데이터 탐색 함수
    def search(self, data) :
        return [index for index, stored in enumerate(self.list) if stored == data]

    # 데이터 참조 함수
    def get(self, index) :
        if 0 <= index < self.count :
            return self.list[index]

        else :
            raise IndexError

    # 가장 최근에 삽입된 데이터 삭제 함수
    def pop(self) :
        val = self.list[self.count - 1]
        self.remove(self.count - 1)

        return val

    # 데이터 삭제 함수
    def remove(self, index) :
        for index in range(index, self.count - 1) :
            self.list[index] = self.list[index + 1]

        del self.list[self.count - 1]
        self.count -= 1

    # 리스트 출력 함수
    def display(self) :
        for index in range(self.count) :
          print(self.list[index])


if __name__ == '__main__' :

    # 리스트 클래스 선언
    list = ArrayBaseList()

    # 리스트에 데이터 삽입
    list.add(10), list.add(20)
    list.add(30), list.add(40)
    list.add(50), list.add(60)

    # 리스트의 데이터 출력
    print('Add Data')
    list.display()
    print()
    '''
    Adding Data
    10
    20
    30
    40
    50
    60
    '''

    # 가장 최근에 저장된 데이터 삭제 후 출력
    print('pop : ' + str(list.pop())) # pop : 60

    # pop 연산 후 리스트의 데이터 출력
    print('After Pop')
    list.display()
    print()
    '''
    After pop
    10
    20
    30
    40
    50
    '''

    # 두 번째 인덱스의 데이터 삭제
    list.remove(2)

    # 삭제 후 리스트의 데이터 출력
    print('After Remove 2nd index item')
    list.display()
    print()
    '''
    After Remove 2nd index item
    10
    20
    40
    50
    '''

    # 두 번째 인덱스의 데이터 참조
    print('Get list[2] : ' + str(list.get(2))) # Get list[2] : 40

    # 40 데이터 탐색
    print('item(40) in list : ' + str(list.search(40)) + ' index') # item(40) in list : [2] index
