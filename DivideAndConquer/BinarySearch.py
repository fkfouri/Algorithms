
# Python Program for recursive binary search. 

# Returns index of x in arr if present, else -1 
def binarySearch (col, l, r, x): 

	# Check base case 
	if r >= l: 

		mid = l + (r - l)//2

		# If element is present at the middle itself 
		if col[mid] == x: 
			return mid 
		
		# If element is smaller than mid, then it can only 
		# be present in left subarray 
		elif col[mid] > x: 
			return binarySearch(col, l, mid-1, x) 

		# Else the element can only be present in right subarray 
		else: 
			return binarySearch(col, mid+1, r, x) 

	else: 
		# Element is not present in the array 
		return -1

# Test array 

vetor = [0,1,2,3,4,5,6,7,8,9]
x = 5

# Function call 
result = binarySearch(vetor, 0, len(vetor)-1, x) 

if result != -1: 
	print ("Element is present at index %d" % result )
else: 
	print ("Element is not present in array")



