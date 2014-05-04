def fb(n):
    fizz_buzz = ["", "", "", "Fizz", "", "Buzz",
                 "Fizz", "", "", "Fizz", "Buzz",
                 "", "Fizz", "", "", "FizzBuzz",
                 "", "", "Fizz", "", "Buzz"]

    return fizz_buzz[n]
 
i = 1
while i <= 20:
    print i, fb(i)
    i = i + 1
