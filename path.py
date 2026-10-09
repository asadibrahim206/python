from pathlib import Path


#for current working directory
cwd = Path.cwd()
print("this is my curr: ",cwd)


#Home Directory 
home = Path.home()
print("this is my home directory: ",home)


#joining paths
base  = "project"
file_path = base / "data" / "api"

print(file_path )