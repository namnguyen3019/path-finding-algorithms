'''
    Problem: Find shortest path from A to Z
    Solution:
    - Dijkstra's algorithm main idea:
    cost = {'A': 0, 'B': 'inf', 'C': 'inf', ...}    
    1. Initialize cost from A to other points = infinite. but cost['A'] = 0
    2. Travel from A to other nodeS using prority queue
    3. Constantly update the cost from point A to other nodes  

'''

import copy
import heapq
from collections import deque


def dijkstra(maze, startNode, endNode):
    cost = {startNode: 0}
    predecessors = {startNode: None}
    visited = set()
    path = []
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            cost[(r, c)] = float('inf')

    cost[startNode] = 0
    q = []
    heapq.heappush(q, [cost[startNode], startNode])

    while q:
        # USING HEAPQ
        curNode = heapq.heappop(q)[1]
        if curNode == endNode:
            while curNode in predecessors and predecessors[curNode]:
                path.append(curNode)
                curNode = predecessors[curNode]
            path.append(startNode)
            return path
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = set([])
        for move in moves:
            (r, c) = (curNode[0] + move[0], curNode[1] + move[1])
            # check out of bound
            if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
                continue
            # Check if next node is available, add to neighbors
            if maze[r][c] == 0:
                neighbors.add((r, c))

        # Default distance from curNode to its neighbors
        dist = 1
        for node in neighbors:
            if node in visited:
                continue
            heapq.heappush(q, [cost[node], node])
            new_cost = cost[curNode] + dist
            if new_cost < cost[node]:
                cost[node] = new_cost
                predecessors[node] = curNode
                for n in q:
                    if n[1] == node:
                        n[0] = new_cost
                        break
                heapq.heapify(q)
        visited.add(curNode)
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
    path = dijkstra(maze, start, end)
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
