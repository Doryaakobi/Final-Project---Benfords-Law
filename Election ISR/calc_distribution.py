from time import sleep


def count_leading_digits(file_name):
    digit_count = {}
    total_count = 0  # Keep track of the total count of numbers

    with open(file_name, 'r') as file:
        for line in file:
            number = line.strip()
            if number and number != '0':
                leading_digit = number[0]
                digit_count[leading_digit] = digit_count.get(leading_digit, 0) + 1
                total_count += 1

    digit_percentages = {digit: (count / total_count) * 100 for digit, count in digit_count.items()}
    return digit_percentages


sum_result = [0] * 10
for i in range(1, 41):
    file_name = "Data/num" + str(i) + ".txt"
    result = count_leading_digits(file_name)
    print(f"file is: num{str(i)}")
    for j in range(1,10):
        if str(j) in result:
            print(f"Digit {j}: {result.get(str(j)):.2f}% ")
        else:
            print(f"Digit {j}: 0% ")
        j += 1

    print("\n")
print("\nTotal cities: 1216\n")
sleep(60)




