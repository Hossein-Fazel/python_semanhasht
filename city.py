from dataclasses import dataclass

@dataclass
class edge:
    value : float = float("inf")
    line : str
    vehicle : str

class paths:
    def __init__(self):
        self.edges :list[edge] = []

    def add_edge(self, path :edge):
        if isinstance(path, edge):
            self.edges.append(path)

    def get_min_dist(self):
        medge = edge()

        for item in self.edges:
            if medge.value > item.value :
                medge = item
        
        return medge

    def get_vehicle(self, line:str, name:str):
        for item in self.edges:
            if item.line == line and item.vehicle == name:
                return item
