import os

# Deleting an empty directory
if os.path.exists("Folder 1"):
    os.rmdir("Folder 1")
    print("Directory deleted.")
else:
    print("Directory does not exist.")
