#Tip Calculator

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? "))
num = int(input("How many people to split the bill? "))
tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
t_bill = bill + (bill*tip)/100
print("Each person should pay:",round(t_bill/num,2))