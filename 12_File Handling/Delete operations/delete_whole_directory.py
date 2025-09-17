import shutil
import os

# Deleting a directory and its contents
if os.path.exists("Folder 2"):
    shutil.rmtree("Folder 2")
    print("Directory and its contents delted")
else:
    print("Directory does not exist.")
