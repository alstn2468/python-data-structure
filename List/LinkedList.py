# LinkedList.py

# 연결 리스트의 노드 클래스
class Node :

    def __init__(self, data, next) :
        self.data = data
        self.next = next

# 연결 리스트의 클래스
class LinkedList :

    def __init__(self, sort = None) :
        self.head = Node(None, None)
        self.tail = None
        self.count = 0
        self.sort = sort if sort else lambda x, y : x > y

    # 데이터를 앞에 삽입하는 함수
    def add(self, data) :
        new_node = Node(data, self.head.next)
        self.head.next = new_node

        if not self.tail :
            self.tail = new_node

        self.count += 1

        return new_node

    # 데이터를 뒤에 삽입하는 함수
    def add_with_sort(self, data) :
        new_node = Node(data, None)
        prev = self.head

        while prev.next :
            current = prev.next

            if self.sort(current.data, data) :
                break

            prev = prev.next

        new_node.next = prev.next
        prev.next = new_node

    # 데이터 탐색 함수
    def search(self, data) :
        hits = []
        current = self.head

        while current.next :
            current = current.next

            if current.data == data :
                hits.append(current)

        return hits

    # 데이터 참조 함수
    def get(self, index) :
        if 0 <= index < self.count :
            current = self.head.next

            for _index in range(self.count) :

                if _index == index :
                    return current

                current = current.next

        else :
            raise IndexError

    # 가장 최근에 저장된 데이터를 삭제 함수
    def pop(self) :
        node = self.head.next
        self.head.next = node.next
        self.count -= 1

        return node

    # 데이터 삭제 함수
    def remove(self, index) :
        before = None
        current = self.head.next

        for _index in range(self.count) :

            if _index == index :

                if _index == 0 :
                    self.head.next = current.next

                else :
                    before.next = current.next

            before = current
            current = current.next

        self.count -= 1

    # 리스트 출력 함수
    def display(self) :
        current = self.head

        while current.next :
            current = current.next
            print(current.data)


if __name__ == '__main__' :

    # 연결 리스트 클래스 생성
    list = LinkedList()
    list2 = LinkedList()

    # 연결 리스트 데이터 삽입 (정렬 X)
    list.add(10), list.add(20)
    list.add(30), list.add(40)
    list.add(50), list.add(60)

    # 연결 리스트 데이터 출력 (정렬 X)
    print('Add Data With No Sort')
    list.display()
    print()
    '''
    Add Data With No Sort
    60
    50
    40
    30
    20
    10
    '''

    # 연결 리스트 데이터 삽입 (정렬 O)
    list2.add_with_sort(10), list2.add_with_sort(20)
    list2.add_with_sort(30), list2.add_with_sort(40)
    list2.add_with_sort(50), list2.add_with_sort(60)

    # 연결 리스트 데이터 출력 (정렬 O)
    print('Add Data With Sort')
    list2.display()
    print()
    '''
    Add Data With Sort
    10
    20
    30
    40
    50
    60
    '''

    # 두 번째 노드의 데이터 참조
    print('Get List 2nd Node Data : ' + str(list.get(2).data)) # Get List 2nd Node Data : 40

    # 40 데이터 탐색
    print('Item(40) In List : ' + str(list.search(40))) # Item(40) In List : [<__main__.Node object at 0x03214A90>]

    # 가장 최근에 저장된 데이터 삭제 후 출력
    print('Pop : ' + str(list.pop().data) + '\n') # Pop : 60

    # pop 연산 후 리스트의 데이터 출력
    print('After Pop')
    list.display()
    print()
    '''
    After pop
    50
    40
    30
    20
    10
    '''

    # 두 번째 노드의 데이터 삭제
    list.remove(2)

    # 삭제 후 리스트의 데이터 출력
    print('After Remove 2nd Node Item')
    list.display()
    '''
    After Remove 2nd Node Item
    50
    40
    20
    10
    '''
