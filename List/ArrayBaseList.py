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
            print(self.list)


if __name__ == '__main__' :

    # 리스트 클래스 선언
    list = ArrayBaseList()

    # 리스트에 데이터 삽입
    list.add(10), list.add(20)
    list.add(30), list.add(40)
    list.add(50), list.add(60)

    # 리스트의 데이터 출력
    list.display()

    # 가장 최근에 저장된 데이터 삭제 후 출력
    print(list.pop())

    # pop 연산 후 리스트의 데이터 출력
    list.display()

    # 두 번째 인덱스의 데이터 삭제
    list.remove(2)

    # 삭제 후 리스트의 데이터 출력
    list.display()

    # 두 번째 인덱스의 데이터 참조
    print(list.get(2))

    # 40 데이터 탐색
    print(list.search(40))
