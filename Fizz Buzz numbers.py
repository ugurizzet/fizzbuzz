for a in range(1, 101):
    if a % 3 == 0 and a % 5 == 0:  # we simply printed fizzbuzz for numbers divisible by 3 and 5
        print("fizzbuzz")
    elif a % 3 == 0:  # we simply printed fizz for numbers divisible by 3
        print("fizz")
    elif a % 5 == 0:  # we simply printed buzz for numbers divisible by 5
        print("buzz")
    else:
        print(a)