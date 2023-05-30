#This code helps split a bill evenly amongst multiple diners- including tip
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
split = input("How many people will be splitting the bill? ")
each = float(total_bill) / float(split)
percent_tip = input("What percentage tip would you like to give? ")
pct = ((float(percent_tip) / 100) + 1)
amt_per_person = (round(pct * each, 2))
#This line of code (amt_per_person = "{:.2f}".format(amt_per_person)) allows for ALL answers to come out in the right format- $_ _. _ _
amt_per_person = "{:.2f}".format(amt_per_person)
print(f"Each person should pay: ${amt_per_person}")
