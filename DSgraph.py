#edge list graph (shows all connecting points):
    #if weighted, each point would contain a third number to represent the weight
'''
    2--0
   / \ 
  1---3 
'''
edge = [(1,2), (1,3), (2,3), (2,0)]

#adjacenct list (value is node name):
    #if weighted zero would look like [(2,weight)] instead of [2]
    #can also use dict instead of array
'''
    2--0 <- the index of 0 contains 2, the index of 2 contains 0, 1 & 3
   / \ 
  1---3  <- the index of 1 contains 2 & 3, and the index of 3 contains 1 & 2
'''
adj = [[2], [2,3], [0,1,3], [1,2]]

#adjacent matrix (contains 0 if number not connected and 1 if number connected):
    #if weighted would put # of weight instead of 1
matrix = [[0,0,1,0], [0,0,1,1], [1,1,0,1], [0,1,1,0]]
              #^here the only number 0 is connected to is 2 

class Graph():

    def __init__(self):
        self.num_nodes = 0
        self.adj_list = {} 

    
    def add_vertex(self, node):
        if node not in self.adj_list.keys():
            self.adj_list.update({node:[]})
            self.num_nodes+=1
        

    def add_edge(self,n1,n2):
        if n1 not in self.adj_list.keys():
            self.adj_list.update({n1:[n2]})
            self.num_nodes +=1
        else:
            l = []
            l = self.adj_list.get(n1)
            l.append(n2)
            self.adj_list.update({n1:l})

        if n2 not in self.adj_list.keys():
            self.adj_list.update({n2 : [n1]})
            self.num_nodes +=1
        else:
            l = self.adj_list.get(n2)
            l.append(n1)
            self.adj_list.update({n2:l})


    def show_connections(self):
        print(self.adj_list)


if __name__ == "__main__":
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.show_connections()
    g.add_edge(1,2)
    g.show_connections()
    print(g.num_nodes)




