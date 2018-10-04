#conditional logic with dictionaries
num_list = [1,2,3,4]
{num:("even" if num %2==0 else "odd") for num in num_list}

#{num:("even" if num %2==0 else "odd") for num in range(1,20)}
