class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return repr(self.data)

class Vertex(Node):
    def __init__(self,data,edges=[]):
        self.data = data
        self.edges = edges

    def __eq__(self,other):
        if isinstance(other,self.__class__):
            return self.data == other.data
        elif type(self.data) == type(other):
            return self.data == other
        else:
            return False
    def __ne__(self,other):
        return not self.__eq__(other)
    
class Graph:
    def __init__(self):
        self.vertices = []
        self.edge_list = [] #a list of dictionaries

    def print_nodes(self):
        for v in self.vertices:
            print v

    def print_edges(self):
        for pair in self.edge_list:
            print pair
            
    def add_node(self,vertex):
        v = Vertex(vertex)
        self.vertices.append(v)
        self.vertices.sort()

    def add_edge(self,vertex1,vertex2):
        if not vertex1 in self.vertices:
            self.add_node(vertex1)
        if not vertex2 in self.vertices:
            self.add_node(vertex2)
        v1 = Vertex(vertex1)
        v2 = Vertex(vertex2)
        v1.edges.append(v2)
        v2.edges.append(v1)
        self.edge_list.append({vertex1:vertex2})
        self.edge_list.append({vertex2:vertex1})
    
        
if __name__ == '__main__':
    g = Graph()
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5,7)
    g.print_nodes()
    g.print_edges()
    
