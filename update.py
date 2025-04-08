import os
import subprocess

def update_repository(repo_path):
   
    os.chdir(repo_path)

    try:
     
        subprocess.run(["git", "fetch"], check=True)
    
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        
        print("Repository updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while updating the repository: {e}")

if __name__ == "__main__":
    repository_path = ""
    update_repository(repository_path)
