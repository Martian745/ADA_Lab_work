
## Approach_1
"""
def leaders_in_array(arr):
    result=[]
    max_right=arr[-1] # here we've made last element a default leader
    result.append(max_right)

    for i in range(len(arr)-2,-1,-1): # Here we're comparing right to left and passing leaders tag
        if arr[i]>= max_right:
            max_right=arr[i]
            result.append(arr[i])
    
    return result[::-1]
"""
## Approach_2
# we're picking up every element & comparing it with whole list
"""
def leaders_in_array(arr):
    leaders=[]
    for i in range(len(arr)):
        is_leader=True
        for j in range(i+1,len(arr)): # checking numbers right side in the list are greater than the one we're comparing
            if(arr[j]>arr[i]):
                is_leader=False
                break
        if is_leader:
            leaders.append(arr[i])
    return leaders
"""

## Approach_3
# In this approach we're picking up one element and comparing it with maximum of remaining list 
def leaders_in_array(arr):
    result=[]

    for i in range(len(arr)):
        if i==len(arr)-1 or arr[i]>=max(arr[i+1:]):
            result.append(arr[i])
    return result

arr=[16,17,4,3,5,2]
print(leaders_in_array(arr))