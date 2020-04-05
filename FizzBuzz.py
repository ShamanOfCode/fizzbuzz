
my_num = int(input("Enter a number: "))

if my_num % 3 == 0 and my_num % 5 == 0:
    print("FizzBuzz")
elif my_num % 3 == 0:
    print("Fizz")
elif my_num % 5 == 0:
    print("Buzz")
else:
    print(str(my_num) + " can't divided by 3 and 5.")
    