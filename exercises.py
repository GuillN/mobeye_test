import collections

# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)

def is_anagram(s1, s2):
    obj = {}
    for char in s1:
        if char in obj :
            obj[char] = obj[char] + 1
        else:
            obj[char] = 1
    for char in s2:
        if char in obj:
            obj[char] = obj[char] - 1
        else :
            return False
    for elem in obj:
        if elem != 0:
            return False
    return True

def check_parenthesis_consistency(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
            if count < 0 :
                return False
    return count == 0

def shortest_path(start, end, maze):
    # init queue and visited arrays
    queue = collections.deque([[start]])
    visited = {start}
    # init width and height of the maze
    width = len(maze[0])
    height = len(maze)
    # start operations
    while queue:
        # add queue element to path
        path = queue.popleft()
        x, y = path[-1]
        # check end condition: if ended return path
        if (x, y) == end:
            return path
        # if not ended continue building path by checking neighbors
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            # check if we are within maze boundaries, if we hit a wall and if we are backtracking
            if 0 <= y2 < width and 0 <= x2 < height and maze[x2][y2] != 0 and (x2, y2) not in visited:
                # add neighboring elements to queue and visited arrays
                queue.append(path + [(x2, y2)])
                visited.add((x2, y2))
    # if there is no path from start to end
    return False