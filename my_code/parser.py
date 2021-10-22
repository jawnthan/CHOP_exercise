import csv
import os

filename = os.path.expanduser('~/Desktop/CHOP_exercise/analyst-take-home-task-master/datasets/encounters.csv')

date = 

with open(filename, 'r') as encounters_csv:

   encounters = csv.DictReader(encounters_csv)

   for row in encounters:

      print(row)
