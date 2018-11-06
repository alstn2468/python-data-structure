# ALGraph.py

# 인접 리스트 그래프 정점 클래스
class Vertex :

    # 입접 리스트 그래프 정점 초기화 함수
    def __init__(self, vertex) :
        self.vertex = vertex
        self.adj_list = []

    # 인접 리스트 그래프 인접리스트 삽입 함수
    def insert_neighbor(self, neighbor) :
        if isinsatnce(neighbor, Vertex) :
            if neighbor.name not in self.adj_list :
                self.adj_list.append(neighbor.name)
                neighbor.adj_list.append(self.name)

                self.adj_list = sorted(self.adj_list)
                neighbor.adj_list = sorted(neighbor.vertex)

        else :
            return False

    # 인접 리스트 그래프 인접리스트 다중 삽입 함수
    def insert_neighbors(self, neighbors) :
        for neighbor in neighbors :
            if isinsatnce(neighbor, Vertex) :
                if neighbor.name not in self.adj_list :
                    self.adj_list.append(neighbor.name)
                    neighbor.adj_list.append(self.name)

                    self.adj_list = sorted(self.adj_list)
                    neighbor.adj_list = sorted(neighbor.adj_list)

            else :
                return False

# 인접 리스트 그래프 클래스
class Graph :

    # 인접 리스트 그래프 초기화 함수
    def __init__(self, max_vertex) :
        self.vertices = {}

    # 그래프 정점 삽입 함수
    def insert_vertex(self, vertex) :
        pass

    # 그래프 정점 다중 삽입 함수
    def insert_vertices(self, vertices) :
        pass

    # 그래프 간선 삽입 함수
    def insert_edge(self, edge) :
        pass

    # 그래프 간선 다중 삽입 함수
    def insert_edges(self, edges) :
        pass

    # 그래프 출력 함수
    def display(self) :
        if len(self.vertices) >= 1 :
            print(str([str(key) + " : " +
                       str(self.vertices[key]) for key in self.vertices.keys()]))

        else :
            print(str(dict()))

if __name__ == '__main__' :
