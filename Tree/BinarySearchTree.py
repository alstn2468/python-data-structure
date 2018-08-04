# BinarySearhTree.py

# 이진 탐색 트리 노드 클래스
class Node :

    def __init__(self, data) :
        self.data = None
        self.lnode = None
        self.rnode = None

# 이진 탐색 트리 클래스
class BinarySearhTree :

    def __init__(self) :
        self.root = None

    def insert(self, data) :
        pass

    def find(self, key) :
        pass

    def delete(self, key) :
        pass

    def display(self) :
        pass

if __name__ == '__main__' :
    # 이진 탐색 트리 클래스 선언
    BST = BinarySearhTree()

    # 이진 탐색 트리 데이터 삽입
    for i in range(1, 11) :
        BST.insert(i)

    # 이진 탐색 트리 데이터 출력
    BST.display()

    # 이진 탐색 트리 데이터 검색
    print(BST.find(6))
    print(BST.find(8))

    # 이진 탐색 트리 데이터 삭제
    BST.delete(3)
    BST.display()
