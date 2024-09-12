import sys
class prims:
    #inintilization function for intilizing vertices and graph
    def __init__(self,vertices,graph):
        self.v=vertices
        self.graph=graph

    #this is solution funtion is only responsible for the displying mst 
    def solution(self,parent):
        for i in range(self.v):
            print("edges\t\t","weight")
            print(parent[i],"\t",i,"\t",graph[i][parent[i]])

    #this is utility function is finding minimum key value for vertices
      #--key[i] is less than infinity
      #--mstset[i] is false
      #we have to return min value
    def find_min(self,key,mstset):
        min=sys.maxsize
        for i in range(self.v):
            if key[i]<min and mstset[i]==False:
                min=key[i]
                min_value=i
        return min_value

    #this is our main function which is algorithm for finding MST
    def prims(self):
        mstset=[False]*self.v
        key=[sys.maxsize]*self.v
        parent=[None]*self.v
        
        key[0]=0
        parent[0]=-1
        #upto this initialization step
        #below that execution step
        for i in range(self.v):
            u=self.find_min(key,mstset)
            mstset[u]=True #if minimum key is found then add to mstset
            #this is for updating the adjacent vertices of u
            #for that also we have conditions
            #--key[i]>graph[u][i]
            #--then key[i]=graph[u][i]
            #--update parent[i]=u
            for v in range(self.v):
                if graph[u][v]>0 and mstset[v]==False and key[v]>graph[u][v]:
                    key[v]=graph[u][v]
                    parent[v]=u
        self.solution(parent)



graph=[     [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
obj=prims(5,graph)
obj.prims()


        