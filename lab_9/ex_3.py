def edge_list(N, edges):
    ed_list = [set() for i in range(N)]
    for edge in edges:
        ed_list[edge[0]].add(edge[1])
        ed_list[edge[1]].add(edge[0])
    for v in range(N):
        ed_list[v] = list(ed_list[v])
        ed_list[v].sort()
    return ed_list


def print_graph(ed_list):
    for ed in ed_list:
        if ed == []:
            print()
        else:
            print(" ".join(map(str, ed)))

if __name__ == '__main__':
    N = int(input())
    edges = []
    try:
        while True:
            edge = tuple(map(int, input().split()))
            edges.append(edge)
    except:
        pass

    print_graph(edge_list(N, edges))