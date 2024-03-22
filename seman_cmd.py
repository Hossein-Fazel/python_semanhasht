from city import *
from Time import Time

src = input()
dest = input()
t1 = Time(input())

ct1 = Tehran()
try:
    ct1.read_from_file("line", "Bus")

except:
    print("oops some file does not exist!")

try:
    path = ct1.find_shortest_path(src, dest)
    ct1.print_sp(path)
    print(t1 + ct1.get_arrive_time_sp(path, t1))

    path = ct1.find_best_time(src, dest, t1)
    ct1.print_bt(path, t1)

    path = ct1.find_best_cost(src, dest, t1)
    ct1.print_bc(path, t1)
    print(t1 + ct1.get_arrive_time_bc(path, t1))
except ValueError as error:
    print(error)