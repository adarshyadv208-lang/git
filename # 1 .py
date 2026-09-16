# 1 . Initialize and Modify
grades = [85 , 92 , 78 ]
grades.append(95) # [85 , 92 , 78 , 95 ]
grades.remove(78) # [85 , 92, 95 ]

# 2 . Membership and Boundries
if 92 in grades :
    print("92 is in the list ") 

#3 . Native Statistical Functions
total_count = len(grades) 
total_sum = sum (grades)
lowest = min (grades)
highest = max(grades) 

print("total count is", total_count)
print("total sum is " , total_sum)
print("lowest is " , lowest)
print("highest is " , highest)