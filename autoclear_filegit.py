# import os  
# import shutil  
# from pathlib import Path  
# import subprocess  

# # Specify the root folder path  
# root_folder_path = Path("D:\\cd_data_C\\Desktop\\Prepare\\Lab_Python")  # Use double backslashes  

# # List all files in the directory and subdirectories  
# all_files = list(root_folder_path.rglob('*'))  # Use `*` to match all files  

# # Print the list of all files  
# for file in all_files:  
#     if file.is_file():  # Ensure it's a file  
#         file_str = str(file)  
#         if ".git" in file_str:  
#             print(file_str)  
#             command = f'del "{file_str}"'  # Use double quotes for file paths with spaces  

#             try:  
#                 # Run the delete command  
#                 result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)  
#                 # subprocess.run(command) 
#                 # # Print the standard output  
#                 print('Output:', result.stdout)  

#                 # # Print the standard error if there's any  
#                 if result.stderr:  
#                     print('Error:', result.stderr)  

#             except subprocess.CalledProcessError as e:  
#                 print(f"An error occurred: {e}")


import subprocess  
import shutil  
from pathlib import Path  

# Specify the path to your repository  
repo_path = Path("D:\cd_data_C\Desktop\Prepare\Lab_Python")  

# Change to the repository directory  
subprocess.run(f'cd "{repo_path}"', shell=True)  

# Function to push changes to Git and remove .git directory  
def push_and_delete_git():  
    # # Step 1: Push changes to the remote repository  
    # try:  
    #     subprocess.run('git push origin main', check=True, shell=True)  # Change 'main' if necessary  
    #     print("Changes pushed to the remote repository.")  
    # except subprocess.CalledProcessError as e:  
    #     print(f"An error occurred while pushing: {e}")  
    #     return  
    
    # Step 2: Remove the .git directory  
    git_dir = repo_path / '.git'  
    if git_dir.exists():  
        shutil.rmtree(git_dir)  # Remove the .git directory  
        print(".git directory has been deleted.")  
    else:  
        print("No .git directory found.")  

# Run the function  
push_and_delete_git()