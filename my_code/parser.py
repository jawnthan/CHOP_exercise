import csv
import os

filename = os.path.expanduser('~/Desktop/CHOP_exercise/analyst-take-home-task-master/datasets/encounters.csv')

#encounter_date = 

counter = 0

with open(filename, 'r') as encounters_csv:

   encounters = csv.DictReader(encounters_csv)

   for row in encounters:

      if row["START"] >= "1999-07-15 00:00:00":

         print(row["START"])

         counter += 1

   print(counter)
#
#         if counter == 9:
#
#            break
