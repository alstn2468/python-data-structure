# CircularQueue.py

# 배열 기반 원형 큐 클래스
class CircularQueue :

    def __init__(self, max = 50) :
        self.items = [0 for i in range(max)]
        self.front = 0
        self.rear = 0
        self.max_length = max

    # 배열 기반 원형 큐 삽입 함수
    def enqueue(self, data) :
        if self.is_full() :
            raise Exception('QUEUE FULL ERROR!')

        else :
            self.rear = (self.rear + 1) % self.max_length
            self.items[self.rear] = data

    # 배열 기반 원형 큐 삭제 함수
    def dequeue(self) :
        if self.is_empty() :
            raise Exception('QUEUE EMTPY ERROR!')

        else :
            self.front = (self.front + 1) % self.max_length
            del_data = self.items[self.front]

            return del_data

    # 배열 기반 원형 큐 참조 함수
    def peek(self) :
        return self.items[(self.front + 1) % self.max_length]

    # 배열 기반 원형 큐 공백 확인 함수
    def is_empty(self) :
        return self.front == self.rear

    # 배열 기반 원형 큐 포화 확인 함수
    def is_full(self) :
        return self.front == ((self.rear + 1) % self.max_length)

    # 배열 기반 원형 큐 출력 함수
    def display(self) :
        if self.is_empty() :
            raise Exception('QUEUE EMPTY ERROR!')

        else :

            for i in range(self.front + 1, self.rear + 1) :

                if i == self.rear :
                    print('%3d' % self.items[i])

                else:
                    print('%3d <- ' % self.items[i], end = "")


if __name__ == '__main__' :

    # 배열 기반 원형 큐 클래스 선언
    queue = CircularQueue()

    # 배열 기반 원형 큐 공백 확인
    print('Is Empty : %s' % queue.is_empty())
    '''
    Is Empty : True
    '''

    # 배열 기반 원형 큐 데이터 삽입
    queue.enqueue(10), queue.enqueue(20)
    queue.enqueue(30), queue.enqueue(40)
    queue.enqueue(50), queue.enqueue(60)

    # 배열 기반 원형 큐 출력
    print('Add Data')
    queue.display()
    '''
    Add Data
     10 <- 20 <- 30 <- 40 <- 50 <- 60
    '''

    # 배열 기반 원형 큐 데이터 삭제
    print('Dequeue : %d' % queue.dequeue())
    print('After Dequeue')
    queue.display()
    '''
    Dequeue : 10
    After Dequeue
     20 <- 30 <- 40 <- 50 <- 60
    '''

    # 배열 기반 원형 큐 상태 출력
    print('Front : %d' % queue.front)
    print('Rear : %d' % queue.rear)
    print('Peek : %d' % queue.peek())
    print('Is Empty : %s' % queue.is_empty())
    print('Is Full : %s' % queue.is_full())
    '''
    Front : 1
    Rear : 6
    Peek : 20
    Is Empty : False
    Is Full : False
    '''
