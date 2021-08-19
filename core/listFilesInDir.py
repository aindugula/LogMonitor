import os

#function to get list of files in a directory
def listFilesInDir(dirname):
    list = []
    #extension could be anything but for this prototype used .log
    extension = ".log"
    for x in os.listdir(dirname):
        if x.endswith(extension):
            list.append(x)
    return list

if __name__ == "__main__":
    print(listFilesInDir("/var/log/"))

