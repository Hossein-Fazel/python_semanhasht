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
except ValueError as error:
    print(error)