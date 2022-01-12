"""Find the maximum sum of the edges"""
def solution(N: int, A: list, B: list):
    """Test from Trend's online test.

    Key knowledge:
    Graph, adjacent list, dict sort and comprehesion, zip in python, hash map, seen/visit-list.

    Solution:
    1. generate adjacent list
    2. sort the list according to the number of edges connecting to the vertices
    3. assgin value to vertices according to the sorted result in a hash map
    4. traverse the vertices according the adjacent list
    5. Sum up the edges of vertices with visit-list to avoid the duplicate edges  

    :param N: Number of the vertices and the values can be assigned (1..N)
    :param A: A vertice of an edge. With B, it is the representation of edges between vertices
    :param B: B vertice of an edge
    :return The maximum sum of edges
    """
    # Generate adjacent list to represent the vertices and edges in graph
    adjacent_dict = {i: [] for i in range(1, N + 1, 1)}
    edges = list(zip(A, B))  # zip two lists into tuple
    for edge in edges:
        adjacent_dict[edge[0]].append(edge[1])
        adjacent_dict[edge[1]].append(edge[0])
    
    # Sort according to k, and k is the length of K's value
    # Sort the vertice according to the number of its edges to other vertices, 
    # as the values will be assigned according to it
    sorted_adjacency = dict(sorted(adjacent_dict.items(), key= lambda k: len(k[1]), reverse=True))

    # Vertices to value map
    vertice_value_dict = {i: [] for i in sorted_adjacency}

    value = N
    for vertice in vertice_value_dict:
        vertice_value_dict[vertice] = value
        value -= 1

    # Calculate the sum of the edges
    seen_edges = [] # need to know the edge which has been calculated
    total_sum = 0
    for vertice, edges in adjacent_dict.items():
        if edges:
            for edge in edges:
                if not sorted([vertice, edge]) in seen_edges:  # the calculated edges are not taken into account
                    total_sum += vertice_value_dict[vertice] + vertice_value_dict[edge]
                    seen_edges.append(sorted([vertice, edge]))

    return total_sum

def main():
    # edge (A, B)
    # (2,1), (2,4), (2,3), (1,3)
    A = [2, 2, 2, 1]
    B = [1, 4, 3, 3]
    N = 5 # number of vertice and the range of the value (1-5) which can be in the vertice
    # the maximum sum is 31 in this case. 
    result = solution(N, A, B)
    print(result)

if __name__ == "__main__":
    main()