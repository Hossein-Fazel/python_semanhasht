from dataclasses import dataclass
from collections import defaultdict as dd

from Time import Time
from Vehicle import machine
@dataclass
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
        medge = edge("", "", float("inf"))

        for item in self.edges:
            if medge.value > item.value :
                medge = item
        
        return medge

    def get_vehicle(self, line:str, name:str):
        for item in self.edges:
            if item.line == line and item.vehicle == name:
                return item

@dataclass
class save_direction:
    line : list[str]
    vehicle :list[str]
    stations: list[str]
    value : float = float("inf")

class Tehran:
    def __init__(self):
        self.city_graph = dd(lambda : dd(paths))
        self.nodes = dd(list[tuple])
        self.lines = dd(list[str])
    
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
                        e1 = edge(line, "Subway", dist)
                        e2 = edge(line, "Taxi", dist)

                        self.city_graph[stat1][stat2].add_edge(e1)
                        self.city_graph[stat1][stat2].add_edge(e2)

                        self.city_graph[stat2][stat1].add_edge(e1)
                        self.city_graph[stat2][stat1].add_edge(e2)

                        self.nodes[stat1].append((line, "Subway"))
                        self.nodes[stat1].append((line, "Taxi"))

                        self.nodes[stat2].append((line, "Subway"))
                        self.nodes[stat2].append((line, "Taxi"))

                    elif line[0] == 'b':
                        e1 = edge(line, "Bus", dist)

                        self.city_graph[stat1][stat2].add_edge(e1)
                        self.city_graph[stat2][stat1].add_edge(e1)

                        self.nodes[stat1].append((line, "Bus"))
                        self.nodes[stat2].append((line, "Bus"))

                    if(stat1 not in self.lines[line]):
                        self.lines[line].append(stat1)
                    if(stat2 not in self.lines[line]):
                        self.lines[line].append(stat2)

            except:
                raise ValueError(f"There is no file with name {name}")
    
    def get_min(self, nodes: dd, visited: set):
        min_num = float("inf")
        min_name = ""
        for key, value in nodes.items():
            if value.value < min_num and (key not in visited):
                min_num = value.value
                min_name = key

        return min_name
    
    def find_shortest_path(self, src:str, dest:str):
        visited_node : set[str] = set()
        node_data = dd(lambda : save_direction([] , [] , []))
        node_data[src].value = 0;
        node_data[src].stations.append(src)

        for i in range(len(self.city_graph)):
            min_station = self.get_min(node_data, visited_node)
            visited_node.add(min_station)

            if min_station == dest:
                break;
            for key,value in self.city_graph[min_station].items():
                if (key not in visited_node and value.get_min_dist().value != float("inf") and
                    node_data[min_station].value != float("inf") and value.get_min_dist().value + node_data[min_station].value < node_data[key].value):

                    node_data[key].value = value.get_min_dist().value + node_data[min_station].value
                    
                    node_data[key].line = node_data[min_station].line.copy()
                    node_data[key].line.append(value.get_min_dist().line)

                    node_data[key].stations = node_data[min_station].stations.copy()
                    node_data[key].stations.append(key)
            
        
        return node_data[dest]

    def print_sp(self, path:save_direction): # print shortest path function
        print(f"{path.value} Km")
        for i in range(len(path.stations) - 1):
            print(f"{path.stations[i]} -- ", end="")

            if path.line[i][0] == 'b':
                print("Bus", end="")
            elif path.line[i][0] == 'l':
                print("Subway or Taxi", end="")
            
            print(" --> ", end="")
        
        print(path.stations[len(path.stations) - 1])