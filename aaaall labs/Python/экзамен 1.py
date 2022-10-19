with open('exam1.txt','r') as f:
    data = f.readlines()
    for i in data:
        split_lines = i.split()
        the_longest_words = ''
        for c in split_lines:
            if len(c) > len(the_longest_words):
                the_longest_words = c
        print(the_longest_words)

                         
    
print()
print()
def bubbleSort(arr): 
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
           
# Driver code to test above 
arr = ['functions','trew','school'] 
   
bubbleSort(arr) 
   
print ("Sorted array :") 
for i in range(len(arr)): 
    print (arr[i],end=" ")                 
    

