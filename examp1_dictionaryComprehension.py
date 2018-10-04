#DICTIONARY COMPREHENSION
# example 1
nums = dict(first=1,second=2,third=3)
squared_numbers = {key: value **2 for key,value in nums.items()}
print(squared_numbers)

#example 2
#{num: num**2 for num in[1,2,3,4,5]}
