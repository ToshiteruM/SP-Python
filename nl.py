import sys
 
argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "rU")
    except IOError:
        sys.exit("wc: %s: No such file or directory" % (sys.argv[1]))
else:
    sys.exit("usage: wc [file]")
 
