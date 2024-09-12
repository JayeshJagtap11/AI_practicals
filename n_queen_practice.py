# global N
# N=4

# def display_solution(board):
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j],end=" ")
#         print()

# def isSafe(board,col,row):
#     for i in range (N):
#         if board[row][col]==1:
#             return False
#     for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
#         if board[i][j]==1:
#             return False
#     for i,j in zip(range(row,N,1),range(col,-1,-1)):
#         if board[i][j]==1:
#             return False
#     return True
    
        
    

# def solve(board,col):
#     if col>=N:
#         return True
#     for i in range (N):
#         if isSafe(board,col,i):
#             board[i][col]="Q"

#             if solve(board,col+1)==True:
#                 return True

#             board[i][col]=0
#     return False
    
    
# def main1():
#     board=[[0,0,0,0],
#            [0,0,0,0],
#            [0,0,0,0],
#            [0,0,0,0]]
    
#     if solve(board,0)==False:
#         print("solution does not exists")
#         return False
#     display_solution(board)
#     return True
# main1()



global S
S=4

def result(board):
    for i in range(S):
        for j in  range(S):
            print(board[i][j],end=" ")
        print()

def issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,S,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True

def solve(board,col):
    if col>=S:
        return True
    for i in range(S):
        if issafe(board,i,col):
            board[i][col]=1

            if solve(board,col+1)==True:
                return True
            board[i][col]=0
    return False

def main():
    board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    
    if solve(board,0)==False:
        print("solution is not exists")
        return False
    
    result(board)
    return True

main()
