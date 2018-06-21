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

    # 배열 기반 원형 큐 삭제 함수
    def dequeue(self) :

    # 배열 기반 원형 큐 참조 함수
    def peek(self) :

    # 배열 기반 원형 큐 공백 확인 함수
    def is_empty(self) :

    # 배열 기반 원형 큐 포화 확인 함수
    def is_full(self) :

    # 배열 기반 원형 큐 출력 함수
    def display(self) :


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
    print('Front : %d' % self.front)
    print('Rear : %d' % self.rear)
    print('Is Empty : %s' % queue.is_empty())
    print('Is Full : %s' % queue.is_full())
    '''
    Front : 1
    Rear : 6
    Is Empty : False
    Is Full : False
    '''
