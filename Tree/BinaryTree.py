# BinaryTree.py

# 이진 트리 노드 클래스
class Node :

    def __init__(self, data) :
        self.rnode = None
        self.lnode = None
        self.data = data

# 이진 트리 클래스
class BinaryTree :

    def __init__(self) :
        self.root = None

    # 이진 트리 삽입 함수
    def insert(self, data) :
        self.root = self._insert_value(self.root, data)

        return self.root is not None

    def _insert_value(self, node, data) :
        if node is None :
            node = Node(data)

        else :
            if data <= node.data :
                node.lnode = self._insert_value(node.lnode, data)

            else :
                node.rnode = self._insert_value(node.rnode, data)

        return node

    # 이진 트리 탐색 함수
    def find(self, key) :
        return self._find_value(self.root, key)

    def _find_value(self, root, key) :
        if root is None or root.data == key :
            return root is not None

        elif key < root.data :
            return self._find_value(root.lnode, key)

        else :
            return self._find_value(root.rnode, key)

    # 이진 트리 삭제 함수
    def delete(self, key) :
        self.root, deleted = self._delete_value(self.root, key)

        return deleted

    def _delete_value(self, node, key) :
        if node is None :
            return node, False

        deleted = False

        if key == node.data :
            deleted = True

            if node.lnode and node.rnode :
                parent, child = node, node.rnode

                while child.lnode is not None :
                    parent, child = child, child.lnode

                child.lnode = node.lnode

                if parent != node :
                    parent.lnode = child.rnode
                    chile.rnode = node.rnode

                node = child

            elif node.lnode or node.rnode :
                node = node.lnode or node.rnode

            else :
                node = None

        elif key < node.data :
            node.lnode, deleted = self._delete_value(node.lnode, key)

        else :
            node.rnode, deleted = self._delete_value(node.rnode, key)

        return node, deleted

    '''
    트리 순회 알고리즘

    - 깊이 우선 순회(Depth First Traversal)
        1. 전위 순회(Pre-order traversal)
        2. 정위 순회(In-order traversal)
        3. 후위 순회(Post-order traversal)

    - 너비 우선 순회(Breadth First Traversal)
        1. 레벨 순회(Level-order traversal)
    '''

    # 이진 트리 전위 순회 함수
    def pre_order_traversal(self) :
        def _pre_order_traversal(root) :
            if root is None :
                pass

            else :
                print(root.data, end = ' ')
                _pre_order_traversal(root.lnode)
                _pre_order_traversal(root.rnode)

        _pre_order_traversal(self.root)
        print()

    # 이진 트리 정위 순회 함수
    def in_order_traversal(self) :
        def _in_order_traversal(root) :
            if root is None :
                pass

            else :
                _in_order_traversal(root.lnode)
                print(root.data, end = ' ')
                _in_order_traversal(root.rnode)

        _in_order_traversal(self.root)
        print()

    # 이진 트리 후위 순회 함수
    def post_order_traversal(self) :
        def _post_order_traversal(root) :
            if root is None :
                pass

            else :
                _post_order_traversal(root.lnode)
                _post_order_traversal(root.rnode)
                print(root.data, end = ' ')

        _post_order_traversal(self.root)
        print()

    # 이진 트리 레벨 순회 함수
    def level_order_traversal(self) :
        def _level_order_traversal(root) :
            queue = [root]

            while queue :
                root = queue.pop(0)

                if root is not None :
                    print(root.data, end = ' ')

                    if root.lnode :
                        queue.append(root.lnode)

                    if root.rnode :
                        queue.append(root.rnode)

        _level_order_traversal(self.root)
        print()

if __name__ == '__main__' :

    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

    # 이진 트리 클래스 선언
    bst = BinaryTree()

    # 이진 트리 데이터 삽입
    for x in array:
        bst.insert(x)

    # 이진 트리 데이터 탐색
    print('- BinaryTree find method test -')
    print(bst.find(15))
    print(bst.find(17))
    '''
    - BinaryTree find method test -
    True
    False
    '''

    # 이진 트리 데이터 삭제
    print('- BinaryTree delete method test -')
    print(bst.delete(55))
    print(bst.delete(14))
    print(bst.delete(11))
    '''
    - BinaryTree delete method test -
    True
    True
    False
    '''

    # 이진 트리 전위 순회 함수
    print('- BinaryTree pre_order_traversal test -')
    bst.pre_order_traversal()
    '''
    - BinaryTree pre_order_traversal test -
    40 4 34 15 13 45 48 47 49
    '''

    # 이진 트리 정위 순회 함수
    print('- BinaryTree in_order_traversal test -')
    bst.in_order_traversal()
    '''
    - BinaryTree in_order_traversal test -
    4 13 15 34 40 45 47 48 49
    '''

    # 이진 트리 후위 순회 함수
    print('- BinaryTree post_order_traversal test -')
    bst.post_order_traversal()
    '''
    - BinaryTree post_order_traversal test -
    13 15 34 4 47 49 48 45 40
    '''

    # 이진 트리 레벨 순회 함수
    print('- BinaryTree level_order_traversal test -')
    bst.level_order_traversal()
    '''
    - BinaryTree level_order_traversal test -
    40 4 45 34 48 15 47 49 13
    '''
