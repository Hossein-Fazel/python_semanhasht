from dataclasses import dataclass
from collections import defaultdict as dd
from copy import copy

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
        return edge("", "")

@dataclass
class save_direction:
    line : list[str]
    vehicle :list[str]
    stations: list[str]
    value : float = float("inf")
    minutes : int = 0

    def __copy__(self):
        return save_direction(copy(self.line), copy(self.vehicle), copy(self.stations), self.value, self.minutes)

class Tehran:
    def __init__(self):
        self.city_graph = dd(lambda : dd(paths))
        self.nodes = dd(set[tuple])
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
                        line = file.readline().replace(":\n" , "")
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

                        self.nodes[stat1].add((line, "Subway"))
                        self.nodes[stat1].add((line, "Taxi"))

                        self.nodes[stat2].add((line, "Subway"))
                        self.nodes[stat2].add((line, "Taxi"))

                    elif line[0] == 'b':
                        e1 = edge(line, "Bus", dist)

                        self.city_graph[stat1][stat2].add_edge(e1)
                        self.city_graph[stat2][stat1].add_edge(e1)

                        self.nodes[stat1].add((line, "Bus"))
                        self.nodes[stat2].add((line, "Bus"))

                    if(stat1 not in self.lines[line]):
                        self.lines[line].append(stat1)
                    if(stat2 not in self.lines[line]):
                        self.lines[line].append(stat2)

            except:
                raise ValueError(f"There is no file with name {name}")
    
    def get_min(self, dj_table: dd, visited: set):

        min_num = float("inf")
        min_name = ""
        for key, value in dj_table.items():
            if value.value < min_num and (key not in visited):
                min_num = value.value
                min_name = key

        return min_name
    
    def find_shortest_path(self, src:str, dest:str):
        if src in self.city_graph.keys() and dest in self.city_graph.keys():
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
                    if (key not in visited_node and node_data[min_station].value != float("inf") 
                        and value.get_min_dist().value + node_data[min_station].value < node_data[key].value):

                        node_data[key].value = value.get_min_dist().value + node_data[min_station].value
                        
                        node_data[key].line = node_data[min_station].line.copy()
                        node_data[key].line.append(value.get_min_dist().line)

                        node_data[key].stations = node_data[min_station].stations.copy()
                        node_data[key].stations.append(key)

                        node_data[key].vehicle = node_data[min_station].vehicle.copy()
                        node_data[key].vehicle.append("Subway or Taxi" if value.get_min_dist().line[0] == 'l' else "Bus")
                
            return node_data[dest]
        else:
            raise ValueError("Station does not exist!")

    def print_sp(self, path:save_direction): # print shortest path function
        print(f"\n{" Shortest Path ":-^30}")
        print(f"{path.value} Km")
        for i in range(len(path.vehicle)):
            print(f"{path.stations[i]} -- {path.vehicle[i]} --> ", end="")
        
        print(path.stations[len(path.stations) - 1])
    
    def travel_line_time(self, line : str, vehicle:str, src:str, t1: Time, dj_table: dd[str, save_direction], visited: set[str]):
        src_index = self.lines[line].index(src)
        m1 = machine(vehicle)
        start_time = copy(dj_table[src])

        for i in range(src_index, len(self.lines[line])-1):
            if self.lines[line][i+1] not in visited:

                if i == src_index:
                    if len(start_time.line) == 0:
                        start_time.value += m1.get_in_time(t1 + start_time.value)
                    elif start_time.line[len(start_time.line) - 1] != line:
                        start_time.value += m1.get_in_time(t1 + start_time.value)
                    elif start_time.vehicle[len(start_time.vehicle) - 1] != vehicle:
                        start_time.value += m1.get_in_time(t1 + start_time.value)
                
                start_time.value += (self.city_graph[self.lines[line][i]][self.lines[line][i+1]].get_vehicle(line, vehicle).value
                                      * m1.get_pass_time(t1 + start_time.value))
                start_time.stations.append(self.lines[line][i+1])
                start_time.line.append(line)
                start_time.vehicle.append(vehicle)

                if start_time.value < dj_table[self.lines[line][i+1]].value:
                    dj_table[self.lines[line][i + 1]] = copy(start_time)
            else:
                break
        
        start_time = copy(dj_table[src])

        for i in range(src_index, 0, -1):
            if self.lines[line][i-1] not in visited:

                if i == src_index:
                    if len(start_time.line) == 0:
                        start_time.value += m1.get_in_time(t1 + start_time.value)
                    elif start_time.line[len(start_time.line) - 1] != line:
                        start_time.value += m1.get_in_time(t1 + start_time.value)
                    elif start_time.vehicle[len(start_time.vehicle) - 1] != vehicle:
                        start_time.value += m1.get_in_time(t1 + start_time.value)

                start_time.value += (self.city_graph[self.lines[line][i]][self.lines[line][i - 1]].get_vehicle(line, vehicle).value 
                                      * m1.get_pass_time(t1 + start_time.value))
                start_time.stations.append(self.lines[line][i - 1])
                start_time.line.append(line)
                start_time.vehicle.append(vehicle)

                if start_time.value < dj_table[self.lines[line][i - 1]].value:
                    dj_table[self.lines[line][i - 1]] = copy(start_time)
                    
            else:
                break
    
    def find_best_time(self, src: str, dest: str, t1: Time):
        if src in self.city_graph.keys() and dest in self.city_graph.keys():
            visited_node : set[str] = set()
            node_data = dd(lambda : save_direction([] , [] , []))

            node_data[src].value = 0;
            node_data[src].stations.append(src)

            for i in range(len(self.city_graph)):
                min_station = self.get_min(node_data, visited_node)

                if min_station == dest:
                    break;
                for pair in self.nodes[min_station]:
                    self.travel_line_time(pair[0], pair[1], min_station, t1, node_data, visited_node)
                
                visited_node.add(min_station)
                
            return node_data[dest]
        else:
            raise ValueError("Station does not exist!")
    
    def print_bt(self, path: save_direction, t1: Time):
        print(f"\n{" Best Time ":-^30}")

        print(t1 + path.value)

        for i in range(len(path.vehicle)):
            print(f"{path.stations[i]} -- {path.vehicle[i]} --> ", end="")
        print(path.stations[len(path.stations) - 1])
    
    def get_arrive_time_sp(self, path: save_direction, t1: Time):
        minutes = 0
        for i in range(len(path.vehicle)):
            vehicle = "Subway" if path.line[i][0] == 'l' else "Bus"
            m1 = machine(vehicle)

            if i == 0:
                minutes += m1.get_in_time(t1 + minutes)
            elif path.line[i] != path.line[i-1]:
                minutes += m1.get_in_time(t1 + minutes)
            elif path.vehicle[i] != path.vehicle[i-1]:
                minutes += m1.get_in_time(t1 + minutes)

            minutes += (self.city_graph[path.stations[i]][path.stations[i+1]].get_vehicle(path.line[i], vehicle).value 
                            * m1.get_pass_time(t1 + minutes))
            
        return minutes
    
    def travel_line_cost(self, line: str, vehicle: str, src: str, t1: Time, dj_table: dd[str, save_direction], visited: set[str]):
        src_index = self.lines[line].index(src)
        m1 = machine(vehicle)
        start_cost = copy(dj_table[src])
        cost = 0

        if vehicle == "Taxi":
            get_in = 0 
            if len(start_cost.line) == 0:
                get_in += m1.get_in_time(t1 + start_cost.minutes)
            elif start_cost.line[len(start_cost.line) - 1] != line:
                get_in += m1.get_in_time(t1 + start_cost.minutes)
            elif start_cost.vehicle[len(start_cost.vehicle) - 1] != vehicle:
                get_in += m1.get_in_time(t1 + start_cost.minutes)
            
            start_cost.minutes += get_in
            for i in range(src_index, len(self.lines[line]) - 1):
                
                start_cost.value += (self.city_graph[self.lines[line][i]][self.lines[line][i + 1]].get_vehicle(line, vehicle).value
                                     * m1.get_price(t1 + start_cost.minutes))
                
                start_cost.minutes +=(self.city_graph[self.lines[line][i]][self.lines[line][i + 1]].get_vehicle(line, vehicle).value
                                       * m1.get_pass_time(t1 + start_cost.minutes))
                start_cost.line.append(line)
                start_cost.vehicle.append(vehicle)
                start_cost.stations.append(self.lines[line][i + 1])
                
                if dj_table[self.lines[line][i + 1]].value > start_cost.value:
                    dj_table[self.lines[line][i + 1]] = copy(start_cost)
            
            start_cost = copy(dj_table[src])
            start_cost.minutes += get_in

            for i in range(src_index, 0, -1):
                
                start_cost.value += (self.city_graph[self.lines[line][i]][self.lines[line][i - 1]].get_vehicle(line, vehicle).value
                                     * m1.get_price(t1 + start_cost.minutes))
                
                start_cost.minutes +=(self.city_graph[self.lines[line][i]][self.lines[line][i - 1]].get_vehicle(line, vehicle).value
                                       * m1.get_pass_time(t1 + start_cost.minutes))
                start_cost.line.append(line)
                start_cost.vehicle.append(vehicle)
                start_cost.stations.append(self.lines[line][i - 1])
                
                if dj_table[self.lines[line][i - 1]].value > start_cost.value:
                    dj_table[self.lines[line][i - 1]] = copy(start_cost)

        

        else:
            start_cost = copy(dj_table[src])
            cost = 0
            if len(start_cost.line) == 0:
                cost += m1.get_price(t1 + start_cost.minutes)
            elif start_cost.line[len(start_cost.line) - 1] != line:
                cost += m1.get_price(t1 + start_cost.minutes)
            elif start_cost.vehicle[len(start_cost.vehicle) - 1] != vehicle:
                cost += m1.get_price(t1 + start_cost.minutes)

            start_cost.value += cost

            for i in range(src_index + 1, len(self.lines[line])):
                start_cost.line.append(line)
                start_cost.vehicle.append(vehicle)
                start_cost.stations.append(self.lines[line][i])
                
                if dj_table[self.lines[line][i]].value > start_cost.value:
                    dj_table[self.lines[line][i]] = copy(start_cost)
            
            start_cost = copy(dj_table[src])
            start_cost.value += cost

            for i in range(src_index, 0, -1):
                start_cost.line.append(line)
                start_cost.vehicle.append(vehicle)
                start_cost.stations.append(self.lines[line][i - 1])
                
                if dj_table[self.lines[line][i - 1]].value > start_cost.value:
                    dj_table[self.lines[line][i - 1]] = copy(start_cost)
        
    def find_best_cost(self, src: str, dest: str, t1: Time):
        if src in self.city_graph.keys() and dest in self.city_graph.keys():
            visited_node : set[str] = set()
            node_data = dd(lambda : save_direction([] , [] , []))
            
            node_data[src].value = 0;
            node_data[src].stations.append(src)

            for i in range(len(self.city_graph)):
                min_station = self.get_min(node_data, visited_node)

                if min_station == dest:
                    break;
                for pair in self.nodes[min_station]:
                    self.travel_line_cost(pair[0], pair[1], min_station, t1, node_data, visited_node)
                
                visited_node.add(min_station)
            
            return node_data[dest]

            
        else:
            raise ValueError("Station does not exist!")