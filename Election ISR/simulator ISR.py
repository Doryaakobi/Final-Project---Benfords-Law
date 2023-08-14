import random
from time import sleep

print("********** Welcome to the ISR election simulator **********\n")
print("\nThis election simulation is running over 1216 cities in Israel."
      "\nEach city is a single record for each group (candidate) which"
      "his leading digit will count according to Benford's law.\n"
      "\nTotal votes: 4,764,742\nNote: a group that has less than 1% of total votes are not included\n"
      "therefore group ID's is different, look "
      "simulator_group_keys.txt in order to get the real group ID\n")

data_percentage = open("Data/sim_percentage_groups.txt", "r")

random.seed(1)
groups_digits = []  # list of lists , each inner list contains the record's leading digit for a specific group
for i in range(1, 14):
    groups_digits.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
groups_total_votes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 13 groups
groups_pct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_cities = 1216
total_votes = 0

my_input = open('Total_Votes_Per_City.txt')
for line in my_input:
    fields = line.strip().split()
    num_voters = int(fields[0])
    groups_votes_in_city = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 13 groups total
    for j in range(num_voters):  # iterate over current city voters
        random_num = random.random() * 100
        if random_num <= 4:
            groups_votes_in_city[0] += 1  # vote goes for group 1
            groups_total_votes[0] += 1
        elif random_num <= 5:
            groups_votes_in_city[1] += 1  # vote goes for group 2
            groups_total_votes[1] += 1
        elif random_num <= 11:
            groups_votes_in_city[2] += 1  # vote goes for group 3
            groups_total_votes[2] += 1
        elif random_num <= 14:
            groups_votes_in_city[3] += 1  # vote goes for group 4
            groups_total_votes[3] += 1
        elif random_num <= 18:
            groups_votes_in_city[4] += 1  # vote goes for group 5
            groups_total_votes[4] += 1
        elif random_num <= 29:
            groups_votes_in_city[5] += 1  # vote goes for group 6
            groups_total_votes[5] += 1
        elif random_num <= 38:
            groups_votes_in_city[6] += 1  # vote goes for group 7
            groups_total_votes[6] += 1
        elif random_num <= 42:
            groups_votes_in_city[7] += 1  # vote goes for group 8
            groups_total_votes[7] += 1
        elif random_num <= 65:
            groups_votes_in_city[8] += 1  # vote goes for group 9
            groups_total_votes[8] += 1
        elif random_num <= 68:
            groups_votes_in_city[9] += 1  # vote goes for group 10
            groups_total_votes[9] += 1
        elif random_num <= 72:
            groups_votes_in_city[10] += 1  # vote goes for group 11
            groups_total_votes[10] += 1
        elif random_num <= 90:
            groups_votes_in_city[11] += 1  # vote goes for group 12
            groups_total_votes[11] += 1
        elif random_num <= 98:  # The missing 2% belongs to the groups that have less than 1% of votes.
            groups_votes_in_city[12] += 1  # vote goes for group 13
            groups_total_votes[12] += 1
        total_votes += 1
    for group in range(0, 13):
        digit = int(str(groups_votes_in_city[group])[0])
        groups_digits[group][digit - 1] += 1

for group in range(0, 13):
    groups_pct[group] = 100.0 * groups_total_votes[group] / total_votes
    print(f'Group {group + 1} winning pct: {(groups_pct[group]):.2f} %')

print("\n-------------------Leading Digit Distribution-------------------")
for group in range(0, 13):
    print(f"\n---Group {group + 1} Distribution---")
    for i in range(9):
        info = "Digit " + str(i + 1) + ":   " + str(int(groups_digits[group][i] * 100.0 / total_cities)) + "%"
        print(info)
sleep(60)
