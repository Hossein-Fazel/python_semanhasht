from city import *
from Time import Time

src = input()
dest = input()
t1 = Time(input())

def print_bc(path: save_direction, t1: Time): # print best cost function
    print(f"\n{" Best Cost ":-^30}")
    print(f"{path.value} Toman")

    for i in range(len(path.vehicle)):
        print(f"{path.stations[i]} -- {path.vehicle[i]} --> ", end="")
    print(path.stations[len(path.stations) - 1])

    
def print_bt(path: save_direction, t1: Time): # print best time function
    print(f"\n{" Best Time ":-^30}")

    print(t1 + path.value)

    for i in range(len(path.vehicle)):
        print(f"{path.stations[i]} -- {path.vehicle[i]} --> ", end="")
    print(path.stations[len(path.stations) - 1])

def print_sp(path:save_direction): # print shortest path function
    print(f"\n{" Shortest Path ":-^30}")
    print(f"{path.value} Km")
    for i in range(len(path.vehicle)):
        print(f"{path.stations[i]} -- {path.vehicle[i]} --> ", end="")
    
    print(path.stations[len(path.stations) - 1])

ct1 = Tehran()
try:
    ct1.read_from_file("line", "Bus")

except:
    print("oops some file does not exist!")

try:
    path = ct1.find_shortest_path(src, dest)
    print_sp(path)
    print(t1 + ct1.get_arrive_time_sp(path, t1))

    path = ct1.find_best_time(src, dest, t1)
    print_bt(path, t1)

    path = ct1.find_best_cost(src, dest, t1)
    print_bc(path, t1)
    print(t1 + ct1.get_arrive_time_bc(path, t1))
except ValueError as error:
    print(error)