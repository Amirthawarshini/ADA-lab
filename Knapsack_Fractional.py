# Time Complexity: O(n log n)

items = []
n = int(input("Enter number of items: "))

for i in range(n):
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))
    items.append((value,weight))

capacity = int()

# TODO: incomplete


# Step 1: Start the program
# Step 2: Read number of items (n)
# Step 3: For each item
#   Read value and weight
#   Store them as a pair (value, weight)
# Step 4: Read knapsack capacity
# Step 5: For each item
#   Calculate value-to-weight ratio
# Step 6: Sort all items in decreasing order
#   based on value-to-weight ratio
# Step 7: Initialize
#   total_value = 0
#   remaining_capacity = capacity
# Step 8: Select items greedily
#   For each item in sorted list:
#       If item weight <= remaining_capacity
#           Take full item
#           Add value to total_value
#           Reduce remaining_capacity
#       Else
#           Take fraction of item
#           Add proportional value
#           Break the loop
# Step 9: Print the maximum value obtained
# Step 10: Stop the program
