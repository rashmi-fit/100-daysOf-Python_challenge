class Graph:
    def __init__(self, edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges :
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("graph dict: ", self.graph_dict)


if __name__ =='__main__':
    routes=[
        ("Mumbai" , "Paris"),
        ("Mumbai" , "Dubai"),
        ("Pune" , "Dubai"),
        ("Dubai" , "New York"),
        ("New York" , "Torronto")

    ]

    route_graph= Graph(routes)


    d={
        "Mumbai" :["Paris","Dubai"],
        "Paris" :["Dubai","New York"]
    }