import os
import json

data = {
        0: {
            "total_calories": 0,
            "individual_calories": [],
        }
    }

# import "input.txt" file line by line
total_cal = 0

curr_elf = 0
with open("input.txt", "r") as f:
    for line in f:
        if line == "\n":
            curr_elf += 1
            data[curr_elf] = {
                "total_calories" : 0,
                "individual_calories" : [],
            }
        else:
            curr_cal = int(line)
            data[curr_elf]["total_calories"] += curr_cal
            data[curr_elf]["individual_calories"].append(curr_cal)


# Get the index of the elf with the most calories
max_cal_elf = max(data, key=lambda x: data[x]["total_calories"])
print("Elf with the most calories: ", max_cal_elf, data[max_cal_elf]["total_calories"])

# Sort the data by total calories
sorted_data = sorted(data.items(), key=lambda x: x[1]["total_calories"], reverse=True)

total_cals = 0
# Sum up the total calories for the top 3 elves
for i in range(3):
    total_cals += sorted_data[i][1]["total_calories"]

print("Total calories for the top 3 elves: ", total_cals)