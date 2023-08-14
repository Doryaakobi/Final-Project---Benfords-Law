sum_result = [0] * 10
total_count = 0
for i in range(1, 41):
    file_name = "Data/num" + str(i) + ".txt"
    with open(file_name, 'r') as file:
        for line in file:
            number = line.strip()
            if number and number != '0':
                leading_digit = number[0]
                sum_result[int(leading_digit)] += 1
                total_count += 1

for i in range(1, 10):
    sum_result[i] = sum_result[i] / 18716 * 100

print(f"----------Results----------\n{sum_result}")
print(f"total count: {total_count}")
