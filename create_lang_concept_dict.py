import csv
import os

swedish_entities = []

language = "swedish"

language_source_files_path = "./lang/"

with open(os.path.join(language_source_files_path, f"{language}_variables.csv"),
           "r") as file:
    reader = csv.reader(file)
    for row in reader: 
        swedish_entities.append([row[1], "", row[0], "DT4H", "2024-06-01"])

with open(os.path.join(language_source_files_path, f"{language}_medication.csv"),
          "r") as file:
    reader = csv.reader(file)
    for row in reader:
        swedish_entities.append([row[1], "Medication", row[0], "DT4H", "2024-06-01"])

with open("./english_entities.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader: 
        for idx in range(len(swedish_entities)):
            if swedish_entities[idx][2] == row[2]:
                if swedish_entities[idx][1] == "":
                    swedish_entities[idx][1] = row[1]

with open(f"./{language}_entities.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(swedish_entities)
