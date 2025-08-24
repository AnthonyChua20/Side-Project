weight = int(input("Enter the weight of the items in grams:"))
cost = float()
match weight:
    case weight if weight <= 20:
        cost = 0.3
    case weight if weight > 20 and weight < 40:
        cost = 0.6
    case weight if weight > 40 and weight <100:
        cost = 0.9
    case weight if weight >= 100:
        cost = 1.15

print("The postage cost is $",cost)