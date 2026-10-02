import os

"""
@brief - Load Json file and return dictionary / Create new json file
"""
def load_file(fileName):
    os.chdir("Lab_05")
    cwd = os.getcwd()

    ## Create Empty Dictionary

    try:
        with open(f"{cwd}/{fileName}","r") as inventory:
            print(f"Found!!")
    except FileNotFoundError:
        with open(f"{cwd}/{fileName}","w") as inventory:
            print(f"Created!!")

    pass


def save_inventory():
    pass