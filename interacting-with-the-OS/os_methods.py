import os
import datetime
from pathlib import Path


# os.remove("first_draft.txt")
# os.rename("first_draft.txt", "finished_masterpiece.txt")
# print(os.path.exists("finished_masterpiece.txt"))

print(os.path.getsize("spider.txt"))

#unix timestamp
print(os.path.getmtime("spider.txt"))

#provide the date and time for the file in an 
#easy-to-understand format
timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))

#takes the file name and turns it into an absolute path
print(os.path.abspath("spider.txt"))

#returns true if  it is a file
print(os.path.isfile("spider.txt"))

#creates and removes new dir
os.mkdir("new_dir")
os.rmdir("new_dir")

#changes directory
# os.chdir("../crash-course")
print(os.getcwd())

#this loop will iterate through the files and directories in the specified directory and print out whether each item is a file or a directory
dir = "../interacting-with-the-OS"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))


#Use of pathlib module to move a file from one directory to another
# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)



