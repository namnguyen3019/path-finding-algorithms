import copy


def dfs(maze, startNode, endNode):
    visited = set()
    trace_path = {}
    path = []
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def helper(maze, curNode, endNode):

        visited.add(curNode)

        # Check if current node is the end node
        if curNode == endNode:
            while curNode in trace_path and trace_path[curNode]:
                path.append(curNode)
                curNode = trace_path[curNode]
            path.append(startNode)  # add the start node
            return path
        # if not, keep moving to the next node
        for move in moves:
            nextNode = (curNode[0] + move[0], curNode[1] + move[1])
            (r, c) = nextNode
            # Check the out of index in the maze
            if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
                continue
            # Check if nextNode is visited:
            if nextNode not in visited:
                # if nextNode is available, do search
                if maze[r][c] == 0:
                    trace_path[nextNode] = curNode
                    helper(maze, nextNode, endNode)
        return []
    helper(maze, startNode, endNode)
    return path


def printMaze(maze):
    for row in maze:
        for cell in row:
            print("{:" ">3d}".format(cell), end="")
        print()


if __name__ == "__main__":
    # Represent maze: 0 is available, -1 is unavailable
    maze = [[0, -1, 0, 0],
            [0, 0, 0, 0],
            [0, -1, -1, 0],
            [0, 0, 0, 0]]
    start = (0, 0)  # starting position
    end = (3, 3)  # ending position
    original_maze = copy.deepcopy(maze)
    path = dfs(maze, start, end)
    print("path ", path)
    count = 0
    for cell in path[::-1]:
        maze[cell[0]][cell[1]] = count
        count += 1

    print("Original: ")
    printMaze(original_maze)
    print("Solved maze")
    printMaze(maze)
    print()
    print("Start to End: ", start, " =>", end)
    print("Path showed in the maze From 0 to ", len(path)-1)
    print("-1: unavailable, -2: available but not choosen")
