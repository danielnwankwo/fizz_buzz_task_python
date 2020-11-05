

for num in range(1, 101):

    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")

    elif num % 3 == 0:
        print("fizz")

    elif num % 5 == 0:
        print("buzz")

    else:
        print(num)





class fizzbuzz:
    def __init__(self, fizz, buzz):
        self.fizz = fizz
        self.buzz = buzz
        self.fizzbuzz = fizz + "" + buzz

