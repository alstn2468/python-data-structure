# CircularLinkedList.py

# 원형 연결 리스트의 노드 클래스
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None

# 원형 연결 리스트의 클래스
class CircularLinkedList :

    def __init__(self) :
        self.head = None
        self.tail = None

    # 원형 연결 리스트 맨 앞 삽입 함수
    def add_first(self, data) :
        new_node = Node(data)

        if self.head is None :
            self.head = self.tail = new_node

        else :
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    # 원형 연결 리스트 맨 뒤 삽입 함수
    def add_last(self ,data) :
        new_node = Node(data)

        if self.tail is None :
            self.tail = self.head = new_node

        else :
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    # 원형 연결 리스트 맨 앞 삭제 함수
    def delete_first(self, data) :
        return

    # 원형 연결 리스트 맨 뒤 삭제 함수
    def delete_last(self, data) :
        return

    # 원형 연결 리스트 출력 함수
    def display(self, node) :
        temp = node

        while True :

            if temp.next is node :
                print(temp.data, end = "")

            else :
                print(str(temp.data) + ' -> ', end = "")

            temp = temp.next
            if temp is node :
                break
        print()

if __name__ == '__main__' :

    # 원형 연결 리스트 클래스 선언
    Clist = CircularLinkedList()

    # 원형 연결 리스트 데이터 삽입
    Clist.add_first(10), Clist.add_last(40)
    Clist.add_first(20), Clist.add_last(50)
    Clist.add_first(30), Clist.add_last(60)

    # 원형 연결 리스트 데이터 출력
    Clist.display(Clist.head)
    print('Clist Head : ', Clist.head.data)
    print('Clist Tail : ', Clist.tail.data)
    print('Clist Tail->Next : ', Clist.tail.next.data)
    '''
    30 -> 20 -> 10 -> 40 -> 50 -> 60
    Clist Head : 30
    Clist Tail : 60
    Clist Tail->Next : 30
    '''
