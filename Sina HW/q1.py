def get_component(component, node, visited):
    visited[node] = True
    component.append(node)
    for adj_node in adj[node]:
        if not visited[adj_node]:
            component = get_component(component, adj_node, visited)
    return component


no_nodes, no_edges = list(map(int, input().split()))
adj = [[] for i in range(no_nodes)]
for _ in range(no_edges):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

visited = []
components = []
for _ in range(no_nodes):
    visited.append(False)
for node in range(no_nodes):
    if not visited[node]:
        component = []
        components.append(get_component(component, node, visited))
# print(components)
# print()

for component in components:
    adj_matrix = [[1 if (component[j] in adj[component[i]]) else 0 for j in range(len(component))] for i in range(len(component))]
    for row in adj_matrix:
        print(row)
    print()
    
