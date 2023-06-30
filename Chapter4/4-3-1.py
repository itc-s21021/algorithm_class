LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, 10],
    [3, 4, 5],
    [5, None, 12],
    [None, None, 2],
    [6, 7, 8],
    [None, None, 11],
    [None, None, 6],
    [None, None, 9]
]

def travarse(p):
    if p != None:
        travarse(node[p][LEFT])
        print(node[p][DATA])
        travarse(node[p][RIGHT])

print("二分探索木を通りがけに巡回")
travarse(0)
