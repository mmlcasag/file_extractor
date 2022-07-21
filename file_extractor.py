import os
import shutil

input_folder = "input"
output_folder = "output"

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for folder_name in os.listdir(input_folder):
    
    full_folder_name = os.path.join(input_folder, folder_name)
    print("Folder: {}".format(full_folder_name))
    
    for file_name in os.listdir(full_folder_name):
        
        full_file_name = os.path.join(input_folder, folder_name, file_name)
        print("File: {}".format(full_file_name))

        # copies the file to the output folder
        shutil.copy2(
            full_file_name, # from
            os.path.join(output_folder, file_name) # to
        )
        
        # removes the file from the input folder
        os.remove(full_file_name)
    
    # removes the empty folder from the input folder
    os.rmdir(full_folder_name)