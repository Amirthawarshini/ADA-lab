n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
    
# Step 1: Start
# Step 2: Read number of terms n
# Step 3: Initialize a = 0, b = 1
# Step 4: Repeat for i = 1 to n
# Print a
# Set next = a + b
# Set a = b
# Set b = next
# Step 5: Stop