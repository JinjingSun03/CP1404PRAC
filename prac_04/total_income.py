"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

"""
def main():
    Display income report for incomes over a given number of months.
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
main()
"""

"""
def print_report(months, incomes):
    display Income Report
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        display (f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    income_list = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        income_list.append(income)
    print_report(num_months, income_list)
main()
"""


def print_report(months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    income_list = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        income_list.append(income)
    print_report(num_months, income_list)
main()
