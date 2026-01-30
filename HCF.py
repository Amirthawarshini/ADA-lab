import time

start  = time.time()

a = 874
b = 598
hcf = 0

# a=bq+r

while True:
    q = a/b
    r = a%b
    a = b*q+r
    if r==0:
        break
    a = b
    b = r

hcf = b

print(hcf)

end = time.time()
print(f"Time taken: {end-start} ms")


# Step 1: Start the program
# Step 2: Note the start time
# Step 3: Assign two numbers a and b
# Step 4: Repeat the process
#   Find remainder r = a % b
#   If r is equal to 0
#       HCF is b
#       Stop the loop
#   Else
#       Set a = b
#       Set b = r
#       Continue the loop
# Step 5: Store b as the HCF
# Step 6: Print the HCF
# Step 7: Note the end time
# Step 8: Calculate and print time taken
# Step 9: Stop the program
