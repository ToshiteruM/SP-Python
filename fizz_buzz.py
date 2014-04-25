def fb(n):
    s = ""
    if n % 3 == 0:
        s = s + 'Fizz'
    if n % 5 == 0:
        s = s + 'Buzz'
    return s
 
i = 1
while i <= 20:
    print i, fb(i)
    i = i + 1
