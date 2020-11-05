

# create the fizzbuzz class
class fizzbuzz:
    def __init__(self, fizz, buzz): # initialise the class + pass through arguments for fizz and buzz and fizzbuzz
        self.fizz = fizz
        self.buzz = buzz
        self.fizzbuzz = fizz * buzz # if fizz and buzz are 3 and 5 then fizz x buzz is 15 therefore the loop will work for mutiples of 15

# create a function which can take an empty list and pass the list of numbers 1-100 as per the task
# for each point in the loop it will either append a number with fizz or buzz or fizzbuzz if it is a multiple of 3,5 or both respectively

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

three_five = fizzbuzz(3, 5) # create the object for the class and define the multiples we use in the order they come in the initialising statement
print(three_five.fizz_buzz()) # print results





