
def total_cost(meal_cost, tip_per, tax_per):
    total = 0
    total_tip = (meal_cost / 100) * tip_per
    total_tax = (meal_cost / 100) * tax_per
    total = meal_cost + total_tip + total_tax
    print(round(total))

cost = float(input())
tip_per = int(input())
tax_per = int(input())
total_cost(cost, tip_per, tax_per)
