numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Ascending order
ascending = sorted(numbers)

# Descending order
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)
