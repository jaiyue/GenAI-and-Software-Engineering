import os
import json
import shutil


# Delete all the folders with name of the folder
def delete_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)


# Define a function creates a folder with id as the name of the folder
def create_folder(folder_name):
    # Create a folder with the name of id
    os.mkdir(folder_name)
    # Change the current directory to the folder
    os.chdir(folder_name)


# Define a function given a json file index open the json file and return the json object
def get_json_object(index):
    # Open the json file
    with open(index + '.json', 'r') as f:
        data = json.load(f)
        
        return data
