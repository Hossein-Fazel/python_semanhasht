from dataclasses import dataclass
from collections import defaultdict as dd
from typing import Any

@dataclass()
class edge:
    line : str
    vehicle : str
    value : float = float("inf")

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


class Tehran:
    def __init__(self):
        self.city_graph = dd(lambda : dd(paths))
    
    def read_from_file(self, *names):
        for name in names:
            try:
                file = open(f"{name}.txt", 'r')
                line = file.readline().replace(":\n" , "")
                stat1 = ""
                stat2 = ""
                dist = 0
                while True:
                    # read parts like line, station1, station2 and distance
                    stat1 = file.readline().replace("\n", "")
                    if stat1 == "" or line == "":
                        break
                    elif stat1 == "end" :
                        line = file.readline()
                        continue
                    stat2 = file.readline().replace("\n", "")
                    dist = int(file.readline().replace("\n", ""))

                    if line[0] == 'l':
                        e1 = edge(dist, line, "Subway")
                        e2 = edge(dist, line, "Taxi")

                        self.city_graph[stat1][stat2].add_edge(e1)
                        self.city_graph[stat1][stat2].add_edge(e2)

                        self.city_graph[stat2][stat1].add_edge(e1)
                        self.city_graph[stat2][stat1].add_edge(e2)

                    elif line[0] == 'b':
                        e1 = edge(dist, line, "Bus")

                        self.city_graph[stat1][stat2].add_edge(e1)
                        self.city_graph[stat2][stat1].add_edge(e1)
            except:
                raise ValueError(f"There is no file with name {name}")