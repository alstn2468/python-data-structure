# ArrayBaseQueue.py

# 배열 기반 선형 큐 클래스
class ArrayBaseQueue :

    def __init__(self, max = 50) :
        self.items = []
        self.front = 0
        self.rear = 0
        self.max_length = max

    # 배열 기반 선형 큐 삽입 함수
    def enqueue(self, data) :
        if self.is_full() :
            raise Exception('QUEUE FULL ERROR!')

        else :
            self.items.append(data)
            self.rear += 1

    # 배열 기반 선형 큐 삭제 함수
    def dequeue(self) :
        if self.is_empty() :
            raise Exception('QUEUE EMPTY ERROR!')

        else :
            del_data = self.items[self.front]
            self.front += 1

            return del_data

    # 배열 기반 선형 큐 공백 확인 함수
    def is_empty(self) :
        return self.front == self.rear

    # 배열 기반 선형 큐 포화 확인 함수
    def is_full(self) :
        return self.rear == self.max_length - 1

    # 배열 기반 선형 큐 출력 함수
    def display(self) :
        for i in range(self.front, self.rear) :

            if i == self.rear - 1 :
                print(self.items[i])

            else :
                print('%3d <- ' % self.items[i], end = "")

if __name__ == '__main__' :

    # 배열 기반 선형 큐 클래스 선언
    queue = ArrayBaseQueue()

    # 배열 기반 선형 큐 데이터 삽입
    queue.enqueue(10), queue.enqueue(20)
    queue.enqueue(30), queue.enqueue(40)
    queue.enqueue(50), queue.enqueue(60)

    # 데이터 삽입 후 선형 큐 출력
    print('Add Data')
    queue.display()
    '''
    Add Data
     10 <-  20 <-  30 <-  40 <-  50 <- 60
    '''

    # 데이터 삭제 후 선형 큐 출력
    print('Dequeue : %d' % queue.dequeue())
    print('After Dequeue')
    queue.display()
    '''
    Dequeue : 10
    After Dequeue
     20 <-  30 <-  40 <-  50 <- 60
    '''

    # 선형 큐의 상태 출력
    print('Is Empty : %s' % queue.is_empty())
    print('Is Full : %s' % queue.is_full())
    print('Front : %d' % queue.front)
    print('Rear : %d' % queue.rear)
    '''
    Is Empty : False
    Is Full : False
    Front : 1
    Rear : 6
    '''
