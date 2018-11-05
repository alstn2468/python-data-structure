# Graph.py

# 그래프 클래스 선언
class Graph :

    def __init__(self, graph_dict = None) :
        if graph_dict is None :
            graph_dict = {}

        self.graph_dict = graph_dict

    # 그래프 정점 삽입 함수
    def insert_vertex(self, vertex) :
        if vertex not in self.graph_dict :
            self.graph_dict[vertex] = []

    # 그래프 간선 삽입 함수
    def insert_edge(self, edge) :
        edge = set(edge)

        (vertex1, vertex2) = tuple(edge)

        if vertex1 in self.graph_dict :
            self.graph_dict[vertex1].append(vertex2)

        else :
            self.graph_dict[vertex2] = [vertex2]

if __name__ == '__main__' :
