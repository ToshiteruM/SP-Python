import sys

argc = len(sys.argv)
if argc == 2:
  f = sys.stdin
elif argc == 3:
  f = open(sys.argv[2], "rU")
pat = sys.argv[1].lower()
  
i = len(pat)
l = f.readlines()
