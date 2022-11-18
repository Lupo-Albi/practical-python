total = 0
expenses = []

num_expenses = int(input("How many lunches did you buy this week?"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, " on lunch this week", sep='')
