import tkinter
import os
import subprocess
from tkinter import filedialog


def select_target_dir():
    root = tkinter.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    root.destroy()

    return directory


def git_folder_find(path: str):
    walker = os.walk(path)
    repo_path = []
    for (root, dirs, files) in walker:
        if ".git" in dirs:
            repo_path.append(root)
    
    return repo_path

def liveprint_exec(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    for c in iter(lambda: process.stdout.read(1), b""):
        print(c.decode("ascii"), sep="",end="")

def check_repo(path: str) -> bool:
    print(path)
    drive_letter = path[ : path.find('/')]
    liveprint_exec(['git_status.bat', drive_letter, path])
    user_input = input('go next (any) , or save favor list (f) \n(any / f) : ')
    if user_input == 'f':
        return True
    else:
        return False



if __name__ == "__main__":
    target_dir = select_target_dir()
    git_repo_list:list[str] = git_folder_find(target_dir)
    favor_list = []
    while True:
        for repo_path in git_repo_list:
            print("\033[H\033[J", end="")
            path_organized = repo_path.replace("\\\\", "/")
            is_favor = check_repo(path_organized)
            if is_favor:
                favor_list.append(path_organized)
        
        if input('do you want to see your favor list? (y) \n \
                 or just shut down the program?(any) \n(y / any)  : ') != 'y':
            break
        git_repo_list = favor_list
        favor_list = []


    
