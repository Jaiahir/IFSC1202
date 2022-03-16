def changecalc(population):
    pop = [None]
    for i in range(1, len(population)):
        pop.append(population[i] - population[i - 1])
    return pop


def percentcalc(change, population):   
    percentage = [None] 
    for i in range(1, len(population)):
        percentage.append(change[i] / population[i - 1] *100)
    return percentage

year = list(range(1950, 1991))

file = open('08.11 USPopulation.txt', 'r')

population = []

lines = file.readlines()
for i in lines: 
    population.append(int(i.rstrip("\n")) * 1000) 

change = changecalc(population)
percent = percentcalc(change, population) 

print("Year\tPopulation\tChange\tPercent Change")  

for i in range(len(population)):
    if i != 0: 
        print(f"{year[i]}\t{population[i]}\t{change[i]}\t{percent[i]:.2f}%")
    else:  
        print(f"{year[i]}\t{population[i]}\t{change[i]}\t{percent[i]}")
avgpop = sum(change[1:])/len(change)

print("Average Change: ", round(avgpop))

min = min(change[1:]) 
min_year = year[change.index(min)]

max = max(change[1:])
max_year = year[change.index(max)]

print("Minimum Change = ", min, {min_year})
print("Maximum Change = ", max, {max_year}) 
