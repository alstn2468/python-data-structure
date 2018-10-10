# ArrayBaseHeap.py

# 배열 기반 히프 클래스
class ArrayBaseHeap :

    def __init__(self, len) :
        self.data = []
        self.count = 0
        self.max_len = len

    def is_empty(self) :
        return self.count == 0

    def is_full(self) :
        return self.count == (self.max_len - 1)


if __name__ == '__main__' :
    Heap = ArrayBaseHeap(50)

    print(Heap.is_empty())
    print(Heap.is_full())
