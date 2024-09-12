from collections import defaultdict

class kruskal:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[]
    
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i]==i:
            return i
        self.find(parent,parent[i])


    def unioun(self,parent,rank,x,y):
        x_root=self.find(parent,x)
        y_root=self.find(parent,y)

        if rank[x_root]<rank[y_root]:
            rank[x_root]=rank[y_root]
        elif rank[y_root]<rank[x_root]:
            rank[y_root]=rank[x_root]
        else:
            rank[y_root]=rank[x_root]
            rank[x_root]+=1


    def kruskal(self):
        result=[]
        i=0
        e=0
        self.graph=sorted(self.graph,key=lambda item:item[2])
        parent=[]
        rank=[]
        for i in range(self.vertices):
            parent.append(i)
            rank.append(0)

        while e < self.vertices-1:
            u,v,w=self.graph[i]
            i=i+1

            x=self.find(parent,u)
            y=self.find(parent,v)

            if x!=y:
                result.append([u,v,w])
                self.unioun(parent,rank,x,y)


        total_cost=0
        for u,v,w in result:
            total_cost=total_cost+w
            print("%d -- %d == %d" % (u, v, w))
        print(total_cost)

                

g = kruskal(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)          
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
# Function call
g.kruskal()