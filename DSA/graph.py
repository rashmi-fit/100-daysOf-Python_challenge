# https://www.geeksforgeeks.org/finding-minimum-vertex-cover-graph-using-binary-search/

def isCover(V, k, E):

    # Set has first 'k' bits high initially
    Set = (1 << k) - 1

    limit = (1 << V)

    # to mark the edges covered in each
    # subSet of size 'k'
    vis = [[None] * maxn for i in range(maxn)]

    while (Set < limit):

        # ReSet visited array for every
        # subSet of vertices
        vis = [[0] * maxn for i in range(maxn)]

        # Set counter for number of edges covered
        # from this subSet of vertices to zero
        cnt = 0

        # selected vertex cover is the
        # indices where 'Set' has its bit high
        j = 1
        v = 1
        while(j < limit):
            if (Set & j):

                # Mark all edges emerging out of
                # this vertex visited
                for k in range(1, V + 1):
                    if (gr[v][k] and not vis[v][k]):
                        vis[v][k] = 1
                        vis[k][v] = 1
                        cnt += 1
            j = j << 1
            v += 1

        # If the current subSet covers all the edges
        if (cnt == E):
            return True

        # Generate previous combination with k bits high
        # Set & -Set = (1 << last bit high in Set)
        c = Set & -Set
        r = Set + c
        Set = (((r ^ Set) >> 2) // c) | r
    return False

# Returns answer to graph stored in gr[][]
def findMinCover(n, m):

    # Binary search the answer
    left = 1
    right = n
    while (right > left):
        mid = (left + right) >> 1
        if (isCover(n, mid, m) == False):
            left = mid + 1
        else:
            right = mid

    # at the end of while loop both left and
    # right will be equal,/ as when they are
    # not, the while loop won't exit the
    # minimum size vertex cover = left = right
    return left

# Inserts an edge in the graph
def insertEdge(u, v):
    gr[u][v] = 1
    gr[v][u] = 1 # Undirected graph

# Driver code
maxn = 25

# Global array to store the graph
# Note: since the array is global,
# all the elements are 0 initially
gr = [[None] * maxn for i in range(maxn)]

#
#     6
#     /
#     1 ----- 5 vertex cover = {1, 2}
#     /|\
# 3 | \
# \ | \
#     2 4
V = 6
E = 6
insertEdge(1, 2)
insertEdge(2, 3)
insertEdge(1, 3)
insertEdge(1, 4)
insertEdge(1, 5)
insertEdge(1, 6)
print("Minimum size of a vertex cover = ",
      findMinCover(V, E))

# Let us create another graph
gr = [[0] * maxn for i in range(maxn)]

#
#     2 ---- 4 ---- 6
#     /|     |
# 1 |     | vertex cover = {2, 3, 4}
#     \ |     |
#     3 ---- 5
V = 6
E = 7
insertEdge(1, 2)
insertEdge(1, 3)
insertEdge(2, 3)
insertEdge(2, 4)
insertEdge(3, 5)
insertEdge(4, 5)
insertEdge(4, 6)
print("Minimum size of a vertex cover = ",
      findMinCover(V, E))