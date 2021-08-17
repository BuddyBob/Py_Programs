triangle = [[-1],[2,3],[1,-1,-3]]
def pathFind(tri):
    path = []
    for lines in tri: path.append(sorted(lines)[0])
    return sum(path)
print(pathFind(triangle))
