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
 
s = f.read()
f.close()
 
s = s.lower()
s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace('-', '')
s = s.replace('_', '')
s = s.replace(';', '')
s = s.replace(':', '')
s = s.replace('"', '')
s = s.replace("'", '')
s = s.replace('?', '')
s = s.replace('!', '')
s = s.replace('(', '')
s = s.replace(')', '')
s = s.replace('/', '')
words = s.split()
 
d = {}
 
for w in words:
    if d.has_key(w):
        d[w] += 1
    else:
        d[w] = 1
 
sored_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)
print "Number of words: %d" % len(words)
print "Top 10 frequent words:"
 
i = 0
for k in sored_keys:
    if i == 20:
        break
    print " %s %d" % (k, d[k])
    i += 1
