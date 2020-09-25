import random
from collections import Counter

seriesLength = []

for i in range(0,1000000):
    homeWins = 0
    awayWins = 0
    for j in range(0,7):
        if random.random() > 0.5:
            homeWins+=1
        else:
            awayWins+=1

        if 4 in [homeWins, awayWins]:
            seriesLength.append(j+i)
            break
print(Counter(seriesLength).most_common())