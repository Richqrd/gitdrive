import os
import sys
from os import listdir


ignore = ['.DS_Store', '.git']

def setup():
    os.chdir('/Users/richardzhang/Desktop/gitdrive/githubstorage')

def save():
    files_list = [i for i in listdir() if i not in ignore and i[0] != '~']
    if not files_list:
        return
    files = '" "'.join(files_list)
    print(files_list)
    os.system('git add "' + files + '"')
    os.system('git commit -m "File modified"')
    os.system('git push')
    os.system('rm "' + files + '"')
    
def list_files():
    os.system('git fetch --all')
    os.system('git ls-tree --full-tree -r --name-only HEAD')

def open_file(filename):
    os.system('git fetch --all')
    os.system('git checkout origin/main -- ' + '"' + filename + '"')
    os.system('open ' + '"' + filename + '"' )

def new_file(filename):
    os.system('touch ' + '"' + filename + '"')
    save()

def remove_file(filename):
    os.system('git rm ' + '"' + filename + '"')
    os.system('git commit -m "File removed"')
    os.system('git push')

def reset_to_main():
    os.system('git fetch --all')
    os.system('git reset --hard origin/main')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        os.system('open /Users/richardzhang/Desktop/gitdrive/githubstorage')
        exit()

    setup() 

    if sys.argv[1] == "s":
        save()
    if sys.argv[1] == "l":
        list_files()
    if sys.argv[1] == "reset-to-main":
        reset_to_main()

    if sys.argv[1] == "o":
        if len(sys.argv) >= 3:
            open_file(sys.argv[2])
        else:
            print("Specify file path")
    if sys.argv[1] == "n":
        if len(sys.argv) >= 3:
            new_file(sys.argv[2])
        else:
            print("Specify file path")
    if sys.argv[1] == "r":
        if len(sys.argv) >= 3:
            remove_file(sys.argv[2])
        else:
            print("Specify file path")




# open_file("newfile.doc")