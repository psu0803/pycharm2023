data = []

for i in range(5):

            value = int(input(f"Enter value {i + 1} between 0 and 100: "))
            if 0 <= value <= 100:
                data.append(value)
                break
            else:
                print("Value must be between 0 and 100. Try again.")

average = sum(data) / len(data)


greater_than_average = []


for value in data:
    if value > average:
        greater_than_average.append(value)
    else:
        data.remove(value)

while len(greater_than_average) < 5:
    min_value = min(data)
    data.remove(min_value)
    greater_than_average.append(min_value)

print("Entered data:", data)
print("Average:", average)
print("Five different values greater than the average:", greater_than_average)
