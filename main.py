import os
import sys
commitName = "autocommit"
currentFolder = __file__[:-7]
os.chdir(currentFolder)
anyChange = False

def updateDates():
    f = open(currentFolder + "fileDates.txt", "w")
    for file in os.listdir(currentFolder):
        if (file != "main.py" and file != ".git" and file != "fileDates.txt"):
            f.write(file + "=" + str(os.stat(currentFolder + file).st_mtime) + "\n")
    f.close()

def getsavedMDate(fileName):
    f = open(currentFolder + "fileDates.txt", "r")
    for line in f:
        if (len(line) > 0 and line.split("=")[0] == fileName):
            return line.split("=")[1]

def getcurrentMDate(fileName):
    for file in os.listdir(currentFolder):
        if (file == fileName):
            return os.stat(currentFolder + file).st_mtime

while True:
    os.system("cd " + currentFolder)
    for file in os.listdir(currentFolder):
        if not file in ["main.py", ".git", "fileDates.txt", "tempCodeRunnerFile.py"]:
            if (float(getcurrentMDate(file)) > float(getsavedMDate(file))):
                anyChange = True
                os.system("git add --all")
                updateDates()
    if (anyChange):
        anyChange = False
        os.system("git commit -m " + commitName)
        os.system("git push origin master")
