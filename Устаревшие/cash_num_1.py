import sys

res = [x for x in range (-1000, 1000) if(sys.getrefcount(x) > 3)]
print(res)
