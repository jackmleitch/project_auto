import sys
import os
import config
from github import Github

subFolders = config.SUB_FOLDERS
path = config.FILEPATH
token = config.TOKEN

def create():
    # create directory 
    folderName = str(sys.argv[1])
    os.makedirs(path+str(folderName))
    for i in range(0, len(subFolders)):
        subPath = str(path) + str(folderName) + '/' + str(subFolders[i])
        os.makedirs(subPath)

    user = Github(token).get_user()
    repo = user.create_repo(folderName)
    print(f"Succesfully created repository {folderName}")


if __name__ == "__main__":
    create()