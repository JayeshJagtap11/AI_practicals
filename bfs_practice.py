from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def add_edges(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)

        
        queue=[]
        visited[s]=True
        queue.append(s)
        
        while True:
            curr_v=queue.pop(0)
            print(curr_v,end=" ")
            for i in self.graph[curr_v]:
                if visited[i]==False:
                    queue.append(i)
                visited[i]=True

    def new(self,visited,s):
        visited.add(s)
        print(s,end=" ")
        for i in self.graph:
            if i not in visited:
                
                self.new(visited,i)
        
    def dfs(self,s):
        visited=set()
        self.new(visited,s)

    

        
    


obj=graph()
obj.add_edges(0,1)
obj.add_edges(0,2)
obj.add_edges(1,2)
obj.add_edges(2,0)
obj.add_edges(2,3)
obj.add_edges(3,3)
print(obj.graph)
# obj.bfs(2)
obj.dfs(2)