from city import *
from Time import Time

src = input()
dest = input()
t1 = Time(input())

t1 = Tehran()
try:
    t1.read_from_file("line", "Bus")

except:
    print("oops some file does not exist")