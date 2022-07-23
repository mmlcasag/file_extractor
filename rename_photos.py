import os
import re

input_folder = "input"

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    
for file_name in os.listdir(input_folder):
    full_file_name = os.path.join(input_folder, file_name)
    print("File: {}".format(full_file_name))

    new_file_name = re.search('\d{14}', full_file_name)[0]
    new_file_name = os.path.join(input_folder, "IMG_" + new_file_name[0:8] + "_" + new_file_name[8:])
    print("New File: {}".format(new_file_name))
    
    try:
        os.rename(full_file_name, new_file_name + ".jpg")
    except FileExistsError:
        os.rename(full_file_name, new_file_name + " (2).jpg")