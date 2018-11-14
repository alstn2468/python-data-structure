# Graph.py

# 그래프 정점 클래스
class Vertex :

    # 그래프 정점 초기화 함수
    def __init__(self, vertex) :
        self.name = vertex
        self.neighbors = []

    # 그래프 인접리스트 삽입 함수
    def insert_neighbor(self, neighbor) :
        if isinstance(neighbor, Vertex) :
            if neighbor.name not in self.neighbors :
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)

                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)

        else :
            return False

    # 그래프 인접리스트 다중 삽입 함수
    def insert_neighbors(self, neighbors) :
        for neighbor in neighbors :
            if isinstance(neighbor, Vertex) :
                if neighbor.name not in self.neighbors :
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)

                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)

            else :
                return False

    def __repr__(self) :
        return str(self.neighbors)

# 그래프 클래스
class Graph :

    # 그래프 초기화 함수
    def __init__(self) :
        self.vertices = {}

    # 그래프 정점 삽입 함수
    def insert_vertex(self, vertex) :
        if isinstance(vertex, Vertex) :
            self.vertices[vertex.name] = vertex.neighbors

    # 그래프 정점 다중 삽입 함수
    def insert_vertices(self, vertices) :
        for vertex in vertices :
            if isinstance(vertex, Vertex) :
                self.vertices[vertex.name] = vertex.neighbors

    # 그래프 간선 삽입 함수
    def insert_edge(self, vertex_from, vertex_to) :
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex) :
            vertex_from.insert_neighbor(vertex_to)

            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex) :
                self.vertices[vertex_from.name] = vertex_from.neighbors;
                self.vertices[vertex_to.name] = vertex_to.neighbors;

    # 그래프 간선 다중 삽입 함수
    def insert_edges(self, edges) :
        for edge in edges :
            self.insert_edge(edge[0], edge[1])

    # 그래프 인접 리스트 반환 함수
    def adjacency_list(self) :
        if len(self.vertices) >= 1 :
            for key in self.vertices.keys() :
                print(str(key) + " : " + str(self.vertices[key]))

        else :
            print(dict())

    # 그래프 인접 행렬 반환 함수
    def adjacency_matrix(self) :
        if len(self.vertices) >= 1 :
            import numpy as np

            self.vertex_names = sorted(g.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names))))
            self.adjacency_matrix = np.zeros(shape = (len(self.vertices), len(self.vertices)))

            for i in range(len(self.vertex_names)) :
                for j in range(i, len(self.vertices)) :
                    for el in g.vertices[self.vertex_names[i]] :
                        j = g.vertex_indices[el]
                        self.adjacency_matrix[i, j] = 1

            print(self.adjacency_matrix)

        else :
            print(dict())

if __name__ == '__main__' :

    # 정점 클래스 정의
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')

    # 각 정점 연결 정점 삽입
    a.insert_neighbors([b, c, e])
    b.insert_neighbors([a, c])
    c.insert_neighbors([b, d, a, e])
    d.insert_neighbor(c)
    e.insert_neighbors([a, c])
    '''
    현재 정점 상태
    'A' : ['B', 'C', 'E']
    'B' : ['A', 'C']
    'C' : ['A', 'B', 'D', 'E']
    'D' : ['C']
    'E' : ['A', 'C']
    '''

    # 그래프 클래스 선언
    g = Graph()

    # 그래프 정점 삽입
    g.insert_vertices([a, b, c, d, e])

    # 그래프 인접 리스트 출력
    print("- Graph Adjacency List -")
    g.adjacency_list()
    '''
    - Graph Adjacency List -
    A : ['B', 'C', 'E']
    B : ['A', 'C']
    C : ['A', 'B', 'D', 'E']
    D : ['C']
    E : ['A', 'C']
    '''

    print()

    # 그래프 인접 행렬 출력
    print("- Graph Adjacency Matrix -")
    g.adjacency_matrix()
    '''
    - Graph Adjacency Matrix -
    [[ 0.  1.  1.  0.  1.]
     [ 1.  0.  1.  0.  0.]
     [ 1.  1.  0.  1.  1.]
     [ 0.  0.  1.  0.  0.]
     [ 1.  0.  1.  0.  0.]]
    '''

    print()

    # 그래프 간선 삽입
    g.insert_edge(b, d)
    '''
    현재 정점 상태
    'A' : ['B', 'C', 'E']
    'B' : ['A', 'C', 'D']
    'C' : ['A', 'B', 'D', 'E']
    'D' : ['B', 'C']
    'E' : ['A', 'C']
    '''

    print("- Graph Adjacency List -")
    g.adjacency_list()
    '''
    - Graph Adjacency List -
    A : ['B', 'C', 'E']
    B : ['A', 'C', 'D']
    C : ['A', 'B', 'D', 'E']
    D : ['B', 'C']
    E : ['A', 'C']
    '''

    print()

    print("- Graph Adjacency Matrix -")
    g.adjacency_matrix()
    '''
    - Graph Adjacency Matrix -
    [[ 0.  1.  1.  0.  1.]
     [ 1.  0.  1.  1.  0.]
     [ 1.  1.  0.  1.  1.]
     [ 0.  1.  1.  0.  0.]
     [ 1.  0.  1.  0.  0.]]
    '''
