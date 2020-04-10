import numpy as np

def dfs(array, start, goal):
    neighbors = np.array([(0, 1), (-1, 1), (-1, 0), (-1, -1),
                          (0, -1), (1, -1), (1, 0), (1, 1)])
    stack = []
    stack.append(start)
    step = 0

    while stack:
        step += 1
        print("Step: ", step)
        
        cNode = stack.pop()
        mapStats[cNode[0]][cNode[1]] = 2

        for i in range(np.shape(mapStats)[0]):
            for j in range(np.shape(mapStats)[1]):
                if mapStats[i][j] == 1:
                    print('■', end='')
                elif mapStats[i][j] == 0:
                    print(' ', end='')
                else:
                    print(nmap[i][j], end='')
            print()
        print()

        if np.array_equal(cNode, goal):
            return

        for i in range(len(neighbors)):
            nNode = cNode + neighbors[i]
            if nmap[nNode[0]][nNode[1]] == 0 and mapStats[nNode[0]][nNode[1]] == 0:
                stack.append(nNode)
            else:
                pass

nmap = np.array([(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                 (0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                 (1, 1, 1, 1, 1, 1, 1, 0, 1, 1),
                 (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                 (1, 0, 1, 1, 0, 1, 1, 1, 1, 1),
                 (1, 0, 0, 1, 0, 1, 0, 0, 0, 1),
                 (1, 0, 1, 1, 0, 1, 0, 1, 0, 1),
		         (1, 0, 1, 1, 1, 1, 0, 1, 0, 1),
		         (1, 0, 0, 0, 0, 0, 0, 1, 0, 1),
		         (1, 1, 1, 1, 1, 1, 1, 1, 0, 1)])

mapStats = np.array([(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                     (1, 1, 1, 1, 1, 1, 1, 0, 1, 1),
                     (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                     (1, 0, 1, 1, 0, 1, 1, 1, 1, 1),
                     (1, 0, 0, 1, 0, 1, 0, 0, 0, 1),
                     (1, 0, 1, 1, 0, 1, 0, 1, 0, 1),
		             (1, 0, 1, 1, 1, 1, 0, 1, 0, 1),
		             (1, 0, 0, 0, 0, 0, 0, 1, 0, 1),
		             (1, 1, 1, 1, 1, 1, 1, 1, 0, 1)])

print("Map:")
for i in range(np.shape(nmap)[0]):
    for j in range(np.shape(nmap)[1]):
        if nmap[i][j] == 1:
            print('■ ', end='')
        elif nmap[i][j] == 0:
            print('  ', end='')
        else:
            print(nmap[i][j], end='')
    print()

print("=============START=============")

start = np.array([1, 0])
goal = np.array([9, 8])
dfs(nmap, start, goal)
