import os
import shutil

# if os.path.exists("Pig.py"):
#     print("the file exists!")

# print(os.system("ls -la"))

# a = shutil.disk_usage("/home/toro/Desktop/Python-piscine")
# # print(a)
rs = shutil.copytree("python00", "copy-python")
print(rs)
shutil.rmtree("copy-python")