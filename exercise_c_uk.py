united_kingdom = [
    {
        "name": "Scotland",
        "population": 5295000,
        "capital": "Edinburgh"
    },
    {
        "name": "Wales",
        "population": 3063000,
        "capital": "Swansea"
    },
    {
        "name": "England",
        "population": 53010000,
        "capital": "London"
    }
]

united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom[1])

united_kingdom.append({"name": "Northern Ireland",
                       "population": 1811000, "capital": "Belfast"})
print(united_kingdom)

index = 0

for countries in united_kingdom:
    print(united_kingdom[index]["name"])
    index += 1

index = 0
for population_uk in united_kingdom:
    print(united_kingdom[index]["population"])
    index += 1


# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
# 3. Use a loop to print the names of all the countries in the UK.
# 4. Use a loop to find the total population of the UK.
