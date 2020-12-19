import sys
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

# Get data from a .env file thats in .gitignore
path = os.getenv("FILEPATH")
# Access to token generated from github 
token = os.getenv("TOKEN")
subFolders = ['input', 'src', 'models', 'notebooks', 'notes']


def create():
    # Extract project name from the command line 
    folderName = str(sys.argv[1])
    # Make directory in my files 
    os.makedirs(path+str(folderName))
    # Adds in sub-directories of src, input, ...
    for i in range(0, len(subFolders)):
        subPath = str(path) + str(folderName) + '/' + str(subFolders[i])
        os.makedirs(subPath)

    # Uses Githubs API to create repository 
    user = Github(token).get_user()
    repo = user.create_repo(folderName)
    print(f"Succesfully created repository {folderName}")

if __name__ == "__main__":
    create()