# lab04

from Stack import Stack

def solveMaze(maze, startX, startY):
    stack = Stack()
    stack.push([startX, startY])
    stepnum = 1
    maze [startX] [startY] = stepnum
    while stack.isEmpty() == False:
        currentx, currenty = stack.peek()
    
        if (maze[currentx-1][currenty] == ' ') or (maze[currentx-1][currenty] == 'G'):
            if maze[currentx-1][currenty] == 'G':
                return True
            stack.push([currentx-1,currenty])
            stepnum += 1
            maze[currentx-1][currenty] = stepnum 
        elif (maze[currentx][currenty-1] == ' ') or (maze[currentx][currenty-1] == 'G'):
            if maze[currentx][currenty-1] == 'G':
                return True
            stack.push([currentx,currenty-1])
            stepnum += 1
            maze[currentx][currenty-1] = stepnum
        
        elif (maze[currentx+1][currenty] == ' ') or (maze[currentx+1][currenty] == 'G'):
            if maze[currentx+1][currenty] == 'G':
                return True
            stack.push([currentx+1,currenty])
            stepnum += 1
            maze[currentx+1][currenty] = stepnum
        
        elif (maze[currentx][currenty+1] == ' ') or (maze[currentx][currenty+1] == 'G'):
            if maze[currentx][currenty+1] == 'G':
                return True
            stack.push([currentx,currenty+1])
            stepnum += 1
            maze[currentx][currenty+1] = stepnum
        else:
            stack.pop()
            if stack.isEmpty():
                return False
    return False
