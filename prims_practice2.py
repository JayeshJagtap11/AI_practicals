import sys
class Graph:
    def __init__(self,vetices,graph1):
        self.v=vetices
        self.graph1=graph1

    def solution(self,parent):
        print("edges\t\t\tweight")
        for i in range(self.v):
            print(parent[i],"\t",i,"\t",graph1[i][parent[i]])

    def find_min(self,key,mstset):
        min=sys.maxsize
        for i in range(self.v):
            if key[i]<min and mstset[i]==False:
                min=key[i]
                min_value=i
        return min_value

    def prims(self):
        mstset=[False]*self.v
        parent=[None]*self.v
        key=[sys.maxsize]*self.v
        key[0]=0
        parent[0]=-1

        for i in range (self.v):
            u=self.find_min(key,mstset)
            mstset[u]=True

            for v in range(self.v):
                if graph1[u][v]>0 and mstset[v]==False and key[v]>graph1[u][v]:
                    key[v]=graph1[u][v]
                    parent[v]=u
        self.solution(parent)

graph1=[     [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
g=Graph(5,graph1)
g.prims()
