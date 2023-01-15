import csv
import random

with open('scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'chinese', 'math', 'english'])
    names = ['guan', 'zhang', 'zhao', 'ma', 'huang']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3) ]
        scores.insert(0, name)
        writer.writerow(scores)
