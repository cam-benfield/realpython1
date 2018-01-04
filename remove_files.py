import os
import glob

my_path = "/home/cameryn/projects/realpython1/practice_files/little pics"

for current_folder, subfolders, file_names in os.walk(my_path):
    possible_files = os.path.join(current_folder, "*.jpg")
    for file_name in glob.glob(possible_files):
        print(file_name)
        file_size = os.path.getsize(file_name)
        if file_size < 2000:
            os.remove(file_name)
            print("Removed:", file_name)
