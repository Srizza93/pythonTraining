import fileinput
import shutil
import os
def navigate_and_rename(src):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        if os.path.isdir(s):
            navigate_and_rename(s)
        elif s.endswith(".text"):
            shutil.copy(s, os.path.join(src, "Rename.text"))
print("                    Text WordCounter")
print("\n")
dirs = input("Tap here the address of your file: ")
print(dirs)
#dir_src = "/Users/martina/PycharmProjects/pythonforprogrammers"
dir_src = dirs
navigate_and_rename(dir_src)
def counter():
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(",", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(".", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("!", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(";", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(":", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("-", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("_", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("\\", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("|", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("(", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(")", ""), end='')
  with fileinput.FileInput('Rename.text', inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("[", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("]", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("{", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("}", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(">", ""), end='')
  with fileinput.FileInput("Rename.text" , inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("<", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("?", ""), end='')
  with fileinput.FileInput("Rename.text", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("'", " "), end='')
  with open("Rename.text", 'r+') as f:
      wordcount={}
      f.write("\n")
      for word in f.readline().split():
        if word not in wordcount:
              wordcount[word] = 1
        else:
              wordcount[word] += 1
      for k,v in sorted(wordcount.items(), key=lambda item: item[1], reverse=True):
          result = ("%s: %s" % (k, v)) # sort items
          print(result)
          f.write("\n")
          f.write(str(result))
counter()
