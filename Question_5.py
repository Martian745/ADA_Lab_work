
def fractional_knapsack(weights, values, capacity):
    items = sorted(
        zip(weights, values),
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    total_profit = 0.0

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_profit += value
            capacity -= weight
        else:
            total_profit += value * (capacity / weight)
            capacity = 0

    return total_profit


# Main program
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter knapsack capacity: "))

profit = fractional_knapsack(weights, values, capacity)
print("Maximum profit:", profit)
