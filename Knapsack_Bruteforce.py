from itertools import combinations

weights = [7,3,4,5]
values = [42,12,40,25]
capacity = 10
n = len(weights)

best_value = 0
best_subset = None

print("Subset\t\tTotal Value")
print("-"*45)

for r in range(n+1):
    for subset in combinations(range(n),r):
        total_weight = sum(weights[i] for i in subset)
        total_value = sum(values[i] for i in subset)

        subset_display = "{" + ",".join(str(i+1) for i in subset) + "}"

        if total_weight <= capacity:
            print(f"{subset_display:<15}{total_weight:<15}${total_value}")
            
            if total_value > best_value:
                best_value = total_value
                best_subset = subset
            
        else:
            print(f"{subset_display:<15}{total_weight:<15}not feasible")

print("Optimal Solution:")
print("Items selected:", {i+1 for i in best_subset})
print("Maximum value: $", best_value)


# Step 1: Start the program
# Step 2: Take inputs
# Store weights of items
# Store values of items
# Store maximum capacity of the bag
# Find number of items
# Step 3: Initialize
# Set best_value = 0
# Set best_subset = empty
# Step 4: Generate all possible item combinations
# Check combinations from 0 items to all items
# Step 5: For each combination
# Calculate total weight of selected items
# Calculate total value of selected items
# Step 6: Check feasibility
# If total weight is less than or equal to capacity
#   Print the subset and its total value
#   If total value is greater than best_value
#       Update best_value
#       Update best_subset
# Else
#   Print not feasible
# Step 7: After checking all combinations
# Print items selected in best_subset
# Print maximum value obtained
# Step 8: Stop the program
