class node:
      
    def __init__(self,data,level,fval):
         self.data=data
         self.level=level
         self.fval=fval
         
    def generate_child(self):
         children=[]
         x,y=self.empty_pos(self.data,"_")

         val_list=[[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
         for i in val_list:
              child=self.shuffel(x,y,i[0],i[1],self.data)
              if child is not None:
                   child_node=node(child,self.level+1,0)
                   children.append(child_node)
         return children
                   


    def shuffel(self,x1,y1,x2,y2,puz):
         
         if x2 >=0 and x2 <len(self.data) and y2>=0 and y2<len(self.data):
              template=[]
              template=self.copy_start(puz)
              temp=template[x2][y2]
              template[x2][y2]=template[x1][y1]
              template[x1][y1]=temp
              return template
         else:
              None

    def copy_start(self,root):
         copy_start=[]
         for i in root:
              t=[]
              for j in i:
                   t.append(j)
              copy_start.append(t)
         return copy_start

    def empty_pos(self,puz,x):
         for i in range(0,len(self.data)):
              for j in range(0,len(self.data)):
                   if puz[i][j]==x:
                     return i,j  
         
        
class my:
    def __init__(self,size):
         self.n=size
         self.open=[]
         self.cosed=[]

    

    def accept(self):
            """ Accepts the puzzle from the user """
            puzle=[]
            for i in range(0,3):
               temp=input().split(" ")
               puzle.append(temp)
            return puzle 
       
    def h(self,start,goal):
         temp=0                   #this function calculate the difference between start and goal state
         for i in range (0,self.n):
              for j in range(0,self.n):
                   if start[i][j]!=goal[i][j] and start[i][j]!="_":
                        temp+1
         return temp
         
         
    def f(self,start,goal):
         #it is the heurastic function
         return self.h(start.data,goal)+start.level
         
    def process(self):
            """ Accept Start and Goal Puzzle state"""
            print("Enter the starting state of puzzel:\n")
            start=self.accept()
            print(start)
            goal=self.accept()
            print(goal)
            start = node(start, 0, 0)
            start.fval = self.f(start, goal)
            """ Put the start node in the open list"""
            self.open.append(start)
            print("\n\n")
            while True:
                cur = self.open[0]
                print("---------------------------------------------------------------------------------------------------------------------------------------")
            
                for i in cur.data:
                    for j in i:
                        print(j, end=" ")
                    print(" ")
                """ If the difference between current and goal node is 0 we ha
                ve reached the goal node"""
                if(self.h(cur.data, goal) == 0):
                    break
                for i in cur.generate_child():
                    i.fval = self.f(i, goal)
                    self.open.append(i)
                self.closed.append(cur)
                del self.open[0]
                """ sort the opne list based on f value """
                self.open.sort(key=lambda x: x.fval, reverse=False)
           
obj=my(3)
obj.process()