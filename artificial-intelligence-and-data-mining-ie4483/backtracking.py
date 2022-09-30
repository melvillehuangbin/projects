# graph =
# [
#     {'node': 'A', 'children': ['B', 'C', 'D']},
#     {'node': 'B', 'children': ['E', 'F']},
#     {'node': 'C', 'children': ['F', 'G']},
#     {'node': 'D', 'children': []},
#     {'node': 'E', 'children': ['H', 'I']},
#     {'node': 'H', 'children': []},
#     {'node': 'I', 'children': []},
#     {'node': 'F', 'children': ['J']},
#     {'node': 'G', 'children': []},
#     {'node': 'J', 'children': []},
# ]

# node:children
# simple implementation of backtracking algorithm
graph =
[
    {'A': ['B', 'C', 'D']},
    {'B': ['E', 'F']},
    {'C': ['F', 'G']},
    {'D': []},
    {'E': ['H', 'I']},
    {'H': []},
    {'I': []},
    {'F': ['J']},
    {'G': []},
    {'J': []},
]

CS = graph[0]['node']
SL = [graph[0]['node']]
NSL = [graph[0]['node']]
DE = []
goal = 'G'

if CS = goal:
    return SL

for nodes in graph:
    for node, children in nodes.items():
        if (nodes[CS] = null) and (CS = SL[0]):
            while (not SL) and CS = SL[0]:
                DE.append(CS)
