# LinkedListBaseQueue.py

# 연결 리스트 기반 큐 노드 클래스
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None

# 연결 리스트 기반 큐 클래스
class LinkedListBaseQueue :

    def __init__(self) :
        self.front = None
        self.rear = None

    # 연결 리스트 기반 큐 삽입 함수
    def enqueue(self, data) :
        new_node = Node(data)

        if self.front is None :
            self.front = new_node
            self.rear = new_node

        else :
            self.rear.next = new_node
            self.rear = new_node

    # 연결 리스트 기반 큐 삭제 함수
    def dequeue(self) :
        del_node = self.front
        del_data = self.front.data
        self.front = self.front.next

        del del_node

        if self.front is None :
            self.rear = None

        return del_data

    # 연결 리스트 기반 큐 참조 함수
    def peek(self) :
        return self.front.data

    # 연결 리스트 기반 큐 공백 확인 함수
    def is_empty(self) :
        return self.front == None and self.rear == None

    # 연결 리스트 기반 큐 출력 함수
    def display(self) :
        temp = self.front

        while temp is not None :

            if temp.next is None :
                print(temp.data)

            else :
                print('%3d <- ' % temp.data, end = "")

            temp = temp.next

if __name__ == '__main__' :

    # 연결 리스트 기반 큐 클래스 선언
    queue = LinkedListBaseQueue()

    # 연결 리스트 기반 큐 공백 확인
    print('Is Empty : %s' % queue.is_empty())
    '''
    Is Empty : True
    '''

    # 연결 리스트 기반 큐 데이터 삽입
    queue.enqueue(10), queue.enqueue(20)
    queue.enqueue(30), queue.enqueue(40)
    queue.enqueue(50), queue.enqueue(60)

    # 연결 리스트 기반 큐 데이터 출력
    print('Add Data')
    queue.display()
    '''
    Add Data
     10 <-  20 <-  30 <-  40 <-  50 <- 60
    '''

    print('Dequeue : %d' % queue.dequeue())
    print('After Dequeue')
    queue.display()
    '''
    Dequeue : 10
    After Dequeue
     20 <-  30 <-  40 <-  50 <- 60
    '''

    print('Front : %d' % queue.front.data)
    print('Rear : %d' % queue.rear.data)
    print('Is Empty : %s' % queue.is_empty())
    '''
    Front : 20
    Rear : 60
    Is Empty : False
    '''
