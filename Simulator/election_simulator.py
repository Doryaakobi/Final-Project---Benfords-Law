import random
from time import sleep

random.seed(1)
biden_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trump_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
biden_win_pct = 69.13
trump_win_pct = 29.28
number_of_sims = 100
total_wards = 0
total_trump_votes = 0
total_biden_votes = 0
total_votes = 0
print("\n2020 Election Simulation is running over 478 wards in Milwaukee."
      "\nEach ward has 1000 votes in avg.\nEach ward is a single record which "
      "his leading digit will count according to Benford's law."
      "\nFor the reliability, this simulator executes 1000 times and gives us the avg result."
      "\nTotal votes: 458,935\n\nSimulation progress:")
for i in range(number_of_sims):
    my_input = open('milwaukee_total_voters.txt')
    for line in my_input:
        total_wards += 1
        fields = line.strip().split()
        num_voters = int(fields[0])
        trump_votes_in_ward = 0
        biden_votes_in_ward = 0
        for j in range(num_voters):
            random_num = random.random() * 100
            if random_num <= biden_win_pct:
                biden_votes_in_ward += 1
                total_biden_votes += 1
            elif random_num <= (biden_win_pct + trump_win_pct) :
                trump_votes_in_ward += 1
                total_trump_votes += 1
            total_votes += 1
        trump_digit = int(str(trump_votes_in_ward)[0])
        biden_digit = int(str(biden_votes_in_ward)[0])
        trump_digits[trump_digit] += 1
        biden_digits[biden_digit] += 1
    if i % 100 == 0:
        print(str(int(i/10))+'%  ('+str(i)+" simulations completed)")
    if i == 999:
        print("1000 simulations completed, here is the results:")

trump_win_pct = 100.0 * total_trump_votes / total_votes
biden_win_pct = 100.0 * total_biden_votes / total_votes
print('Biden votes: ' + str(biden_win_pct) + '%')
print('Trump votes: ' + str(trump_win_pct) + '%')
print("\n-------------------Distribution-------------------")
print("\n---Biden distribution---")
for i in range(10):
    if i != 0:
        print_info = "Digit "+str(i)+":   "+str(int(biden_digits[i] * 100.0 / total_wards))+"%"
        print(print_info)

print("\n---Trump distribution---")
for i in range(10):
    if i != 0:
        print_info = "Digit "+str(i)+":   "+str(int(trump_digits[i] * 100.0 / total_wards))+"%"
        print(print_info)

sleep(300)
