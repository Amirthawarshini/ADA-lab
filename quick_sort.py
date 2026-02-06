def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

def partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high

    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break

    arr[low],arr[j]=arr[j],arr[low]
    return j

arr=[5,8,1,2,6,3,9]
print("Before sorting",arr)

quick_sort(arr,0,len(arr)-1)
print("After sorting",arr)


# Step 1: Start
# Step 2: Call QUICK_SORT(arr, low, high)
# Step 3: If low < high then
# Find pivot position using PARTITION(arr, low, high)
# Call QUICK_SORT(arr, low, pivot - 1)
# Call QUICK_SORT(arr, pivot + 1, high)
# Step 4: Define PARTITION(arr, low, high)
# Choose the first element as pivot
# Set i = low + 1 and j = high
# While i <= j do
# Increase i while arr[i] <= pivot
# Decrease j while arr[j] >= pivot
# If i <= j then swap arr[i] and arr[j]
# Swap pivot element with arr[j]
# Return j as pivot position
# Step 5: Repeat steps until the array is sorted
# Step 6: Stop