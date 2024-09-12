# # now i am implementing queue using list

# queue=[]

# # enqueue
# queue.append(2)
# queue.append(5)
# queue.append(10)

# # dequeue
# queue.pop(0)

# # peek
# print(queue[0])

# # isempty
# print(not bool(queue))

# # size
# print(len(queue))
# print(queue)

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

# from collections import defaultdict
# # This class represents a directed graph
# # using adjacency list representation
# class Graph:
# # Constructor
#         def __init__(self):
#             # default dictionary to store graph
#             self.graph = defaultdict(list)
#             # function to add an edge to graph
#         def addEdge(self,u,v):
#             self.graph[u].append(v)
#             # Function to print a BFS of graph
#         def BFS(self, s):
#             # Mark all the vertices as not visited
#             visited = [False] * (max(self.graph) + 1)
#             # Create a queue for BFS
#             queue = []
#             # Mark the source node as
#             # visited and enqueue it
#             queue.append(s)
#             visited[s] = True
#             while queue:
#             # Dequeue a vertex from
#             # queue and print it
#                 curr_n = queue.pop(0)
#                 print (curr_n, end = " ")
#                 # Get all adjacent vertices of the
#                 # dequeued vertex s. If a adjacent
#                 # has not been visited, then mark it

#                 # visited and enqueue it
#                 for i in self.graph[curr_n]:
#                     if visited[i] == False:
#                         queue.append(i)
#                     visited[i] = True

# # Driver code
# # Create a graph given in
# # the above diagram
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
# print ("Following is Breadth First Traversal"
# " (starting from vertex 2)")
# g.BFS(0)
# print(g.graph)


from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def create_gaph(self,u,v):
        self.graph[u].append(v)
    

    def BFS(self, s):
            # Mark all the vertices as not visited
            visited = [False] * (max(self.graph) + 1)
            # Create a queue for BFS
            queue = []
            # Mark the source node as
            # visited and enqueue it
            queue.append(s)
            visited[s] = True        
            while queue:
            # Dequeue a vertex from
            # queue and print it
                curr_n = queue.pop(0)
                print (curr_n, end = " ")
                # Get all adjacent vertices of the
                # dequeued vertex s. If a adjacent
                # has not been visited, then mark it

                # visited and enqueue it
                for i in self.graph[curr_n]:
                    if visited[i] == False:
                        queue.append(i)
                    visited[i] = True

    def dfs_util(self,v,visited):
         visited.add(v)
         print(v,end=" ")

         for neighbour in self.graph[v]:
              if neighbour not in visited:
                   self.dfs_util(neighbour,visited)

    def dfs(self,v):
         visited=set()
         self.dfs_util(v,visited)

obj=graph()
obj.create_gaph(0,1)
obj.create_gaph(0,2)
obj.create_gaph(1,2)
obj.create_gaph(2,0)
obj.create_gaph(2,3)
obj.create_gaph(3,3)
print(obj.graph)
obj.BFS(2)
print("\n")
obj.dfs(2)




