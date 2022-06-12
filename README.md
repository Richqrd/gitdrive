This is a python app that helps users use Github as a cloud storage platform (similar to Google Drive). 

The app works by utilizing a Github repository (in this case, it is the directory labelled "githubstorage" - this repository can also be seen on my Github account) that is constantly being modified. Whenever there are new files added to the folder, the app can be run to save those files and upload them to the Github repository. Afterwards, all files will be locally deleted so that they do not take up local storage. 

To open files stored on the Github repository, they are first locally downloaded. Once changes are finished, the app can be run to save everything and once again then delete all files from local storage.

To use the app, type "python3 app.py [argument]" into the command line. Arguments can be "s" (save local files to Github), "l" (list all saved Github files), "n" (create a new file in Github), "o" (open a file from Github), or "r" (remove a file from Github). Naturally, the "n" "o" and "r" arguments require a second argument specifying a file type or name.

For ease of use, zsh can be modified to abbreviate "python3 app.py" to something else, such as the single letter "f."