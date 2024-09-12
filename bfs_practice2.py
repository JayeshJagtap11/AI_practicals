from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add_edges(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)
        queue=[]

        queue.append(s)
        visited[s]=True
        while True:
            curr_n=queue.pop(0)
            print(curr_n,end=" ")
            for i in self.graph[curr_n]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        
                
    def dfs_utility(self,s,visited):
        visited.add(s)
        print(s,end=" ")
        for i in self.graph[s]:
            if i not in visited:
                self.dfs_utility(i,visited)
    def dfs(self,s):
        visited=set()
        self.dfs_utility(s,visited)

g=graph()
g.add_edges(0,1)
g.add_edges(0,2)
g.add_edges(1,2)
g.add_edges(2,0)
g.add_edges(2,3)
g.add_edges(3,3)
g.bfs(2)
        