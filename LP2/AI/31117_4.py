# 31117 - Udayan Chavan - K1
# ASSIGNMENT 4 - Implement a solution for a graph coloring problem

class Graph:
    def __init__(self, edges, n):
        # n : number of vertices
        self.adjList = [[] for i in range(n)]
        
        # Adding edges to vertices
        for(s, d) in edges:
            self.adjList[s].append(d)
            self.adjList[d].append(s)

def colorGraph(graph, n):
    results = {}
    
    # Assigning colors to the vertices one by one
    for i in range(n):
        # Check for colors of adjacent vertices of i
        assignedColors = set([results.get(p) for p in graph.adjList[i] if p in results])               

        # Checking for colors
        color = 1
        for c in assignedColors:
            if color != c:
                break;
            color += 1
            
        # Assigning the first available color to i
        results[i] = color
        
    # Display function
    for p in range(len(results)):
        print("Color assigned to vertex", p, "is", colors[results[p]])
    
# ------------------------------------------------------------------------------------------------

colors = ['', 'Blue', 'Green', 'Yellow', 'Orange', 'Pink', 'White', 'Purple', 'Black', 'Cyan']

# Enter the number of vertices and edges here
n = 6
e = ((0, 1), (0, 5), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (4, 5))

# --------------------------------------------

# Create a graph 
g = Graph(e, n)

# Color the graph
colorGraph(g, n)