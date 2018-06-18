# ArrayBaseStack.py

# 배열 기반 스택 클래스
class ArrayBaseStack :

    def __init__(self, max_length = 50) :
        self.items = []
        self.top = 0
        self.max_length = max_length

    # 스택의 삽입 함수
    def push(self, data) :
        if self.is_full() :
            raise Exception('STACK FULL ERROR!')

        self.items.append(data)
        self.top += 1

    # 스택의 삭제 함수
    def pop(self) :
        if self.is_empty() :
            raise Exception('STACK EMPTY ERROR!')

        self.top -= 1
        data = self.items[self.top]
        del self.items[self.top]

        return data

    # 스택의 참조 함수
    def peek(self) :
        if self.is_empty() :
            raise Exception('STACK EMPTY ERROR!')

        return self.items[self.top - 1]

    # 스택이 비어있는지 확인하는 함수
    def is_empty(self) :
        return self.top == 0

    # 스택이 가득 차있는지 확인하는 함수
    def is_full(self) :
        return self.top == self.max_length

    # 스택의 출력 함수
    def display(self) :
        index = self.top - 1
        while index >= 0 :
            print('│ %3d │' % self.items[index])
            index -= 1

        print('└─────┘')


if __name__ == '__main__' :

    # 스택 클래스 선언
    stack = ArrayBaseStack()

    # 스택의 데이터 삽입
    stack.push(10), stack.push(20)
    stack.push(30), stack.push(40)
    stack.push(50), stack.push(60)

    # 데이터 삽입 후 스택 출력
    print('Add Data')
    stack.display()
    '''
    Add Data
    │  60 │
    │  50 │
    │  40 │
    │  30 │
    │  20 │
    │  10 │
    └─────┘
    '''

    # 데이터 삭제 후 스택 출력
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

    # 스택의 상태 출력
    print('Peek : %d' % stack.peek())
    print('Is_Empty : %s' % stack.is_empty())
    print('Is_Full : %s' % stack.is_full())

    '''
    Peek : 50
    Is_Empty : False
    Is_Full : False
    '''
