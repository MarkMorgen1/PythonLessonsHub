# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions.

# num_fibs = int(input(" How many Fibs >= 2 do you want? 0 to exit "))
# while num_fibs >= 2:
#     fib_list = [1, 1]
#     for i in range(1, num_fibs - 1):
#         fib_list.append(fib_list[-1] + fib_list[-2])
#     print(" ", fib_list)
#     num_fibs = int(input(" How many Fibs >= 2 do you want? 0 to exit "))


# from ChatGPT using a generator function:
def fib_generator(n):
    a, b = 1, 1
    yield a
    yield b
    for _ in range(n - 2):
        a, b = b, a + b
        yield b


num_fibs = int(input("How many Fibs >= 2 do you want? 0 to exit: "))

while num_fibs >= 2:
    # Generate Fibonacci numbers one at a time
    fibs = fib_generator(num_fibs)

    # Print them (converts generator to list for display only)
    print(" ", list(fibs))

    num_fibs = int(input("How many Fibs >= 2 do you want? 0 to exit: "))
