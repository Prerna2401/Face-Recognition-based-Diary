import os
dir='C:/xampp/htdocs/AI_PROJECT'
""" count = 0
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,path)):
        count+=1
print('File count:',count) """

from pathlib import Path

li = os.listdir("C:/xampp/htdocs/AI_PROJECT/DIARY_DATA/Prer/")
arr= []
for x in li:
    print(Path(x).stem)
    arr.append(Path(x).stem)
print(arr)