print("Welcome to the tip calculator.")
bill = float(input("what was the total bill? "))

tip = int(input("What peercentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

bill_after_tip =bill+ bill*(tip/100)
split_bill = (bill_after_tip/people)
print(f"Each person should pay: {round(split_bill, 2)}")