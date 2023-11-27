#Tip Calculator

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? "))
num = int(input("How many people to split the bill? "))
tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
t_bill = (bill + (bill*tip)/100)/num
final = "{:.2f}".format(t_bill)
print(f"Each person should pay: {final}")
