import os
import subprocess

def update_repository(repo_path):
    # Change directory to the repository path
    os.chdir(repo_path)

    try:
        # Fetch the latest changes from the remote
        subprocess.run(["git", "fetch"], check=True)
        
        # Pull the latest changes from the main branch
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        
        print("Repository updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while updating the repository: {e}")

if __name__ == "__main__":
    # Specify the path to your local GitHub repository
    repository_path = "/path/to/your/repo"  # Replace this with your actual path
    update_repository(repository_path)