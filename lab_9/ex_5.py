def tree_edges(edges):
    res = list(edges)
    for edge in edges:
        if [edge[1], edge[0]] not in edges:
            res.append([edge[1], edge[0]])
    return sorted(res)


def prefix(edges, root=None, first=True):
    if edges == [] or root == None:
        if first and root != None:
            print(root, end='')
        return

    print(root, end='')

    for edge in edges:
        if edge[0] == root:
            edges_without_edge = list(edges)
            print(' ', end='')
            edges_without_edge.remove(edge)
            edges_without_edge.remove([edge[1], edge[0]])
            prefix(edges_without_edge, edge[1], False)


def postfix(edges, root=None, first=True):
    if edges == [] or root == None:
        if first and root != None:
            print(root)
        return

    for edge in edges:
        if edge[0] == root:
            edges_without_edge = list(edges)
            edges_without_edge.remove(edge)
            edges_without_edge.remove([edge[1], edge[0]])
            postfix(edges_without_edge, edge[1], False)

    if first:
        print(root)
    else:
        print(root, end=' ')


if __name__ == '__main__':
    r = int(input())
    edges = []
    try:
        while True:
            edge = list(map(int, input().split()))
            edges.append(edge)
    except:
        pass
    edges = tree_edges(edges)
    prefix(edges, r)
    print()
    postfix(edges, r)