import os
import sys
commitName = "autocommit"
projectFolder = "C:\\Users\\salsa\\Desktop\\project4\\test_project\\"

def updateDates():
    f = open(projectFolder + "fileDates.txt", "w")
    for file in os.listdir(projectFolder):
        if (file != "main.py" and file != ".git" and file != "fileDates.txt"):
            f.write(file + "=" + str(os.stat(projectFolder + file).st_mtime) + "\n")
    f.close()

def getsavedMDate(fileName):
    f = open(projectFolder + "fileDates.txt", "r")
    for line in f:
        if (len(line) > 0 and line.split("=")[0] == fileName):
            return line.split("=")[1]

def getcurrentMDate(fileName):
    for file in os.listdir(projectFolder):
        if (file == fileName):
            return os.stat(projectFolder + file).st_mtime

currentFolder = __file__[:-7]

os.chdir(currentFolder)
os.system("git add --all")
os.system("git commit -m " + commitName)
os.system("git push origin master")

# while True:
#     os.system("cd " + projectFolder)
#     for file in os.listdir(projectFolder):
#         if not file in ["main.py", ".git", "fileDates.txt", "tempCodeRunnerFile.py"]:
#             if (float(getcurrentMDate(file)) > float(getsavedMDate(file))):
#                 os.system("git add --all")
#                 updateDates()
#     os.system("git commit -m " + commitName)
#     # os.system("git push origin master")
