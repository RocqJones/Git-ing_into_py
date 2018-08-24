print("How many kilometers did you run today?")
klms = input()
miles = float(klms)/1.60934
#the value will have lotta decimals lets round off
miles = round(miles, 2)
print(f"Your {klms}Km ride is {miles}miles.")
