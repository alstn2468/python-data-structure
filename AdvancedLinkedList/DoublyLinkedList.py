# DoublyLinkedList.py

# 이중 연결 리스트의 노드 클래스
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None

# 이중 연결 리스트의 클래스
class DoublyLinkedList :

    def __init__(self) :
        self.head = None
        self.tail = None

    # 이중 연결 리스트의 맨 앞 삽입 함수
    def add_first(self, data) :
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None :
            self.head.prev = new_node

        if self.tail is None :
            self.tail = new_node

        self.head = new_node

    # 이중 연결 리스트의 맨 뒤 삽입 함수
    def add_last(self, data) :
        new_node = Node(data)
        new_node.prev = self.tail

        if self.tail is not None :
            self.tail.next = new_node

        if self.head is None :
            self.head = new_node

        self.tail = new_node

    # 이중 연결 리스트의 특정 노드 삭제 함수
    def delete_node(self, data) :
        del_node = self.head
        count = 0

        while del_node :

            if del_node.data == data :

                del_node.prev.next = del_node.next
                del_node.next.prev = del_node.prev
                del del_node
                count += 1
                del_node = self.head

            del_node = del_node.next

        return count

    # 이중 연결 리스트의 출력 함수
    def display(self, node) :
        while(node is not None) :

            if node.next == None :
                print(str(node.data), end = "")

            else :
                print(str(node.data) + ' -> ', end = "")

            last = node
            node = node.next

        print()

if __name__ == '__main__' :

    # 이중 연결 리스트 클래스 선언
    Dlist = DoublyLinkedList()

    # 이중 연결 리스트 데이터 삽입
    Dlist.add_first(10), Dlist.add_last(20)
    Dlist.add_first(30), Dlist.add_last(30)
    Dlist.add_first(50), Dlist.add_last(60)

    # 이중 연결 리스트의 데이터 출력
    Dlist.display(Dlist.head)  # 50 -> 30 -> 10 -> 20 -> 30 -> 60

    print('Delete ' + str(Dlist.delete_node(30)) + ' item(30) in Dlist') # Delete 2 item(30) in Dlist

    Dlist.display(Dlist.head) # 50 -> 10 -> 20 -> 60
