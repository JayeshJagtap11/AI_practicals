class node:
    def __init__(self,data,level,fval):
        self.data=data
        self.level=level
        self.fval=fval

    def find(self,data,x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if data[i][j]==x:
                    return i,j
                
    def generate_child(self):
        x,y=self.find(self.data,"_")
        future_val=[[x,y-1],[x,y+1],[x+1,y],[x-1,y]]
        children=[]
        for i in future_val:
            child=self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node=node(child,self.level+1,0)
                children.append(child_node)
        return children

    def shuffle(self,start,x,y,x1,y1):
      if x1>=0 and x1<len(self.data) and y1>=0 and y1<len(self.data):
        list=[]
        list=self.copy(start)
        temp=list[x1][y1]
        list[x1][y1]=list[x][y]
        list[x][y]=temp
        return list
      else:
          return None

    def copy(self,start):
        copy=[]
        for i in start:
            t=[]
            for j in i:
                t.append(j)
            copy.append(t)
        return copy
    
class main:
    def __init__(self,size):
        self.n=size
        self.open=[]
        self.closed=[]

    def accept(self):
        acc=[]
        for i in range (0,self.n):
            t=input().split(" ")
            acc.append(t)
        return acc

    def f(self,start,goal):
        return self.h(start,goal)+start.level
    
    def h(self,start,goal):
        temp=0
        for i in range (0,self.n):
            for j in range (0,self.n):
                if start[i][j]!=goal[i][j] and start[i][j]!="_":
                    temp+=1
        return temp
    
    def process(self):
        print("enter the start state:")
        start=self.accept()
        print("enter the goal state:")
        goal=self.accept()
        obj=node(start,0,0)
        obj.fval=self.f(start,goal)
        self.open.append(start)
        while True:
            curr=self.open[0]
            print("------------------------------------------------------------------------------------------------------------------------------")
            for i in curr:
                for j in i:
                    print(j,end=" ")
                print(" ")

            if(self.h(curr,goal)==0):
                break
            for i in curr.generate_child():
                i.fval=self.f(i,goal)
                self.open.append(i)
            self.closed.append(curr)
            del self.open[0]

            self.open.sorted(key=lambda x:x.fval,reversed=False)

p=main(3)
p.process()

    
    
