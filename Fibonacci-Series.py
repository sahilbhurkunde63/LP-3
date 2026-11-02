
# Fibonacci Series using Recursive and Non-Recursive Methods

# Non-Recursive Function
def fibonacci_non_recursive(n):
    a = 0
    b = 1

    print("Non-Recursive Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()


# Recursive Function
def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Main Program
n = int(input("Enter the number of terms: "))

# Calling Non-Recursive Function
fibonacci_non_recursive(n)

# Calling Recursive Function
print("Recursive Fibonacci Series:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

print()
