import os  
import shutil  
from pathlib import Path  
import subprocess  

# Specify the root folder path  
root_folder_path = Path("D:\\cd_data_C\\Desktop\\Prepare\\Lab_Python")  # Use double backslashes  

# List all files in the directory and subdirectories  
all_files = list(root_folder_path.rglob('*'))  # Use `*` to match all files  

# Print the list of all files  
for file in all_files:  
    if file.is_file():  # Ensure it's a file  
        file_str = str(file)  
        if ".git" in file_str:  
            print(file_str)  
            command = f'del "{file_str}"'  # Use double quotes for file paths with spaces  

            try:  
                # Run the delete command  
                result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)  
                # subprocess.run(command) 
                # # Print the standard output  
                print('Output:', result.stdout)  

                # # Print the standard error if there's any  
                if result.stderr:  
                    print('Error:', result.stderr)  

            except subprocess.CalledProcessError as e:  
                print(f"An error occurred: {e}")