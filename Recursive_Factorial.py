def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))


# Step 1: Start
# Step 2: Read a number n
# Step 3: Define a function factorial(n)
# Step 4: If n is 0 or 1
#   Return 1
# Step 5: Else
#   Return n * factorial(n - 1)
# Step 6: Print the factorial value
# Step 7: Stop
