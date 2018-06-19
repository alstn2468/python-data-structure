# LinkedListBaseStack.py

# 연결 리스트 기반 스택 노드 클래스
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None

# 연결 리스트 기반 스택 클래스
class LinkedListBaseStack :

    def __init__(self) :
        self.top = None

    # 연결 리스트 기반 스택 삽입 함수
    def push(self, data) :
        new_node = Node(data)

        if self.top is None :
            self.top = new_node

        else :
            new_node.next = self.top
            self.top = new_node

    # 연결 리스트 기반 스택 삭제 함수
    def pop(self) :
        if self.is_empty() :
            raise Exception('STACK EMPTY ERROR!')

        else :
            del_node = self.top
            del_data = del_node.data
            self.top = self.top.next
            del del_node

            return del_data

    # 연결 리스트 기반 스택 참조 함수
    def peek(self) :
        if self.is_empty() :
            raise Exception('STACK EMPTY ERROR!')

        else :
            return self.top.data

    # 연결 리스트 기반 스택 공백 확인 함수
    def is_empty(self) :
        return self.top == None

    # 연결 리스트 기반 스택 출력 함수
    def display(self) :
        if self.is_empty() :
            raise Exception('STACK EMPTY ERROR!')

        else :
            temp = self.top

            while temp is not None :
                print('│ %3d │' % temp.data)
                temp = temp.next

            print('└─────┘')


if __name__ == '__main__' :

    # 연결 리스트 기반 스택 클래스 선언
    stack = LinkedListBaseStack()

    # 연결 리스트 기반 스택 데이터 삽입
    stack.push(10), stack.push(20)
    stack.push(30), stack.push(40)
    stack.push(50), stack.push(60)

    # 연결 리스트 기반 스택 데이터 출력
    stack.display()
    '''
    │  60 │
    │  50 │
    │  40 │
    │  30 │
    │  20 │
    │  10 │
    └─────┘
    '''

    # 연결 리스트 기반 스택 데이터 삭제
    print('Pop : %d' % stack.pop())
    print('After Pop')
    stack.display()
    '''
    Pop : 60
    After Pop
    │  50 │
    │  40 │
    │  30 │
    │  20 │
    │  10 │
    └─────┘
    '''

    # 연결 리스트 기반 스택 상태 확인
    print('Peek : %d' % stack.peek())
    print('Is Empty : %s' % stack.is_empty())
    '''
    Peek : 50
    Is Empty : False
    '''
