# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])

# temperature = int(input("What is the temperature outside?"))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows")

# #What is the score?
# score = int(input("What is your test score?"))

# if score >= 90:
#     print ("Your Grade is an A.")
# else:
#     if score >= 80:
#         print("Your Grade is a B.")
#     else:
#         if score >= 70:
#             print("Your Grade is a C.")
#         else:
#             if score >= 60:
#                 print("Your Grade is a D.")
#             else:
#                 print("Your Grade is an F.")

# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# counties = ["Arapahoe","Denver","Jefferson"]
# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in range(5):
#     print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county, registered_voters in voting_data.items():
    print(f"{county} county has {registered_voters:,} registered voters.")