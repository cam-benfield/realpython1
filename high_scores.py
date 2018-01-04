import csv
import os
scores_dict = dict()

my_path = "/home/cameryn/projects/realpython1/practice_files/"
scores_path = os.path.join(my_path, "scores.csv")

with open(scores_path, "r") as scores_file:
    my_file_reader = csv.reader(scores_file)
    for name, score in my_file_reader:
        if name not in scores_dict:
            scores_dict[name] = int(score)
        else:
            old_score = scores_dict[name]
            new_score = int(score)
            if new_score > old_score:
                scores_dict[name] = new_score
            else:
                pass

for name in sorted(scores_dict.keys()):
    print(name, scores_dict[name])
