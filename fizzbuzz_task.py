


class fizzbuzz:
    def __init__(self, fizz, buzz):
        self.fizz = fizz
        self.buzz = buzz
        self.fizzbuzz = fizz * buzz

    def fizz_buzz(self):

        counter = []


        for num in range(1, 101):
            if num % self.fizzbuzz == 0:
                counter.append("fizzbuzz")

            elif num % self.fizz == 0:
                counter.append("fizz")

            elif num % self.buzz == 0:
                counter.append("buzz")
            else:
                counter.append(num)
        return counter

three_five = fizzbuzz(3, 5)
print(three_five.fizz_buzz())





